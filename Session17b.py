#write a python program to print even numbers in a list

list1  = [2,7,5,64,14]

for i in list1:
    if i%2==0:
        print(i,end=" ")


#write a python program to print positive numbers in a list

list1 = [2,4,-5,3,8,-10,-11]

for i in list1:
    if i>0:
        print(i,end=" ")

#write a python program to remove empty list from list and print it
list1 = [2,5,6,[],8,[],[],0]
list2=[]
for i in list1:
    if not isinstance(i,list):
       list2.append(i)
print(list2)

#write a python program to print the list having sum of digits
list1 = [12, 67, 98, 34]
list2=[]
for i in list1:
    sum = 0
    for digit in str(i): 
        sum += int(digit) 
    list2.append(sum)
print(list2)

# write a python program to find string in a list and print it
list1 = [1, 2.0, 'have', 'a', 'nice', 'day'] 

s = 'nice'
for i in list1:
    if i == s:
       print(f'{s} is  present in the list')


#write a python function to swap two numbers in a list and return the list
def swapPositions(list, pos1, pos2): 
      
    list[pos1], list[pos2] = list[pos2], list[pos1] 
    return list
  
# Driver function 
List1 = [23, 65, 19, 90] 
pos1, pos2  = 1, 3

print(swapPositions(List1, pos1-1, pos2-1)) 

# write a python function tp print the occurences of i before first j in list
list1 = [4, 5, 6, 4, 1, 4, 8, 5, 4, 3, 4, 9] 
               
# initializing i, j  
i, j = 4, 8

count=0
for k in list1:
    if k==i and k!=j:
       count=count+1
    elif k==j:
         break;   

print(count)


# write  a python program to print element with maximum values from a list

list1 = ["gfg", "best", "for", "geeks"] 
   
s=[]
for i in list1:
    count=0  
    for j in i:
        if j in ('a','e','i','o','u'):
           count=count+1
    s.append(count)
print(s)    
if  count== max(s):      
    print(list1[s.index(max(s))])

#9 write a python program to omit K length rows and print the list
list1 = [[4, 7], 
             [8, 10, 12, 8], 
             [10, 11],  
             [6, 8, 10]] 
 
# initializing K  
K = 2

for i in test_list:
    if len(i)==K:
       list1.remove(i)
print(list1)       

#10 write a python program to construct equidigit tuple and print them

list1 = [5654, 223, 982143, 34, 1021]

list2 = [] 
for sub in list1: 
      
    # getting mid element 
    mid_idx = len(str(sub)) // 2
      
    # slicing Equidigits 
    el1 = str(sub)[:mid_idx] 
    el2 = str(sub)[mid_idx:] 
      
    list2.append((int(el1), int(el2))) 
  
# printing result  
print("Equidigit tuples List : " + str(list2)) 

#11 write a python function to filter Rows with a specific pair sum and return boolean value

def pair_sum(x, k): 
  
    # checking pair sum 
    for idx in range(len(x)): 
        for ix in range(idx + 1, len(x)): 
            if x[idx] + x[ix] == k: 
                return True
    return False
  
  
# initializing list 
test_list = [[1, 5, 3, 6], [4, 3, 2, 1], [7, 2, 4, 5], [6, 9, 3, 2]] 
  
# printing original list 
print("The original list is : " + str(test_list)) 
  
# initializing K 
k = 8
  
# checking for pair sum 
res = [ele for ele in test_list if pair_sum(ele, k)] 
  
# printing result 
print("Filtered Rows : " + str(res)) 

#12 write a python program to find decreasing point in a list and print them
test_list = [3, 6, 8, 9, 12, 5, 18, 1] 
  
res = -1
for idx in range(0, len(test_list) - 1): 
      
    # checking for 1st decreasing element 
    if test_list[idx + 1] < test_list[idx]: 
        res = idx 
        break
  
# printing result  
print("Decreasing Point : " + str(res)) 


#13 Write a python program to test if all elements are unique in columns in matrix and print them

test_list = [[3, 4, 5], [1, 2, 4], [4, 1, 10]] 
  
 
res = True 
for idx in range(len(test_list[0])): 
      
    # getting column  
    col = [ele[idx] for ele in test_list] 
      
    # checking for all Unique elements 
    if len(list(set(col))) != len(col): 
        res = False 
        break
  
# printing result  
print("Are all columns Unique : " + str(res)) 

#14 Write a python program to find elements with the same index and print them

list1 = [3, 1, 2, 5, 4, 10, 6, 9] 
 
list2 = [] 
for idx, ele in enumerate(list1): 
    if idx == ele: 
        list2.append(ele) 
  
# printing result  
print("Filtered elements : " + str(list2))

#15 Write a python program to check if two list are reverse equal and print boolean value

list1 = [5, 6, 7, 8] 
list2 = [8, 7, 6, 5] 
  
# Check if two lists are reverse equal 
# Using reversed() + == operator 
res = list1 == list(reversed(list2)) 
  
# printing result  
print("Are both list reverse of each other ? : " + str(res))


