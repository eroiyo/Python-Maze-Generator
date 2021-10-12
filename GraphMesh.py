import queue
import random
import Edge
class GraphMesh:
  def __init__(self, anchor, lenght):
      self.edgeL= queue.PriorityQueue()
      self.edge_id=0
      self.numvertexs = anchor*lenght
      self.anchor=anchor
      self.height=lenght
      self.list = []
      self.character = []
      for x in range(self.numvertexs):
          self.list.append(dict())
          self.character.append(0)

  def fullramdon(self):
      ramdon = 0
      i=1
      e=1
      while (i <=self.height):
          while ( e <= self.anchor):
              if(i>1):
                  ramdon=random.randint(1,100)
                  self.aristand_UP(i,e,ramdon,True)
              if(e<self.anchor):
                  ramdon=random.randint(1,100)
                  self.aristand_RIGHT(i,e,ramdon,True)
              e = e+1
          i=i+1
          e=1

  def addVertex(self,number):
    self.numvertexs=self.numvertexs+1
    list.append(dict())

  def delVertex(self, id):
      self.list.pop(id)

  def aristand_UP(self, row, column, weight, conditional):
      if((column>=1 and column <=self.anchor) or conditional == False):
          if(((row>1) and (row<=self.height)) or conditional == False):
              rowo =row
              row = row*self.anchor
              row = row-self.anchor
              vertex = row+column
              
              newA = Edge.Edge((vertex),(vertex-self.anchor),weight,rowo,column,"up")
              newB = Edge.Edge((vertex-self.anchor),(vertex),weight,rowo-1,column,"down")

              self.edge_id = self.edge_id+1
              self.list[vertex-1].update({"up": self.edge_id})
              self.edgeL.put(newA)
              self.character[vertex-1]=self.character[vertex-1]+8

              self.edge_id = self.edge_id+1
              self.list[(vertex-self.anchor)-1].update({"down": self.edge_id})
              self.edgeL.put(newB)
              self.character[(vertex-self.anchor)-1] = self.character[(vertex-self.anchor)-1]+4

      else:
          print("up error",row," "," ",column)

  def aristand_DOWN(self, row, column, weight, conditional):
      if((row>0 and row<=self.height) or conditional==False):
          if(((column<self.anchor) and  (column >=1)) or conditional==False):
              rowo=row
              row = row*self.anchor
              row=row-self.anchor
              vertex =row+column
              newA = Edge.Edge((vertex-1),(vertex+self.anchor)-1,weight,rowo,column,"down")
              newB = Edge.Edge((vertex+self.anchor)-1,(vertex-1),weight,rowo+1,column,"up")
              
              self.edge_id = self.edge_id+1
              self.list[vertex-1].update({"down": self.edge_id})
              self.edgeL.put(newA)
              self.character[vertex-1]=self.character[vertex-1]+4

              self.edge_id = self.edge_id+1
              self.list[(vertex+self.anchor)-1].update({"up": self.edge_id})
              self.edgeL.put(newB)
              self.character[vertex+self.anchor-1]=self.character[vertex+self.anchor-1]+8

      else:
          print("down error")

  def aristand_RIGHT(self, row, column, weight, conditional):
      if((row>0 and row<=self.height) or conditional==False):
          if(((column<self.anchor) and  (column >=1)) or conditional==False):
                rowo=row
                row = row*self.anchor
                row = row-self.anchor
                vertex =row+column
                
                newA = Edge.Edge((vertex),(vertex+1),weight,rowo,column,"right")
                newB = Edge.Edge((vertex+1),(vertex),weight,rowo,column+1,"left")

                self.edge_id = self.edge_id+1
                self.list[vertex-1].update({"right": self.edge_id})
                self.edgeL.put(newA)
                self.character[vertex-1]=self.character[vertex-1]+1

                self.edgeL.put(newB)
                self.edge_id = self.edge_id+1
                self.list[(vertex)].update({"left": self.edge_id})
                self.character[vertex]=self.character[vertex]+2

      else:
          print("right error")

  def aristand_LEFT(self, row, column, weight, conditional):
      if((row>0 and row<=self.height) or conditional==False):
          if(((column<self.anchor) and  (column >=1)) or conditional==False):
                rowo=row
                row = row*self.anchor
                row = row-self.anchor
                vertex =row+column
                
                newA = Edge.Edge((vertex-1),(vertex-2),weight,rowo,column,"left")
                newB = Edge.Edge((vertex-2),(vertex-1),weight,rowo,column-1,"right")

                self.edge_id = self.edge_id+1
                self.list[vertex-1].update({"left": self.edge_id})
  
                self.character[vertex-1]=self.character[vertex-1]+2
                self.edgeL.put(newA)
                self.edge_id = self.edge_id+1
                self.list[(vertex-2)].update({"right": self.edge_id})
                self.edgeL.put(newB)
                self.character[vertex-2]=self.character[vertex-2]+1

      else:
          print("right error")

  def vertex_grade(self, id):
      return len(self.list[id-1])

  def  vertexQ(self):
      return self.numvertexs

  def debug(self,id):
      return self.list[(id-1)]

  def show(self):
      d=0
      for x in range(self.height):
          print("")
          for e in range(self.anchor):
              print((self.decode(self.character[d])), end = '')
              d=d+1
  def decode (self, number):
      switch={
          1: '╶',
          2: '╴',
          3: '─',
          4: '╷',
          5: '┌',
          6: '┐',
          7: '┬',
          8: '╵',
          9: '└',
          10: '┘',
          11: '┴',
          12: '│',
          13: '├',
          14: '┤',
          15: '┼'
      }
      return switch.get(number,"")

  def find(self, Arr, A, B):
      if(Arr[A] == Arr[B]):
          return True
      else:
          return False

  def union(self, Arr, N, A, B):
      TEMP = Arr[A]
      for i in range(N):
          if(Arr[i] == TEMP):
              Arr[i] = Arr[B]

  def addEdge(self, edge):
      if(edge.direction == "up"):
          self.aristand_UP(edge.row,edge.column, edge.weight,False)
      if(edge.direction == "down"):
          self.aristand_DOWN(edge.row,edge.column, edge.weight,False)
      if(edge.direction == "right"):
          self.aristand_RIGHT(edge.row,edge.column, edge.weight,False)
      if(edge.direction == "left"):
          self.aristand_LEFT(edge.row,edge.column, edge.weight,False)

  def addEdgeF(self, edge):
      e=0
      i=0
      d=0
      for i in range(self.height+1):
          for e in range(self.anchor+1):
              d=d+1
              if(d==edge.vertex_A()):
                  break
          if(d==edge.vertex_A()):
              break
      switch={
          'up': self.aristand_UP(i,e, edge.weight,False),
          'down':self.aristand_DOWN(i,e, edge.weight,False),
          'right':self.aristand_RIGHT(i,e, edge.weight,False),
          'left':self.aristand_LEFT(i,e, edge.weight,False),
      }
      return switch.get(edge.direction,"error")

  def kruskal(self):
      minimun =GraphMesh(self.anchor, self.height)
      Arr =[]

      for i in range(self.numvertexs):
          Arr.append(i)
      while not self.edgeL.empty():
          a = self.edgeL.get()
          if(self.find(Arr,a.myVertex_A()-1,a.myVertex_B()-1) == False):
            self.union(Arr,self.numvertexs,a.myVertex_A()-1,a.myVertex_B()-1)
            minimun.addEdge(a)
      return minimun