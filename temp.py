# def bfs(visited, graph, node):
#     visited.append(node)  # Append the visited node to the visited list
#     queue.append(node)    # Append the visited node to the queue list

#     while queue:  # Run a while loop until the queue is not empty
#         s = queue.pop(0)    # Remove the first element from the queue and assign it to 's'
#         print(s, end = " ") # Print the visited node

#         for neighbour in graph[s]:  # Run a for loop for each neighbour of 's'
#             if neighbour not in visited:  # Check if the neighbour has not been visited
#                 visited.append(neighbour)  # Append the neighbour to the visited list
#                 queue.append(neighbour)    # Append the neighbour to the queue list

def bfs(visited, graph, node,queue):
     queue.append(node)
     while queue:
           temp = queue.pop(0)
           if temp not in visited:
               for i in graph[temp]:
                     queue.append(i)
               print(temp)
               visited.append(temp)
           
# Example graph
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = []  # List for visited nodes.
queue = []    # Initialize a queue

# Driver Code
print("Following is the Breadth-First Search:")
bfs(visited, graph, '5',queue)  # Function calling
