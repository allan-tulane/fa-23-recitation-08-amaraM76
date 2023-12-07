# CMPS 2200 Recitation 08

## Answers

**Name:**___Amara Midouhas______________________
**Name:**_________________________


Place all written answers from `recitation-08.md` here for easier grading.



- **1b)** The work is O(E + V log V). E represents Edges and V vertex. The worst case for the heap operations would be if has to go through all the vertex so O(V log V). Then in the main loop for neighbor, edge_weight in graph[current_vertex]: , the worst case would be if it has to go through each edge so O(E). 
Then since its sequential the span is also O(E + V log V)



- **2b)** The get path is a way to make the parent dictionary from BFS more readable. As it will begin with the destination node and will trace backwards and each node it encounters it will insert in the beginning of the path list so that nodes are in reverse order (destination to source) and it will do this until it reaches the source node. Then it will get rid of the source node because it has a none parent which was used in bfs to end the tracing back process. Then at the end it will put everything as a string to show the actual shortest path from source to destination 
