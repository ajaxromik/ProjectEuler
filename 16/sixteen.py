file = open("unformatted2to1000.txt")
lines = file.readlines()

sum = 0

for line in lines:
    for digit in line:
        if digit.isdigit():
            sum += int(digit)

print(sum)
