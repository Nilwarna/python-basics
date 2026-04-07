
# a= str(input("enter name of your 1st fav movie: "))
# b= str(input("enter name of your 2nd fav movie: "))
# c= str(input("enter name of your 3rd fav movie: "))

# movies = [a,b,c]
# print(type(movies))
# print("ur fav movies are:", movies)


# #WAP to ask the name of their 3 fav movies and store them in a list
# movies=[]
# movies.append(input("enter name of 1st fav movie: "))
# movies.append(input("enter name of 2nd fav movie: "))
# movies.append(input("enter name of 3rd fav movie: "))

# print(movies)




# #WAP to check if a list contains a palindrome of element (Hint:use copy() method )
data = input("enter your data: ")

data = input("enter ur data: ")
temp = list(data)

rev = temp.copy()
rev.reverse()

if temp == rev:
  print("palindrome")
else:
  print("not palindrome")