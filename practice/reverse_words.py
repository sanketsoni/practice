""" time complexity is O(n) ans additional space complexity is O(1)

example: Input string:            ram is costly
         Reverse word output:     costly is ram
"""

def reverse_words(s):
    def reverse_range(s, start, finish):
        while start < finish:
            s[start], s[finish] = s[finish], s[start]
            start, finish = start + 1, finish - 1

    # First, reverse the whole string
    reverse_range(s, 0, len(s)-1)

    start = 0
    while True:
        finish = start
        while finish < len(s) and s[finish] != " ":
            finish += 1
        if finish == len(s):
            break
        # Reverses eash word in a string
        reverse_range(s, start, finish-1)
        start = finish + 1
    # Reverses the last word
    reverse_range(s, start, len(s)-1)
    return ''.join(s)

if __name__ == '__main__':
    my_string = "ram is costly"
    print("Input string:\t\t {}".format(my_string))
    s = list(my_string)
    response = reverse_words(s)
    print("Reverse word output:\t {}".format(response))