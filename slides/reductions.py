import re, graphviz, os, sys

"""
Installation (in a venv):

Mac OSX directions:

virtualenv venvmac
source venvmac/bin/activate
pip uninstall rpds pyzmq psutil
pip install graphviz jupyter rpds-py pyzmq psutil
python -m ipykernel install --user


Linux (Ubuntu 24.04):

virtualenv venv
source venv/bin/activate
pip install graphviz jupyter

"""

"""

To call this directly from the *.qmd file, put the following at the top:

```{python}
from reductions import *
reset_graph_num()
```


Then include code such as:

```{python}
#| output: asis
flow_graph(1)
```

This has to print() (not return) the SVG or HTML code
"""


graph_num = 0
cache_dir = ".graph-cache"
output_to_file = True


def xprint(str,filename):
    global output_to_file
    if output_to_file:
        with open(f"graphs/reductions/{filename}.svg","w") as f:
            print(str,file=f)
    else:
        print(str)

def param_join(l):
    if l == []:
        return ""
    l2 = [str(x) for x in l]
    return "-" + "-".join(l2)

def reset_graph_num():
    global graph_num
    graph_num = 0

def check_if_in_cache(graph_num,file):
    return False

    # this was used when it was generating the images for each quarto preview run, 
    # but is not needed now that they are generated separately
    os.system(f"mkdir -p {cache_dir}")
    source_name = f"{cache_dir}/graph-{graph_num}"
    svg_name = source_name + ".svg"
    if not os.path.exists(cache_dir) or not os.path.exists(source_name):
        return False
    else:
        with open(source_name) as f:
            cached_source = f.read()
        if cached_source.strip() == file.strip():
            #print("<p>same</p>")
            with open(svg_name) as f:
                return f.read()
        else:
            #print("<p>different</p>")
            os.unlink(source_name)
            os.unlink(svg_name)
            return False

def register_in_cache(graph_num,source,svg):
    return

    # this was used when it was generating the images for each quarto preview run, 
    # but is not needed now that they are generated separately
    with open(f"{cache_dir}/graph-{graph_num}","w") as f:
        f.write(source)
    with open(f"{cache_dir}/graph-{graph_num}.svg","w") as f:
        f.write(svg)


#--------------------------------------------------
# Bipartite graphs
#--------------------------------------------------

# set the field to the color to render that edge
# they are, in order: l1--r1, l1--r4, l2--r1, l2--r2, l2--r3, l3--r1, l3--r3, l4--r1, l4--r2
preset_colors = [
    #l1--r1, l1--r4, l2--r1, l2--r2, l2--r3, l3--r1, l3--r3, l4--r1, l4--r2
    ["red",  "red",  "red",  "red",  "red",  "red",  "red",  "red",  "red",  ],
    ["blue", "red",  "red",  "blue", "red",  "red",  "blue", "red",  "red",  ],
    ["red",  "blue", "red",  "red",  "blue", "blue", "red",  "red",  "blue", ],
    ["red",  "blue", "red",  "blue", "red",  "red",  "blue", "blue", "red",  ],
]

def bipartite_graph_dot(coloring,flow_graph,label=0):
    # label value:
    # 0: no labels
    # 1: capacity only
    # 2: flow (based on color)
    colors = preset_colors[coloring]

    ret = f"""
graph G2 {{
    // bipartite graph with all edges red
    rankdir = "LR";
    bgcolor=transparent;
    graph [start=144;fontsize=36;newrank=true;splines=false;];
    node [fontname="Arial",shape=square,fixedsize=true,width="2in",color=transparent];
    edge [fontname="Arial",fontcolor=black;fontsize=24;penwidth=6;style=solid,minlen=1];
    subgraph cluster_profs {{
        graph [start=144;rank=same;style=filled;color=lightgrey;label="professors"];
        node [shape=rect,width="0.5in",height="2in"];
        spacer1 [style=rect,width="2in",height="0.01in",color=transparent,style=filled,fixedsize=true,label=""];
        l1; l2; l3; l4;
    }}
    subgraph cluster_dogs {{
        graph [start=144;rank=same;style=filled;color=lightgrey;label="dogs"];
        node [shape=rect,width="0.5in",height="2in"];
        spacer2 [style=rect,width="2in",height="0.01in",color=transparent,style=filled,fixedsize=true,label=""];
        r2; r3; r1; r4;
    }}
    // to keep the two sides spaced apart
    spacer [width="3in",shape=none,label=""];
    l4 -- spacer -- r4 [style=invis];"""

    if flow_graph:
        ret += f"""     // start and terminus nodes
     edge [style=solid,color={"red" if coloring == 0 else "blue"}];
     s [shape=circle,style=filled,color=purple,width="1in",fontsize=36];
     t [shape=circle,style=filled,color=navy,width="1in";fontcolor=white;fontsize=36];
     edge [minlen=4,xlabel="{"1" if label==1 else "" if label==0 else "1/1"}"];
     s -- l1;
     s -- l2;
     s -- l3;
     s -- l4;
     r1 -- t;
     r2 -- t;
     r3 -- t;
     r4 -- t;
     edge [minlen=1];
"""

    ret += f"""// the bipartite edges
    edge [style=solid,color=red];
    l1 -- r1 [color={colors[0]},xlabel="{"1" if label==1 else "" if label==0 else "0/1" if colors[0]=="red" else "1/1"}"];
    l1 -- r2 [style=invis];
    l1 -- r3 [style=invis];
    l1 -- r4 [color={colors[1]},xlabel="{"1" if label==1 else "" if label==0 else "0/1" if colors[1]=="red" else "1/1"}"];
    l2 -- r1 [color={colors[2]},xlabel="{"1" if label==1 else "" if label==0 else "0/1" if colors[2]=="red" else "1/1"}"];
    l2 -- r2 [color={colors[3]},xlabel="{"1" if label==1 else "" if label==0 else "0/1" if colors[3]=="red" else "1/1"}"];
    l2 -- r3 [color={colors[4]},xlabel="{"1" if label==1 else "" if label==0 else "0/1" if colors[4]=="red" else "1/1"}"];
    l2 -- r4 [style=invis];
    l3 -- r1 [color={colors[5]},xlabel="{"1" if label==1 else "" if label==0 else "0/1" if colors[5]=="red" else "1/1"}"];
    l3 -- r2 [style=invis];
    l3 -- r3 [color={colors[6]},xlabel="{"1" if label==1 else "" if label==0 else "0/1" if colors[6]=="red" else "1/1"}"];
    l3 -- r4 [style=invis];
    l4 -- r1 [color={colors[7]},xlabel="{"1" if label==1 else "" if label==0 else "0/1" if colors[7]=="red" else "1/1"}"];
    l4 -- r2 [color={colors[8]},xlabel="{"1" if label==1 else "" if label==0 else "0/1" if colors[8]=="red" else "1/1"}"];
    l4 -- r3 [style=invis];
    l4 -- r4 [style=invis];
    // to keep the bottom nodes on the bottom
    l4 -- end [style=invis];
    r4 -- end [style=invis];
    end [shape=none,label="",width="0in"];
}}
"""
    return ret

def div_header(w=None,h=None):
    ret = "<div class='cell'"
    if w is not None:
        ret += f" data-fig-width='{w}'"
    if h is not None:
        f" data-fig-height='{h}'"
    ret += """ data-layout-align="default">
<div class="cell-output-display">
<div>
<figure class="">
<div>"""
    return ret

