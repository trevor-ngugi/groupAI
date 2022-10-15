graph=[['Strathmore Sports Complex','Siwaka',450],
       ['Siwaka','Ph.1 A',10],
       ['Siwaka','Ph.1 B',230],
       ['Ph.1 A','Mada',850],
       ['Ph.1 A','Ph.1 B',100],
       ['Ph.1 B','Phase 2',112],
       ['Ph.1 B','STC',50],
       ['Phase 2','STC',50],
       ['Phase 2','J1',600],
       ['Phase 2','Phase 3',500],
       ['J1','Mada',200],
       ['STC','Parking Lot',250],
       ['Phase 3','Parking Lot',350],
       ['Mada','Parking Lot',700]]
temp = []
temp1 = []
for i in graph:
  temp.append(i[0])
  temp1.append(i[1])
nodes = set(temp).union(set(temp1))
def UCS(graph, costs, open, closed, cur_node):
  if cur_node in open:
    open.remove(cur_node)
  closed.add(cur_node)
  for i in graph:
    if(i[0] == cur_node and costs[i[0]]+i[2] < costs[i[1]]):
      open.add(i[1])
      costs[i[1]] = costs[i[0]]+i[2]
      path[i[1]] = path[i[0]] + ' -> ' + i[1]
  costs[cur_node] = 999999
  small = min(costs, key=costs.get)
  if small not in closed:
    UCS(graph, costs, open,closed, small)
costs = dict()
temp_cost = dict()
path = dict()
for i in nodes:
  costs[i] = 999999
  path[i] = ' '
open = set()
closed = set()
start_node = input("Enter the starting destination for the robot: ")
open.add(start_node)
path[start_node] = start_node
costs[start_node] = 0
UCS(graph, costs, open, closed, start_node)
goal_node = input("Enter the Final destination for the robot: ")
print("The path(lowest cost) that the robot will follow is: ",path[goal_node])