#16 write a python program to extract priority elements in tuple list


test_list = [(5, 1), (3, 4), (9, 7), (10, 6)] 
  
 
# initializing Priority list  
prior_list = [6, 4, 7, 1] 
  
# Extracting Priority Elements in Tuple List and print the list 
# loop 
res = [] 
for sub in test_list: 
    for val in prior_list: 
        if val in sub: 
            res.append(val) 
print(res)

#17 Write a python program to check if any string is empty in list and print true or False

  
list1 = ['the', 'sun', 'rises', '', 'the', 'east'] 
  

# Check if any String is empty in list 
# using len() + any() 
res = any(len(ele) == 0 for ele in list1) 
  
# printing result 
print("Is any string empty in list? : " + str(res)) 

#18 write a python program to increment numeric string by K  

list = ["gfg", "234", "is", "98", "123", "best", "4"] 

# initializing K 
K = 6
  
res = []
for ele in test_list: 
  
    # incrementing on testing for digit. 
    if ele.isdigit(): 
        res.append(str(int(ele) + K)) 
    else: 
        res.append(ele) 
  
# printing result 
print("Incremented Numeric Strings : " + str(res)) 


#19 Write a python function to remove i'th character from a string

def remove(string, i):  
  
    # Characters before the i-th indexed 
    # is stored in a variable a 
    a = string[ : i]  
      
    # Characters after the nth indexed 
    # is stored in a variable b 
    b = string[i + 1: ] 
      
    # Returning string after removing 
    # nth indexed character. 
    return a + b 

#20 Write a python program to move number to end of string and print them
test_str = 'the2sun4rises5sinthe6east9'
  
# printing original string 
print("The original string is : " + str(test_str))
s=''
r=''
for i in test_str:
    if i.isdigit():
      s=s+i
    else:
      r=r+i 
print(r+s)

#21 Write a python program to count the number of spaces in a string and print it

count=0
string = "Welcome to schoolofAI"
for i in string:
    if i==" ":
        count=count+1
print(f'number of spaces {count}')

#22 Write a python program to Concatenate all elements of a list into a string and print it

 
l = ['hello', 'guys', 'have', 
   'a', 'nice', 'day'] 
  
# this will join all the  
# elements of the list with ' ' 
l = ' '.join(l)  
print(l) 

#23 Write a python program to filter similar case strings and print it

x=[]
for i in test_list:
    if i.islower() or i.isupper():
       print(x.append(i))
    
print(x) 


#24 Write a python program to increment Suffix number in string and print it

test_str = 'hello006'
x=''
r=''
for i in test_str:
    if i.isdigit() and int(i)>0:
       x=x+str(int(i)+1)
    else:
      r=r+i
print(r+x)  


#25 Write a python program to add phrase in the middle of string and print it 

test_str = 'The sun in the east'
mid_str = "rises"

s=""
l=test_str.split(" ")
for i in range(0,len(l)):
    if i==len(l)//2:
       l.insert(i,mid_str)
       break
s=" ".join(i for i in l)
print(s) 


#26 Write a program to split a string by custom length and print it

test_str = 'geeksforgeeks'
  
# printing original string 
print("The original string is : " + str(test_str)) 
  
# initializing length list 
cus_lens = [5, 3, 2, 3] 

res = [] 
strt = 0
for size in cus_lens: 
      
    # slicing for particular length 
    res.append(test_str[strt : strt + size]) 
    strt += size 
      
# printing result  
print("Strings after splitting : " + str(res)) 

#27 Write a python program to extract strings with successive alphabets in alphabetical order and print the list

list1 = ['gfg', 'is', 'best', 'for', 'geeks'] 

  
res = [] 
for i in range(0,len(list1)):
    for j in range(0,len(list1[i])-1):
        if ord(list1[i][j+1])- ord(list1[i][j])==1:
           res.append(list1[i])
print(res)

#28 Write a python program to compute arithmetic operation from String and print it


test_str = '5x6, 9x10, 7x8'
  
# using replace() to create eval friendly string 
temp = test_str.replace(',', '+').replace('x', '*') 
  
# using eval() to get the required result 
res = eval(temp) 
  
# printing result 
print("The computed summation of products : " + str(res)) 


#29 write a python  program to Extract string till first Non-Alphanumeric character and print it

test_str = 'geeks4g!!!eeks'
s=''
for i in test_str:
    
    if i.isalnum()==False:
       break
    else:
      s+=i  
print(s)   

#30 write a python program  to extract domain name from Email address and print it

test_str = 'md.shakiluzzaman@gmail.com'
  
# printing original string 
print("The original string is : " + str(test_str))
s=test_str.split('@')
print(s[1])


#31 write a python program to  check if string starts with any element in list

test_string = "GfG is best"
  
# initializing prefix list 
pref_list = ['best', 'GfG', 'good'] 
  
 
  
# using filter() + startswith() 
# Prefix tests in Strings 
res = list(filter(test_string.startswith, pref_list)) != [] 
  