div_footer = """</div>
</figure>
</div>
</div>
</div>"""

bipartite_image_table_body = """
<tr><td> ![](https://engineering.virginia.edu/sites/default/files/styles/square_xxsml/public/Headshot.webp?itok=5IwaFPya){style=""} </td><td> </td><td> ![](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Sobaka_Husky.JPG/940px-Sobaka_Husky.JPG){style=""} </td></tr>
<tr><td> ![](https://engineering.virginia.edu/sites/default/files/styles/square_xxsml/public/2024-07/RobbieHott-2023.JPG?h=83d1c70a&itok=kpjw11sp){style=""} </td><td> </td><td> ![](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Labrador_Retriever_snow.jpg/1196px-Labrador_Retriever_snow.jpg){style=""} </td></tr>
<tr><td> ![](https://engineering.virginia.edu/sites/default/files/styles/square_xxsml/public/Pettit3.JPG?h=7d5d1757&itok=jvoP0ymk){style=""} </td><td> </td><td> ![](https://upload.wikimedia.org/wikipedia/commons/f/f4/MiniDachshund1_wb.jpg){style=""} </td></tr>
<tr><td> ![](https://www.cs.virginia.edu/~asb/images/me.jpg){style=""} </td><td> </td><td> ![](https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/Jonangi.jpg/1280px-Jonangi.jpg){style=""} </td></tr>
"""

def bipartite_graph(w,h,coloring,flow_graph=False,label=0):
    global graph_num

    params = [w,h,coloring]
    if flow_graph and label == 0:
        params.append(True)
    if label != 0:
        params.append(True)
        params.append(label)
    output_filename = "bipartite_graph" + param_join(params)

    # if width & height are given in inches, conver it to pixels (96 dpi)
    if w < 20:
        w *= 96
    if h < 20:
        h *= 96
    # which coloring are we using?
    assert coloring >= 0 and coloring < len(preset_colors)
    # generate the graph
    dot_source = bipartite_graph_dot(coloring,flow_graph,label)
    #print("\n\n\n\n\n",dot_source)
    html = check_if_in_cache(graph_num,dot_source)
    if not html:
        g = graphviz.Source(dot_source,format='svg')
        html = g.pipe(format='svg').decode('utf-8')
        register_in_cache(graph_num,dot_source,html)
    html = re.sub(r'<svg width="[0-9]+pt" height="[0-9]+pt"', f'<svg width="{w}" height="{h}"', html)
    where = html.find("<svg ")
    xprint(html[where:], output_filename)
    graph_num += 1


#--------------------------------------------------
# Flow graphs
#--------------------------------------------------

def flow_graph_dot(labels, edgecolors, revlabels):
    return f"""
digraph graph1 {{
    // the layout when the edge labels are a single character or digit
    // capacities only; the graph on day20 slides 13&15 of day20.pptx
    layout=fdp;
    start=144; 
    graph[K=1.5];
    node [fontname="Arial",shape=circle,fillcolor=cornflowerblue,style="rounded,filled"];
    edge [fontname="Arial",fontcolor=forestgreen;fontsize=24;penwidth=4;minlen=32];
    s [style=filled;fillcolor=purple;fontcolor=white];
    a [];
    b [];
    c [];
    d [];
    t [style=filled;fillcolor=navy;fontcolor=white];
    // edge flows: 
    // - first three are the top flow from s->t
    // - second three are the bottom flow from s->t
    // - last 5 are the remaining edges from left-to-right
    s -> a [label=<{str(labels[0])}>  {",color=transparent,fontcolor=transparent" if str(labels[0])==''  else 'color='+edgecolors[0]} ];
    a -> b [label=<{str(labels[4])}>  {",color=transparent,fontcolor=transparent" if str(labels[4])==''  else 'color='+edgecolors[4]} ];
    b -> t [label=<{str(labels[9])}>  {",color=transparent,fontcolor=transparent" if str(labels[9])==''  else 'color='+edgecolors[9]} ];
    s -> c [label=<{str(labels[1])}>  {",color=transparent,fontcolor=transparent" if str(labels[1])==''  else 'color='+edgecolors[1]} ];
    c -> d [label=<{str(labels[6])}>  {",color=transparent,fontcolor=transparent" if str(labels[6])==''  else 'color='+edgecolors[6]} ];
    d -> t [label=<{str(labels[10])}> {",color=transparent,fontcolor=transparent" if str(labels[10])=='' else 'color='+edgecolors[10]}];
    c -> s [label=<{str(labels[2])}>  {",color=transparent,fontcolor=transparent" if str(labels[2])==''  else 'color='+edgecolors[2]} ];
    c -> a [label=<{str(labels[3])}>  {",color=transparent,fontcolor=transparent" if str(labels[3])==''  else 'color='+edgecolors[3]} ];
    b -> c [label="&nbsp;",xlabel=<&nbsp;&nbsp;&nbsp;{str(labels[5])}>  {",color=transparent,fontcolor=transparent" if str(labels[5])==''  else 'color='+edgecolors[5]} ];
    d -> b [label=<{str(labels[7])}>  {",color=transparent,fontcolor=transparent" if str(labels[7])==''  else 'color='+edgecolors[7]} ];
    b -> d [label=<{str(labels[8])}>  {",color=transparent,fontcolor=transparent" if str(labels[8])==''  else 'color='+edgecolors[8]} ];
    edge [color=magenta,fontcolor=magenta];
    a -> s [label="&nbsp;",xlabel=<&nbsp;&nbsp;{str(revlabels[0])}>  {",color=transparent,fontcolor=transparent" if str(revlabels[0])==''  else ''}];
    b -> a [xlabel=<{str(revlabels[4])}>,label="&nbsp;"  {",color=transparent,fontcolor=transparent" if str(revlabels[4])==''  else ''}];
    t -> b [label=" ",xlabel=<{str(revlabels[9])}>  {",color=transparent,fontcolor=transparent" if str(revlabels[9])==''  else ''}];
    c -> s [label=<{str(revlabels[1])}>  {",color=transparent,fontcolor=transparent" if str(revlabels[1])==''  else ''}];
    d -> c [xlabel=<{str(revlabels[6])}>,label=<&nbsp;>  {",color=transparent,fontcolor=transparent" if str(revlabels[6])==''  else ''}];
    t -> d [xlabel=<&nbsp;&nbsp;{str(revlabels[10])}>,label=<&nbsp;> {",color=transparent,fontcolor=transparent" if str(revlabels[10])=='' else ''}];
    s -> c [label=<{str(revlabels[2])}>  {",color=transparent,fontcolor=transparent" if str(revlabels[2])==''  else ''}];
    a -> c [label=<{str(revlabels[3])}>  {",color=transparent,fontcolor=transparent" if str(revlabels[3])==''  else ''}];
    c -> b [label=<{str(revlabels[5])}>  {",color=transparent,fontcolor=transparent" if str(revlabels[5])==''  else ''}];
    b -> d [label=<{str(revlabels[7])}>  {",color=transparent,fontcolor=transparent" if str(revlabels[7])==''  else ''}];
    d -> b [label=<{str(revlabels[8])}>  {",color=transparent,fontcolor=transparent" if str(revlabels[8])==''  else ''}];
}}
"""

