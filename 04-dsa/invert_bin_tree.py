

class Node:
   def __init__(self, data, l, r):
      self.left = r
      self.right = l
      self.data = data
   def invertTree(self, root):
       try :
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root
       except :
           return root

if __name__ == '__main__':
    Tree = Node(10, 4, 5)
    Tree.left = Node(4, 5, 6);

    print(f"Before inverting {Tree.left}")
    Tree.invertTree(Tree);
    print(f"After inverting {Tree.left}");