# print result 
print("Does string start with any prefix list sublist ? : " + str(res))


#32 write a python function to find all permutations of a string and print the result

ini_str = "abc"
  
# Printing initial string 
print("Initial string", ini_str) 
  
# Finding all permuatation 
result = [] 
  
def permute(data, i, length):  
    if i == length:  
        result.append(''.join(data) ) 
    else:  
        for j in range(i, length):  
            # swap 
            data[i], data[j] = data[j], data[i]  
            permute(data, i + 1, length)  
            data[i], data[j] = data[j], data[i]   
permute(list(ini_str), 0, len(ini_str)) 
  
# Printing result 

print("Resultant permutations", str(result))

#33 write a python program to delete all occurences of character and print it 

test_str = "TheSchoolofAI"
  
# initializing removal character 
rem_char = "e"
  
  
# Using replace() 
# Deleting all occurrences of character 
res = test_str.replace(rem_char, "") 
  
# printing result  
print("The string after character deletion : " + str(res))

#34 Write a python program for printing alternate Strings Concatenation

test_list = ["Early", "morning", "is", "good", "for", "health"] 
  
# printing original list  
print("The original list : " + str(test_list)) 
s=[]
k=test_list[::2]
a=["".join(i for i in k)]
print(a)
l=test_list[1::2]
b=["".join(i for i in l)]
print(b)

print(a+b)

#35 Write a python program to remove duplicate word from sentence and print it
str1 = "Good bye bye world world"
l=str1.split(" ")
#s=[]
s=list(set(l))
print(" ".join(i for i in s))


#36 Write a python program to trim tuples by k and print it

test_list = [(5, 3, 2, 1, 4), (3, 4, 9, 2, 1), 
             (9, 1, 2, 3, 5), (4, 8, 2, 1, 7)] 
  
# printing original list 
print("The original list is : " + str(test_list)) 
  
# initializing K 
K = 2

l=[]
for i in test_list:
    #for j in i:
    s=tuple()
    s+=i[K:len(i)-K]
    l.append((s))
print(l)

#37 write a python program to sort Tuples by their maximum element and print it

def get_max(sub): 
    return max(sub) 
  
# initializing list 
test_list = [(4, 5, 5, 7), (1, 3, 7, 4), (19, 4, 5, 3), (1, 2)] 
  
# printing original list 
print("The original list is : " + str(test_list)) 
  
# sort() is used to get sorted result 
# reverse for sorting by max - first element's tuples 
test_list.sort(key = get_max, reverse = True) 
  
# printing result  
print("Sorted Tuples : " + str(test_list)) 


#38 write a python program to extract digits from Tuple list and print it

test_list = [(15, 3), (3, 9), (1, 10), (99, 2)] 
  
# printing original list 
print("The original list is : " + str(test_list))
s=[]
k=''
for i in test_list:
    for j in  i:
        k+=str(j)
print(list(set(k)))


#39 write a python program  to print all pair combinations of two tuples

test_tuple1 = (4, 5) 
test_tuple2 = (7, 8) 
  
# printing original tuples 
print("The original tuple 1 : " + str(test_tuple1)) 
print("The original tuple 2 : " + str(test_tuple2)) 
  
# All pair combinations of 2 tuples 
# Using list comprehension 
res =  [(a, b) for a in test_tuple1 for b in test_tuple2] 
res = res +  [(a, b) for a in test_tuple2 for b in test_tuple1] 
  
# printing result  
print("The filtered tuple : " + str(res)) 

#40 write a python program to find minimum k records from tuple list

