def Palindrome(s):
    """
    :type s: str
    """
    return all(s[i] == s[~i] for i in range(len(s)//2))


if __name__ == '__main__':
    s = "abba"
    is_palindrome = Palindrome(s)
    print("Is Palindrome?: {}".format(is_palindrome))