import re, graphviz, os

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

graph_num = 0
cache_dir = ".graph-cache"

def reset_graph_num():
    global graph_num
    graph_num = 0

def check_if_in_cache(graph_num,file):
    os.system(f"mkdir -p {cache_dir}")
    source_name = f"{cache_dir}/graph-{graph_num}"
    svg_name = source_name + ".svg"
    if not os.path.exists(source_name):
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

def bipartite_graph_dot(coloring,flow_graph):
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
     edge [minlen=4,xlabel="1"];
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
    l1 -- r1 [color={colors[0]}];
    l1 -- r2 [style=invis];
    l1 -- r3 [style=invis];
    l1 -- r4 [color={colors[1]}];
    l2 -- r1 [color={colors[2]}];
    l2 -- r2 [color={colors[3]}];
    l2 -- r3 [color={colors[4]}];
    l2 -- r4 [style=invis];
    l3 -- r1 [color={colors[5]}];
    l3 -- r2 [style=invis];
    l3 -- r3 [color={colors[6]}];
    l3 -- r4 [style=invis];
    l4 -- r1 [color={colors[7]}];
    l4 -- r2 [color={colors[8]}];
    l4 -- r3 [style=invis];
    l4 -- r4 [style=invis];
    // to keep the bottom nodes on the bottom
    l4 -- end [style=invis];
    r4 -- end [style=invis];
    end [shape=none,label="",width="0in"];
}}
"""
    return ret

def div_header(w,h):
    return f"""<div class="cell" data-fig-width="{w}" data-fig-height="{h}" data-layout-align="default">
<div class="cell-output-display">
<div>
<figure class="">
<div>"""

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

def bipartite_graph(w,h,coloring,flow_graph):
    global graph_num
    # if width & height are given in inches, conver it to pixels (96 dpi)
    if w < 20:
        w *= 96
    if h < 20:
        h *= 96
    # which coloring are we using?
    assert coloring >= 0 and coloring < len(preset_colors)
    # generate the graph
    dot_source = bipartite_graph_dot(coloring,flow_graph)
    html = check_if_in_cache(graph_num,dot_source)
    if not html:
        g = graphviz.Source(dot_source,format='svg')
        html = g.pipe(format='svg').decode('utf-8')
        register_in_cache(graph_num,dot_source,html)
    html = re.sub(r'<svg width="[0-9]+pt" height="[0-9]+pt"', f'<svg width="{w}" height="{h}"', html)
    where = html.find("<svg ")
    if flow_graph:
        table_header = "<table style=\"width:55% !important;margin-bottom:15px !important;margin-left:112px\">"
    else:
        table_header = "<table style=\"margin-top:75px !important\">"
    print(div_header(w,h) + html[where:] + div_footer + table_header + bipartite_image_table_body + "</table>")
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
                positioning}  % for nodes positioning
\\begin{document}
"""

def tec(labels,i,hide): # tec == tikz_edge_color
    label = labels[i]
    #if not hide:
    #    return "black"
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


