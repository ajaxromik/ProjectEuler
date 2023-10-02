# can't go past 1000
def intToText(number):
    total = ''
    if number > 999:
        total = 'one thousand'

    elif number > 99:
        intToText(int(number / 100)) + ' hundred and ' intToText(number % 100)

    
    return total
