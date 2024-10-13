ex.1 Say "Hello, World!" With Python

if __name__ == '__main__':
    print("Hello, World!")

ex.2 Python If-Else

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n%2==1:
        print ('Weird')
    if n%2==0 and 2 <= n <= 5:
        print ('Not Weird')
    if n%2==0 and 6 <= n <= 20:
        print ('Weird')
    if n%2==0 and n > 20:
        print ('Not Weird')        

ex.3 Python: Division

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)


ex.4 Loops

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i*i)

ex.5 Arithmetic Operators

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)

ex.6 Write a function

def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%4==0:
        leap=True
        if year%100==0:
            leap=False
            if year%400==0:
                leap=True
    
    
    
    return leap

ex. 7 Print Function

f __name__ == '__main__':
    n = int(input())
    for i in range(1, n+1):
        print(i, end='')

ex.8 List Comprehensions

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    


    interi = []
    for i in range(x + 1):
        for j in range(y + 1):
            for k in range(z + 1):
                if i + j + k != n:
                    interi.append([i, j, k])
    
    print(interi)

ex. 9 Find the Runner-Up Score!

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    arr=list(arr)
    massimo = max(arr)
    nuova_lista_senza_massimo=[]
    for score in arr:
        if score != massimo:
            nuova_lista_senza_massimo.append(score)
    nuovo_massimo = max(nuova_lista_senza_massimo)
    print(nuovo_massimo)
                
ex.10 Nested Lists

if __name__ == '__main__':
    
    lista=[]
    lista_score=[]
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        lista.append([name, score])
        lista_score.append(score)
    secondo_voto_basso=min([score for score in lista_score if score != min(lista_score)])
    studenti_secondo_voto_basso=[i[0] for i in lista if i[1]==secondo_voto_basso]
    for nome_studenti in sorted(studenti_secondo_voto_basso):
        print(nome_studenti)

ex. 11 Finding the percentage

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    media = sum(student_marks[query_name])/len(student_marks[query_name])
    print(f"{media:.2f}")

ex. 12 Lists

if __name__ == '__main__':
    N = int(input())
     
    lista = [] 
    
    for i in range(N):
        command = input().split()  
        operation = command[0]  
        
        if operation == 'insert':
            index = int(command[1])
            element = int(command[2])
            lista.insert(index, element)
            
        elif operation == 'print':
            print(lista)  
        
        elif operation == 'remove':
            element = int(command[1])
            lista.remove(element) 
            
        elif operation == 'append':
            element = int(command[1])
            lista.append(element)  
        
        elif operation == 'sort':
            lista.sort()  
        
        elif operation == 'pop':
            lista.pop()  
        
        elif operation == 'reverse':
            lista.reverse()  

ex. 13 Tuples

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
    t=tuple(integer_list)
    print(hash(t))

ex. 14 sWAP cASE

def swap_case(s):
    return s.swapcase()

ex. 15 String Split and Join

def split_and_join(line):
    # write your code here
    a = line.split(" ")
    return "-".join(a)
    
    

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

ex. 16 What's Your Name?

#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    # Write your code here
    print('Hello ' + first_name + ' ' + last_name + '! You just delved into python.')

ex. 17 Mutations

def mutate_string(string, position, character):
    lista=list(string)
    lista[position]=character
    string =''.join(lista)
    return  string

ex. 18 Find a string

def count_substring(string, sub_string):
    
    count=0
    len_substring=len(sub_string)
    
    for i in range(len(string)-len_substring+1):
        if string[i:i+len_substring]==sub_string:
            count+=1
    return count

ex. 19 String Validators

if __name__ == '__main__':
    s = input()
    
    print(any(lettera.isalnum() for lettera in s))
    print(any(lettera.isalpha() for lettera in s))
    print(any(lettera.isdigit() for lettera in s))
    print(any(lettera.islower() for lettera in s))
    print(any(lettera.isupper() for lettera in s))

ex. 20 Text Wrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

ex. 21 Text Alignment

#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

ex. 22 Designer Door Mat

# Enter your code here. Read input from STDIN. Print output to STDOUT

N, M = map(int, input().split())

for i in range(1, N, 2):
    pattern = ".|." * i
    print(pattern.center(M, '-'))

print("WELCOME".center(M, '-'))

for i in range(N-2, 0, -2):
    pattern = ".|." * i
    print(pattern.center(M, '-'))

