# def isPalindrome( x: int) -> bool:
#     n = x
#     rev = 0
#     if x < 0:
#          return False
#     else:
#         while x > 0:
#             y = x % 10
#             rev = rev*10 + y
#             x = x // 10
#     return n == rev
# x=434
# print(isPalindrome(x))


#GCD of two numbers
# n1,n2=2,3
# till = n1 if n1 > n2 else n2
# GCD = 0
# print(till)
# for i in range(1,till):
#     if (n1 % i==0 and n2 % i==0):
#         GCD = i
# print("GCD is:", GCD)

#Armstrong number 
# def isArmstrong(num)->bool:
#     n=num
#     m=num
#     isarm=0
#     count=0
#     while n != 0:
#         y = n % 10
#         count+= 1
#         n//=10
#     while m != 0:
#         y= m % 10
#         isarm = isarm + y**count
#         m//=10
#     return isarm==num
# print(isArmstrong(1))

#all divisors of a number
# n=10
# divisor_list=[]
# for i in range(1,n+1):
#     if n % i==0:
#         divisor_list.append(i)
# print(divisor_list)
a=56
b=2
GCD=0
print(max(a,b))
for i in range(2,max(a,b)+1):
    if (a % i==0 and b % i==0):
        GCD = i
print("GCD is:", GCD)
arr=[0,0]
arr[0,1]=5,6
print(arr)
   
1 2 3 4 5 6 
   
    


