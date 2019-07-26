""" Reorder array entries so that even entries appear first
    Do this without allocating additional storage

    example-
        a = 3 2 4 5 3 1 6 7 4 5 8 9 0
        output = [0, 2, 4, 8, 4, 6, 7, 1, 5, 3, 9, 5, 3]

    time complexity is O(n), Space complexity is O(1)
"""

def even_first_array(a):
    next_even, next_odd = 0, len(a) - 1
    while next_even < next_odd:
        if a[next_even] % 2 == 0:
            next_even += 1
        else:
            a[next_even], a[next_odd] = a[next_odd], a[next_even]
            next_odd -= 1
    print(a)

if __name__ == '__main__':
    my_array = [int(x) for x in input("Enter Numbers: ").split()]
    even_first_array(my_array)