ex. 23 String Formatting

def print_formatted(number):
    # your code goes here
    width = len(bin(number)) - 2
    

    for i in range(1, number + 1):
       
        decimal_value = str(i).rjust(width)
        octal_value = oct(i)[2:].rjust(width)
        hex_value = hex(i)[2:].upper().rjust(width)
        binary_value = bin(i)[2:].rjust(width)
        
       
        print(f"{decimal_value} {octal_value} {hex_value} {binary_value}")

ex. 24 Alphabet Rangoli

def print_rangoli(size):
    # your code goes here
    
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    
    
    linee = []
    
    
    for i in range(size):
       
        s = '-'.join(alfabeto[size-1:i:-1] + alfabeto[i:size])
        # Centrare la stringa con trattini sulla larghezza massima
        linee.append(s.center(4*size - 3, '-'))
    
    # Stampare il risultato combinando la parte superiore con quella inferiore
    print('\n'.join(linee[::-1] + linee[1:]))

ex. 25 Capitalize!

# Complete the solve function below.
def solve(s):
    return ' '.join([parola.capitalize() for parola in s.split(' ')])

ex. 26 The Minion Game

def minion_game(string):
    # your code goes here
    vocali= 'AEIOU'
    punteggio_kevin= 0
    punteggio_stuart= 0
    lunghezza = len(string)
    
    for i in range(lunghezza):
        if string[i] in vocali:
            punteggio_kevin+=lunghezza-i
        else:
            punteggio_stuart+=lunghezza-i
            
    if punteggio_kevin > punteggio_stuart:
       print("Kevin " + str(punteggio_kevin))
    elif punteggio_stuart > punteggio_kevin:
        print("Stuart " + str(punteggio_stuart))
    else:
        print("Draw")

ex. 27 Merge the Tools!

def merge_the_tools(string, k):
    # your code goes here
    for i in range(0, len(string), k):
        substring = string[i:i+k]
        
        seen = set()
        result = []
        
        for carattere in substring:
            if carattere not in seen:
                seen.add(carattere)
                result.append(carattere)
        
     
        print(''.join(result))

ex. 28 Introduction to Sets

def average(array):
    # your code goes here
    altezze_distinte= set(array)
    
    return round(sum(altezze_distinte)/len(altezze_distinte),3)
    
ex. 29 Symmetric Difference

# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())  

a_input = input()  
a_list = a_input.split() 
a_set = set(map(int, a_list)) 

n = int(input()) 

b_input = input()  
b_list = b_input.split() 
b_set = set(map(int, b_list))  

symmetric_diff = a_set.symmetric_difference(b_set) 

sorted_result = sorted(symmetric_diff)

for num in sorted_result:
    print(num)

ex. 30 Set .add()

# Enter your code here. Read input from STDIN. Print output to STDOUT
country_stamps = set()

n = int(input())

for _ in range(n):
    country = input().strip()  
    country_stamps.add(country)

print(len(country_stamps))

ex. 31 No Idea!

# Enter your code here. Read input from STDIN. Print output to STDOUT
def calculate_happiness(arr, A, B):
    happiness = 0
    for element in arr:
        if element in A:
            happiness += 1
        elif element in B:
            happiness -= 1
    return happiness

if __name__ == '__main__':
    n, m = map(int, input().split())  
    arr = list(map(int, input().split()))  
    A = set(map(int, input().split()))  
    B = set(map(int, input().split()))
    
    result = calculate_happiness(arr, A, B)
    
    print(result)

ex. 32 Set .discard(), .remove() & .pop()

n = int(input())
s = set(map(int, input().split()))

num_command=int(input())
for _ in range(num_command):
    command=input().split()
    
    if command[0]=="pop":
        s.pop()
        
    if command[0]=="remove":
        s.remove(int(command[1]))
        
    if command[0]=="discard":
        s.discard(int(command[1]))
        
print(sum(s))           

ex. 33 Set .union() Operation

# Enter your code here. Read input from STDIN. Print output to STDOUT
num_ing=int(input())
matr_ing=set(map(int, input().split()))

num_fr=int(input())
matr_fr=set(map(int, input().split()))

unione=matr_ing.union(matr_fr)

print(len(unione))

ex. 34 Set .intersection() Operation

# Enter your code here. Read input from STDIN. Print output to STDOUT
num_ing=int(input())
matr_ing=set(map(int, input().split()))

