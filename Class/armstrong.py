n = 1532
pow = len(str(n))
sum = 0
temp = n
while temp > 0:
    sepa = temp % 10
    sum += sepa ** pow
    termi = temp // 10
    temp = termi
if n == sum:
    print("Armstrong")
else:
    print("not an Armstrong")