test_list = [('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)] 
  
# Initializing K 
K = 2
  
# printing original list 
print("The original list is : " + str(test_list)) 
  
# Minimum K records 
# Using sorted() + lambda 
res = sorted(test_list, key = lambda x: x[1])[:K] 
  
# printing result 
print("The lowest K records are : " + str(res)) 


#41 write a python program to check if one tuple is subset of other and print it

test_tup1 = (10, 4, 5, 6) 
test_tup2 = (5, 10) 
  
# printing original tuples 
print("The original tuple 1 : " + str(test_tup1)) 
print("The original tuple 2 : " + str(test_tup2)) 
  
# Check if one tuple is subset of other 
# using issubset() 
res = set(test_tup2).issubset(test_tup1) 
  
# printing result 
print("Is 2nd tuple subset of 1st ? : " + str(res)) 


#42 write a python program to display keys with same values in a dictionary List

# initializing Matrix 
test_list = [{"Gfg": 5, "is": 8, "best": 0}, 
             {"Gfg": 5, "is": 1, "best": 0}, 
             {"Gfg": 5, "is": 0, "best": 0}] 
  
  
# getting keys 
keys = list(test_list[0].keys()) 
  
res = [] 
# iterating each dictionary for similar key's value 
for key in keys: 
    flag = 1
    for ele in test_list: 
  
        # checking for similar values 
        if test_list[0][key] != ele[key]: 
            flag = 0
            break
  
    if flag: 
        res.append(key) 
  
# printing result 
print("Similar values keys : " + str(res))


#43 write a python program to filter dictionaries with ordered values

test_list = [{'gfg': 2, 'is': 8, 'good': 10}, 
             {'gfg': 1, 'for': 10, 'geeks': 9}, 
             {'love': 3, 'gfg': 4}] 
  
  
# sorted to check with ordered values 
# values() extracting dictionary values 
res = [sub for sub in test_list if sorted( 
    list(sub.values())) == list(sub.values())] 
  
# printing result 
print("The filtered Dictionaries : " + str(res)) 

#44 write a python program to  rotate dictionary by K


# Python3 code to demonstrate working of 
# Rotate dictionary by K 
# Using list comprehension + items() + dictionary comprehension 
  
# initializing dictionary 
test_dict = {1: 6, 8: 1, 9: 3, 10: 8, 12: 6, 4: 9} 
  
  
# initializing K 
K = 2
  
# converting to tuples list 
test_dict = list(test_dict.items()) 
  
# performing rotate 
res = [test_dict[(i - K) % len(test_dict)] 
       for i, x in enumerate(test_dict)] 
  
# reconverting to dictionary 
res = {sub[0]: sub[1] for sub in res} 
  
# printing result 
print("The required result : " + str(res)) 

#45 write a python program to Count if dictionary position equals key or value and print it

test_dict = {5: 3, 1: 3, 10: 4, 7: 3, 8: 1, 9: 5} 
  

  
res = 0
test_dict = list(test_dict.items()) 
for idx in range(0, len(test_dict)): 
  
    # checking for key or value equality 
    if idx == test_dict[idx][0] or idx == test_dict[idx][1]: 
        res += 1
  
# printing result 
print("The required frequency : " + str(res)) 

#46 write a python program to test if Values Sum is Greater than Keys Sum in dictionary and print it

test_dict = {5: 3, 1: 3, 10: 4, 7: 3, 8: 1, 9: 5} 
  

  
res = sum(list(test_dict.keys())) < sum(list(test_dict.values())) 
  
# printing result 
print("The required result : " + str(res))

#47 write a program to  sort Dictionary by key-value Summation and print it

test_dict = {3: 5, 1: 3, 4: 6, 2: 7, 8: 1} 

# sorted() to sort, lambda provides key-value addition 
res = sorted(test_dict.items(), key=lambda sub: sub[0] + sub[1]) 
  
# converting to dictionary 
res = {sub[0]: sub[1] for sub in res} 
  
# printing result 
print("The sorted result : " + str(res)) 


#48 write a program  to divide dictionary and its keys into K equal dictionaries and print it

test_dict = {"Gfg": 20, "is": 36, "best": 100} 
  
# printing original dictionary 
print("The original dictionary is : " + str(test_dict)) 
  
# initializing size 
K = 4

s=list(test_dict.keys())
print(s)
q=list(test_dict.values())
t=[]
for i in q:
    t.append(i//K)
print(t)
q=[]
d={}
for i in range(K):
    for i in range(0,len(s)):
       d[s[i]] = t[i]
    q.append(d)
print(q) 

#49 Write a  Python function to Sort a List of Dictionaries by the Sum of their Values and print it

test_list = [{1 : 3, 4 : 5, 3 : 5}, {1 : 7, 10 : 1, 3 : 10}, {1 : 100}, {8 : 9, 7 : 3}]

def func(test_list):
    return sum(list(test_list.values()))


for i in test_list:
  test_list.sort(key=func) 
print(test_list)

#50 write a python program to remove double quotes from dictionary keys and print it

test_dict = {'"Geeks"' : 3, '"is" for' : 5, '"g"eeks' : 9} 
  
  
# dictionary comprehension to make double quotes free 
# dictionary 
res = {key.replace('"', ''):val for key, val in test_dict.items()} 
      
# printing result  
print("The dictionary after removal of double quotes : " + str(res))

#51 write a python program to check whether the values of a dictionary are in same order as in a list

test_dict = {"gfg" : 4, "is" : 10, "best" : 11, "for" : 19, "geeks" : 1} 
  

  
# initializing list  
sub_list = [4, 10, 11, 19, 1]

l=list(test_dict.values())


if l == sub_list:
   print(True)
else:
  print(False)  
  
 #52 write a python program to update a dictionary with the values from a dictionary list and print it
 
 test_dict = {"Gfg" : 2, "is" : 1, "Best" : 3} 
  
# printing original dictionary 
print("The original dictionary is : " + str(test_dict)) 
  
# initializing dictionary list  
dict_list = [{'for' : 3, 'all' : 7}, {'geeks' : 10}, {'and' : 1, 'CS' : 9}]

for i in dict_list:
    test_dict.update(i)
print(test_dict) 


#53 write a python program that displays the key of list value with maximum range and print it

test_dict = {"Gfg" : [6, 2, 4, 1], "is" : [4, 7, 3, 3, 8], "Best" : [1, 0, 9, 3]} 
  
 
max_res = 0
for sub, vals in test_dict.items(): 
      
    # storing maximum of difference 
    max_res = max(max_res, max(vals) - min(vals))     
    if max_res == max(vals) - min(vals): 
        res = sub 
          
# printing result  
print("The maximum element key : " + str(res)) 

#54 write a pythom program to find Maximum value from dictionary whose key is present in the list

test_dict = {"Gfg": 4, "is" : 5, "best" : 9, 
             "for" : 11, "geeks" : 3} 
  
# printing original dictionary 
print("The original dictionary is : " + str(test_dict)) 
  
# initializing list  
test_list = ["Gfg", "best", "geeks"] 
c=sorted(test_dict.values(),reverse=True)
for key,value in test_dict.items():
    if key in test_list and value in c[0:2]:
       print(key)

#55 write a python program to extract  N largest dictionaries keys and print it

test_dict = {6 : 2, 8: 9, 3: 9, 10: 8} 
  

# initializing N  
N = 4
  
res = [] 
  
# write a python program to extract N largest dictionaries keys  and print it
for key, val in sorted(test_dict.items(), key = lambda x: x[0], reverse = True)[:N]: 
    res.append(key) 
  
# printing result  
print("Top N keys are: " + str(res))


#56 write a python program to print a  Dictionary Keys whose Values summation equals K

test_dict = {"Gfg" : 3, "is" : 5, "Best" : 9, "for" : 8, "Geeks" : 10} 
  
# printing original dictionary 
print("The original dictionary is : " + str(test_dict)) 
  
# initializing K  
K = 14
l=[]
s=list(test_dict.values())
v=list(test_dict.keys())
for i in range(0,len(s)):
    for j in range(i+1,len(s)-1):
        if s[i]+s[j] == K:
           #print((i,j)) 
           print([v[i],v[j]]) 

#57 write a python program  to add prefix to each key name in dictionary and print it

test_dict = {'Gfg' : 6, 'is' : 7, 'best' : 9, 'for' : 8, 'geeks' : 11}  
  

  
# initializing prefix  
temp = "Pro"

d={}
for key,value in test_dict.items():
    d.update({temp+key:value})
print(d)


#58 write a python program to extract Kth index elements from Dictionary Value list and print it

test_dict = {"Gfg" : [4, 7, 5], "Best" : [8, 6, 7], "is" : [9, 3, 8]} 
  
# printing original dictionary 
print("The original dictionary is : " + str(test_dict)) 
  
# initializing K  
K = 1

s=[]
for key,value in test_dict.items():
    s.append(value[K])
print(s)    


#59 write a python program to  remove digits from Dictionary String Values List

import re 
  
# initializing dictionary 
test_dict = {'Gfg' : ["G4G is Best 4", "4 ALL geeks"], 
             'is' : ["5 6 Good"],  
             'best' : ["Gfg Heaven", "for 7 CS"]}  
  
# printing original dictionary 
print("The original dictionary is : " + str(test_dict)) 
  
# using dictionary comprehension to go through all keys 
res = {key: [re.sub('\d', '', ele) for ele in val] 
       for key, val in test_dict.items()} 
          
# printing result  
print("The filtered dictionary : " + str(res))  

#60 write a program to Test for Even values dictionary values lists and print it

test_dict = {"Gfg" : [6, 7, 3],  
             "is" :  [8, 10, 12, 16],  
             "Best" : [10, 16, 14, 6]} 
  
  
res = dict() 
for sub in test_dict: 
    flag = 1
      
    # checking for even elements 
    for ele in test_dict[sub]: 
        if ele % 2 != 0: 
            flag = 0
            break
    # adding True if all Even elements 
    res[sub] = True if flag else False
  
# printing result  
print("The computed dictionary : " + str(res))

#61 write a program to sort Dictionary by Values and Keys and print it

test_dict = {"Gfg" : 1, "is" :  3, "Best" : 2, "for" : 3, "Geeks" : 2} 
  
# printing original dictionary 
print("The original dictionary is : " + str(test_dict)) 
  
# - sign for descended values, omit if low-high sorting required 
res = {val[0] : val[1] for val in sorted(test_dict.items(), key = lambda x: (-x[1],x[0]))} 
  
# printing result  
print("Sorted dictionary : " + str(res))


#62 write a program to concatenate Ranged Values in String list and print it

test_list = ["abGFGcs", "cdforef", "asalloi"] 
  
  
# initializing range 
i, j = 2, 5
r=''
for z in test_list:
    r += z[i:j] 
print(r)

#63 write a program to replace dictionary value from other dictionary and print it


test_dict = {"Gfg" : 5, "is" : 8, "Best" : 10, "for" : 8, "Geeks" : 9} 
  
# printing original dictionary 
print("The original dictionary is : " + str(test_dict)) 
  
# initializing updict 
updict = {"Gfg"  : 10, "Best" : 17} 
d={}
for key in test_dict.keys():
     if key in updict:
        d.update({key:updict[key]})
     else:
        d.update({key:test_dict[key]})
print(d)       


#64 write a program  to convert string to dictionary and print it


# Python implementation of converting 
# a string into a dictionary 
  
# initialising string  
str = " Jan = January; Feb = February; Mar = March"
  
 
# generates key:value pair for each item 
dictionary = dict(subString.split("=") for subString in str.split(";")) 
  
# printing the generated dictionary 
print(dictionary) 

#65 write a python program to extract item with Maximum Tuple Value

test_dict = {'gfg' : (4, 6), 
             'is' : (7, 8), 
             'best' : (8, 2)} 

  
# initializing tuple index  
# 0 based indexing 
tup_idx = 1
  
# Extract Item with Maximum Tuple Value 
# Using max() + lambda 
res = max(test_dict.items(), key = lambda ele: ele[1][tup_idx])
# printing result  
print("The extracted maximum element item : " + str(res)) 


#66 write a python program  to Remove dictionary Key Words and print it

test_str = 'gfg is best for geeks'
  
# printing original string 
print("The original string is : " + str(test_str)) 
  
# initializing Dictionary 
test_dict = {'geeks' : 1, 'best': 6} 
l=test_str.split()
print(l)
s=''
for i in l:
    if i in test_dict:
       l.remove(i)
print(" ".join(i for i in l))


#67 write a python program to group Strings on Kth character and print it

test_list = ["gfg", "is", "best", "for", "geeks"] 
  
# printing original list 
print("The original list is : " + str(test_list)) 
  
# initializing K  
K = 2
d={}
for i in test_list:
    d.update({i[K-1]:[i]})
print(d) 


#68 write a python program to convert List of Dictionaries to List of Lists and print it 

test_list = [{'Nikhil' : 17, 'Akash' : 18, 'Akshat' : 20}, 
             {'Nikhil' : 21, 'Akash' : 30, 'Akshat' : 10}, 
             {'Nikhil' : 31, 'Akash' : 12, 'Akshat' : 19}] 

s=[]
count=0
for i in test_list:
    if count<1: 
       s.append(list(i.keys()))
    s.append(list(i.values()))
    count+=1
print(s) 

#69 write a python program for printing custom order dictionary 


# initializing dictionary 
test_dict = {'is' : 2, 'for' : 4, 'gfg' : 1, 'best' : 3, 'geeks' : 5}  
  

  
# initializing order 
ord_list = ['gfg', 'is', 'best', 'for', 'geeks'] 
 
c={}
for i in ord_list:
    if i in test_dict:
       c.update({i:test_dict[i]})
print(c) 


#70 write a python program to extract Numerical Dictionary values and print it

test_dict = {"Gfg" : ["34", "45", 'geeks'], 'is' : ["875", None, "15"], 'best' : ["98", 'abc', '12k']} 
  
# printing original dictionary 


res = [] 
for a, b, c in zip(*test_dict.values()):
    
    if a.isdigit() : 
        res.append((a, b, c)) 
      
# printing result  
print("The Numerical values : " + str(res)) 


#71 write a python program to count dictionaries in a list in Python and print it

test_list = [10, {'gfg' : 1}, {'ide' : 2, 'code' : 3}, 20] 
  
# printing original list 
print("The original list is : " + str(test_list)) 
count=0
for i in test_list:
    if isinstance(i,dict):
       count=count+1
print(count)    


#72 write a python program to Filter and Double keys greater than K and print it

test_dict = {'Gfg' : 4, 'is' : 2, 'best': 3, 'for' : 6, 'geeks' : 1} 
  
# printing original dictionary 
print("The original dictionary : " + str(test_dict)) 
d={}  
# initializing K 
K = 2
for keys,values in test_dict.items():
    if values >K:
       d.update({keys:2*values})
    else:
       d.update({keys:values})       
print(d)

#73 write a python program to Convert Frequency dictionary to list and print it

test_dict = {'gfg' : 4, 'is' : 2, 'best' : 5} 
  
# printing original dictionary 
print("The original dictionary : " + str(test_dict))
s=[]
for key,value in test_dict.items():
    for i in range(0,value):
        s.append(key)
print(s)

#74 write a python program to assign list items to Dictionary and print it 


test_list = [{'Gfg' :  1, 'id' : 2 },  
             {'Gfg' :  4, 'id' : 4 }] 
  
 
  
# initializing key  
new_key = 'best'
  
# initializing list  
add_list = [12, 2] 
  
# Assign list items to Dictionary 
# Using zip() + loop 
res = [] 
for sub, val in zip(test_list, add_list): 
    sub[new_key] = val 
    res.append(sub) 
      
# printing result  
print("The modified dictionary : " + str(res))


#75 write a python program to test Boolean Value of Dictionary and print it


test_dict = {'gfg' : True, 'is' : False, 'best' : True} 
  
# printing original dictionary 
print("The original dictionary is : " + str(test_dict))

res=True
for key,value in test_dict.items():
    if value==False:
       res=False
       break
print(f"Dictionary is {res}")

#76 write a python program  to print Dictionary values String Length Summation 

test_dict = {'gfg' : '2345', 
             'is' : 'abcde', 
             'best' : 'qwerty'} 
  
# printing original dictionary 
print("The original dictionary is : " + str(test_dict)) 
list1=list(test_dict.values())
print(list1)
s="".join(i for i in list1)
print(f'Summation of string values is {len(s)}')


#77 write a python program to printlist of  Keys with shortest length lists in dictionary

test_dict = {'gfg' : [4, 5], 
             'is' : [9, 7, 3, 10], 
             'best' : [11, 34], 
             'for' : [6, 8, 2],  
             'geeks' : [12, 24]} 
  
# printing original dictionary 
print("The original dictionary is : " + str(test_dict)) 
s=[]
a=0
q=[]
for key,value in test_dict.items():
    s.append(len(value))
    q.append(key)
l=[]
print(s)
print(q) 
for k,z in zip(q,s):
      if z==min(s):
         l.append(k)
print(l) 


#78 write a python program to decrement Dictionary value by K

test_dict = {'gfg' : 1, 'is' : 2, 'for' : 4, 'CS' : 5} 
  
# printing original dictionary 
print("The original dictionary : " + str(test_dict)) 
  
# Initialize K  
K = 5

for key,value in test_dict.items():
    test_dict.update({key:value-K})
print(test_dict) 


#79 write a python program to find Common items among dictionaries and print it 

test_dict1 = {'gfg' : 1, 'is' : 2, 'best' : 3} 
test_dict2 = {'gfg' : 1, 'is' : 2, 'good' : 3} 
  
# printing original dictionaries 
print("The original dictionary 1 is : " + str(test_dict1)) 
print("The original dictionary 2 is : " + str(test_dict2))

count=0
for key1,value1 in test_dict1.items():
    for key2,value2 in test_dict2.items():
        if key1==key2 and value1==value2:
           count=count+1
print(count)

#80 write a python program to print Nth largest values in dictionary









#81 write a python program to print consecutive Kth column Difference in Tuple List

# Consecutive Kth column Difference in Tuple List

test_list = [(5, 4, 2), (1, 3, 4), (5, 7, 8), (7, 4, 3)] 
  
# printing original list 
print("The original list is : " + str(test_list)) 
  
# initializing K  
K = 1 
s=[]
for i in range(0,len(test_list)-1):
    s.append(abs(test_list[i][K]-test_list[i+1][K]))
print(s)


#82 write a python program to find Tuples with positive elements in List of tuples and print it

test_list = [(4, 5, 9), (-3, 2, 3), (-3, 5, 6), (4, 6)] 
  
# printing original list 
print("The original list is : " + str(test_list)) 

#[all(i) for i in test_list if i>0]

result = [i for i in test_list if all(ele >= 0 for ele in i)] 
  
# printing result 
print("Positive elements Tuples : " + str(result))  


#83 write a python program to remove given character from first element of Tuple and print it

test_list = [("GF ! g !", 5), ("! i ! s", 4), ("best !!", 10)] 
  
# printing original list 
print("The original list is : " + str(test_list)) 
  
# initializing K  
K = "!"
  
# replace with empty string removes the desired char. 
res = [(sub[0].replace(K, ''), sub[1]) for sub in test_list] 
  
# printing result  
print("The filtered tuples : " + str(res)) 

#84  write a python program remove particular data type Elements from Tuple and print it

test_tuple = (4, 5, 'Gfg', 7.7, 'Best') 
  
# printing original tuple 
print("The original tuple : " + str(test_tuple)) 
  
# initializing data type 
a=tuple()
data_type = int 
for i in test_tuple:
    if not isinstance(i,data_type):
       a=a+(i,)
print(list(a))

#85 write a python program to print rear element extraction from list of tuples records

test_list = [(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)] 
  
# printing original list  
print ("The original list is : " + str(test_list))
s=[]
for i in test_list:
    l=len(i)
    s.append(i[l-1])

print(s)

#86 write a python program to raise elements of tuple as power to another tuple and print it

test_tup1 = (10, 4, 5, 6)  
test_tup2 = (5, 6, 7, 5) 
s=tuple() 
  
# printing original tuples  
print("The original tuple 1 : " + str(test_tup1))  
print("The original tuple 2 : " + str(test_tup2))

for i in range(0,len(test_tup1)):
    s+= (test_tup1[i] ** test_tup2[i],)
print(s)


#87 write a python program to Count the elements till first tuple and print it

test_tup = (1, 5, 7, (4, 6), 10) 
  
# printing original tuple 
print("The original tuple : " + str(test_tup))
count=0
for i in test_tup:
    if isinstance(i,tuple):
       
       break
    count=count+1
print(f'count of element till first tuple is {count}')

#88 write a python program to print Dissimilar Elements in Tuples


test_tup1 = (3, 4, 5, 6) 
test_tup2 = (5, 7, 4, 10) 
  
# printing original tuples 
print("The original tuple 1 : " + str(test_tup1)) 
print("The original tuple 2 : " + str(test_tup2))
c=tuple()
c=tuple(set(test_tup1) ^ set(test_tup2))
print(f'Dissimilar element tuple is {c}')


#89 write a python program to flatten Tuples List to String and print it

test_list = [('1', '4', '6'), ('5', '8'), ('2', '9'), ('1', '10')] 
  
# printing original tuples list 
print("The original list : " + str(test_list)) 
s=''
for i in test_list:
    for j in i:
        s+=' '+j+' '
print(f' string after flattening is {s}')

#90 write a python program to filter tuples according to list element presence and print it

test_list = [(1, 4, 6), (5, 8), (2, 9), (1, 10)] 
s=[]  
# initialize target list  
tar_list = [6, 10] 

for i in test_list:
    for j in i:
        #print(j)
        if j in tar_list:
           #print(j)
           s.append(i)
print(s)         


#91 write a python program to concatenate tuple and print it

test_tup1 = (1, 3, 5) 
test_tup2 = (4, 6) 
  
# printing original tuples 
print("The original tuple 1 : " + str(test_tup1)) 
print("The original tuple 2 : " + str(test_tup2)) 
c=test_tup1+test_tup2
print(c)

#92 write a python program to sort list under tuples and print it 

test_tup = ([7, 5, 4], [8, 2, 4], [0, 7, 5]) 
  
# printing original tuple 
print("The original tuple is : " + str(test_tup)) 
s=tuple(sorted([j for j in i],reverse=False ) for i in test_tup)
print(f'the sorted list inside tuple is {s}')

#93 write a  python program for  removing strings from tuple and printing it

test_list = [('Geeks', 1, 2), ('for', 4, 'Geeks'), (45, 'good')] 
  
# printing original list 
print("The original list : " + str(test_list)) 

s=[]
for i in test_list:
    t=tuple()
    for j in i:
        if not isinstance(j,str):
           t+=(j,)
    s.append(t)       
print(f'List after removing string from tuple is {s}')

#94 write a program to remove matching tuples and print it

test_list1 = [('Early', 'morning'), ('is','good'), ('for', 'Health')] 
test_list2 = [('Early', 'morning'), ('is','good')] 

l=[]
for i in range(0,len(test_list1)):
    for j in range(0,len(test_list2)):
        if test_list1[i]  not in test_list2:
           #continue
           l.append(test_list1[i])
           break
print(l) 

#95  write a program to Split tuple into groups of n and print it

ini_tuple = (1, 2, 3, 4, 8, 12, 3, 34, 
             67, 45, 1, 1, 43, 65, 9, 10)
n=4
N=0
s=tuple()
#t=tuple()
for i in range(0,len(ini_tuple)//n):
    t=tuple()
    for j in range(N,N+n):
        #print(ini_tuple[j])
        t+=(ini_tuple[j],)
        
    N=N+n
    s+=(t,)    
print(s)

#96 write a python program to convert  list of tuples into digits and print it



lst = [(11, 100), (22, 200), (33, 300), (44, 400), (88, 800)]
a=''
for i in lst:
    for j in i:
        a+=str(j)
print(list(set(a)))

#97 write a python program to Join tuple elements in a list and print it

test_list = [('geeks', 'for', 'geeks'), 
             ('computer', 'science', 'portal')] 
  
# printing original list 
print ("The original list is : " + str(test_list)) 
l=[]
#s=''
for i in test_list:
    s=''
    for j in i:
        s+=j+' '
    l.append(s)
print(l)    

#98 write a python program to  count the elements in a list until an element is a Tuple  and print it

li = [4, 5, 6, 10, (1, 2, 3), 11, 2, 4]
count=0
for i in li:
    if  isinstance(i,tuple):
        break
    count=count+1
print(f'count of element till tuple is encountered {count}')

#99 write a python program  to get maximum of each key Dictionary List and print it

test_list = [{"Gfg": 8, "is": 1, "Best": 9}, 
             {"Gfg": 2, "is": 9, "Best": 1}, 
             {"Gfg": 5, "is": 10, "Best": 7}] 
  
# printing original list 
print("The original list is : " + str(test_list)) 
  
  
res = {} 
for i in test_list: 
    for key, value in i.items(): 
  
        # checking for key presence and updating max 
        if key in res: 
            res[key] = max(res[key], value) 
        else: 
            res[key] = value 
  
# printing result 
print("All keys maximum : " + str(res))

#100 write a python program to extract Keys with specific Value Type

test_dict = {'gfg': 2, 'is': 'hello', 'best': 2, 'for': {'1': 3}, 'geeks': 4} 
  
# printing original dictionary 
print("The original dictionary is : " + str(test_dict)) 
  
# initializing type 
targ_type = int
  
res = [] 
for key, val in test_dict.items(): 
  
    # checking for values datatype 
    if isinstance(val, targ_type): 
        res.append(key) 
  
# printing result 
print("The extracted keys : " + str(res))


















 




 





    
# Driver Code 
if __name__ == '__main__': 
      
    string = "SchoolofAI"
      
    # Remove nth index element 
    i = 5
    
    # Print the new string 
    print(remove(string, i))