num_fr=int(input())
matr_fr=set(map(int, input().split()))

unione=matr_ing.intersection(matr_fr)

print(len(unione))

ex. 35 Set .difference() Operation

# Enter your code here. Read input from STDIN. Print output to STDOUT
num_ing=int(input())
matr_ing=set(map(int, input().split()))

num_fr=int(input())
matr_fr=set(map(int, input().split()))

diff=matr_ing.difference(matr_fr)

print(len(diff))

ex. 36 Set .symmetric_difference() Operation

# Enter your code here. Read input from STDIN. Print output to STDOUT
num_ing=int(input())
matr_ing=set(map(int, input().split()))

num_fr=int(input())
matr_fr=set(map(int, input().split()))

sym_diff=matr_ing.symmetric_difference(matr_fr)

print(len(sym_diff))

ex. 37 Set Mutations

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())  
s = set(map(int, input().split()))  

n_operations = int(input())  

for _ in range(n_operations):
    command = input().split()
    operation=command[0]
    
    other_set = set(map(int, input().split()))  
    
    if operation == "intersection_update":
        s.intersection_update(other_set)
    elif operation == "update":
        s.update(other_set)
    elif operation == "symmetric_difference_update":
        s.symmetric_difference_update(other_set)
    elif operation == "difference_update":
        s.difference_update(other_set)


print(sum(s))

ex. 38 The Captain's Room

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

k=int(input())

numero_stanza= list(map(int, input().split()))

contatore_stanze=Counter(numero_stanza)

for stanza, conteggio in contatore_stanze.items():
    if conteggio == 1:
        print(stanza)
        break

ex. 39 Check Subset

# Enter your code here. Read input from STDIN. Print output to STDOUT
x=int(input())

for _ in range(x):
    num_a=int(input())
    set_a=set(map(int, input().split()))
    
    num_b=int(input())
    set_b=set(map(int, input().split()))
    
    print(set_a.issubset(set_b))
    
ex. 40 Check Strict Superset

# Enter your code here. Read input from STDIN. Print output to STDOUT


A = set(map(int, input().split()))
n = int(input())

is_st_sub = True

for _ in range(n):
    B = set(map(int, input().split()))
    if not A > B:
        is_st_sub = False

print(is_st_sub)

ex. 41 collections.Counter()

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

scarpe_disponibili=int(input())

taglia_scarpe=list(map(int, input().split()))

inventario=Counter(taglia_scarpe)

clienti=int(input())

guadagno=0

for _ in range(clienti):
    taglia, prezzo=map(int, input().split())
    
    if inventario[taglia]>0:
        guadagno+=prezzo
        inventario[taglia]-=1
        
print(guadagno)

ex. 42 DefaultDict Tutorial

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import defaultdict

n, m =map(int, input().split())

positions= defaultdict(list)

for i in range(1, n+1):
    word=input().strip()
    positions[word].append(i)
    
for _ in range(m):
    query = input().strip()
    if query in positions:
        print(" ".join(map(str, positions[query])))
    else:
        print(-1)

ex. 43 Collections.namedtuple()

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
Num_stud = int(input())
columns = input().split()
Student = namedtuple('Student', columns)
print(f"{sum(int(Student(*input().split()).MARKS) for _ in range(Num_stud)) / Num_stud:.2f}")

ex. 44 Collections.OrderedDict()

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

num_art = int(input())
items = OrderedDict()

for _ in range(num_art):
    line = input().split()
    
    price = int(line[-1])
    
    item_name = ' '.join(line[:-1])
    
    if item_name in items:
        items[item_name] += price
    else:
        items[item_name] = price

for item_name, net_price in items.items():
    print(item_name, net_price)

ex. 45 Word Order

# Enter your code here. Read input from STDIN. Print output to STDOUT
num_par = int(input())

word_count = {}
distinct_words = []

for _ in range(num_par):
    word = input().strip()  
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1   
        distinct_words.append(word)  

print(len(distinct_words))
print(" ".join(str(word_count[word]) for word in distinct_words))

ex. 46 Collections.deque()

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

num_op=int(input())
d=deque()

for _ in range(num_op):
    command= input().split()
    method=command[0]
    
    if method=="append":
        d.append(int(command[1]))
        
    if method=="appendleft":
        d.appendleft(int(command[1]))
        
    if method=="pop":
        d.pop()
        
    if method=="popleft":
        d.popleft()
        