tex_header = """
\\documentclass[border=3mm]{standalone}
\\usepackage[dvipsnames]{xcolor}
\\usepackage{tikz}
\\usetikzlibrary{arrows.meta,  % define arrows head styles
                positioning,  % for nodes positioning
                shapes.geometric} % for ellipses
\\newcommand{\\comment}[1]{}
\\begin{document}
"""

def tec(labels,edge,hide,cut_graph): # tec == tikz_edge_color
    label = labels[edge]
    #if not hide:
    #    return "black"
    if (cut_graph == 1 and edge in [4,6]) or \
       (cut_graph == 2 and edge in [1,4]):
        return "ForestGreen,"
    if (str(label) == "" or (len(str(label)) > 0 and str(label)[0] == "0")) and hide:
        return "transparent,"
    #if (str(label) != "" and (len(str(label)) > 0 and str(label)[0] != "0")) and hide:
    #    return "orange"
    return ""
    #assert False

def tch(source,terminus,color,highlights): # tch = tikz check highlights
    if (source,terminus,color) in highlights:
        return "dashed,"
    elif (source,terminus,color,'o') in highlights:
        return "dashed,orange,"
    elif (source,terminus,color,'m') in highlights:
        return "dashed,magenta,"
    else:
        return ""


def flow_graph_tikz(labels, res, revres, revlabels, highlights, cut_graph): # labels, residual, reverse-residual, reverse-residual labels
    # cut graph 0 is no cut graph
    # cut graph 1 has three nodes in the left cut, and the two edges that cross the cut are colored green
    # cut graph 2 has two nodes in the left cut, and the two edges that cross the cut are colored green
    # cut graph 3 has two nodes in the left cut, and the two edges that cross the cut are colored green and brown
    # cut graph 4 has two nodes in th eleft cut, and no change of edge colorings
    ret = f"""
\\begin{{tikzpicture}}[
     C/.style = {{circle, draw, very thick, minimum size = 8mm, node distance = 20mm, fill=CornflowerBlue}},
     every edge/.style = {{->, draw, ultra thick, -stealth}},
]

\\tikzset{{font=\\sffamily}}
"""

    if cut_graph == 1:
        ret += f"""
\\node (S) at (1.5,0.65) [circle,draw,fill=Lavender!70,minimum size=44mm] {{}};
\\node (T) at (6,1.3) [circle,draw,fill=SkyBlue!50,minimum size=44mm] {{}};
\\node (Sl) at (0.5,2) [text=magenta] {{\\LARGE S}};
\\node (Tl) at (6,3) [text=blue] {{\\LARGE T}};

"""
    if cut_graph in [2,3,4]:
        ret += f"""
%\\node (S) at (0.5,1) [circle,draw,fill=Lavender!70,minimum size=36mm] {{}};
\\draw[rotate around={{50:(0.8,1)}}, fill=Lavender!70] (0.8,1) ellipse[x radius=2, y radius=1];
%\\node (T) at (5.2,1.3) [circle,draw,fill=SkyBlue!50,minimum size=58mm] {{}};
\\draw[rotate around={{20:(5.5,1)}}, fill=SkyBlue!50] (5.25,1) ellipse[x radius=3.25, y radius=2];
\\node (Sl) at (0.5,2.75) [text=magenta] {{\\LARGE S}};
\\node (Tl) at (3.55,2.75) [text=blue] {{\\LARGE T}};


"""

    ret += f"""
\\node (a) at (1.5,2) [C] {{a}};
\\node (b) at (4.5,2) [C] {{b}};
\\node (t) at (7.5,2) [C, fill=Blue, text=white] {{t}};
\\node (s) at (0,0) [C, fill=Plum, text=white] {{s}};
\\node (c) at (3,0) [C] {{c}};
\\node (d) at (6,0) [C] {{d}};
"""
    if not revres:
        # this has (mostly) straight edges
        if res:
            ret += "\\tikzset{text=orange}\n\\path[orange]\n"
        else:
            ret += "\\path\n"
        ret += f"""
    (s) edge[{tch('s','a','b',highlights)} {tec(labels,0,res,cut_graph)}] node[above left] {{{str(labels[0])}}} (a)
    (s) edge[{tch('s','c','b',highlights)} {tec(labels,1,res,cut_graph)} bend left=15] node[above] {{{str(labels[1])}}} (c)
    (c) edge[{tch('c','s','b',highlights)} {tec(labels,2,res,cut_graph)} bend left=15] node[below] {{{str(labels[2])}}} (s)
    (c) edge[{tch('c','a','b',highlights)} {"Bittersweet," if cut_graph==3 else tec(labels,3,res,cut_graph)}] node[right] {{{str(labels[3])}}} (a)
    (a) edge[{tch('a','b','b',highlights)} {"ForestGreen," if cut_graph==3 else tec(labels,4,res,cut_graph)}] node[above] {{{str(labels[4])}}} (b)
    (b) edge[{tch('b','c','b',highlights)} {tec(labels,5,res,cut_graph)}] node[above] {{{str(labels[5])}}} (c)
    (c) edge[{tch('c','d','b',highlights)} {tec(labels,6,res,cut_graph)}] node[below] {{{str(labels[6])}}} (d)
    (d) edge[{tch('d','b','b',highlights)} {tec(labels,7,res,cut_graph)} bend left=15] node[left] {{{str(labels[7])}}} (b)
    (b) edge[{tch('b','d','b',highlights)} {tec(labels,8,res,cut_graph)} bend left=15] node[above right] {{{str(labels[8])}}} (d)
    (b) edge[{tch('b','t','b',highlights)} {tec(labels,9,res,cut_graph)}] node[above] {{{str(labels[9])}}} (t)
    (d) edge[{tch('d','t','b',highlights)} {tec(labels,10,res,cut_graph)}] node[below right] {{{str(labels[10])}}} (t);

"""
    else:
        ret += f"""
\\path[orange]
    (s) edge[{tch('s','a','o',highlights)} {tec(labels,0,res,cut_graph)} bend left=15] node[above left] {{{str(labels[0])}}} (a)
    (s) edge[{tch('s','c','o',highlights)} {tec(labels,1,res,cut_graph)} bend left=30] node[above] {{{str(labels[1])}}} (c)
    (c) edge[{tch('c','s','o',highlights)} {tec(labels,2,res,cut_graph)} bend left=10] node[below] {{{str(labels[2])}}} (s)
    (c) edge[{tch('c','a','o',highlights)} {"Bittersweet," if cut_graph==3 else tec(labels,3,res,cut_graph)} bend left=15] node[right] {{{str(labels[3])}}} (a)
    (a) edge[{tch('a','b','o',highlights)} {"ForestGreen," if cut_graph==3 else tec(labels,4,res,cut_graph)} bend left=15] node[above] {{{str(labels[4])}}} (b)
    (b) edge[{tch('b','c','o',highlights)} {tec(labels,5,res,cut_graph)} bend left=15] node[above left] {{{str(labels[5])}}} (c)
    (c) edge[{tch('c','d','o',highlights)} {tec(labels,6,res,cut_graph)} bend left=15] node[below] {{{str(labels[6])}}} (d)
    (d) edge[{tch('d','b','o',highlights)} {tec(labels,7,res,cut_graph)} bend left=30] node[left] {{{str(labels[7])}}} (b)
    (b) edge[{tch('b','d','o',highlights)} {tec(labels,8,res,cut_graph)} bend left=10] node[above right] {{{str(labels[8])}}} (d)
    (b) edge[{tch('b','t','o',highlights)} {tec(labels,9,res,cut_graph)} bend left=15] node[above] {{{str(labels[9])}}} (t)
    (d) edge[{tch('d','t','o',highlights)} {tec(labels,10,res,cut_graph)} bend left=15] node[below right] {{{str(labels[10])}}} (t);

"""

    if revres:
        ret += f"""
\\tikzset{{text=magenta}}
\\draw[magenta]
    (a) edge[{tch('a','s','m',highlights)}{tec(revlabels,0,revres,cut_graph)} bend left=15] node[above left] {{{revlabels[0]}}} (s)
    (c) edge[{tch('c','s','m',highlights)}{tec(revlabels,1,revres,cut_graph)} bend right=10] node[above] {{{revlabels[1]}}} (s)
    (s) edge[{tch('s','c','m',highlights)}{tec(revlabels,2,revres,cut_graph)} bend right=30] node[below] {{{revlabels[2]}}} (c)
    (a) edge[{tch('a','c','m',highlights)}{tec(revlabels,3,revres,cut_graph)} bend left=15] node[right] {{{revlabels[3]}}} (c)
    (b) edge[{tch('b','a','m',highlights)}{tec(revlabels,4,revres,cut_graph)} bend left=15] node[above] {{{revlabels[4]}}} (a)
    (c) edge[{tch('c','b','m',highlights)}{tec(revlabels,5,revres,cut_graph)} bend left=15] node[above] {{{revlabels[5]}}} (b)
    (d) edge[{tch('d','c','m',highlights)}{tec(revlabels,6,revres,cut_graph)} bend left=15] node[below] {{{revlabels[6]}}} (c)
    (b) edge[{tch('b','d','m',highlights)}{tec(revlabels,7,revres,cut_graph)} bend right=10] node[left] {{{revlabels[7]}}} (d)
    (d) edge[{tch('d','b','m',highlights)}{tec(revlabels,8,revres,cut_graph)} bend right=30] node[above right] {{{revlabels[8]}}} (b)
    (t) edge[{tch('t','b','m',highlights)}{tec(revlabels,9,revres,cut_graph)} bend left=15] node[above] {{{revlabels[9]}}} (b)
    (t) edge[{tch('t','d','m',highlights)}{tec(revlabels,10,revres,cut_graph)} bend left=15] node[below right] {{{revlabels[10]}}} (d);
"""
    """
    if cut_graph == 3:
        ret += f""
\\tikzset{{text=magenta}}
\\draw[magenta]
    (a) edge[ForestGreen, bend left=15] node[above] {{0}} (b)
    (c) edge[Bittersweet, bend left=15] node[right] {{3}} (a);
"""


    ret += "\\end{tikzpicture}"
    return ret



