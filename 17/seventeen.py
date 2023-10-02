# can't go past 1000
def intToText(number):
    total = ''
    if number > 999:
        total = 'one thousand'

    elif number > 99:
        intToText(int(number / 100)) + ' hundred and ' intToText(number % 100)

    elif number > 19:
        twenties = {
            20 : 'twenty',
            30 : 'thirty',
            40 : 'forty',
            50 : 'fifty',
            60 : 'sixty',
            70 : 'seventy',
            80 : 'eighty',
            90 : 'ninety'
        }
        

    elif number > 9:
        tens = {
            10 : 'ten',
            11 : 'eleven',
            12 : 'twelve',
            13 : 'thirteen',
            14 : 'fourteen',
            15 : 'fifteen',
            16 : 'sixteen',
            17 : 'seventeen',
            18 : 'eighteen',
            19 : 'nineteen'
        }

    else:

        ones = {
            1 : 'one',
            2 : 'two',
            3 : 'three',
            4 : 'four',
            5 : 'five',
            6 : 'six',
            7 : 'seven',
            8 : 'eight',
            9 : 'nine'
        }
    return total
