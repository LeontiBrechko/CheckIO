FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    if number > 99:
        if number % 100 == 0:
            return " ".join([FIRST_TEN[number // 100 - 1], HUNDRED])
        return " ".join([FIRST_TEN[number // 100 - 1], HUNDRED, checkio(number % 100)])
    elif number > 19:
        if number % 10 == 0:
            return OTHER_TENS[number // 10 - 2]
        return " ".join([OTHER_TENS[number // 10 - 2], checkio(number % 10)])
    elif number > 9:
        return SECOND_TEN[number % 10]
    elif number > 0:
        return FIRST_TEN[number - 1]
'''
string = []
    
    hundreds, tens, units = [int(d) for d in str(number).zfill(3)]
    
    if hundreds > 0 : string += (FIRST_TEN[hundreds - 1], HUNDRED)
    if tens == 1    : return ' '.join(string + [SECOND_TEN[units]])
    if tens > 1     : string += [OTHER_TENS[tens - 2]]
    if units        : string += [FIRST_TEN[units - 1]]
​
    return ' '.join(string)
    '''                
    
        

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
