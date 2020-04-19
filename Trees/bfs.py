class Node:
  def __init__(self, data):
    self.left = None
    self.right = None
    self.data = data

class binarySearchTree:
  def __init__(self):
    self.root = None
    
  def BFS_traverse(self):
    q = []
    q.append(self.root)
      
    while q:
        node = q.pop(0)
        print(node.data)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return

  def BFS_print_level(self):
      q = []
      level = 0
      q.append(self.root)
      q.append(None)
      print("Level {}".format(level))
      while q:
          node = q.pop(0)
          # if a None node is dequeued, enqueue a None and incerement level
          # EXCEPT when it is the last node in the queue and we need to return
          if node is None:
              if len(q) == 0:
                  # last node
                  return
              else:
                  level += 1
                  print("Level {}".format(level))
                  q.append(None)
          else:
              print(node.data)
              if node.left:
                  q.append(node.left)
              if node.right:
                  q.append(node.right)


      
      

  

  


nodeA = Node('A')
nodeB = Node('B')
nodeC = Node('C')
nodeD = Node('D')
nodeE = Node('E')
nodeF = Node('F')

nodeA.left = nodeB
nodeA.right = nodeC
nodeB.left = nodeD
nodeB.right = nodeE
nodeC.left = nodeF


bst = binarySearchTree()
bst.root = nodeA
#bst.BFS_traverse()
bst.BFS_print_level()



    
        
            
