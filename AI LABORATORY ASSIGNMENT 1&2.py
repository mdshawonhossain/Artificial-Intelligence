
# coding: utf-8

# # PYTHON SYNTEX:

# In[1]:


if 5 > 2:
  print("Five is greater than two!")


# # PYTHON VARIABLE:

# In[2]:


x = "Python is "
y = "awesome"
z =  x + y
print(z)


# # PYTHON NUMBER INT:

# In[3]:


x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))


# # PYTHON NUMBER FLOAT:

# In[4]:


x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))


# # PYTHON NUMBER COMPLEX:

# In[5]:


x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))


# # PYTHON CASTING:

# In[6]:


x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3


# # PYTHON STRING:

# In[ ]:


print("Enter your name:")
x = input()
print("Hello, " + x)


# # PYTHON IF/ELSE:

# In[ ]:


a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")


# # PYTHON LOOP:

# In[ ]:


i = 0
while i < 6:
  i += 1 
  if i == 3:
    continue
  print(i)


# # PYTHON FUNCTION:

# In[ ]:


def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


# # PYTHON CLASS:

# In[ ]:


class Employee:
   
    def __init__(self,id, name,b_salary,sales,department,designation,h_rent,medical,commission):
        self.id = id
        self.name = name
        self.b_salary = b_salary
        self.sales=sales
        self.department=department
        self.designation =designation
        self.h_rent=h_rent
        self.medical=medical
        self.commission=commission
        
    def calculatecomission(self):
        return self.commission*self.sales    
    
    def displayEmp(self):
        print("ID: "+" "+str(self.id)+"\n"+
              "Name: "+" "+str(self.name)+"\n"+ 
              "Department: "+" "+str(self.department)+"\n"+
              "Designation: " + " "+ str(self.designation)+"\n"+
              "Basic: "+str(self.b_salary)+"\n"
              +"Sales: "+" "+str(self.sales)+"\n"+
              "Houserent: "+str(self.h_rent)+"\n"+ 
              "Medical: "+" "+str(self.medical)+"\n"+
              "Commission: "+" "+str(self.commission*self.sales)+"\n\n")
     
    
        
emp = Employee(1001,"Faisal",10000,25000,"Sales","Executive",5000,500,.2)
emp1= Employee(1002,"Shawon",20000,15000,"Sales","Executive",10000,1000,.3)
emp.displayEmp()
emp1.displayEmp()


# # PYTHON GRAPH COLOR:

# In[ ]:


def color_nodes(graph):
  # Order nodes in descending degree
  nodes = sorted(list(graph.keys()), key=lambda x: len(graph[x]), reverse=True)
  color_map = {}

  for node in nodes:
    available_colors = [True] * len(nodes)
    for neighbor in graph[node]:
      if neighbor in color_map:
        color = color_map[neighbor]
        available_colors[color] = False
    for color, available in enumerate(available_colors):
      if available:
        color_map[node] = color
        break

  return color_map


if __name__ == '__main__':
  graph = {
    'w': list('ns'),
    's': list('wnvqm'),
    'n': list('wsq'),
    'q': list('nsm'),
    'm': list('sqv'),
    'v': list('sm')
  }
  print(color_nodes(graph))


# # PYTHON BFS:

# In[ ]:


def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

bfs(graph, 'A') # {'B', 'C', 'A', 'F', 'D', 'E'}


# # PYTHON DFS:

# In[ ]:


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

dfs(graph, 'C') # {'E', 'D', 'F', 'A', 'C', 'B'}


# # PYTHON DLS/IDDFS:

# In[ ]:


# Python program to print DFS traversal from a given 
# given graph 
from collections import defaultdict 
  
# This class represents a directed graph using adjacency 
# list representation 
class Graph: 
  
    def __init__(self,vertices): 
  
        # No. of vertices 
        self.V = vertices 
  
        # default dictionary to store graph 
        self.graph = defaultdict(list) 
  
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    # A function to perform a Depth-Limited search 
    # from given source 'src' 
    def DLS(self,src,target,maxDepth): 
  
        if src == target : return True
  
        # If reached the maximum depth, stop recursing. 
        if maxDepth <= 0 : return False
  
        # Recur for all the vertices adjacent to this vertex 
        for i in self.graph[src]: 
                if(self.DLS(i,target,maxDepth-1)): 
                    return True
        return False
  
    # IDDFS to search if target is reachable from v. 
    # It uses recursive DLS() 
    def IDDFS(self,src, target, maxDepth): 
  
        # Repeatedly depth-limit search till the 
        # maximum depth 
        for i in range(maxDepth): 
            if (self.DLS(src, target, i)): 
                return True
        return False
  
