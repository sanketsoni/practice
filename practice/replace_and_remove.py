def replace_and_remove(sl):
    """
    :type n: array (of characters)

    time complexity O(n), no additional space is required
    """
    write_idx, a_count = 0, 0
    for i in range(len(sl)):
        if sl[i] != 'b':
            sl[write_idx] = sl[i]
            write_idx += 1
        if sl[i] == 'a':
            a_count += 1
    cur_idx = write_idx - 1
    write_idx = write_idx + a_count - 1
    final_count = write_idx + 1
    while cur_idx >= 0:
        if sl[cur_idx] == 'a':
            sl[write_idx] = 'd'
            sl[write_idx - 1] = 'd'
            write_idx -= 2
        else:
            sl[write_idx] = sl[cur_idx]
            write_idx -= 1
        cur_idx -= 1
    return sl

if __name__ == '__main__':
    n = ['a','c','d', 'b', 'b', 'c', 'a']
    response = replace_and_remove(n)
    print("Output: {}".format(response))