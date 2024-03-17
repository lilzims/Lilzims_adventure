# Search list
test_scores = [88, 93, 75, 100, 80, 67, 71, 92, 90, 83]

#Linear Search Algorithm
def linear_search(search_list):
  maximum_score_index = None
  for idx in range(len(search_list)):
    if maximum_score_index == None or search_list[idx] > search_list[maximum_score_index]:
      maximum_score_index = idx
      print("The list {} the index{}".format(search_list[idx],idx))
  return maximum_score_index

# Function call
highest_score = linear_search(test_scores)

#Prints out the highest score in the list
print(highest_score)

# A list of the ingredients for tuna sushi
recipe = ["nori", "tuna", "soy sauce", "sushi rice"]
target_ingredient = "avocado"

def linear_search2(search_list, target_value):
  for idx in range(len(search_list)):
    if search_list[idx] == target_value:
      return idx
  raise ValueError("{0} not in list".format(target_value))

print(linear_search2(recipe, target_ingredient))