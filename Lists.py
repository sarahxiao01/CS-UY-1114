## Sarah Xiao
## CS-UY 1114
## 29 March 2019
## Homework 6

            
 Problem #1
"""
mystery1(x) takes a string as a parameter and returns a new string; if the input string is 'yes', 'no', or 'maybe', a string exactly the same as the input will be returned;
if not, the string 'unknown' will be returned.
example: mystery1('yes')='yes' ; mystery('ohno')= 'unknown'
mystery2(lst) takes a list of strings as a parameter and returns a new string that combines all the items(i.e.strings) in the list.
example: mystery2(['i', 'woke','up','in','the','morning'])='iwokeupinthemorning'
mystery3(lst) takes a list of integers as parameter and returns a new list of integers of half its length. (which, in the case of a odd number, if the length of the original list is n,
the returned list is of length (n-1)/2.) For the new list, it takes first half (or first (n-1)/2 items in the case of odd-numbered-length lists) of the n items in the original list,
and add each of them up with another item in the original list that is n/2 greater in index to yield a correspondingly new item in the returned list. 
example: mystery3([1,3,5,7,9,10]) = [8,12,15]
mystery4() takes nothing as parameter, and returns the list [a, b, c, aa, bb, cc, aaa, bbb, ccc].
example: mystery4()= [a, b, c, aa, bb, cc, aaa, bbb, ccc]
"""

Problem #2
def avg (numbers) :
    sum= 0
    for i in range(len(numbers)):
        sum+= numbers[i]
    avg = sum / len(numbers)
    return avg
print(avg ([2,4,6,8,10]))

Problem #3
def sum_some(lower, upper, numbers):
    sum= 0
    for i in range(len(numbers)):
        if numbers[i] >= lower:
             if numbers [i] <= upper:
                 sum += numbers [i]
    return sum
print(sum_some(1, 10, [1,3, 5, 9, 15, 17, 22, 28]))

Problem #4
def is_sorted(lst): 
    isnotsorted=True
    while(isnotsorted):
        isnotsorted=False
        for i in range (len(lst)-1):
            if(lst[i+1]< lst[i]):
                isnotsorted=True
                temp = lst[i]
                lst[i] = lst[i+1]
                lst[i+1] = temp
    print(lst)
is_sorted([1,5,3,2,7,0])

Problem #5
def indices(needle, haystack):
    lst = []
    for i in range(len(haystack)):
        if needle== haystack[i]:
            lst.append(i)
    return lst
print(indices (7 , []))
print(indices (7 , [6]))
print(indices (7 , [7,8,9]))
print(indices (7 , [1,7,7,6]))
print(indices (7 , [0,7,1,7,2,7,3]))

##
##Problem #6
def Intersperse():
    new_lst=[]
    str_1= str(input('Enter a sentence:'))
    str_2= str(input('Enter a sentence:'))
    lst_1=str_1.split()
    lst_2=str_2.split()
    minLength = min(len(lst_1), len(lst_2));
    print(minLenght
    for i in range(minLength):
        new_lst+=lst_1[i]
        print(i)
        new_lst+=lst_2[i]
    if minLength== (len(lst_1)):
        for i in range(len(lst_1), len(lst_2)-len(lst_1)):
            new_lst+=lst_2[i]
    else:
        for i in range(len(lst_2)-len(lst_1),len(lst_1)):
            new_lst+=lst_1[i]  
    return new_lst
print(Intersperse())

#Problem #7
def rlencode(s):
    lst= []
    count= 1
    for i in range(1, len(s)):
        if s[i]==s[i-1]:
            count+=1
        else:
            lst_2=(s[i-1],count)
            lst.append(lst_2)
            count=1
        if i == len(s)-1:
            lst.append((s[i],count))
        return lst

def rldecode(rle):
    acc = ""
    for (ch,count) in rle:
          acc+= ch*count
    return acc
print(rlencode("abba"))
print(rlencode("aaaaaaaaaaaaaa"))
print(rlencode("Hello!"))
print(rldecode(rlencode("Hello!")))


Problem #8

def reverse_pure(xs):
    new_lst=[]
    for  i in range(len(xs)):
        new_lst.append(xs[-i-1])
    return new_lst
print(reverse_pure([1,2,3,4,5]))

def reverse_mut(xs):
    for  i in range(len(xs)//2):
        xs[i], xs[-i-1] = xs[-i-1], xs[i]  
    return xs
print(reverse_mut([1,2,3,4,5]))
    




    
