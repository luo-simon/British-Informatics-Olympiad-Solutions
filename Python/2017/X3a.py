'''
Write a program to determine the number of ways parcels can be distributed.
Your program should input four integers in order:

- p (1 ≤ p ≤ 5) indicating the number of parcels
- i (1 ≤ i ≤ 10) indicating that items can weigh any integer from 1 to i inclusive
- n (1 ≤ n ≤ 25) indicating the total number of items in all the parcels
- w (1 ≤ w ≤ 25) indicating the weight of each parcel.

You will not be given input that requires an answer greater than 231
Marks are available for the case where p = 1
'''
import itertools
while True:
    p, i, n, w = (int(x) for x in input().split())

    parcel_arrangements = list(itertools.combinations_with_replacement([x for x in range(1, n-p+2)], p))
    parcel_valid_arrangements = [comb for comb in parcel_arrangements if sum(comb) == n]

    arrangements_count = 0

    for parcel_arrangement in parcel_valid_arrangements:
        #multiplier = len(set([x for x in itertools.permutations(parcel_arrangement, p)]))
        listel = []
        for num_parcels in parcel_arrangement:
            item_arrangements = list(itertools.combinations_with_replacement([x for x in range(1, i+1)], num_parcels ))
            item_valid_arrangements = [comb for comb in item_arrangements if sum(comb) == w]
            listel.extend(item_valid_arrangements)
        #arrangements_count = arrangements_count + (multiplier * len(listel))
        add = set([x for x in itertools.permutations(listel, p)])
        arrangements_count += len(add)

    print(arrangements_count)

 
