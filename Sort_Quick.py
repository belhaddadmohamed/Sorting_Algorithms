def exchange(tab, pos1, pos2):
  """Function To change the position of 2 values in an array
     Inputs: Array, position1, position2
     Output: The updated array
  """
  tab[pos1], tab[pos2] = tab[pos2], tab[pos1]
  return tab


def partition(tab, p, r):
  """Function To find the 2 partitions around the pivot
     Inputs: Array, start index, end index
     Ouptu: Position of the pivot
  """
  pivot = tab[r]
  i = p - 1

  for j in range(p, r-1):
    if tab[j] <= pivot:
      i += 1
      tab = exchange(tab, i, j)
  # Swap the pivot between after the list of i
  tab = exchange(tab, i + 1, r)  

  return i + 1


def quick_sort(tab, p, r):
  """Quick Sort algorithm
     Inputs: Array, start index, end index
     Output: /
  """
  if r <= p:
    return
  else:
    # Partionate the list and find the position of the pivot
    pivot = partition(tab, p, r)    
    # Recursive call of the left and right of pivot
    quick_sort(tab, p, pivot - 1)
    quick_sort(tab, pivot + 1, r)



# Sample
tab = [8, 2, 1, 4, 3, 9, 5]
l = len(tab)
quick_sort(tab, 0, l - 1)
print(tab)







# Other method
# def quicksort(sequence):
    
#     if len(sequence) <= 1:
#       return sequence
    
#     else:
#         pivot = sequence.pop()
#         higher_pivot = []
#         less_pivot = []

#         for item in sequence:
#             if item > pivot:
#                 higher_pivot.append(item)
#             else:
#                 less_pivot.append(item)


#         return quicksort(less_pivot) + [pivot] + quicksort(higher_pivot)

# # print(quicksort([9,1,5,6,3,7,8,2,11,2,5]))
