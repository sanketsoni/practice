"""
write a program that takes an array A and an index i into A, and rearranges the elements
such that all elements less than A[i] appear first, followed by elements equal to the pivot,
followed by elements greater than the pivot

e.g.- A = [-3,4,2,-5,1,1,2,3,-4,1]
      i=5
      Output:  [-3, 0, -1, -5, 1, 1, 3, 4, 2, 2]

time complexity= O(n), space complexity=O(1)
"""

def dutch_flag_partition(A, i):
    pivot=A[i]
    smaller, equal, larger = 0, 0, len(A)
    while equal < larger:
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller, equal = smaller+1, equal+1
        elif A[equal] == pivot:
            equal += 1
        else:  #A[equal] > pivot
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]
    print("Output: ", A)


if __name__ == '__main__':
    A = [-3,4,2,-5,1,1,2,3,-4,1]
    i = 5
    dutch_flag_partition(A, i)

