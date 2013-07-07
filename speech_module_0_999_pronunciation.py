FIRST_TEN = ["zero", "one", "two", "three", "four", "five", "six", "seven", \
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", \
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", \
              "eighty", "ninety"]
HUNDRED = "hundred"

def checkio(number):
    if number in range(10):
        return FIRST_TEN[number]
    elif number in range(10, 20):
        return SECOND_TEN[number - 10]
    elif number in range(20, 100, 10):
        return OTHER_TENS[number // 10 - 2]
    elif number in range(20, 100) and (number % 10 != 0):
        return OTHER_TENS[number // 10 - 2] + ' ' + FIRST_TEN[number % 10]
    elif number in range(100, 1000, 100):
        return FIRST_TEN[number // 100] + ' ' + HUNDRED
    elif number in range(100, 1000) and ( number % 100 in range(1, 10) ):
        return FIRST_TEN[number // 100] + ' ' + HUNDRED + ' ' + \
               FIRST_TEN[number % 100]
    elif number in range(100, 1000) and ( number % 100 in range(10, 20) ):
        return FIRST_TEN[number // 100] + ' ' + HUNDRED + ' ' + \
               SECOND_TEN[ (number % 100) - 10]  
    elif number in range(100, 1000) and (number % 10 == 0) and \
         (number % 100 > 10):
        return FIRST_TEN[number // 100] + ' ' + HUNDRED + ' ' + \
               OTHER_TENS[ (number % 100) // 10 - 2]
    else:
        return FIRST_TEN[number // 100] + ' ' + HUNDRED + ' ' +\
               OTHER_TENS[ (number % 100) // 10 - 2] + ' ' + \
               FIRST_TEN[number % 10]


print checkio(0)
print checkio(3)
print
print checkio(12)
print
print checkio(20)
print
print checkio(21)
print
print checkio(300)
print
print checkio(905)
print
print checkio(115)
print checkio(516)
print
print checkio(720)
print
print checkio(121)
print checkio(543)
print checkio(999)
