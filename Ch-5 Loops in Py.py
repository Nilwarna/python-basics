# # WAP to print hello 5 times
# count = 1
# while count <= 5 :
#   print ("hello")
#   count += 1



# # WAP to print numbers from 1 to 5
# i = 1
# while i <= 5:
#   print (i)
#   i += 1
# print("Loop ended")




# # WAP to print numbers from 1 to 100
# i = 1
# while i <= 100:
#   print(i)
#   i +=1
# print("loop end")



# # WAP to print multiplication table
# n=int(input("Enter ur number"))

# i=1
# while i<=10:
#   print(n*i)
#   i+=1




# # WAP to print elements of list
# nums=[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# idx = 0
# while idx<len(nums):
#   print(nums[idx])
#   idx += 1




# # WAP to search element in tuple
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = int(input("enter ur search number: "))
i = 0
while i < len(nums) :
  if nums[i] == x:
    print("found: ", i)
  else:
    print("finding...")
  i += 1