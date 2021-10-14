import GraphMesh
import sys

print(sys.argv)
height = int(sys.argv[1])
width = int(sys.argv[2])

graph = GraphMesh.GraphMesh(height,width)
graph.fullramdon()
graph.show()
newgraph = graph.kruskal()
newgraph.show()
newgraph.short_find()