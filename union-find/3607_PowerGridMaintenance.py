import heapq
import sys
from collections import defaultdict
from typing import List, Dict

# Increase recursion limit to handle deep DFS in large power grids
sys.setrecursionlimit(200000)

class Vertex:
    def __init__(self, vertex_id: int):
        self.vertex_id = vertex_id
        self.offline = False
        self.grid_id = -1

class Graph:
    def __init__(self):
        self.adj = defaultdict(list)
        self.vertices = {}

    def add_vertex(self, node_id: int, vertex_obj: Vertex):
        self.vertices[node_id] = vertex_obj

    def add_edge(self, u: int, v: int):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def get_vertex(self, node_id: int) -> Vertex:
        return self.vertices[node_id]

    def get_adj(self, node_id: int) -> List[int]:
        return self.adj[node_id]

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        # 1. Build the graph Adjacency List
        graph = Graph()
        for i in range(1, c + 1):
            graph.add_vertex(i, Vertex(i))
        for u, v in connections:
            graph.add_edge(u, v)

        # 2. Pre-process Connected Components (Grids) using DFS
        # We store each grid's station IDs in a Min-Heap for O(log N) access to the smallest ID.
        grids = {} 
        grid_id_counter = 0

        def traverse(u_id, g_id, grid_heap):
            u_node = graph.get_vertex(u_id)
            u_node.grid_id = g_id
            heapq.heappush(grid_heap, u_id)
            for v_id in graph.get_adj(u_id):
                if graph.get_vertex(v_id).grid_id == -1:
                    traverse(v_id, g_id, grid_heap)

        for i in range(1, c + 1):
            v_node = graph.get_vertex(i)
            if v_node.grid_id == -1:
                new_heap = []
                traverse(i, grid_id_counter, new_heap)
                grids[grid_id_counter] = new_heap
                grid_id_counter += 1

        # 3. Process Queries
        ans = []
        for op, x in queries:
            v_node = graph.get_vertex(x)
            if op == 1: # Maintenance Check
                # Rule: If online, resolve by itself.
                if not v_node.offline:
                    ans.append(v_node.vertex_id)
                else:
                    # Rule: If offline, resolve by the smallest ID operational station in the same grid.
                    grid_heap = grids[v_node.grid_id]
                    # LAZY DELETION: discard any nodes from the top of the heap if they have gone offline.
                    while grid_heap and graph.get_vertex(grid_heap[0]).offline:
                        heapq.heappop(grid_heap)
                    
                    ans.append(grid_heap[0] if grid_heap else -1)
            
            elif op == 2: # Station goes Offline
                v_node.offline = True
                
        return ans