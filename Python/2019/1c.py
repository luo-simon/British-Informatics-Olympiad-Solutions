palindromes = [False for _ in range(100000)]
nums = [False for _ in range(100000)]

for x in range(1, 100000):
	if str(x) == str(x)[::-1]:
		palindromes[x] = True

for i in range(1, 100000):
	if palindromes[i] == True:
		for j in range(i, 100000):
			if palindromes[j] == True:
				if i+j < 99999:
					nums[i+j] = True

print(nums.count(False))
