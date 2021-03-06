class Edge(object):

  def __init__(s, u, v, w):
    s.source = u
    s.t = v
    s.capacity = w

class FlowNetwork(object):
  def  __init__(s):
    s.adj = {}
    s.flow = {}

  def AddVertex(s, vertex):
    s.adj[vertex] = []

  def GetEdges(s, v):
    return s.adj[v]

  def AddEdge(s, u, v, w = 0):
    edge = Edge(u, v, w)
    redge = Edge(v, u, 0)
    edge.redge = redge
    redge.redge = edge
    s.adj[u].append(edge)
    s.adj[v].append(redge)
    s.flow[edge] = 0
    s.flow[redge] = 0

  def FindPath(s, source, t, path):
    if source == t:
      return path
    for edge in s.GetEdges(source):
      residual = edge.capacity - s.flow[edge]
      if residual > 0 and not (edge, residual) in path:
        result = s.FindPath(edge.t, t, path + [(edge, residual)])
        if result != None:
          return result

  def MaxFlow(s, source, t):
    path = s.FindPath(source, t, [])
    while path != None:
      flow = min(res for edge, res in path)
      for edge, res in path:
        s.flow[edge] += flow
        s.flow[edge.redge] -= flow
      path = s.FindPath(source, t, [])
    return sum(s.flow[edge] for edge in s.GetEdges(source))

g = FlowNetwork()
map(g.AddVertex, ['s', 'a', 'b', 'c', 'd', 't'])
g.AddEdge('s', 'a', 50) 
g.AddEdge('s', 'c', 40) 
g.AddEdge('a', 'b', 60) 
g.AddEdge('c', 'd', 60)
g.AddEdge('c', 'b', 70)
g.AddEdge('b', 't', 30)
g.AddEdge('d', 't', 50)
print g.MaxFlow('s', 't')
