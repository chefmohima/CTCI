class Node:
  def __init__(self, data):
    self.left = None
    self.right = None
    self.data = data

class binarySearchTree:
  def __init__(self):
    self.root = None
    
  
      
  def dfs_helper(self, type, start_node):
      
      def preorder(node):
          # NLR
          if node is None:
              return
          print(node.data)
          preorder(node.left)
          preorder(node.right)
          
      def inorder(node):
          # LNR
          if node is None:
              return
          inorder(node.left)
          print(node.data)
          inorder(node.right)
          
      def postorder(node):
          # LRN
          if node is None:
              return
          postorder(node.left)
          postorder(node.right)
          print(node.data)
          
      if type == 'preorder':
          preorder(start_node)
      elif type == 'inorder':
          inorder(start_node)
      elif type == 'postorder':
          postorder(start_node)
      
    
      
    
  


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
bst.dfs_helper('postorder' ,bst.root)



    
        
            
