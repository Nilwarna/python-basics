# # Create a new file "practice.txt" using python. Add the following data in it:
# # Hi everyone
# # we are learning File 1/0
# # using Java.
# # I like programming in Java.
# # A Pull up for

# with open("practice.txt","w") as f:
#     f.write("Hi everyone \nwe are learning File 1/0 \nusing Java. \nI like programming in Java. \nA Pull up for")




# WAF that replace all occurrences of "java" with "python" in above
# def replace_name():
#     with open("practice.txt","r") as f:
#         data = f.read()
#         new_data = data.replace("Java","Python")
#         print(new_data)

#     with open("practice.txt","w") as f:
#         f.write(new_data)
# replace_name()



# Search if the word "learning" exists in the file or not.
# word = str(input("enter the word to search: "))
# with open("practice.txt","r") as f:
#     data= f.read()
#     if(data.find(word) != -1):
#         print("Found")
#     else:
#         print("not Found")



# WAF to find in which line of the file does the word "learning"occur first.
# Print -1 if word not found.
# word = str(input("enter the word to search: "))
# def find_line():
#     data=True
#     line_no = 1
#     with open("practice.txt","r") as f:
#         while data:
#             data = f.readline()
#             if(word in data ):
#                 print(line_no)
#                 return
#             line_no += 1
#     return -1

# print(find_line())




# From a file containing numbers separated by comma, print the count of even numbers.
count = 0 
with open("practice.txt","r") as f:
    data = f.read()
    print(data)

    nums = data.split(",")
    for val in nums :
        if (int(val) % 2 == 0 ):
            count += 1
print(count)