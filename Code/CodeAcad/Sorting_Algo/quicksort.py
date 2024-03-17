from random import randrange, shuffle

# This a quicksort algorithm with plenty of print statements to make it obvious exactly whats happening as the program runs
# I totally stole this from code academy but I think the visualization of the recursive function and how it clearly stores
# the functions calls into a stack is really helpful to see 

def quicksort(list, start, end):
  if start >= end:
    return
  print("Running quicksort on {0}".format(list[start: end + 1]))

  pivot_idx = randrange(start, end + 1)
  pivot_element = list[pivot_idx]
  print("Selected pivot {0}".format(pivot_element))

  list[end], list[pivot_idx] = list[pivot_idx], list[end]

  less_than_pointer = start
  
  for i in range(start, end):
    if list[i] < pivot_element:
      print("Swapping {0} with {1}".format(list[i], pivot_element))
      list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
      less_than_pointer += 1

  list[end], list[less_than_pointer] = list[less_than_pointer], list[end]
  print("{0} successfully partitioned".format(list[start: end + 1]))
  quicksort(list, start, less_than_pointer - 1)
  quicksort(list, less_than_pointer + 1, end)


    
  
list = [5,3,1,7,4,6,2,8]
shuffle(list)
print("PRE SORT: ", list)
print(quicksort(list, 0, len(list) -1))
print("POST SORT: ", list)
