from collections import deque # Using a queue from the collections because I didn't feel like implementing mine here

class TreeNode:
  def __init__(self, value):
    self.value = value 
    self.children = [] 
    
  def __repr__(self):
    return self.value

  def add_child(self, child_node):
    print("Adding " + child_node.value)
    self.children.append(child_node) 
    
  def remove_child(self, child_node):
    print("Removing " + child_node.value + " from " + self.value)
    self.children = [child for child in self.children 
                     if child is not child_node]

  def traverse(self):
    nodes_to_visit = [self]
    while len(nodes_to_visit) > 0:
      current_node = nodes_to_visit.pop()
      print(current_node.value)
      nodes_to_visit += current_node.children

      
      
def print_tree(root):
  stack = deque()
  stack.append([root, 0])
  level_str = "\n"
  prev_level = 0
  level = 0
  while len(stack) > 0:
    prev_level = level
    node, level = stack.pop()
    
    if level > 0 and len(stack) > 0 and level <= stack[-1][1]:
      level_str += "   "*(level-1)+ "├─"
    elif level > 0:
      level_str += "   "*(level-1)+ "└─"
    level_str += str(node.value)
    level_str += "\n"
    level+=1
    for child in node.children:
      stack.append([child, level])

  print(level_str)
      
def print_path(path):
  if path == None:
    print("No paths found!")

  else:  
    print("Path found:")
    for node in path:
      print(node.value)

      
sample_root_node = TreeNode("A")
two = TreeNode("B")
three = TreeNode("C")
sample_root_node.children = [three, two]
four = TreeNode("D")
five = TreeNode("E")
six = TreeNode("F")
seven = TreeNode("G")
two.children = [five, four]
three.children = [seven, six]
print(print_tree(sample_root_node))
sample_root_node.traverse()
