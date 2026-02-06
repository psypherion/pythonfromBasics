num = 12345
temp = num
while temp > 0:
    rev = temp % 10
    termi = temp // 10
    temp = termi
    print(rev, end="")