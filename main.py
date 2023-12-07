from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
  short_distance = {}

  for vertex in graph:
    short_distance[vertex] = (float('inf'), float('inf'))

  priority_queue = [(0, 0, source)]
  short_distance[source] = (0, 0)

  while priority_queue:
    current_distance, current_edges, current_vertex = heappop(priority_queue)
        
    if (current_distance, current_edges) <= short_distance[current_vertex]:
       for neighbor, edge_weight in graph[current_vertex]:
        new_distance = current_distance + edge_weight
        new_edges = current_edges + 1
                
        if (new_distance, new_edges) < short_distance[neighbor]:
          short_distance[neighbor] = (new_distance, new_edges)
          heappush(priority_queue, (new_distance, new_edges, neighbor))

  return short_distance

  """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
  """
    ### TODO
  pass
  

    
    
def bfs_path(graph, source):
  parent = {}

  for vertex in graph:
    parent[vertex] = None
    
  queue = deque([source])
  visited = {source}

  while queue:
    current_vertex = queue.popleft()
    
    for neighbor in graph[current_vertex]:
       if neighbor not in visited:
        visited.add(neighbor)
        parent[neighbor] = current_vertex
        queue.append(neighbor)
        
  return parent
  """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
  """
    ###TODO
  pass

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }


    
def get_path(parents, destination):
  shortest_path = []
  current_node = destination

  while current_node is not None:
    shortest_path.insert(0, current_node)
    current_node = parents[current_node]

  return ''.join(shortest_path[:-1])
    
  """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
  """
    ###TODO
  pass

