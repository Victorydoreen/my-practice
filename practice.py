# # to avoid error we import sys, then u call the function only once
# # # # # #import sys
# # # # # #sys.setrecursionlimit(5)
# # # # # #def greet():
# # # # # #    print('Hello World')
    
# # # # # #greet()

# # # # # #base case; the least value u can have in your no. for this case its a 1, n=1
# # # # # # finding the factorial, we first call the function, define its base, return how we get a factorial of a number, result of 5 !,10!,2!,6!,7!
# # # # # def factorial(n):
# # # # #     if n==0:
# # # # #         return 1
# # # # #     return n*factorial(n-1)
# # # # # result=factorial(7)
# # # # # print(result)
# # # from tkinter.messagebox import QUESTION


# # #QUESTION1
# # # # i=1
# # # # while i<=10:
# # # #   print(i)
# # # #   i+=1
# # # #  
# # # # question2
# # # # #Write a program to accept a number from a user and calculate the sum of all
# # # # numbers from 1 to a given number
# # # # For example, if the user entered 10 the output should be 55
# # # # (1+2+3+4+5+6+7+8+9+10)
# # # num=int(input('Enter number'))
# # # sum=0
# # # for num in range(1,num+1,1): #1,starting point, num+1, ending point, 1is the steps or interval in range, if we were usimg even numbers, it would bw 2 instead of1
# # #     sum=sum+num
# # #     # a comma is used to concatenate strings and integers
# # #     print('sum of the first 10 numbers is',sum)
    
# #     #FUNCTIONS
# #    #1; Write a program to create a function that takes two arguments,
# #    # name and age,and print their value
# # from audioop import add


# # # def myfunction(name,age):
# # #   print('rose' +' is ',age)
  
# # # myfunction('rose',22)  

# # # #2 . Write a program to create a function func1() to accept a variable length of
# # # #arguments and print their value. IF WE DONT KNOW THE LENGTH OF
# # # # ARGUMENTS WE USE,asterics(*)
# # # def func1 (*args):
# # #     for i in args:
# # #         print(i)
        
# # # func1(20,40,60)
# # # func1(80,100)

# # # 3 Write a program to create function calculation() such that it can accept two
# # # 

# # # def calculation(a,b):
# # #     print(a+b,a-b)
 
# # # calculation(40,10)

# # # def calc(a,b):
# # #     print(a*b,a/b)
    
# # # calc(10,80)    

# # def calculation(a,b):
# #     addition=a+b
# #     subtraction=a-b
# #     return addition,subtraction
# # res=calculation(40,10)
# # print(res)

# # def calc(m,n):
# #     multiply=m*n
# #     divide=m/n
# #     return multiply,divide
# # result=calc(100,20)
# # print(result)

# # 4 def show_employee(name,salary=9000):
# #     print('Ben',salary)
# #     print('rose',salary)
    
# # show_employee('name',12000)  
# # show_employee('rose',) 
    
# 5 Create an outer function that will accept two parameters, a and b. Create an inner
# # function inside an outer function that will calculate the addition of a and b. At
# last, an outer function will add 5 into addition and return it



# def func1(a,b):
#     def func2(a,b):
#         return a+b
#     #call inner function (func2) from outer function (func1)
#     add=func2(a,b)
#    # add 5 to the result:
#     return add+5

# result=func1(5,10)
# print(result)
    
# # Write a program to create a recursive function to calculate the sum of numbers
# # from 0 to 10. A recursive function is a function that calls itself, again and again  
# if u dont provide  a rcursive function with the base case, it will keep on running, n-1 means the no.s below  10 ie 9,8,7,6,5,4,3,2,1,0



# def addition(num):
#     if num:
#         #call same function by reducing number by 1
#         return num+addition(num-1)
#     else:
#         return 0
    
# result=addition(5)
# print(result)

# def subtraction(num):
#     if num:
#         #call same function by reducing number by 1
#         return num-subtraction(num-1)
#     else:
#         return 0
    
# result=subtraction(10)
# print(result)

    
# 1;Assign a different name to function and call it through the new name
def display_student(name,age):
    print(name, age)
    
display_student('Emma',26) 

def show_student(name,age):
    print(name, age)
    
show_student('Emma',26)

# 2; Generate a Python list of all the even numbers between 4 to 30
list1=[4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]

list2=list1[::2]
print(list2)

# 3; Find the largest item from a given list below
x=[4,6,8,24,12,2]
x1=x[3]
print(x1)
