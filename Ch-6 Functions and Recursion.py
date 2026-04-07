#avg of three numbers
# def calc_avg(a,b,c):
#     sum = a + b + c
#     avg = sum/3
#     print(avg)
#     return avg
# calc_avg(3,4,5)



# WAF to print the length of a list.
# nums =[2,5,3,6,2,7,9,8,1,6,8,1,9,7,3]
# def print_len(list):
#     print(len(list))
# print_len(nums)




# WAF to print elements of list in single line
# nums =[2,5,3,6,2,7,9,8,1,6,8,1,9,7,3]
# def print_ele(list):
#     for item in list:
#         print(item,end=" ")
# print_ele(nums)




# WAF to find factorial
# def calc_fact(n):
#     fact = 1
#     for i in range (1 , n+1):
#         fact *= i
#     print(fact)
# calc_fact(5)



# WAF to convert USD to INR
# def converter(usd):
#     inr = usd * 93
#     print(usd,"USD =",inr,"INR")
# converter(6)




# WAF to check even or odd
# def num_check(n):
#     if (n % 2 == 0):
#         print("Even")
#     else:
#         print("Odd")
# num_check(1564431)




# Recursion example
# def show(n):
#     if(n == 0):
#         return
#     print(n)
#     show(n-1)
# show(5)




# WAF to find sum of n natural numbers (recursion)
# def calc_sum(n):
#     if(n == 0):
#         return 0
#     return calc_sum(n-1) + n
# print(calc_sum(5))




# WAF to print list using recursion
nums = [1,5,3,4,3,6,9,8,7,2,5,8,9,4,1,6,8,2,4]
def print_list(list , idx=0 ):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

print_list(nums)