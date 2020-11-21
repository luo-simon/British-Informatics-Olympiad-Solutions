import math

interest, repayment_percent = (int(x) for x in input('> ').split(" "))

debt = 10000
total_repayment = 0

while debt > 0:
	debt += math.ceil((interest / 100) * debt)
	repayment = math.ceil((repayment_percent/100) * debt)
	repayment = min(max(repayment, 5000), debt)
	debt -= repayment
	total_repayment += repayment


print(round(total_repayment/100, 2))
