
def quicksort(sequence):
    
    if len(sequence) <= 1:
      return sequence
    
    else:
        pivot = sequence.pop()
        higher_pivot = []
        less_pivot = []

        for item in sequence:
            if item > pivot:
                higher_pivot.append(item)
            else:
                less_pivot.append(item)


        return quicksort(less_pivot) + [pivot] + quicksort(higher_pivot)

# print(quicksort([9,1,5,6,3,7,8,2,11,2,5]))
print(quicksort([1, 2, 3, 4, 5, 6, 7]))