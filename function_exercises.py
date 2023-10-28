




def is_two(x):
    '''
    # 1. Define a function named is_two. It should accept one input and return True if the 
# passed input is either the number or the string 2, False otherwise.
'''
    
    if x in (2, '2', 2.0):
        return True
    else:
        return False










def is_vowel(x):
    '''
    # 2. Define a function named is_vowel. 
# It should return True if the passed string is a vowel, False otherwise.
'''
    if type(x) == str:
        if len(x) == 1 and x.isalpha():
            return x.lower() in ('aeiou')
        else:
            return False
    else: return False
    
    
    



def is_consonant(y):
    '''
    # 3. Define a function named is_consonant. It should return True if the passed string is a consonant, 
# False otherwise. Use your is_vowel function to accomplish this.
'''
    if type(y) == str:
        if len(y) == 1 and y.isalpha():
            return not is_vowel(y)
        else:
            return False
    else:
        return False
    






def cap_consonant(word):
    '''
    # 4. Define a function that accepts a string that is a word. 
# The function should capitalize the first letter of the word if the word starts with a consonant.
'''
    first_letter = word[0]
    if type(word) == str:
        if is_consonant(first_letter):
            return word.capitalize()
        else:
            return (f"{word} does not start with a consonant")
    else:
        return (F"{word} is not a string")
    
    







def calculate_tip(tip_percentage, bill):
    '''
    # 5. Define a function named calculate_tip. It should accept a tip percentage 
# (a number between 0 and 1) and the bill total, and return the amount to tip.
''' 
    total = float(tip_percentage) * float(bill)
    return total








def apply_discount(discount_percent, original_price):
    '''
    # 6. Define a function named apply_discount. It should accept a original price, 
# and a discount percentage, and return the price after the discount is applied.
    
    '''
    new_pice = (original_price - (float(discount_percent/100) * float(original_price)))
    return new_pice








def handle_commas(number):
    '''
    # 7. Define a function named handle_commas. It should accept a string that is a 
# number that contains commas in it as input, and return a number as output.
    '''
    if type(number) == str:
        new_number = number.replace(",", "")
        if new_number.isdigit():
            return int(new_number)
        else:
            return False
    else:
        return False
        








def get_letter_grade(grade):
    '''
    # 8. Define a function named get_letter_grade. It should accept a number 
#    and return the letter grade associated with that number (A-F).
    '''
    if type(grade) == int:
        if grade >= 90:
            return print('A')
        elif grade >= 80:
            return print('B')
        elif grade >= 70:
            return print('C')
        elif grade >= 60:
            return print('D')
        else:
            return print('F')
    else:
        return print('please enter a number')









def remove_vowels(string):
    '''
    # 9. Define a function named remove_vowels that accepts a string and 
#     returns a string with all the vowels removed.
    '''
    new_word = ""
    for letter in string:
        if not is_vowel(letter):
            new_word +=letter
        else:
            pass
    return new_word








def normalize_name(string):
    '''
Define a function named normalize_name. It should accept a string and return a valid python identifier, 
that is: 
- anything that is not a valid python identifier should be removed
- leading and trailing whitespace should be removed
- everything should be lowercase
- spaces should be replaced with underscores

for example:
Name will become name
First Name will become first_name
% Completed will become completed
'''
    
    new_string = ""
    string = string.strip().lower()
    for char in string:
        if char.isalpha() or char == ' ':
            new_string += char
        else:
            pass
    return new_string.strip().replace(" ", "_")








def cumulative_sum(a):
    '''
    # 11. Write a function named cumulative_sum that accepts a list of numbers and 
# returns a list that is the cumulative sum of the numbers in the list.
# cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]
 '''   
    new_list=[]
    cum_sum=0
    for num in a:
        cum_sum+=num
        new_list.append(cum_sum)
    return f"newlist: {new_list}"







