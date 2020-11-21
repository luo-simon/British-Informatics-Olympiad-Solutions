'''
def how_many(s):
    if s == 0:
        return 1

    if s < 0:
        return 0

    return 2 * how_many(s - 1) - how_many(s - 10)
'''

def how_many(s):
  return (2 ** (s))


s, n = (int(x) for x in input().split())


def nth_term(s, n):
    if how_many(s - 1) == n:
        return str(s)
    n_count = 0
    digit = 0
    while True:
        digit += 1
        n_count += how_many(s - (digit + 1))
        if n_count >= n:
            n = n - (n_count - how_many(s - (digit + 1)))
            return str(digit) + (nth_term(s - digit, n))

print(nth_term(s, n))
