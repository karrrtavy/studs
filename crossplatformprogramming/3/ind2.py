armnum = 100
while armnum < 10000:
    digits = list(map(int, str(armnum)))
    num_len = len(digits)
    sum = 0
    for digit in digits:
        sum += pow(digit, num_len)
    if sum == armnum:
        print(armnum)
    armnum += 1