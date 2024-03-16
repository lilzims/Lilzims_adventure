def binary_search(sorted_list, left_pointer, right_pointer, target):
  if left_pointer >= right_pointer:
    return "value not found"
	
  mid_idx = (left_pointer + right_pointer) // 2
  mid_val = sorted_list[mid_idx]

  if mid_val == target:
    return mid_idx
  if mid_val > target:
    return binary_search(sorted_list, left_pointer, mid_idx, target)
  if mid_val < target:
    return binary_search(sorted_list, mid_idx + 1, right_pointer, target)
  
values = [77, 80, 102, 123, 288, 300, 540]
start_of_values = 0
end_of_values = len(values)
result = binary_search(values, start_of_values, end_of_values, 288)

print("element {0} is located at index {1}".format(288, result))


def iterative_binary_search(sorted_list, target):
  left_pointer = 0
  right_pointer = len(sorted_list)
  
  while right_pointer > left_pointer:

    mid_idx = (left_pointer + right_pointer) // 2
    mid_val = sorted_list[mid_idx]
    
    if mid_val == target:
      return mid_idx
    if target < mid_val:
      right_pointer = mid_idx
    if target > mid_val:
      left_pointer = mid_idx + 1
  
  return "Value not in list"

print(iterative_binary_search([5,6,7,8,9], 9))
print(iterative_binary_search([5,6,7,8,9], 10))
print(iterative_binary_search([5,6,7,8,9], 8))
print(iterative_binary_search([5,6,7,8,9], 4))
print(iterative_binary_search([5,6,7,8,9], 6))

import random

class BinarySearchTree:
  def __init__(self, value, depth=1):
    self.value = value
    self.depth = depth
    self.left = None
    self.right = None

  def insert(self, value):
    if (value < self.value):
      if (self.left is None):
        self.left = BinarySearchTree(value, self.depth + 1)
        print(f'Tree node {value} added to the left of {self.value} at depth {self.depth + 1}')
      else:
        self.left.insert(value)
    else:
      if (self.right is None):
        self.right = BinarySearchTree(value, self.depth + 1)
        print(f'Tree node {value} added to the right of {self.value} at depth {self.depth + 1}')
      else:
        self.right.insert(value)
        
  def get_node_by_value(self, value):
    if (self.value == value):
      return self
    elif ((self.left is not None) and (value < self.value)):
      return self.left.get_node_by_value(value)
    elif ((self.right is not None) and (value >= self.value)):
      return self.right.get_node_by_value(value)
    else:
      return None
  
  def depth_first_traversal(self):
    if (self.left is not None):
      self.left.depth_first_traversal()
    print(f'Depth={self.depth}, Value={self.value}')
    if (self.right is not None):
      self.right.depth_first_traversal()


print("Creating Binary Search Tree rooted at value 15:")
tree = BinarySearchTree(15)

for x in range(10):
  tree.insert(random.randint(0, 100))
  
print("Printing the inorder depth-first traversal:")
tree.depth_first_traversal()
