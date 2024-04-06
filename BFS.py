import networkx
import matplotlib.pyplot as plt
from collections import deque
graph=networkx.DiGraph()
graph.add_node("node1") #增加節點
graph.add_node("node2")
graph.add_nodes_from(["node3","node4","node5","node6","node7"]) #一次增加多組節點
graph.add_edge("node1","node2") #新增connection

graph.add_edges_from([("node1","node3"),("node2","node4"),("node2","node5"),("node3","node6"),("node3","node7")])   #新增多組connections
networkx.draw(graph,with_labels=True)
#networkx.draw_networkx(graph) #same

start="node1"
BFS_list=["node1"]
node=deque(["node1"])
while node:
    y = node.popleft()
    for neighbors in graph.neighbors(y):
        node.append(neighbors)
        if neighbors not in BFS_list:
            BFS_list.append(neighbors)

for h in BFS_list:
    print(h)



plt.show()  #印出

##digraph needed