#A calender with 3 months in a row.

# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 17:22:06 2020

@author: User
"""
month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

week = ["Sun", "Mon", "Tue", "Wed", "Thur", "Fri", "Sat"]

days=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
                    
months = [[[0 for a in range(7)] for b in range(6)] for c in range(12)]            
        
def leap(year):
    if(year>1752):
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False
    else:
        if year%4 == 0:
            return True
        else:
            return False
yr=int(input('Enter Year: '))
y=yr-1
k=y%100 
j=y//100
strtday=0
if(yr<=1752):
    strtday=1+13*(13+1)//5+k+k//4+5+6*j 
else:
    strtday=1+13*(13+1)//5+k+k//4+j//4+5*j
strtday=strtday%7 
if(strtday==0):
    strtday=6 
else:
    strtday-=1
if(leap(yr)):
    days[1]+=1 
for i in range(12):
    c = 1
    for j in range(6):
        for k in range(7):
            if k == strtday:
                months[i][j][k] = c
                c += 1
                strtday += 1
                if yr == 1752 and i == 8 and c==3:
                    c = 14
                if c > days[i]:
                    break
        strtday %= 7
        if c > days[i]:
            break
print('{0}'.format(yr).center(120))
print()
    
for i in range(0, 12, 3):
    for j in range(3):
        if i == 0 or i == 9:
            print("               ", month[i + j], end="               ")
        elif i == 3:
            print("               ", month[i + j], end="               ")
        else:
            if j == 1:
                print("               ", month[i + j], end="               ")
            else:
                print("               ", month[i + j], end="               ")

    print()
    for k in range(6):
        if k == 0:
            print(end=" ")
            for v in range(3):
                for day in week:
                    print(" ", day, end="")
                print(end="     ")
            print()
        for m in range(3):
            for p in range(7):
                if months[i + m][k][p] == 0:
                    print("     ", end="")
                elif months[i + m][k][p] < 10:
                    print("   ", months[i + m][k][p], end="")
                else:
                    print("  ", months[i + m][k][p], end="")
            print(end="     ")
        print()
    print()