def flow_graph_tikz(labels, res, revres, revlabels, highlights): # labels, residual, reverse-residual, reverse-residual labels
    ret = f"""
\\begin{{tikzpicture}}[
     C/.style = {{circle, draw, very thick, minimum size = 8mm, node distance = 20mm, fill=CornflowerBlue}},
     every edge/.style = {{->, draw, ultra thick, -stealth}},
]

\\tikzset{{font=\\sffamily}}

\\node (a) [C] {{a}};
\\node (b) [C, right=of a] {{b}};
\\node (t) [C, fill=Blue, text=white, right=of b] {{t}};
\\node (s) [C, fill=Plum, text=white, below left=of a] {{s}};
\\node (c) [C, right=of s] {{c}};
\\node (d) [C, right=of c] {{d}};
"""
    if not revres:
        # this has (mostly) straight edges
        if res:
            ret += "\\tikzset{text=orange}\n\\path[orange]\n"
        else:
            ret += "\\path\n"
        ret += f"""
    (s) edge[{tch('s','a','b',highlights)} {tec(labels,0,res)}] node[above left] {{{str(labels[0])}}} (a)
    (s) edge[{tch('s','c','b',highlights)} {tec(labels,1,res)} bend left=15] node[above] {{{str(labels[1])}}} (c)
    (c) edge[{tch('c','s','b',highlights)} {tec(labels,2,res)} bend left=15] node[below] {{{str(labels[2])}}} (s)
    (c) edge[{tch('c','a','b',highlights)} {tec(labels,3,res)}] node[right] {{{str(labels[3])}}} (a)
    (a) edge[{tch('a','b','b',highlights)} {tec(labels,4,res)}] node[above] {{{str(labels[4])}}} (b)
    (b) edge[{tch('b','c','b',highlights)} {tec(labels,5,res)}] node[above] {{{str(labels[5])}}} (c)
    (c) edge[{tch('c','d','b',highlights)} {tec(labels,6,res)}] node[below] {{{str(labels[6])}}} (d)
    (d) edge[{tch('d','b','b',highlights)} {tec(labels,7,res)} bend left=15] node[left] {{{str(labels[7])}}} (b)
    (b) edge[{tch('b','d','b',highlights)} {tec(labels,8,res)} bend left=15] node[above right] {{{str(labels[8])}}} (d)
    (b) edge[{tch('b','t','b',highlights)} {tec(labels,9,res)}] node[above] {{{str(labels[9])}}} (t)
    (d) edge[{tch('d','t','b',highlights)} {tec(labels,10,res)}] node[below right] {{{str(labels[10])}}} (t);

"""
    else:
        ret += f"""
\\path[orange]
    (s) edge[{tch('s','a','o',highlights)} {tec(labels,0,res)} bend left=15] node[above left] {{{str(labels[0])}}} (a)
    (s) edge[{tch('s','c','o',highlights)} {tec(labels,1,res)} bend left=30] node[above] {{{str(labels[1])}}} (c)
    (c) edge[{tch('c','s','o',highlights)} {tec(labels,2,res)} bend left=10] node[below] {{{str(labels[2])}}} (s)
    (c) edge[{tch('c','a','o',highlights)} {tec(labels,3,res)} bend left=15] node[right] {{{str(labels[3])}}} (a)
    (a) edge[{tch('a','b','o',highlights)} {tec(labels,4,res)} bend left=15] node[above] {{{str(labels[4])}}} (b)
    (b) edge[{tch('b','c','o',highlights)} {tec(labels,5,res)} bend left=15] node[above left] {{{str(labels[5])}}} (c)
    (c) edge[{tch('c','d','o',highlights)} {tec(labels,6,res)} bend left=15] node[below] {{{str(labels[6])}}} (d)
    (d) edge[{tch('d','b','o',highlights)} {tec(labels,7,res)} bend left=30] node[left] {{{str(labels[7])}}} (b)
    (b) edge[{tch('b','d','o',highlights)} {tec(labels,8,res)} bend left=10] node[above right] {{{str(labels[8])}}} (d)
    (b) edge[{tch('b','t','o',highlights)} {tec(labels,9,res)} bend left=15] node[above] {{{str(labels[9])}}} (t)
    (d) edge[{tch('d','t','o',highlights)} {tec(labels,10,res)} bend left=15] node[below right] {{{str(labels[10])}}} (t);

"""

    if revres:
        ret += f"""
\\tikzset{{text=magenta}}
\\draw[magenta]
    (a) edge[{tch('a','s','m',highlights)}{tec(revlabels,0,revres)} bend left=15] node[above left] {{{revlabels[0]}}} (s)
    (c) edge[{tch('c','s','m',highlights)}{tec(revlabels,1,revres)} bend right=10] node[above] {{{revlabels[1]}}} (s)
    (s) edge[{tch('s','c','m',highlights)}{tec(revlabels,2,revres)} bend right=30] node[below] {{{revlabels[2]}}} (c)
    (a) edge[{tch('a','c','m',highlights)}{tec(revlabels,3,revres)} bend left=15] node[right] {{{revlabels[3]}}} (c)
    (b) edge[{tch('b','a','m',highlights)}{tec(revlabels,4,revres)} bend left=15] node[above] {{{revlabels[4]}}} (a)
    (c) edge[{tch('c','b','m',highlights)}{tec(revlabels,5,revres)} bend left=15] node[above] {{{revlabels[5]}}} (b)
    (d) edge[{tch('d','c','m',highlights)}{tec(revlabels,6,revres)} bend left=15] node[below] {{{revlabels[6]}}} (c)
    (b) edge[{tch('b','d','m',highlights)}{tec(revlabels,7,revres)} bend right=10] node[left] {{{revlabels[7]}}} (d)
    (d) edge[{tch('d','b','m',highlights)}{tec(revlabels,8,revres)} bend right=30] node[above right] {{{revlabels[8]}}} (b)
    (t) edge[{tch('t','b','m',highlights)}{tec(revlabels,9,revres)} bend left=15] node[above] {{{revlabels[9]}}} (b)
    (t) edge[{tch('t','d','m',highlights)}{tec(revlabels,10,revres)} bend left=15] node[below right] {{{revlabels[10]}}} (d);
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


def flow_graph(label_set,residual=False,highlight_set=0,revresidual=True):
    global graph_num
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
        tex_file = tex_header + flow_graph_tikz(revflowedgelabels,residual,revresidual,flowedgelabels,highlights) + "\n\\end{document}"
    elif residual:
        tex_file = tex_header + flow_graph_tikz(revflowedgelabels,residual,revresidual,flowedgelabels,highlights) + "\n\\end{document}"
    else:
        tex_file = tex_header + flow_graph_tikz(edgelabels,residual,revresidual,revflowedgelabels,highlights) + "\n\\end{document}"
    cached = check_if_in_cache(graph_num,tex_file)
    if not cached:
        with open("reductions.tmp.tex","w") as f:
            f.write(tex_file)
        os.system ("pdflatex reductions.tmp.tex > /dev/null")
        os.system ("inkscape reductions.tmp.pdf -n 1 --export-type=svg --export-filename=reductions.tmp.svg >& /dev/null")
        with open("reductions.tmp.svg","r") as f:
           svg = f.read()
        where = svg.find("<svg\n")
        register_in_cache(graph_num,tex_file,svg[where:])
        print(svg[where:])
        pass
    else:
        print(cached)
        pass
    graph_num += 1


if __name__ == "__main__":
    graph_num = 0
    #bipartite_graph(13.69,9.69,0,True)
    #flow_graph(1)
    #flow_graph(2)
    #flow_graph(2,True,0,False)
    #flow_graph(1)
    #flow_graph(2,True,1)
    #flow_graph(3,True)
    #flow_graph(0,True)
    flow_graph(7,False,4)






