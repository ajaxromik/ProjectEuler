# intToText can only handle numbers in the range [1,1000]
def intToText(number):
    total = ''
    if number > 999:
        total = 'one thousand'

    elif number > 99:
        total = intToText(int(number / 100)) + ' hundred and ' intToText(number % 100)

    elif number > 19:
        twenties = {
            2 : 'twenty',
            3 : 'thirty',
            4 : 'forty',
            5 : 'fifty',
            6 : 'sixty',
            7 : 'seventy',
            8 : 'eighty',
            9 : 'ninety'
        }
        total = twenty[int(number / 10)] + '-' + intToText(number % 10)

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
        total = tens[number]

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
        total = ones[number]

    return total
