import math

interest, repayment_percent = 43, 46
debt = 10000
num_payments = 0

while debt > 0:
	debt += math.ceil((interest / 100) * debt)
	repayment = math.ceil((repayment_percent/100) * debt)
	repayment = min(max(repayment, 5000), debt)
	debt -= repayment
	num_payments += 1

print(num_payments)