print(" ".join(map(str, d)))

ex. 47 Company Logo

#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter

if __name__ == '__main__':

    
    s=input()
    count=Counter(s)
    
    sorted_chars = sorted(count.items(), key=lambda x: (-x[1], x[0]))
    
    for char, count in sorted_chars[:3]:
        print(char, count)

ex. 48 Calendar Module

# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

month, day, year= map(int, input().split())

giorni_settimana= calendar.weekday(year, month, day)

giorni= days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

print(giorni[giorni_settimana])

ex. 49 Time Delta

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the time_delta function below.

from datetime import datetime
def time_delta(t1, t2):
    time_format = "%a %d %b %Y %H:%M:%S %z"
    
    dt1=datetime.strptime(t1, time_format)
    dt2=datetime.strptime(t2, time_format)

    diff_sec=abs(int((dt1-dt2).total_seconds()))
    
    return str(diff_sec)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()

ex. 50 Exceptions

# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(input())

for _ in range(t):
    try:
        a, b = map(int, input().split())
        result = a // b
        print(result)
    
    except ZeroDivisionError as e:
        print("Error Code:", e)
    
    except ValueError as e:
        print("Error Code:", e)

ex. 51 Zipped!

# Enter your code here. Read input from STDIN. Print output to STDOUT

stud, mat = map(int, input().split())
voti= [list(map(float, input().split())) for _ in range(mat)]

for voti_stud in zip(*voti):
    media = sum(voti_stud)/mat
    print(f"{media:.1f}")

ex. 52 Athlete Sort

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    arr.sort(key=lambda x: x[k])
    for row in arr:
        print(*row)

ex. 53 ginortS

# Enter your code here. Read input from STDIN. Print output to STDOUT

s= input().strip()

minuscolo=[]
maiuscolo=[]
dispari=[]
pari=[]

for char in s:
    if char.islower():
        minuscolo.append(char)
    elif char.isupper():
        maiuscolo.append(char)
    elif char.isdigit():
        if int(char) % 2 == 1:
            dispari.append(char)
        else:
            pari.append(char)
        
minuscolo.sort()
maiuscolo.sort()
dispari.sort()
pari.sort()

finale= ''.join(minuscolo+maiuscolo+dispari+pari)

print(finale)

ex. 54 Map and Lambda Function

cube = lambda x: x**3 # complete the lambda function 


def fibonacci(n):
      fib_list = []
      a, b = 0, 1
      for _ in range(n):
         fib_list.append(a)
         a, b = b, a + b
      return fib_list

ex. 55 Detect Floating Point Number

# Enter your code here. Read input from STDIN. Print output to STDOUT

N= int(input())
for _ in range(N):
    i= input()
    if i =="0":
        print(False)
    else:
        try:
            float(i)
            print(True)
        except ValueError:
            print(False)

ex. 56 Re.split()

regex_pattern = r"[,.]"	# Do not delete 'r'.

ex. 57 Group(), Groups() & Groupdict()

# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

s = input().strip()

trovato = re.search(r'([a-zA-Z0-9])\1', s)

if trovato:
    print(trovato.group(1))
else:
    print(-1)

ex. 58 Re.findall() & Re.finditer()

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

s = input().strip()

pattern = r'(?<=[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ])([aeiouAEIOU]{2,})(?=[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ])'

matches = re.findall(pattern, s)

if matches:
    for match in matches:
        print(match)
else:
    print(-1)

ex. 59 Re.start() & Re.end()

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

S = input().strip()
sub = input().strip()

matches = list(re.finditer(f'(?={sub})', S))

if matches:
    for match in matches:
        start = match.start()
        print((start, start + len(sub) - 1))
else:
    print((-1, -1))

ex. 60 Regex Substitution

# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

n = int(input().strip())

lines = [input() for _ in range(n)]

for line in lines:
    line = re.sub(r'(?<= )&&(?= )', 'and', line)
    
    line = re.sub(r'(?<= )\|\|(?= )', 'or', line)
    
    print(line)

ex. 61 Validating Roman Numerals

regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"	# Do not delete 'r'.

ex. 62 Validating phone numbers

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n = int(input())

for _ in range(n):
    mobile_number = input().strip()
    
    if re.match(r"^[789]\d{9}$", mobile_number):
        print("YES")
    else:
        print("NO")

ex. 63 Validating and Parsing Email Addresses

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
import email.utils

n = int(input())