# Create a graph given in the above diagram 
g = Graph (7); 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 3) 
g.addEdge(1, 4) 
g.addEdge(2, 5) 
g.addEdge(2, 6) 
  
target = 6; maxDepth = 3; src = 0
  
if g.IDDFS(src, target, maxDepth) == True: 
    print ("Target is reachable from source " +
        "within max depth") 
else : 
    print ("Target is NOT reachable from source " + "within max depth")  




# # PYTHON A*:

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
class Node:
    def __init__(self,value,point):
        self.value = value
        self.point = point
        self.parent = None
        self.H = 0
        self.G = 0
    def move_cost(self,other):
        return 0 if self.value == '.' else 1
        
def children(point,grid):
    x,y = point.point
    links = [grid[d[0]][d[1]] for d in [(x-1, y),(x,y - 1),(x,y + 1),(x+1,y)]]
    return [link for link in links if link.value != '%']
def manhattan(point,point2):
    return abs(point.point[0] - point2.point[0]) + abs(point.point[1]-point2.point[0])
def aStar(start, goal, grid):
    #The open and closed sets
    openset = set()
    closedset = set()
    #Current point is the starting point
    current = start
    #Add the starting point to the open set
    openset.add(current)
    #While the open set is not empty
    while openset:
        #Find the item in the open set with the lowest G + H score
        current = min(openset, key=lambda o:o.G + o.H)
        #If it is the item we want, retrace the path and return it
        if current == goal:
            path = []
            while current.parent:
                path.append(current)
                current = current.parent
            path.append(current)
            return path[::-1]
        #Remove the item from the open set
        openset.remove(current)
        #Add it to the closed set
        closedset.add(current)
        #Loop through the node's children/siblings
        for node in children(current,grid):
            #If it is already in the closed set, skip it
            if node in closedset:
                continue
            #Otherwise if it is already in the open set
            if node in openset:
                #Check if we beat the G score 
                new_g = current.G + current.move_cost(node)
                if node.G > new_g:
                    #If so, update the node to have a new parent
                    node.G = new_g
                    node.parent = current
            else:
                #If it isn't in the open set, calculate the G and H score for the node
                node.G = current.G + current.move_cost(node)
                node.H = manhattan(node, goal)
                #Set the parent to our current item
                node.parent = current
                #Add it to the set
                openset.add(node)
    #Throw an exception if there is no path
    raise ValueError('No Path Found')
def next_move(pacman,food,grid):
    #Convert all the points to instances of Node
    for x in xrange(len(grid)):
        for y in xrange(len(grid[x])):
            grid[x][y] = Node(grid[x][y],(x,y))
    #Get the path
    path = aStar(grid[pacman[0]][pacman[1]],grid[food[0]][food[1]],grid)
    #Output the path
    print len(path) - 1
    for node in path:
        x, y = node.point
        print x, y
pacman_x, pacman_y = [ int(i) for i in raw_input().strip().split() ]
food_x, food_y = [ int(i) for i in raw_input().strip().split() ]
x,y = [ int(i) for i in raw_input().strip().split() ]
 
grid = []
for i in xrange(0, x):
    grid.append(list(raw_input().strip()))
 
next_move((pacman_x, pacman_y),(food_x, food_y), grid)


# # PYTHON GREEDY:

# In[ ]:


smalls = [1]
smallf = [0, 4]

start = [0, 1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
finish = [0, 4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]

def recursive_activity_selector(s, f, k, n):
    """
        Args:
            s: a list of start times
            f: a list of finish times
            k: current position in
            n: total possible activities
        Returns:
            A maximal set of activities that can be scheduled.
            (We use a list to hold the set.)
    """
    m = k + 1
    while m < n and s[m] < f[k]:  # find an activity starting after our last
                                   # finish
        m = m + 1
    if m < n:
        print("Adding activity " + str(m) + " that finishes at "
              + str(f[m]))
        return [m] + recursive_activity_selector(s, f, m, n)
    else:
        return []


def greedy_activity_selector(s, f):
    """
        Args:
            s: a list of start times
            f: a list of finish times
        Returns:
            A maximal set of activities that can be scheduled.
            (We use a list to hold the set.)
    """
    assert(len(s) == len(f))  # each start time must match a finish time
    n = len(s)  # could be len f as well!
    a = []
    k = 0
    for m in range(1, n):
        if s[m] >= f[k]:
            a.append(m)
            k = m
    return a

