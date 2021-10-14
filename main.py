import GraphMesh

graph = GraphMesh.GraphMesh(10,10)
graph.fullramdon()
graph.show()
newgraph = graph.kruskal()
newgraph.show()
newgraph.short_find()