for _ in range(n):
    line = input().strip()  
    name, email_address = email.utils.parseaddr(line) 

    if re.match(r'^[a-zA-Z][\w\.\-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$', email_address):
        print(name + " <" + email_address + ">") 

ex. 64 Validating UID

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n = int(input())

for _ in range(n):
    uid = input().strip()
    
    if len(uid) != 10:
        print('Invalid')
        continue
    
    if not uid.isalnum():
        print('Invalid')
        continue
    
    if len(re.findall(r'[A-Z]', uid)) < 2:
        print('Invalid')
        continue
    
    if len(re.findall(r'\d', uid)) < 3:
        print('Invalid')
        continue
    
    if len(set(uid)) != 10:
        print('Invalid')
        continue
    
    print('Valid')

ex. 65 Validating Credit Card Numbers

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n = int(input())

for _ in range(n):
    card_number = input().strip()

   
    if re.match(r'^[456]\d{3}(-?\d{4}){3}$', card_number):
        
        clean_card = card_number.replace('-', '')
        
        if re.search(r'(\d)\1{3,}', clean_card):
            print('Invalid')
        else:
            print('Valid')
    else:
        print('Invalid')

ex. 66 Validating Postal Codes

regex_integer_in_range = r"^[1-9]\d{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(?=(\d)(?=\d\1))"	# Do not delete 'r'.

ex. 67 XML2 - Find the Maximum Depth

maxdepth = 0
def depth(elem, level):
    global maxdepth
    # your code goes here
    level += 1
    
    if level > maxdepth:
        maxdepth = level
    
    for child in elem:
        depth(child, level)

ex. 68 Standardize Mobile Number Using Decorators

def wrapper(f):
    def fun(l):
        # complete the function
        l = ['+91 ' + n[-10:-5] + ' ' + n[-5:] for n in l]
        return f(l)
    return fun

ex. 69 Decorators 2 - Name Directory

def person_lister(f):
    def inner(people):
        # complete the function
        people.sort(key=lambda x: int(x[2]))
        return [f(person) for person in people]
    return inner

ex. 70 Arrays

def arrays(arr):
    # complete this function
    # use numpy.array
    np_array = numpy.array(arr, float)
    rev_arr = np_array[::-1]
    return rev_arr

ex. 71 Shape and Reshape

import numpy

arr= input().strip().split(" ")

int_np_arr= numpy.array(arr, int)

reshape_arr= numpy.reshape(int_np_arr, (3,3))

print (reshape_arr)

ex. 72 Transpose and Flatten

import numpy

n, m = map(int, input().split())

mat = []

for _ in range(n):
    row = list(map(int, input().split()))
    mat.append(row)

matrix = numpy.array(mat)

print(numpy.transpose(matrix))

print(matrix.flatten())

ex. 73 Concatenate

import numpy

N, M, P = map(int, input().split())

array_1 = [list(map(int, input().split())) for _ in range(N)]
array_2 = [list(map(int, input().split())) for _ in range(M)]

array_1_np = numpy.array(array_1)
array_2_np = numpy.array(array_2)

concatenated_array = numpy.concatenate((array_1_np, array_2_np), axis=0)

print(concatenated_array)

ex. 74 Zeros and Ones

import numpy

shape = tuple(map(int, input().split()))

zeros_array = numpy.zeros(shape, dtype=int)  
ones_array = numpy.ones(shape, dtype=int)   

print(zeros_array)
print(ones_array)

ex. 75 Eye and Identity

import numpy

numpy.set_printoptions(legacy='1.13')

n, m = map(int, input().split())

array = numpy.eye(n, m)

print(array)

ex. 76 Array Mathematics

import numpy

n, m = map(int, input().split())

array1 = numpy.array([input().split() for _ in range(n)], int)
array2 = numpy.array([input().split() for _ in range(n)], int)

add_result = array1 + array2
subtract_result = array1 - array2
multiply_result = array1 * array2
floor_divide_result = numpy.floor_divide(array1, array2)  # Usando floor division
mod_result = array1 % array2
power_result = numpy.power(array1, array2)

print(add_result)
print(subtract_result)
print(multiply_result)
print(floor_divide_result)
print(mod_result)
print(power_result)

ex. 77 Floor, Ceil and Rint

import numpy



numpy.set_printoptions(legacy='1.13') 

A = numpy.array(input().split(), float)

