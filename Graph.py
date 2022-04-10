class Graph:
    def __init__(self,edges):
        self.edges = edges
        self.graph = {}
        for start,end in self.edges:
            if start in self.graph:
                self.graph[start].append(end)
            else:
                self.graph[start] = [end]

        # print(self.graph)
#   start = 'Dubai'
#   end = 'Dubai'
#path = ['M','P','D']
    def get_paths(self,start,end,path=[]):

        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph:
            return []
            
        paths = []
        for node in self.graph[start]:
            if node not in path:
                new_path = self.get_paths(node, end,path)
                for p in new_path:
                    paths.append(p)
        return paths

    def shortest_path(self,start,end,path=[]):
        
        path = path + [start]

        if start == end:
            return path

        if start not in self.graph:
            return None

        shortest_paths = None 

        for node in self.graph[start]:
            if node not in path:
                new_path = self.shortest_path(node, end,path)
                if new_path:
                    if shortest_paths is None or len(new_path) < len(shortest_paths):
                        shortest_paths = new_path

        return shortest_paths


if __name__ == '__main__':

    routes = [
        ('Mumbai','Paris'),
        ('Mumbai','Dubai'),
        ('Paris','Dubai'),
        ('Paris','New York'),
        ('Dubai','New York'),
        ('New York','Toronto')
    ]

    graph = Graph(routes)

    start = 'Mumbai'
    end = 'Dubai'

    # All_paths  = graph.get_paths(start, end)

    # print(f'All paths between {start} to {end} :')
    # for i in All_paths:
    #     print('->'.join(i))

    shortest_path = graph.shortest_path(start, end)
    
    print(f'Shortest path between {start} to {end} :')
    print('->'.join(shortest_path))