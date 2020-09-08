# Sarah Xiao
# CS-UY 1114
# 29 March 2019
# Homework 6

##Problem #1
##mystery1
'''
The program takes a string as a parameter and then returns a string containing alternative characters of the original string.
example: mystery1('banana')='bnn'
'''
##mystery2
##
'''

example:mystery2('banana')=''
'''
##mystery3
##
'''
The program takes two strings as parameters and then returns the number of characters that appear in both strings.
example:mystery3('band,and')='3'
'''
##mystery4
'''
The program takes a string as parameter and then returns a string containing all characters in the string with a preceding character that is a digit number.
example:mystery4('b4h12iuuy')='hi'
'''
Problem #2
def replace_spaces(str):
    newstr= ''
    for i in range(len(str)):
        if str[i]== ' ':
            newstr=newstr+"_"
        else:
            newstr=newstr+str[i]
    print (newstr)
replace_spaces('ll mo')

            
##Problem #3
def has_punctuation(str):
    for i in range(len(str)):
        if str[i] in "'.,;:?!":
            return True
    return False
##print(has_punctuation("s,,llr:"))
print(has_punctuation("sllr"))

Problem #4

def title_case(str):
    newstr=''
    for i in range(len(str)):
        if i==0:
            newstr+=str[i].upper()
        elif str[i-1] in "'.,;:?! ":
            newstr+=str[i].upper()
        else:
            newstr+=str[i]
    return newstr
print(title_case("N!y!u!"))

Problem #5

def is_valid_password(str):
    count_upper=0
    count_lower=0
    count_digit=0
    count_special=0
    for i in range(len(str)):
        if str[i].isdigit() == True:
            count_digit+=1
        if str[i] in "!@#$":
            count_special+=1
        if str[i].islower() == True:
            count_lower+=1
        if str[i].isupper() == True:
            count_upper+=1
    if count_upper>=2 and count_lower>=1 and count_digit>=2 and count_special>=1:
        return True
    else:
        return False
##print(is_valid_password('4555qqQQio!$'))
print(is_valid_password('4qqxx'))            

Problem #6
def calc(numberstr):
  for i in range(len(numberstr)):
      count= 0
      if numberstr[i]==' 'and count=0:
          str_1=numberstr[0:i-1]
          count+=1
      if numberstr[i]==' 'and count=1:
          count+=1
      if numberstr[i]==' 'and count=2:
          count+=1
          str_3=numberstr[i+1:len(numberstr)]
          str_2= numberstr[i-1]
    num_1=float(str_1)
    num_2=float(str_3)
    num_1 


Problem #7
def finder(needle, haystack):
    count=0
    n= len(needle)
    for i in range(len(haystack)):
        if needle == haystack[i:(i+n-1)]:
            count+=i
            return count
        else:
            return -1
print(finder('na', 'banana'))



        
            
