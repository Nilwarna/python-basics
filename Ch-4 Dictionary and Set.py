# # WAP to create a dictionary
# info = {
#     "name": "nilwarna",
#     "cgpt": 9.2,
#     "marks": [92,99,95],
# }
# print(info["marks"])




# # WAP to update dictionary value
# info = {
#     "name": "nilwarna",
#     "cgpt": 9.2,
#     "marks": [92,99,95],
# }

# info["name"]="nik"
# print(info)




# # WAP to add new key in dictionary
# info = {
#     "name": "nilwarna",
#     "cgpt": 9.2,
#     "marks": [92,99,95],
# }

# info["age"]="22"
# print(info)

# # WAP to create nested dictionary
# info = {
#     "name":{
#           "nilwarna":"btech",
#              "nik":"mbbs",
#              "nikhil":"btech",
#              },
#     "cgpt": 9.2,
#     "marks": [92,99,95],
# }
# print(info)




# # WAP to store word meanings in dictionary
# words={
#     "table": ["a piece of furniture", "list of facts and figures"],
#     "cat": "a small animal"
# }
# print(words)




# # WAP to count unique subjects using set
# subject={"python","java","c++","python","js","java","python","java","c++","C"}
# print(len(subject))




# # WAP to store marks in dictionary using update
# marks={}

# x=int(input("enter phy marks:"))
# marks.update({"phy":x})

# y=int(input("enter chem marks:"))
# marks.update({"chem":y})

# z=int(input("enter Bio marks:"))
# marks.update({"math":z})

# print(type(marks),marks)




# # WAP to store 9 and 9.0 separately in set
store=set()
store={
    ("float",9.0),
    ("int",9)
}
print(store)