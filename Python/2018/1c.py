import math

debt = 10000
total_repayment = 0
highest = 0
interest, repayment_percent = 0, 0

for i in range(90, 100):
    for r in range(40, 60):
        debt = 10000
        total_repayment = 0
        try:
            while debt > 0:
                debt += math.ceil((i / 100) * debt)
                repayment = math.ceil((r/100) * debt)
                repayment = min(max(repayment, 5000), debt)
                debt -= repayment
                total_repayment += repayment
            if total_repayment > highest:
                highest = total_repayment
                interest, repayment_percent = i, r
                print(i, r)
        except:
            pass

print(interest, repayment_percent)