all_label_sets = [
    #[1,2,3,4,5,6,7,8,9,10,11], # test set
    ["1/2","1/2","1/2","1/3","1/2","1/2","2/3","2/3","1/2","2/3","1/2"], # 0: flow graph with flow 3/4
    [3,2,1,3,2,1,3,3,2,3,2],                                             # 1: first graph showing only capacity
    ["1/3","2/2","0/1","1/3","2/2","1/1","2/3","2/3","1/2","2/3","1/2"], # 2: flow graph with flow 3/4
    ["2/3","2/2","0/1","0/3","2/2","0/1","2/3","2/3","0/2","2/3","2/2"], # 3: flow graph with maxflow = 4 (same as 8)
    ["0/3","0/2","0/1","0/3","0/2","0/1","0/3","0/3","0/2","0/3","0/2"], # 4: flow graph with flow 0
    ["1/3","0/2","0/1","0/3","1/2","1/1","1/3","0/3","0/2","0/3","1/2"], # 5: flow graph with flow 1
    ["2/3","0/2","0/1","0/3","2/2","1/1","1/3","0/3","0/2","1/3","1/2"], # 6: flow graph with flow 2
    ["2/3","1/2","0/1","0/3","2/2","0/1","1/3","0/3","0/2","2/3","1/2"], # 7: flow graph with flow 3
    ["2/3","2/2","0/1","0/3","2/2","0/1","2/3","0/3","0/2","2/3","2/2"], # 8: flow graph with flow 4 (same as 3)

]

all_highlights = [
    [], # for no highlights
    [('s','a','o'),('a','c','m'),('c','b','m'),('b','t','o'),('s','a','b','o'),('b','c','b','m'),('c','a','b','m'),('b','t','b','o')], # first residual graph flow slides
    [('s','a','o'),('a','b','o'),('b','c','o'),('c','d','o'),('d','t','o'),('s','a','b','o'),('a','b','b','o'),('b','c','b','o'),('c','d','b','o'),('d','t','b','o')], # first FF example path
    [('s','a','o'),('a','b','o'),('b','t','o'),('s','a','b','o'),('a','b','b','o'),('b','t','b','o')], # second FF example path
    [('s','c','o'),('c','b','m'),('b','t','o'),('s','c','b','o'),('b','c','b','m'),('b','t','b','o')], # third FF example path
    [('s','c','o'),('c','d','o'),('d','t','o'),('s','c','b','o'),('c','d','b','o'),('d','t','b','o')], # fourth FF example path
]


def flow_graph(label_set,residual=False,highlight_set=0,revresidual=True,cut_graph=0):
    global graph_num

    params = [label_set, residual, highlight_set, revresidual, cut_graph]
    if cut_graph == 0:
        params.pop()
        if revresidual:
            params.pop()
            if highlight_set == 0:
                params.pop()
                if not residual:
                    params.pop()
    output_filename = "flow_graph" + param_join(params)

    w,h = 960,480
    # parameters:
    # flow graph (if so, color edges orange; if not, color edges black)
    # show reverse paths (the magenta ones)
    # show paths with capacity 0
    # labels (False for none, integer for a pre-defined set, or a list of strings for custom labels)
    # if width & height are given in inches, conver it to pixels (96 dpi)

    edgelabels = list(all_label_sets[label_set])
    highlights = all_highlights[highlight_set]
    #print(edgelabels)

    # sanitize parameters
    if not residual:
        revresidual = False

    # generate the labels
    edgecolors = ["black"] * 11
    flowedgelabels = []
    revflowedgelabels = []
    if residual:
        # if a residual graph, compute the forward edges and reverse edges
        for i in range(len(edgelabels)):
            assert len(str(edgelabels[i])) == 3 and str(edgelabels[i][1]) == "/"
            flowedgelabels.append(edgelabels[i][0])
            if flowedgelabels[i] == "0":
                flowedgelabels[i] = ''
            revflowedgelabels.append(str(int(edgelabels[i][2]) - int(edgelabels[i][0])))
            if revflowedgelabels[i] == "0":
                revflowedgelabels[i] = ''
            edgecolors = ["orange"] * 11
    else:
        for i in range(len(edgelabels)):
            if len(str(edgelabels[i])) == 3 and str(edgelabels[i][1]) == "/":
                edgelabels[i] = f'\\textcolor{{red}}{{{edgelabels[i][0]}}}/\\textcolor{{ForestGreen}}{{{edgelabels[i][2]}}}'
                #print(f'edgelabel: {edgelabels[i]}')

    # generate the graph
    #print(f"<p>flowedgelabels: {flowedgelabels}</p><p>revflowedgelabels: {revflowedgelabels}")
    if residual and revresidual:
        tex_file = tex_header + flow_graph_tikz(revflowedgelabels,residual,revresidual,flowedgelabels,highlights,cut_graph) + "\n\\end{document}"
    elif residual:
        tex_file = tex_header + flow_graph_tikz(revflowedgelabels,residual,revresidual,flowedgelabels,highlights,cut_graph) + "\n\\end{document}"
    else:
        tex_file = tex_header + flow_graph_tikz(edgelabels,residual,revresidual,revflowedgelabels,highlights,cut_graph) + "\n\\end{document}"
    cached = check_if_in_cache(graph_num,tex_file)
    if not cached:
        with open("reductions.tmp.tex","w") as f:
            f.write(tex_file)
        os.system ("pdflatex reductions.tmp.tex > /dev/null")
        os.system ("inkscape reductions.tmp.pdf --export-type=svg --export-filename=reductions.tmp.svg >& /dev/null")
        with open("reductions.tmp.svg","r") as f:
           svg = f.read()
        where = svg.find("<svg\n")
        register_in_cache(graph_num,tex_file,svg[where:])
        xprint(svg[where:],output_filename)
        pass
    else:
        xprint(cached,output_filename)
        pass
    graph_num += 1


