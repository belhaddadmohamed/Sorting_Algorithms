# Merge the left and the right arrays
def merge(a,b):
    """Sort and merge 2 arrays
       input: left array, right array
       output: Sorted array
    """
    c=[]
    i = 0
    j = 0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    if i==len(a):
        c.extend(b[j:])
    else:
        c.extend(a[i:])
    return c


# Merge Sort
def merge_sort(a):
    """Merge Sort: Divide and conquer approach => splits the array 2 halves till it become length of 1, sort, combine.
       Input: takes the array
       Output: Returns the array if length=1, else: recursion  
    """
    if len(a) <= 1:
        return a
    else:
        half = int(len(a)/2)
        left = merge_sort(a[:half])
        right = merge_sort(a[half:])

        return merge(left , right)



# Create an array and test the algorithm
def create_array(size=10 , max=50):
    from random import randint
    return [randint(0,max) for _ in range(size)]

arr = create_array()
print(arr)
print(merge_sort(arr))
