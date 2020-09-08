## Sarah Xiao
## CS 1114
## 11 April 2019
## Homework 7

import math
## Problem 1

def read_file(filename):
    file_obj = open(filename, "r")
    newlst=[]
    file_obj.readline()
    for line in file_obj:
        linelst= line.split(',')
        newlst.append(linelst)
    file_obj.close()
    return newlst

colleges = read_file("colleges.csv")
somecollege = colleges[50]
print(somecollege[3])
print(somecollege[6])

## Problem 2
def find_most_exclusive_womens_college(colleges):
    var= 1
    string= ''
    for item in colleges:
        if item[22] == '1':
            if float(item[24])< var:
                var=float(item[24])
                string=item[3]
    return string
print("The most selective women's college is "+ find_most_exclusive_womens_college(colleges))

##Problem 3

def average_sat_score_in_ny(colleges):
    count=0
    total=0
    for item in colleges:
        if item[5]== 'NY':
            if item[25]!= 'NULL':
                count+=1
                total+=float(item[25])
    return total / count
print(average_sat_score_in_ny(colleges))

##Problem 4

def distance(first , second):
    distance= math.sqrt((first[0]-second[0])**2+(first[1]-second[1])**2)
    return distance
print(distance((40.730610, -73.935242), (34.052235, -118.243683)))

##Problem 5

def find_college_nearest_center_of_us(colleges):
    center=(39.833333, -98.583333)
    var=100
    string=''
    for item in colleges:
        if item[18]!= 'NULL' and item[19]!= 'NULL':
            temp= math.sqrt((float(item[18])-center[0])**2+(float(item[19])-center[1])**2)
            if temp< var:
                var=temp
                string=item[3]
    return string
print(find_college_nearest_center_of_us(colleges))                    

##Problem 6
    
def main():
    colleges = read_file("colleges.csv")
    print("Most exclusive women 's college:", find_most_exclusive_womens_college(colleges))
    print("Average SAT of all NY schools:", average_sat_score_in_ny(colleges))
    print("College nearest geographical center of contiguous US:", find_college_nearest_center_of_us(colleges))
main()
        
    