#--------------------------------------------------
# Edge disjoint graphs
#--------------------------------------------------

forestg = "ForestGreen"
edge_disjoint_graph_color_sets = [
    # s->g     g->t     h->g     s->h     h->f     f->t     f->e     s->e       e->t      e->c       s->b     b->c     c->t       b->a     a->c
    ['black', 'black', 'black', 'black', 'black', 'black', 'black', 'black',   'black',   'black',   'black', 'black', 'black',   'black', 'black'],
    ['teal',  'teal',  'black', 'blue',  'blue',  'black', 'blue',  'magenta', 'blue',    'magenta', 'black', 'black', 'magenta', 'black', 'black'],
    ['teal',  'teal',  'black', 'blue',  'blue',  'blue',  'black', 'magenta', 'magenta', 'black',   forestg, forestg, forestg,   'black', 'black'],
]
edge_disjoint_graph_label_sets = [
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    # s->g  g->t   h->g   s->h   h->f   f->t   f->e   s->e   e->t   e->c   s->b   b->c   c->t   b->a   a->c
    ['1/1', '1/1', '0/1', '1/1', '1/1', '1/1', '0/1', '1/1', '1/1', '0/1', '1/1', '1/1', '1/1', '0/1', '0/1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
]

def edge_disjoint_graph_tikz(color_set,label_set,color_e_red):
    colors = edge_disjoint_graph_color_sets[color_set]
    labels = edge_disjoint_graph_label_sets[label_set]
    ret = f"""
\\begin{{tikzpicture}}[
     C/.style = {{circle, draw, very thick, minimum size = 8mm, node distance = 5mm and 16mm, fill=orange}},
     every edge/.style = {{->, draw, ultra thick, -stealth}},
]

\\tikzset{{font=\\sffamily}}

\\node (g) [C] {{g}};
\\node (f) [C, below left=of g] {{f}};
\\node (h) [C, left=of f] {{h}};
\\node (s) [C, fill=Plum, text=white, below left=of h] {{s}};
\\node (e) [C, below right=of f, fill={"red" if color_e_red else "orange"}] {{e}};
\\node (c) [C, below right=of e] {{c}};
\\node (t) [C, fill=Blue, text=white, above right=of c] {{t}};
\\node (a) [C, below left=of c] {{a}};
\\node (b) [C, above left=of a] {{b}};

\\path
    (s) edge [bend left=30, color={colors[0]}]  node[text=black,above] {{{labels[0]}}}  (g)
    (g) edge [bend left=20, color={colors[1]}]  node[text=black,above] {{{labels[1]}}}  (t)
    (h) edge [bend left=10, color={colors[2]}]  node[text=black,above] {{{labels[2]}}}  (g)
    (s) edge [bend left=10, color={colors[3]}]  node[text=black,below] {{{labels[3]}}}  (h)
    (h) edge [              color={colors[4]}]  node[text=black,below] {{{labels[4]}}}  (f)
    (f) edge [bend left=10, color={colors[5]}]  node[text=black,above] {{{labels[5]}}}  (t)
    (f) edge [bend left=10, color={colors[6]}]  node[text=black,below] {{{labels[6]}}}  (e)
    (s) edge [              color={colors[7]}]  node[text=black,below] {{{labels[7]}}}  (e)
    (e) edge [              color={colors[8]}]  node[text=black,above] {{{labels[8]}}}  (t)
    (e) edge [bend left=10, color={colors[9]}]  node[text=black,below] {{{labels[9]}}}  (c)
    (s) edge [bend right=10,color={colors[10]}] node[text=black,above] {{{labels[10]}}} (b)
    (b) edge [              color={colors[11]}] node[text=black,above] {{{labels[11]}}} (c)
    (c) edge [bend right=10,color={colors[12]}] node[text=black,above] {{{labels[12]}}} (t)
    (b) edge [bend right=20,color={colors[13]}] node[text=black,above] {{{labels[13]}}} (a)
    (a) edge [bend right=20,color={colors[14]}] node[text=black,above] {{{labels[14]}}} (c)
    ;

\\end{{tikzpicture}}
"""
    return ret



def edge_disjoint_graph(color_set=0,label_set=0,color_e_red=False):
    global graph_num
    
    params = [color_set, label_set, color_e_red]
    if not color_e_red:
        params.pop()
        if label_set == 0:
            params.pop()
            if color_set == 0:
                params.pop()
    output_filename = "edge_disjoint_graph" + param_join(params)
    
    tex_file = tex_header + edge_disjoint_graph_tikz(color_set,label_set,color_e_red) + "\n\\end{document}"

    cached = check_if_in_cache(graph_num,tex_file)
    if not cached:
        with open("reductions.tmp.tex","w") as f:
            f.write(tex_file)
        os.system ("pdflatex reductions.tmp.tex > /dev/null")
        os.system ("inkscape reductions.tmp.pdf --export-type=svg --export-filename=reductions.tmp.svg >& /dev/null")
        with open("reductions.tmp.svg","r") as f:
           svg = f.read()
        where = svg.find("<svg\n")
        register_in_cache(graph_num,tex_file,svg[where:])
        xprint(svg[where:], output_filename)
    else:
        xprint(cached, output_filename)
    graph_num += 1


def vertex_disjoint_to_edge_disjoint_graph():
    graph_dot = """digraph vd2ed {
    layout=dot;
    rankdir="BT";
    graph [bgcolor=transparent];
    node [fontname="Arial",shape=oval,fillcolor=orange,style="rounded,filled"];
    edge [fontname="Arial",fontcolor=black;fontsize=24;penwidth=4;color=teal];
    empty0 [label="";style=invis];
    empty1 [label="";style=invis];
    g1 [label="g in"];
    g1 -> empty0 [color=invis];
    g2 [label="g out"];
    empty2 [label="empty2";style=invis];
    empty1 -> g1;
    g1 -> g2 [xlabel=<restricts to<br/>1 edge<br/>&nbsp;>;label="           ";fontsize=12];
    g2 -> empty2;
    empty3 [label="";style=invis];
    empty3 -> g1 [color=black];
    empty4 [label="";style=invis];
    empty4 -> g1 [color=invis];
    {rank=same empty1 g1 g2 empty2};
}
"""
    output_filename = "vertex_disjoint_to_edge_disjoint"
    g = graphviz.Source(graph_dot,format='svg')
    svg = g.pipe(format='svg').decode('utf-8')
    xprint(svg,output_filename)


def arrows():
    rarrow = """graph g { bgcolor=transparent;x [penwidth=3;fontname="Arial",shape=rarrow,label="",fontsize=12,height=0.6,color=red,width=2]; }"""
    output_filename = "rarrow"
    g = graphviz.Source(rarrow,format='svg')
    svg = g.pipe(format='svg').decode('utf-8')
    xprint(svg,output_filename)
    larrow = rarrow.replace("rarrow","larrow")
    output_filename = "larrow"
    g = graphviz.Source(larrow,format='svg')
    svg = g.pipe(format='svg').decode('utf-8')
    xprint(svg,output_filename)
    rarrow_square = """graph g { bgcolor=transparent;x [penwidth=3,fontname="Arial",shape=rarrow,label="",fontsize=24,fixedsize=true,height=1,color=red,width=1]; }"""
    output_filename = "rarrow-square"
    g = graphviz.Source(rarrow_square,format='svg')
    svg = g.pipe(format='svg').decode('utf-8')
    xprint(svg,output_filename)

def mini_reduction():
    graph_dot = """
digraph g { 
    graph [bgcolor=transparent;fontname="Arial"];
    node [shape=rect;fontsize=72;height=2.5;width=1.5];
    x [shape=cylinder,label=<A>,style=filled,fillcolor=red];
    y [label=<&rarr;<br/>fast<br/>&larr;>,fontsize=48,style=filled,fillcolor=Plum];
    z [label=<B>,style=filled,fillcolor=yellow];
}
"""
    output_filename = "mini_reduction"
    g = graphviz.Source(graph_dot,format='svg')
    svg = g.pipe(format='svg').decode('utf-8')
    xprint(svg,output_filename)



def cpp():
    tikz = f"""
\\begin{{tikzpicture}}[
     C/.style = {{circle, draw, very thick, minimum size = 8mm, fill=orange}},
     every edge/.style = {{->, draw, ultra thick, -stealth, -}},
]

\\tikzset{{font=\\sffamily}}

\\node at (2,10) [C] {{}};
\\node at (3,8) [C] {{}};
\\node at (7,11) [C] {{}};
\\node at (10,4) [C] {{}};
\\node at (9,9) [C] {{}};
\\node at (7,6) [C] {{}};
\\node at (5,3) [C] {{}};
\\node at (2,1) [C] {{}};
\\node at (7,1) [C] {{}};

\\node at (6,6) [very thick, minimum size=12cm,draw] {{}};

\\node at (2.5,9) [C,fill=none,minimum size=36mm, draw=none] {{}};

\\end{{tikzpicture}}
"""

    tex_file = tex_header + tikz + "\n\\end{document}"
    for i in range(2):
        with open("reductions.tmp.tex","w") as f:
            f.write(tex_file)
        os.system ("pdflatex reductions.tmp.tex > /dev/null")
        os.system ("inkscape reductions.tmp.pdf --export-type=svg --export-filename=reductions.tmp.svg >& /dev/null")
        with open("reductions.tmp.svg","r") as f:
           svg = f.read()
        where = svg.find("<svg\n")
        register_in_cache(graph_num,tex_file,svg[where:])
        xprint(svg[where:],f"cpp-{i}")
        tex_file = tex_file.replace("draw=none","draw=red")



def independent_set():
    tikz1 = f"""
\\begin{{tikzpicture}}[
     C/.style = {{circle, draw, very thick, minimum size = 3mm,scale=0.1}},
     every edge/.style = {{draw, ultra thick, -stealth, -}},
]

\\tikzset{{font=\\sffamily}}

\\node (c) [C] {{}}; % kc3
\\node (b) [C,above left=of c] {{}}; % pm
\\node (d) [C,left=of c] {{}}; % me
\\node (e) [C,below left=of c] {{}}; % ej
\\node (f) [C,below=of c] {{}}; % cpm
\\node (g) [C,below left=of d] {{}}; % bpm
\\node (h) [C,above left=of g] {{}}; % ???
\\node (i) [C,below left=of g] {{}}; % ???
\\node (j) [C,above=of i] {{}}; % rs
\\node (a) [C,above left=of h] {{}}; % a

\\path
    (a) edge (b)
    (b) edge (c)
    (c) edge (f)
    (f) edge (i)
    (i) edge (j)
    (c) edge (d)
    (d) edge (h)
    (c) edge (e)
    (e) edge (g);

\\end{{tikzpicture}}
"""
    tikz2 = f"""
\\begin{{tikzpicture}}[
     C/.style = {{circle, draw, very thick, minimum size = 3mm,scale=0.1}},
     every edge/.style = {{draw, ultra thick, -stealth, -}},
]

\\tikzset{{font=\\sffamily}}

\\node (a) [C] {{}}; % kc3
\\node (b) [C,left=of a] {{}};

\\path
    (a) edge (b);

\\end{{tikzpicture}}
"""

    tex_file = tex_header + tikz1 + "\n\\end{document}"
    with open("reductions.tmp.tex","w") as f:
        f.write(tex_file)
    os.system ("pdflatex reductions.tmp.tex > /dev/null")
    os.system ("inkscape reductions.tmp.pdf --export-type=svg --export-filename=reductions.tmp.svg >& /dev/null")
    with open("reductions.tmp.svg","r") as f:
       svg = f.read()
    where = svg.find("<svg\n")
    register_in_cache(graph_num,tex_file,svg[where:])
    xprint(svg[where:],f"independent_set-1")
    tex_file = tex_header + tikz2 + "\n\\end{document}"
    with open("reductions.tmp.tex","w") as f:
        f.write(tex_file)
    os.system ("pdflatex reductions.tmp.tex > /dev/null")
    os.system ("inkscape reductions.tmp.pdf --export-type=svg --export-filename=reductions.tmp.svg >& /dev/null")
    with open("reductions.tmp.svg","r") as f:
       svg = f.read()
    where = svg.find("<svg\n")
    register_in_cache(graph_num,tex_file,svg[where:])
    xprint(svg[where:],f"independent_set-2")


def vertex_cover():
    vc1_dot = f"""
graph g {{
    layout=circo;
    rankdir="BT";
    graph [bgcolor=transparent];
    node [fontname="Arial",shape=rect,fillcolor=CornflowerBlue,style=filled,fixedsize=true,width="0.25in",height="0.25in",label=""];
    edge [fontname="Arial",fontcolor=black;fontsize=24;penwidth=4;color=black];

    h [shape=diamond,width="0.35in",height="0.35in"];
    h -- 1 -- 2 -- 3 -- h;
    {{rank=same 1 3}}
}}
"""
    vc2_dot = f"""
graph g {{
    layout=fdp;
    rankdir="BT";
    graph [bgcolor=transparent];
    node [fontname="Arial",shape=rect,fillcolor=CornflowerBlue,style=filled,fixedsize=true,width="0.25in",height="0.25in",label=""];
    edge [fontname="Arial",fontcolor=black;fontsize=24;penwidth=4;color=black];

    h -- 1;
    h -- 8;
    1 -- 2;
    1 -- 3;
    1 -- 8;
    2 -- 3;
    2 -- 6;
    3 -- 4;
    3 -- 5;
    4 -- 5;
    5 -- 6;
    5 -- 7;
    7 -- 8;

    7 [shape=diamond,width="0.35in",height="0.35in"];
}}
"""
    vc3_dot = f"""
graph g {{
    layout=fdp;
    rankdir="BT";
    graph [bgcolor=transparent];
    node [fontname="Arial",shape=rect,fillcolor=CornflowerBlue,style=filled,fixedsize=true,width="0.25in",height="0.25in",label=""];
    edge [fontname="Arial",fontcolor=black;fontsize=24;penwidth=4;color=black];

    h -- 1;
    h -- 8;
    1 -- 2;
    1 -- 3;
    1 -- 8;
    2 -- 3;
    2 -- 6;
    3 -- 4;
    3 -- 5;
    4 -- 5;
    5 -- 6;
    5 -- 7;
    7 -- 8;

    5 [fillcolor=red];
    8 [fillcolor=red];
    2 [fillcolor=red];
    3 [fillcolor=red];
    h [fillcolor=red];

    7 [shape=diamond,width="0.35in",height="0.35in"];
}}
"""

    output_filename = "vertex_cover-1"
    g = graphviz.Source(vc1_dot,format='svg')
    svg = g.pipe(format='svg').decode('utf-8')
    xprint(svg,output_filename)
    output_filename = "vertex_cover-2"
    g = graphviz.Source(vc2_dot,format='svg')
    svg = g.pipe(format='svg').decode('utf-8')
    xprint(svg,output_filename)
    output_filename = "vertex_cover-3"
    g = graphviz.Source(vc3_dot,format='svg')
    svg = g.pipe(format='svg').decode('utf-8')
    xprint(svg,output_filename)



#--------------------------------------------------
# diamond flow graphs
#--------------------------------------------------

label_sets = [
    ["20","10","30","10","20",                  0,0,0,0,0], # 0
    ["20/20","10","20/30","10","20/20",         0,0,0,0,0], # 1
    ["20/20","10/10","10/30","10/10","20/20",   0,0,0,0,0], # 2
    ["20/20","0/10","20/30","0/10","20/20",     0,0,0,0,0], # 3
    [0,10,10,10,0, 20,0,20,0,20],                           # 4
    [0,0,20,0,0, 20,10,10,10,20],                           # 5
    ["0/100","0/100","0/1","0/100","0/100",     0,0,0,0,0], # 6
    [100,100,1,100,100, 0,0,0,0,0],                         # 7
    ["1/100",100,"1/1",100,"1/100", 0,0,0,0,0],             # 8
    [99,100,0,100,99, 1,0,1,0,1],                           # 9
    ["1/100","1/100","0/1","1/100","1/100", 0,0,0,0,0],     # 10
    [99,99,1,99,99, 1,1,0,1,1],                             # 11
]

color_sets = [
    ["black","black","black","black","black"],
    ["red","black","red","black","red"],
    ["red","red","red","red","red"],
    ["orange","black","orange","black","orange"],
    ["orange","black","magenta","black","orange"],
]

def diamond_flow(color_set=0,label_set=0,residual=False,highlight=0):
    params = [color_set, label_set, residual, highlight]
    if highlight == 0:
        params.pop()
        if not residual:
            params.pop()
            if label_set == 0:
                params.pop()
                if color_set == 0:
                    params.pop()
    output_filename = "diamond_flow" + param_join(params)

    labels = list(label_sets[label_set])
    origlabels = list(labels)
    for i in range(len(labels)):
        if residual and str(labels[i]) == "0":
            labels[i] = ""
        if not residual:
            if "/" in str(labels[i]):
                pos = labels[i].find("/")
                labels[i] = f"\\textcolor{{red}}{{\\Large {labels[i][:pos]}}}/\\textcolor{{ForestGreen}}{{\\Large {labels[i][pos+1:]}}}"
            else:
                labels[i] = f"\\textcolor{{ForestGreen}}{{\\Large {labels[i]}}}"
    colors = color_sets[color_set]

    tikz1 = f"""
\\begin{{tikzpicture}}[
     C/.style = {{circle, draw, very thick, minimum size = 10mm, node distance = 20mm, fill=CornflowerBlue}},
     every edge/.style = {{->, ultra thick, -stealth}},
]

\\tikzset{{font=\\sffamily}}

\\node (a) at (0,4) [C, draw] {{\\Large a}};
\\node (s) at (-3,2) [C, draw,fill=Blue,text=white] {{\\Large s}};
\\node (t) at (3,2) [C, draw,fill=Plum,text=white] {{\\Large t}};
\\node (b) at (0,0) [C, draw] {{\\Large b}};

{"\\comment{" if residual else ""}
\\path
    (s) edge [{"dashed," if highlight==1 else ""} draw,{colors[0]}] node[above left] {{{str(labels[0])}~}}  (a)
    (s) edge [{"dashed," if highlight==2 else ""} draw,{colors[1]}] node[below left] {{{str(labels[1])}~}} (b)
    (a) edge [{"dashed," if highlight==1 or highlight==2 else ""} draw,{colors[2]}] node[left] {{{str(labels[2])}}} (b)
    (a) edge [{"dashed," if highlight==2 else ""} draw,{colors[3]}] node[above right] {{~{str(labels[3])}}} (t)
    (b) edge [{"dashed," if highlight==1 else ""} draw,{colors[4]}] node[below right] {{~{str(labels[4])}}} (t);
{"}" if residual else ""}

{"\\comment{" if not residual else ""}
\\path
    (s) edge [orange, {"" if str(origlabels[0])[0] == "0" else "draw,"} {"dashed," if highlight==1 else ""} bend left=10] node[above left,text=orange] {{\\Large {str(labels[0])}~}}  (a)
    (s) edge [orange, {"" if str(origlabels[1])[0] == "0" else "draw,"} {"dashed," if highlight==2 else ""} bend right=10] node[below left,text=orange] {{\\Large {str(labels[1])}~}} (b)
    (a) edge [orange, {"" if str(origlabels[2])[0] == "0" else "draw,"} {"dashed,draw," if highlight==1 else ""} bend left=10] node[right,text=orange] {{\\Large {str(labels[2])}}} (b)
    (a) edge [orange, {"" if str(origlabels[3])[0] == "0" else "draw,"} {"dashed," if highlight==2 else ""} bend left=10] node[above right,text=orange] {{\\Large ~{str(labels[3])}}} (t)
    (b) edge [orange, {"" if str(origlabels[4])[0] == "0" else "draw,"} {"dashed," if highlight==1 else ""} bend right=10] node[below right,text=orange] {{\\Large ~{str(labels[4])}}} (t);

\\path
    (a) edge [magenta, {"" if str(origlabels[5])[0] == "0" else "draw,"} bend left=10] node[below right,text=magenta] {{\\Large {str(labels[5])}~}}  (s)
    (b) edge [magenta, {"" if str(origlabels[6])[0] == "0" else "draw,"} bend right=10] node[above right,text=magenta] {{\\Large {str(labels[6])}~}} (s)
    (b) edge [magenta, {"" if str(origlabels[7])[0] == "0" else "draw,"} {"dashed,draw," if highlight==2 else ""} bend left=10] node[left,text=magenta] {{\\Large {str(labels[7])}}} (a)
    (t) edge [magenta, {"" if str(origlabels[8])[0] == "0" else "draw,"} bend left=10] node[below left,text=magenta] {{\\Large ~{str(labels[8])}}} (a)
    (t) edge [magenta, {"" if str(origlabels[9])[0] == "0" else "draw,"} bend right=10] node[above left,text=magenta] {{\\Large ~{str(labels[9])}}} (b);
{"}" if not residual else ""}

\\end{{tikzpicture}}
"""

    tex_file = tex_header + tikz1 + "\n\\end{document}"
    with open("reductions.tmp.tex","w") as f:
        f.write(tex_file)
    os.system ("pdflatex reductions.tmp.tex > /dev/null")
    os.system ("inkscape reductions.tmp.pdf --export-type=svg --export-filename=reductions.tmp.svg >& /dev/null")
    with open("reductions.tmp.svg","r") as f:
       svg = f.read()
    where = svg.find("<svg\n")
    xprint(svg[where:],output_filename)


#--------------------------------------------------
# small_images()
#--------------------------------------------------

small_images_dot = {
    'red_A_cylinder': 'graph g { bgcolor=transparent;x [fontname="Arial",shape=cylinder,label=<A>,fontsize=48,style=filled,fillcolor=red]; }',
    'yellow_B_box': 'graph g { bgcolor=transparent;x [fontname="Arial",shape=rect,label=<B>,fontsize=48,style=filled,fillcolor=yellow;height="1.75in";width="1in"]; }',
    'green_C_cylinder': 'graph g { bgcolor=transparent;x [fontname="Arial",shape=rect,label=<C>,fontsize=48,style=filled,fillcolor=green;height="1.75in";width="1in"]; }',
    'red_X_cylinder': 'graph g { bgcolor=transparent;x [fontname="Arial",shape=cylinder,label=<X>,fontsize=48,style=filled,fillcolor=red]; }',
    'yellow_Y_box': 'graph g { bgcolor=transparent;x [fontname="Arial",shape=rect,label=<Y>,fontsize=48,style=filled,fillcolor=yellow;height="1.75in";width="1in"]; }',

}

def small_images():
    for key in small_images_dot.keys():
        g = graphviz.Source(small_images_dot[key],format='svg')
        html = g.pipe(format='svg').decode('utf-8')
        where = html.find("<svg ")
        xprint(html[where:], key)


graph_cut_dot = """graph graph1 {
    // points start at the lower-left and rotate counter-clockwise
    _background="c 7 -#000080  C 7 -#ADD8E6  P 18  -9 100  20 75  50 75  100 140  150 140  250 110  420 110  490 90  515 90  530 110  530 260  480 300  370 300  240 220  220 220  150 288  70 288  -9 220";
    // xdot (aka _background) format specification: https://web.mit.edu/spin_v4.2.5/share/graphviz/doc/html/info/output.html
    layout=sfdp;
    graph[K=1.5];
    node [fontname="Arial",shape=circle,fillcolor=cornflowerblue,style="rounded,filled"];
    edge [fontname="Arial",fontcolor=black;fontsize=24;penwidth=4;color=green];

    E [];
    A [fillcolor=brown];
    D [fillcolor=brown];
    B [fillcolor=brown];
    H [fillcolor=brown];
    I [fillcolor=brown];
    C [];
    F [];
    G [];

    B -- E [label="8";color=purple];
    B -- A [label="10";color=green];
    E -- H [label="8";color=purple];
    E -- D [label="7";color=purple];
    A -- C [label="12    ";color=purple];
    B -- C [label="9 ";color=purple];
    C -- D [label="3";color=purple];
    C -- F [label="1";color=green];
    D -- F [label="3  ";color=purple];
    E -- G [label="5   ";color=green];
    F -- G [label="6";color=green];
    G -- H [label="9";color=purple];
    G -- I [xlabel="    11";label=" ";color=purple];
    H -- I [label="2 ";color=green];
}"""

def graph_cut():
    g = graphviz.Source(graph_cut_dot,format='svg')
    html = g.pipe(format='svg').decode('utf-8')
    where = html.find("<svg ")
    xprint(html[where:], "graph_cut")


#--------------------------------------------------
# main() equivalent
#--------------------------------------------------

if __name__ == "__main__":
    graph_num = 0
    if len(sys.argv) == 2 and sys.argv[1] == "debug":
        output_to_file = False
        #bipartite_graph(13.69,9.69,0,True)
        #flow_graph(1)
        #flow_graph(2)
        #flow_graph(2,True,0,False)
        #flow_graph(1)
        #flow_graph(2,True,1)
        #flow_graph(3,True)
        flow_graph(1)
        #flow_graph(0,True)
        #flow_graph(7,False,4)
        #edge_disjoint_graph(3)
    else:
        os.system("mkdir -p graphs/reductions")
        #graph_cut() # currently using a hand-written version
        arrows()
        bipartite_graph(13.69,9.69,0,True,1)
        bipartite_graph(13.69,9.69,3,True,2)
        bipartite_graph(8.53,9.64,0)
        bipartite_graph(8.53,9.64,1)
        bipartite_graph(8.53,9.64,2)
        bipartite_graph(8.53,9.64,3)
        cpp()
        diamond_flow() # 0,0
        diamond_flow(1,0)
        diamond_flow(1,1)
        diamond_flow(2,2)
        diamond_flow(0,3)
        diamond_flow(0,4,True)
        diamond_flow(0,4,True,2)
        diamond_flow(0,2)
        diamond_flow(0,5,True)
        diamond_flow(0,6)
        diamond_flow(0,7,True)
        diamond_flow(0,7,True,1)
        diamond_flow(3,8,False,1)
        diamond_flow(0,8)
        diamond_flow(0,9,True)
        diamond_flow(0,9,True,2)
        diamond_flow(4,10,True,2)
        diamond_flow(0,10)
        diamond_flow(0,11,True)
        diamond_flow(0,11,True,1)
        edge_disjoint_graph()
        edge_disjoint_graph(0,1)
        edge_disjoint_graph(0,2)
        edge_disjoint_graph(1)
        edge_disjoint_graph(1,0,True)
        edge_disjoint_graph(2)
        edge_disjoint_graph(2,1)
        flow_graph(1)
        flow_graph(2)
        flow_graph(2,False,1)
        flow_graph(2,True)
        flow_graph(2,True,1)
        flow_graph(2,True,0,False)
        flow_graph(3)
        flow_graph(3,False,1)
        flow_graph(3,True)
        flow_graph(4)
        flow_graph(4,True)
        flow_graph(4,True,2)
        flow_graph(5)
        flow_graph(5,False,2)
        flow_graph(5,True)
        flow_graph(5,True,3)
        flow_graph(6)
        flow_graph(6,False,3)
        flow_graph(6,True)
        flow_graph(6,True,4)
        flow_graph(7)
        flow_graph(7,False,4)
        flow_graph(7,True)
        flow_graph(7,True,5)
        flow_graph(8)
        flow_graph(8,False,5)
        flow_graph(8,True)
        flow_graph(1,False,0,True,1)   
        flow_graph(3,False,0,True,2)
        flow_graph(3,False,0,True,3)
        flow_graph(3,False,0,True,4)
        flow_graph(3,True,0,True,3)
        flow_graph(3,True,0,True,4)
        independent_set()
        mini_reduction()
        small_images()
        vertex_cover()
        vertex_disjoint_to_edge_disjoint_graph()
        os.system('inkscape --actions "select-all;transform-rotate:90;export-filename:darrow.svg;export-do" rarrow-square.svg')
