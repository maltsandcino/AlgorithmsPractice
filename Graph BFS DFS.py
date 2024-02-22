## Task one depth first traversal print
from collections import deque
import pprint

def depth_first_print(graph, source):
    stack = [source]

    while len(stack) > 0:
        current = stack.pop()
        print(current)
        for neighbour in graph[current]:
            stack.append(neighbour)
            ##add all neighbours to stack in order to be one by one popped off, traversed, and printed

###FOR DIRECTED GRAPHS ONLY
def depth_first_print_recursive(graph, source):
    print(source)
    for neighbour in graph[source]:
        depth_first_print_recursive(graph, neighbour)
###FOR DIRECTED GRAPHS ONLY
def breadth_first_print(graph, source):
    queue = deque()
    queue.append(source)
    
    while (len(queue) > 0):
        current = queue.popleft()
        print(current)
        for neighbour in graph[current]:
            queue.append(neighbour)

def depth_has_path(graph, source, end):
  
    if source == end:
        return True
    for neighbour in graph[source]:
        if depth_has_path(graph, neighbour, end) == True:
            return True
    return False

def breadth_has_path(g, s, d):
    q = deque()
    q.append(s)
    while len(q) > 0:
        c = q.popleft()
        if c == d: 
            return True
        for neighbour in g[c]:
            q.append(neighbour)
    return False



graph = {
    'a': ['c', 'b'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

# depth_first_print_recursive(graph, 'a')
breadth_first_print(graph, 'a')

# --------------------------

print(breadth_has_path(graph, 'a', 'f'))

edges = [('i', 'j'), 
        ('k', 'i'),
        ('m', 'k'),
        ('k', 'l'),
        ('o', 'n')]

class Graph:
      def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start == end:
                    if start in self.graph_dict and end not in self.graph_dict[start]:
                        self.graph_dict[start].append(end)
                        break
                    else:
                        self.graph_dict[start] = [end]
                        break 
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]                
            if end in self.graph_dict[start]:
                if end in self.graph_dict:
                    self.graph_dict[end].append(start)
                else:
                    self.graph_dict[end] = [start]

def df_undirected_path(graph, A, B):
    return hasPath(graph, A, B)

def hasPath(Graph, A, B, visited=set()):
    ###We don't want to visit nodes multiple times, otherwise we get an infinite loop
    visited.add(A)
    if A == B:
        return True
    for neighbour in Graph[A]:
        if neighbour not in visited:
            if hasPath(Graph, neighbour, B):
                return True
    
    return False


my_graph = Graph(edges)
pp = pprint.PrettyPrinter(indent=4)

gdict = my_graph.graph_dict
# # print(my_graph.graph_dict)
pp.pprint(gdict)

# print(df_undirected_path(gdict, 'i', 'm'))

## ------- Connected Components Count

new_edges = [['1', '2'],
          ['6', '4'],
          ['6', '8'],
          ['6', '7'],
          ['6', '5'],
          ['3', '3']]

###Helper DFS For Component Count Function
def explore(graph, current, visited):
        if current in visited:
            return False
        visited.add(current)
        for neighbour in graph[current]:
            explore(graph, neighbour, visited)
        return True

def connected_components_count(graph):
    component_count = 0
    visited = set()

    node_list = graph.keys()
    
    for node in node_list:    
        if explore(graph, node, visited) == True:
            component_count += 1
    
    return component_count


### --- find largest component

def largest_component(graph):
    visited = set()
    component_set = set()

    def node_traversal(graph, current, component_set):
        if current in component_set: 
            return False
        component_set.add(current)
        for neighbour in graph[current]:
            node_traversal(graph, neighbour, component_set)
        return True

    for node in graph.keys():
        if node not in visited:
            if node_traversal(graph, node, component_set) == True:
                if len(component_set) > len(visited):
                    visited = component_set.copy()
                component_set.clear()
    
    return len(visited)
        
    

new_graph = Graph(new_edges)
new_graph = new_graph.graph_dict
print(connected_components_count(gdict))

# pp.pprint(new_graph.graph_dict)


bcgraph = [['0', '8'],
           ['0', '1'],
           ['0', '5'],
           ['5', '8'],
           ['2', '3'],
           ['2', '4'],
           ['3', '4']]

latest_graph = Graph(bcgraph)
latest_graph = latest_graph.graph_dict
# pp.pprint(latest_graph)

# print(largest_component(new_graph))

###Shortest Path Algorithm

spath_edges = [['w', 'x'],
               ['x', 'y'],
               ['z', 'y'],
               ['z', 'v'],
               ['w', 'v'],
               ['a', 'a']]

spath_graph = Graph(spath_edges)
spath_graph = spath_graph.graph_dict
pp.pprint(spath_graph)

# We want to return the shortest path length, i.e. number of edges
# More efficient to do a breadth first traversal in this scenario

def shortest_path(graph, start, end):
    q = deque([(start, 0)])
    visited = set()

    while q:
        c, steps = q.popleft()
        visited.add(c)
        
        if c == end: 
            return steps
        
        for neighbour in graph[c]:
            if neighbour not in visited:
                q.append((neighbour, steps + 1))

    return -1

print(shortest_path(spath_graph, 'w', 'a'))



