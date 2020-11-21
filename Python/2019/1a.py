inp = int(input('> '))

def smallestPalindrome(x):
    length = len(x)

    middle = ""

    left = x[:length//2]

    if length % 2 == 0:
        right = x[length//2:]
    else:
        middle = x[length//2]
        right = x[length//2 + 1:]

    if int(left[::-1]) > int(right):
        return (left + middle + left[::-1])
    else:
        return next_palindrome_fast(str(int(left + middle) + 1) + ("0" * len(right)))  

print(smallestPalindrome(inp))
