'''
Created on Sep 21, 2014

@author: Lead
'''
"""# Program to perform all permutation of digits with fixed places(repeating digits are not present in the array)
# This program is done in python 3.4"""

import time
"""The visit function is to print the list for permutation """
def visit (B,n) :
    global Const
    global k
    global size
    if verb>0:
        for i in range(0,(n)):
            if B[i]>0 :
                print(B[i],end = " ")
        print(end = "\n")
    size = size+1
"""The visitx function is to print the list for combination """
def visitx (A,n) :
    global verb
    global Const
    global count
    Const=int(Const)
    if (verb == 0 or verb == 2):
        j=0
        for i in range(0,int(n)):
            if A[i]>0 :
                B[j]=A[i]
                j=j+1
        permute(B,0,Const)
        return
    elif verb == 3:
        for i in range(0,int(n)):
            if A[i]>0 :
                print(A[i],end = " ")
        print(end = "\n")
    else :
        count = count+1
"""Combine is the function which filling the array and generates all the fisible combination 
A = Original Array
Numb = Number of element is the array
i = Number of element is the array
Const = Number of places for which combinations to be performed
Input : Array A which contains all zero, The value is feeded into the array and the combination is performed which will call the function recurrsively
i = The number of element in array
Const =  The number of places in which combination is to be performed
""" 
def Combine (A,i,Const):
    global Numb
    constant = int(Const)
    n=int(Numb)
    k=int(Const)
    i=int(i)
    if k == 0:
        visitx(A,n)
        #print(A)
    elif(i<k):
        return    
    else :
        A[i-1] = i                
        Combine(A,int(i-1),int(k-1))
        A[i-1]=0
        Combine(A,int(i-1),int(k))
"""Permute is the function which filling the array and generates all the fisible permutation 
B = Array which is feeded in visitx function and has combination values and needs to be permuted for all the possible permutation values.
Numb = Number of element is the array
i = Number of element is the array
In case of permutation with fixed number of places we are calling the combination function which generate the combination values.
For each combination values we call permutation to get the all possible permutation values.""" 
def permute (B,j,i):
    #y=x-1
    global Numb
    global Const
    
    Const = int(Const)
    n=int(Numb)
    j=int(j)
    #print (A)
    #i=int(Const)
    if j == i :
        visit(B,i)
    else :
        for k in range(j,i):
            temp = B[j]
            B[j]=B[k]
            B[k]=temp;
            permute(B,j+1,i)
            temp = B[j]
            B[j]=B[k]
            B[k]=temp;  
Numb = input("enter the digits to be permuted : ")
A =[]
B =[]
size = 0
count = 0
j=0
Const = input("enter the numbers of places for which permutation to be performed")
verb = int(input ("Function to be performed value between 0 - 3 :"))
for i in range(0,int(Numb)):# Loop runs to fill the array with 0 at each place
    A.append(0)
for i in range(0,int(Const)):# Loop runs to fill the array with 0 at each place
    B.append(0)    
if (verb == 0 or verb == 2):
    start_time = time.time()
    Combine(A,Numb,Const)
    elapsed_time = time.time()
    if(verb==0):
        print("Count : ",size,"Time Taken : ",(elapsed_time - start_time)*1000, "Miliseconds")
 
elif (verb ==1 or verb == 3):
    start_time = time.time()
    Combine(A,Numb,Const)
    elapsed_time = time.time()
    if(verb==1):
        print("Count : ",count,"Time Taken : ",(elapsed_time - start_time)*1000, "Miliseconds")
else :
    print("Wrong verbose value!!!!!")
    



 
            
        
    
    

            
    
