#!usr/bin/env/python

'''
In Jewish study, “Gematria” is an alphanumeric code where words
are assigned numerical values based on their letters. We can do the
same in English, assigning 1 to the letter A, 2 to the letter B, and so
on, up to 26 for the letter Z. The value of a word is then the sum of the
values of its letters. For example, RIDDLER has an alphanumeric value
of 70, since R + I + D + D + L + E + R
becomes 18 + 9 + 4 + 4 + 12 + 5 + 18 = 70.

But what about the values of different numbers themselves, spelled
out as words? The number 1 (ONE) has an alphanumeric value of
15 + 14 + 5 = 34, and 2 (TWO) has an alphanumeric value of
20 + 23 + 15 = 58. Both of these values are bigger than the
numbers themselves.

Meanwhile, if we look at larger numbers, 1,417 (ONE THOUSAND
FOUR HUNDRED SEVENTEEN) has an alphanumeric value of 379,
while 3,140,275 (THREE MILLION ONE HUNDRED FORTY THOUSAND
TWO HUNDRED SEVENTY FIVE) has an alphanumeric value of 718.
These values are much smaller than the numbers themselves.

If we consider all the whole numbers that are less than their
alphanumeric value, what is the largest of these numbers?

SOLUTION:
https://fivethirtyeight.com/features/can-you-track-the-delirious-ducks/
'''
from math import floor

alphabet = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers = [i for i in range(0,27)]


mapper = {char:num for char, num in zip(alphabet,numbers)}

ones = ["", "one ","two ","three ","four ", "five ", "six ","seven ",
        "eight ","nine ","ten ","eleven ","twelve ", "thirteen ",
        "fourteen ", "fifteen ","sixteen ","seventeen ", "eighteen ",
        "nineteen "]

tens = ["","never called", "twenty ","thirty ","forty ", "fifty ","sixty ",
        "seventy ","eighty ","ninety "]

hundred = 'hundred '

# after playing with the fuctions and outputs, this is massive overkill haha
thousands = [" ","thousand ","million ", "billion ", "trillion ", "quadrillion ",
             "quintillion ", "sextillion ", "septillion ","octillion ", "nonillion ",
             "decillion ", "undecillion ", "duodecillion ", "tredecillion ",
             "quattuordecillion ", "quindecillion", "sexdecillion ", "septendecillion ",
             "octodecillion ", "novemdecillion ", "vigintillion "]

def count_words(word):
    characters = list(word)
    return sum([mapper[i] for i in characters])

def build_words(number):
    words = ''
    commas = floor((len(str(number))-1)/3)
    num_str = str(number)
    front = len(num_str)%3
    
    if front!=0:
        front_nums = num_str[:front]
        if front==2:
            if int(front_nums)<20:
                words += ones[int(front_nums)]
            else:
                words += tens[int(front_nums[0])]
                words += ones[int(front_nums[1])]
                words += thousands[commas]
        if front==1:
            words += ones[int(front_nums[0])]
            words += thousands[commas]
        commas -= 1

    num_str = num_str[front:]
   
    for i in range(int(len(num_str)/3)):
        small = num_str[i*3:i*3+3]
        if int(small[0]) == 0:
            if int(small) < 20:
                words += ones[int(small[1:])]
                words += thousands[commas]
                commas -= 1
                continue
            else:
                words += tens[int(small[1])]
                words += ones[int(small[2])]
                words += thousands[commas]
                commas -= 1
            continue
        words += ones[int(small[0])]
        words += hundred
        if int(small[1:]) < 20:
                words += ones[int(small[1:])]
                words += thousands[commas]
                commas -=  1
                continue
        else:
                words += tens[int(small[1])]
                words += ones[int(small[2])]
                words += thousands[commas]
                commas -= 1
    return words

results = {num : count_words(build_words(num)) for num in range(1000)}
new ={num:results[num] for num in list(results.keys()) if num < results[num]}
print(f'Actual Number: {max(new.keys())}')
print(f'Alphanumeric Score: {new[max(list(new.keys()))]}')

###############################
#                             #
#    Actual Number: 279       #
#                             #
#    Alphanumeric Score: 284  #
#                             #
###############################
        




    
    
