###############
#implementation of graph using lists 
from multipledispatch import dispatch
nodes = []
graph = []
node_count = 0

# insertion in graph
def add_node(v):
    global node_count
    if v in nodes:
        print(v, "already present")
    else:
        node_count = node_count + 1
        nodes.append(v)
        for i in graph:
            i.append(0)
        temp = []
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)


def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(graph[i][j], end=" ")
        print()


# for undirected and unweighted graph
@dispatch(str, str)
def add_edge(v1, v2):
    if v1 not in nodes:
        print(v1, "node not present")

    elif v2 not in nodes:
        print(v2, "node not present")

    else:
        list1 = nodes.index(v1)
        list2 = nodes.index(v2)
        graph[list1][list2] = 1
        graph[list2][list1] = 1


# for undirected and weighted graph
@dispatch(str, str, int)
def add_edge(v1, v2, cost):
    if v1 not in nodes:
        print(v1, "node not present")

    elif v2 not in nodes:
        print(v2, "node not present")

    else:
        list1 = nodes.index(v1)
        list2 = nodes.index(v2)
        graph[list1][list2] = cost
        graph[list2][list1] = cost


# for directed and weighted graph

@dispatch(str, str, int)
def add_edge(v1, v2, cost):
    if v1 not in nodes:
        print(v1, "node not present")

    elif v2 not in nodes:
        print(v2, "node not present")

    else:
        list1 = nodes.index(v1)
        list2 = nodes.index(v2)
        graph[list1][list2] = cost



# #################################
#implementation of graph using dictionary

from multipledispatch import dispatch
graph = {}
node_count = 0


def add_node1(v):
    if v in graph:
        print(v, "already present")
    else:
        graph[v] = []

@dispatch(str, str)
def add_edge1(v1, v2):
    if v1 not in graph:
        print(v1, "node not present")

    elif v2 not in graph:
        print(v2, "node not present")

    else:
        graph[v1].append(v2)
        graph[v2].append(v1)


@dispatch(str, str, int)
def add_edge1(v1, v2, cost):
    if v1 not in graph:
        print(v1, "node not present")

    elif v2 not in graph:
        print(v2, "node not present")

    else:
        list1 = [v2, cost]
        list2 = [v1, cost]
        graph[v1].append(list1)
        graph[v2].append(list2)

# implementation of DFS
def DFSiterative(node, graph):
    visited = set()
    if node not in graph:
        print("node not present")
        return
    stack = []
    stack.append(node)
    while stack:
        current = stack.pop()
        if current not in visited:
            print(current)
            visited.add(current)
            for i in graph[current]:
                stack.append(i)

# deletion of nodes
def delete_node(v):
    global node_count
    if v not in nodes:
        print("node not present")
    else:
        index1 = nodes.index(v)
        node_count = node_count - 1
        nodes.remove(v)
        graph.pop(index1)
        for i in graph:
            i.pop(index1)

# deletion of edges
def delete_edge(v1, v2):
    if v1 not in graph:
        print(v1, "node not present")

    elif v2 not in graph:
        print(v2, "node not present")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = 0
        graph[index2][index1] = 0

# traversal
def DFS(node, visited, graph):
    if node not in graph:
        print("nodes not present")
        return
    if node not in visited:
        print(node)
        visited.add(node)
        for i in graph[node]:
            DFS(i, visited, graph)


def delete_node(v):
    if v not in graph:
        print("nodes not present")
        return
    else:
        graph.pop(v)
        for i in graph:
            list1 = graph[i]
            if v in list1:
    
              list1.remove(v)
def delete_edge(v1, v2):
    if v1 not in graph:
        print(v1, "node not present")

    elif v2 not in graph:
        print(v2, "node not present")

    else:
        if v2 in graph[v1]:
            graph[v1].remove(v2)
            graph[v2].remove(v1)

visited = set()

add_node("A")
add_node("B")

print(graph)
DFSiterative("A", graph)
list = []
list.append(10)
print(list)
