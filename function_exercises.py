
'''

Returns true if argument is 2.

'''

def is_two(x):
    return x == 2


'''
 Returns True if the passed string is a vowel, false otherwise.
 
 '''

def is_vowel(x):
    if x.lower() in ["a", "e", "i", "o", "u"]:
        return True
    else:
        return False
    

    
'''

Returns True if the passed string is a consonant, false otherwise. 

'''

def is_consonant(y):
    return not is_vowel(y)


'''

Accepts a string that is a word. The function capitalizes the first letter of the word if the word starts with a consonant.

'''

def cap_consonant(word):
    first_letter = word[0]
    if type(word) != str:
        return False
    if is_consonant(first_letter):
        return word.capitalize()
    else:
        return print('Word does not start with a consonant')
    
    
'''

It accepts a tip percentage (a number between 0 and 1), the bill total, and returns the amount to tip.
'''

def calculate_tip(tip_percentage, bill_total):
    
    total = float(tip_percentage) * float(bill_total)
    return total


'''
Accepts an original price, a discount percentage, and returns the price after the discount is applied.
'''

def apply_discount(discount_percent, original_price):
    new_pice = (original_price - (float(discount_percent/100) * float(original_price)))
    return new_pice


'''

Accepts a string that is a # number that contains commas in it as input, and returns a number as output.

'''



def handle_commas(number):
    new_num = str(number)
    new_num = int(new_num.replace(",", ""))
    return new_num




'''
Accepts a number and returns the letter grade associated with that number (A-F).

'''

def get_letter_grade(grade):
    if 100 >= int(grade) >= 88:
        return print('A')

    elif 87 >= int(grade) >= 80:
        return print('B')

    elif 79 >= int(grade) >= 67:
        return print('C')

    elif 66 >= int(grade) >= 60:
        return print('D')

    elif 59 >= int(grade) >= 0:
        return print('F')
    else:
        return print('please enter a number between 0 and 100')



'''

Accepts a string and returns a string with all the vowels removed.


'''

# remove vowel function takes a string and returns the string with all vowels removed
def remove_vowels(string):
    # vowels varaible defined as a list
    vowels = ['a','e','i','o','u']
    # list comprehension to make a new list with letters in string that are not in the vowel list
    # x is the iterator variable
    result = [x for x in string if x.lower() not in vowels]
    # join function turns list into string and joins with no space
    result = ''.join(result)
    return (result)



'''
Accepts a string and returns a valid python identifier

'''


def normalize_name(string):
    
    # remove any leading or trailing spaces replace space with _, and lowercase the string
    string = string.strip().replace(" ", "_").lower()
    #remove all the symbols
    new_string = ""
    for letter in string:
        if letter.isalnum() or letter == "_":
            new_string = new_string + letter
    # remove all the numbers in the beggining of the string
    for letter in range (len(new_string)):
        if not new_string[0].isalpha():
            new_string = new_string[1:]
    if new_string == "":
        return print(" You entered an invalid python identifier")
    else:
        return new_string



'''
Accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.

'''


a = [1, 2, 3, 4]
def cumulative_sum(a):
    b = [sum(a[0:x]) for x in range(1, len(a)+1)]
    return (b)




