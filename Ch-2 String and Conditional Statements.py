# # WAP to input name and print its length
# name = input("Enter ur GoodName:")
# print("length of ur Name is:",len(name))




# # WAP to input first name of user and print its length
# # name = str(input("enter ur first name here:"))
# # print("length=",len(name))





# # WAP to count occurrence of "$" in a string
# str ="Hi $ I m $ the $ Sybbol $99.99"
# print(str.count("$"))





# # WAP to Find the occurence of "$" in a string
# # str = "hi ,$ I am the $ symbol $99.99"
# # print(str.count("$"))




# # WAP to check if a person can vote
# age = int(input("enter your age:"))
# if (age >= 18):
#   print("you can vote")
# elif (age < 18):
#   print("Nikal L***e")




# # WAP to assign grade based on marks
# marks=float(input("enter ur marks:"))
# if (marks >=90):
#   print("Congratulation you got A grade")
# elif (marks >=80):
#   print("Congratulation you got B grade")
# elif (marks >=70):
#   print("Congratulation you got C grade")
# else:
#   print("padhai karle fail hogaya")





# #Grade of students based ont heir marks
# # marks = float(input("enter ur marks: "))
# # if (marks >=90):
# #     grade=("A")
# # elif (marks >= 80 and marks < 90):
# #     grade=("B")
# # elif (marks >= 70 and marks < 80):
# #     grade=("C")
# # else:
# #     grade=("Fail")
# # print("Ur grade is:", grade)




# # WAP to check even or odd number
# a = int(input("enter ur number:"))
# if (a % 2 == 0):
#   number="even"
# else:
#   number="odd"
# print("the number is:",number)

# # WAP to check even or odd (method 2)
# num = int(input("enter the number:"))
# rem = num % 2

# if(num == 0):
#   print("Even")
# else:
#   print("Odd")





# # WAP to find greatest among 3 numbers
# a=int(input("enter ur 1st number:"))
# b=int(input("enter ur 2nd number:"))
# c=int(input("enter ur 3rd number:"))

# if(a>b and a>c):
#   print("grater number is:",a)
# elif(b>a and b>c):
#   print("grater number is:",b)
# elif(c>a and c>b):
#   print("grater number is:",c)





# # WAP to find greatest among 4 numbers
# a=int(input("enter ur 1st number:"))
# b=int(input("enter ur 2nd number:"))
# c=int(input("enter ur 3rd number:"))
# d=int(input("enter ur 4st number:"))





# if(a>b and a>c and a>d):
#   print("grater number is:",a)
# elif(b>a and b>c and b>d):
#   print("grater number is:",b)
# elif(c>a and c>b and c>d):
#   print("grater number is:",c)
# else:
#   print("grater number is:",d)





# # WAP to check number divisible by 7
num=int(input("enter ur number:"))

rem = num % 7
if(rem == 0):
  print("divisible by 7")
else:
  print("not divisible by 7")