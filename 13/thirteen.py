file = open("50DigitNumbers.txt")
lines = file.readlines()
sum = 0

for line in lines:
    line = line[:12]
    sum += int(line)
    print(line)

print(str(sum)[:10])
