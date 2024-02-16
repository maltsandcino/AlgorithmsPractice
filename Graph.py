
#This is a directed Graph 

class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
            ## Commenting out section of code to make graph bi-directional
                
            # if end in self.graph_dict[start]:
            #     if end in self.graph_dict:
            #         self.graph_dict[end].append(start)
            #     else:
            #         self.graph_dict[end] = [start]
                
        
    
    ### Function to find path
    def get_path(self, start, end, path=[]):
        ###Add starting point to path. If its the same as the end, we just return it. path is in the parameters as an empty list initially, otherwise it would have to be passed as an empty list when claling the function.
        path = path + [start]
        
        ## Base case, return the path
        if start == end:
            return [path]
        
        ## Check if the starting point is even in the graph, has to happen after above otherwise it will cause an error when making the final path element
        if start not in self.graph_dict:
            return "Not a starting location"
        
        ## Begin recursion when start isn't end. Paths will contain all of our paths we make, as we can make multiple paths as long as the connections exist
        paths = []
        for node in self.graph_dict[start]:
            ##Checking to see if node is visited already
            if node not in path:
                ### recurse by making the first node in the dict the start, the end is the same, and the PATH is passed in order to continue adding path elements
                new_paths = self.get_path(node, end, path)
                ### append new elements to PATHS
                for p in new_paths:
                    paths.append(p)
        
        return paths

    def get_shortest_path(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return path
        
        if start not in self.graph_dict:
            return None
        
        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp
        
        return shortest_path


        
        



if __name__ == "__main__":
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]

route_graph = Graph(routes)

print(route_graph.edges)
start = "Mumbai"
end = "New York"
print(f"Paths between {start} and {end}: ", route_graph.get_shortest_path(start, end))