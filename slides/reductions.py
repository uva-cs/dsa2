import re, graphviz

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
    # if width & height are given in inches, conver it to pixels (96 dpi)
    if w < 20:
        w *= 96
    if h < 20:
        h *= 96
    # which coloring are we using?
    assert coloring >= 0 and coloring < len(preset_colors)
    # generate the graph
    g = graphviz.Source(bipartite_graph_dot(coloring,flow_graph),format='svg')
    html = g.pipe(format='svg').decode('utf-8')
    html = re.sub(r'<svg width="[0-9]+pt" height="[0-9]+pt"', f'<svg width="{w}" height="{h}"', html)
    where = html.find("<svg ")
    if flow_graph:
        table_header = "<table style=\"width:55% !important;margin-bottom:15px !important;margin-left:112px\">"
    else:
        table_header = "<table style=\"margin-top:75px !important\">"
    print(div_header(w,h) + html[where:] + div_footer + table_header + bipartite_image_table_body + "</table>")





if __name__ == "__main__":
    bipartite_graph(13.69,9.69,0,True)









