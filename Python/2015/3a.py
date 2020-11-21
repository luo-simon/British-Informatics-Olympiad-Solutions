import math

inp = [int(x) for x in input().split()]

n = inp[4]

available_letters = inp[:-1] # [1, 2, 1, 0] = A, BB, C, / 

letters = 'ABCD'

# We work out digit by digit and store in *known*

def recursive(n_count_left, available_letters, known):
    n_total_count = 0
    
    for index, num_letters in enumerate(available_letters):
        if num_letters == 0:
            continue

        new_available_letters = available_letters[:] # copy
        new_available_letters[index] -= 1 

        n_count = get_combinations(new_available_letters) #number of combinations when current letter is first

        if n_total_count + n_count > n_count_left: #if the number of combs where this digit is first, exceeds the nth term, we know we have stepped over it
            known.append(index) #now we know what this digit is, so we add to known
            n_count_left -= n_total_count #this is how many terms until the nth term
            return recursive(n_count_left, new_available_letters, known)
        
        n_total_count += n_count #It didn't exceed n, so we add it to the total count and see how many combs for next digit
    
    return known #at the end we return what digits were (the indexes are returned)

def get_combinations(remaining_letters):
    # we took out a letter. that letter is the first digit.
    # now we calculate how many combinations with the remaining letters.
    # n! finds all arrangements IF they were all distinguishable
    # letters are repeated, we have counted some arrangements many times
    # so divide by the ways arranging each letter e.g. 5 'A's can be arranged 5! ways

    answer = math.factorial(sum(remaining_letters)) # This is the total number of arrangements, as if they were all distinct items
    for letter in remaining_letters:
        answer /= math.factorial(letter) # Now we 'remove' the arrangements which we counted repeated times
    return answer

digits_indexes = recursive(n-1, available_letters, [])
output = ""
for index in digits_indexes:
    output += letters[index]

print(output)