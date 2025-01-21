class Graph():
    def __init__(self):
        """
        Initialises an empty dict as the graph data structure.
        """
        self.graph_dict = {}
    
    def add_vertex(self, vertex):
        """
        Adds a vertex to the graph.
        
        Args:
            vertex: vertex to be added in the graph
        """
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []
    
    def vertices(self):
        """
        Returns the graph's vertices.
        """
        return list(self.graph_dict.keys())
    
    def add_edge(self, edge, add_reversed=True):
        """
        Adds an edge to the graph.
        
        Args:
            edge: a tupple of two vertices, (first_vertex, second_vertex)
            add_reversed: whether to add the edge in reversed direction, (second_vertex, first_vertex)
        """
        vertex1, vertex2 = edge
        self.graph_dict[vertex1].append(vertex2)
        if add_reversed:
            self.graph_dict[vertex2].append(vertex1)
    
    def edges(self):
        """
        Returns a list of all edges in the graph.
        """
        edges = []
        for vertex in self.graph_dict:
            for neighbour in self.graph_dict[vertex]:
                edges.append((vertex, neighbour))
        return edges
    
    def neighbours(self, vertex):
        """
        Returns all neighbours of the given vertex.
        """
        return self.graph_dict[vertex]
    
    def remove_vertex(self, vertex_to_remove):
        """
        Removes a vertex from the graph.
        
        First, the vertex's list is removed.
        Then, we remove all the occurances of the vertex in another vertex's list.
        
        Args:
            vertex_to_remove: the vertex to be removed.
        """
        del self.graph_dict[vertex_to_remove]
        for vertex in self.vertices():
            if vertex_to_remove in self.graph_dict[vertex]:
                self.graph_dict[vertex].remove(vertex_to_remove)

    def remove_edge(self, edge_to_remove, remove_reversed=True):
        """
        Removes an edge from the graph.
        
        Args:
            edge_to_remove: the edge to be removed
            remove_reversed: whether to remove the edge in reversed direction
        """
        vertex1, vertex2 = edge_to_remove
        if vertex2 in self.graph_dict[vertex1]:
            self.graph_dict[vertex1].remove(vertex2)
        if remove_reversed:
            if vertex1 in self.graph_dict[vertex2]:
                self.graph_dict[vertex2].remove(vertex1)

    def isolated_vertices(self):
        """
        Returns a list of all isolated vertices.
        """
        isolated_vertices = []
        for vertex in self.graph_dict:
            if not self.graph_dict[vertex]:
                isolated_vertices.append(vertex)
        return isolated_vertices


class WeightedGraph:
    def __init__(self):
        """
        Initialises an empty dict as the graph data structure.
        """
        self.graph_dict = {}
    
    def add_vertex(self, vertex):
        """
        Adds a vertex to the graph.
        
        Args:
            vertex: vertex to be added in the graph
        """
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = {}
    
    def vertices(self):
        """
        Returns the graph's vertices.
        """
        return list(self.graph_dict.keys())
    
    def add_edge(self, edge, add_reversed=True):
        """
        Adds an edge to the graph.
        
        Args:
            edge: a tupple of three vertices, (first_vertex, second_vertex, weight)
            add_reversed: whether to add the edge in reversed direction, (second_vertex, first_vertex)
        """
        vertex1, vertex2, weight = edge
        self.graph_dict[vertex1][vertex2] = weight
        if add_reversed:
            self.graph_dict[vertex2][vertex1] = weight
    
    def edges(self):
        """
        Returns a list of all edges in the graph, with respected weights.
        """
        edges = []
        for vertex in self.graph_dict:
            for neighbour, weight in self.graph_dict[vertex].items():
                edges.append((vertex, neighbour, weight))
        return edges
    
    def neighbours(self, vertex):
        """
        Returns all neighbours of the given vertex.
        """
        return list(self.graph_dict[vertex].items())