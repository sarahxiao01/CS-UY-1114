## Sarah Xiao
## CS 1114
## 18 April 2019
## Homework 8

##Problem 1
def respell(str):
    respellings = {"teh": "the", "relevent": "relevant", "lite": "light", "lol": "haha"}
    lst= str.split()
    new_lst=[]
    for i in range(len(lst)):
        if lst[i] in respellings:
            new_lst.append(respellings[lst[i]])
        else:
            new_lst.append(lst[i])
    newstr=' '.join(new_lst)
    return newstr
print(respell("I ate teh whole thing lol"))

##Problem 2

def word_positions(string):
    lst= string.split()
    my_dict={}
    for i in range(len(lst)):
        if lst[i] not in my_dict:
            my_dict[lst[i]]=[i]
        elif lst[i] in my_dict:
            my_dict[lst[i]].append(i)
    return my_dict
print(word_positions('It was the best of times it was the worst of times '))

##Porblem 3

def commonest(my_dict):
    string=''
    count=0
    for key in my_dict:
        if len(my_dict[key]) >count:
            count= len(my_dict[key])
            string=key
    return string
print(commonest(word_positions("He thought a thought he'd never thought before")))

    
    
    
