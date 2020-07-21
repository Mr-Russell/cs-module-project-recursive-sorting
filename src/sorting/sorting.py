# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    num_elements = len(arrA) + len(arrB)
    merged_arr = []

    # Your code here
    # a = 0
    # b = 0
    # while a < len(arrA) and b < len(arrB):
    #     if arrA[a] < arrB[b]:
    #         merged_arr.append(arrA[a])
    #         a += 1
    #     else:
    #         merged_arr.append(arrB[b])
    #         b += 1
    
    while num_elements > 0:
        if len(arrA) == 0 and len(arrB) > 0:
            merged_arr.extend(arrB)
            break

        elif len(arrB) == 0 and len(arrA) > 0:
            merged_arr.extend(arrA)
            break

        elif arrA[0] < arrB[0]:
            merged_arr.append(arrA.pop(0))
            num_elements -= 1

        elif arrA[0] > arrB[0]:
            merged_arr.append(arrB.pop(0))
            num_elements -= 1


    return merged_arr

####### Mini Test
# arr1 = [1, 3, 5]
# arr2 = [2, 4, 6]

# print(merge(arr1, arr2))

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) > 1:
        mid = len(arr) // 2

        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])

        arr = merge(left, right)
        
        # mid = len(arr) // 2
        # left = arr[:mid]
        # right = arr[mid:]
        # if len(left) > 1:
        #     merge_sort(left)
        # if len(right) > 1:
        #     merge_sort(right)
        # arr = merge(left, right)



    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
	