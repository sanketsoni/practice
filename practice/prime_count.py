

def countPrimes(n):
    """
    :type n: int
    :rtype: int
    """
    # The first and second elements are never used. Otherwise,
    # primesRecord[i] is for interger i.
    primesRecord = [False] * n
    primesCount = 0
    import pdb;pdb.set_trace()
    for number in range(2, n):
        if primesRecord[number] == False:
            # Cannot be divided by any smaller integer. This is
            # a prime nubmer.
            primesCount += 1
            current = number
            while current < n:
                    # This is a composite number.
                primesRecord[current] = True
                current += number
    return primesCount

if __name__ == '__main__':
    n = 10
    prime_count = countPrimes(n)
    print("Prime numbers: {}".format(prime_count))