print(numpy.floor(A))
print(numpy.ceil(A))
print(numpy.rint(A))

ex. 78 Sum and Prod

import numpy



numpy.set_printoptions(legacy='1.13')

x, y = map(int, input().split())

array = numpy.array([input().split() for _ in range(x)], int)

sum_along_axis_0 = numpy.sum(array, axis=0)

product_of_sum = numpy.prod(sum_along_axis_0)

print(product_of_sum)

ex. 79 Min and Max

import numpy

x, y = map(int, input().split())

array = numpy.array([input().split() for _ in range(x)], int)

min_along_axis_1 = numpy.min(array, axis=1)

max_of_min = numpy.max(min_along_axis_1)

print(max_of_min)

ex. 80 Dot and Cross

import numpy


n = int(input())

A = numpy.array([list(map(int, input().split())) for _ in range(n)])
B = numpy.array([list(map(int, input().split())) for _ in range(n)])

result = numpy.dot(A, B)

print(result)

ex. 81 Inner and Outer

import numpy



A = numpy.array(list(map(int, input().split())))
B = numpy.array(list(map(int, input().split())))

inner_product = numpy.inner(A, B)

outer_product = numpy.outer(A, B)

print(inner_product)

print(outer_product)

ex. 82 Polynomials

import numpy

coefficients = list(map(float, input().split()))

x = float(input())

result = numpy.polyval(coefficients, x)

print(result)

ex. 83 Linear Algebra

import numpy

N = int(input())

matrix = numpy.array([list(map(float, input().split())) for _ in range(N)])

determinant = numpy.linalg.det(matrix)

print(round(determinant, 2))

ex. 84 Birthday Cake Candles

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    max_height = max(candles)
    return candles.count(max_height)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()

ex.85 Number Line Jumps

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    # Write your code here
     if v1 == v2:
        if x1 == x2:
            return "YES"
        else:
            return "NO"
     else:
        n = (x2 - x1) / (v1 - v2)
        if n >= 0 and n.is_integer():
            return "YES"
        else:
            return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

ex. 86 Viral Advertising

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    # Write your code here
    shared = 5  
    cumulative_likes = 0  

    for day in range(n):
        liked = shared // 2  
        cumulative_likes += liked  
        shared = liked * 3  

    return cumulative_likes

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

ex. 87 Recursive Digit Sum

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Write your code here
    digit_sum = sum(int(digit) for digit in n)
    
    initial_super_digit = digit_sum * k
    
    def recursive_super_digit(x):
        if x < 10:  
            return x
        else:
            return recursive_super_digit(sum(int(digit) for digit in str(x)))
    
    return recursive_super_digit(initial_super_digit)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

ex. 88 Insertion Sort - Part 1

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    
    to_insert = arr[-1]
    index = n - 1
    
    for i in range(n - 2, -1, -1):
        if arr[i] > to_insert:
            arr[index] = arr[i]  
            print(" ".join(map(str, arr)))  
            index -= 1
        else:
            break  
            
    arr[index] = to_insert
    print(" ".join(map(str, arr)))  


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

ex. 89 Insertion Sort - Part 2

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    # Write your code here
    for i in range(1, n):
        to_insert = arr[i]  
        j = i - 1  
        while j >= 0 and arr[j] > to_insert:
            arr[j + 1] = arr[j]  
            j -= 1

        arr[j + 1] = to_insert

        print(" ".join(map(str, arr)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)

ex. 90 Mean, Var, and Std

import numpy




n,m=input().split()
n,l=int(n),[]

for _ in range(n):
    l.append(list(map(int,input().split())))
my_array=numpy.array(l)

print(numpy.mean(my_array,axis=1))
print(numpy.var(my_array,axis=0))
print(round(numpy.std(my_array),11))

ex. 91 Hex Color Code

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
pattern=r'(#[0-9a-fA-F]{3,6}){1,2}[^\n ]'
for _ in range(int(input())):
    for x in re.findall(pattern,input()):
        print(x)

ex. 92 Detect HTML Tags, Attributes and Attribute Values

# Enter your code here. Read input from STDIN. Print output to STDOUT

from html.parser import HTMLParser

html = '\n'.join([input() for _ in range(int(input()))]) 

parser = HTMLParser()

parser.handle_starttag = lambda tag, attrs: (
    print(tag) or [print('-> {} > {}'.format(*attr)) for attr in attrs]
)

parser.feed(html)



