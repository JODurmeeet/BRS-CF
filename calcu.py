# arr= [1,4, 3, 3]
# arr=sorted(arr)
# n=len(arr)
# a=0
# b=0
# cnt=0
# for i in range(1,len(arr)):
#     cnt+=1
#     if arr[i]==cnt:
#         print(cnt,arr[i])
#         if arr[i]== arr[i-1]:
#             a=arr[i]
#             cnt+=1
#             pass
        
#     else:
#         b=cnt
# print(a,b)   
   
# arr= sorted(arr)
# n=len(arr)
# a=b=cnt=0
# while n>cnt:
#     if arr[cnt]==arr[cnt+1]:
#         a=arr[cnt]
#         cnt+=1
#         pass
#     if arr[cnt]==
# n=5
# if n > 1:
#     def fact(n) :
#         if n==0:
#             return n+1
#         return (n*(fact(n-1)))
#     print(fact(n))
# elif n==1:
#     print(1)
# else:
#     print("Error")\
# arr=[1,2,3,4,5,6,7]
# n=len(arr)
# if n % 2==0:
#     n=n//2
#     for i in range(n):
#         arr[i]=arr[i]+arr[n+n-1-i]
#         arr[n+n-1-i]=arr[i]-arr[n+n-1-i]
#         arr[i]=arr[i]-arr[n+n-1-i]
#     print(arr)
#     print("1st")
# else:
#     n=(n)//2
#     for i in range(n):
#         arr[i]=arr[i]+arr[n+(n+1)-1-i]
#         arr[n+(n+1)-1-i]=arr[i]-arr[n+(n+1)-1-i]
#         arr[i]=arr[i]-arr[n+(n+1)-1-i]
#     print(arr)
# arr=[1,2,3,4,5,6,7]
# n=len(arr)
# p1 = 0
# p2 = n - 1
# while p1 < p2:
#     arr[p1], arr[p2] = arr[p2], arr[p1]
#     p1 += 1
#     p2 -= 1
# print(arr)
# def ra(i1,i2,arr):
#     if i1==i2:
#         return arr
#     arr[i1],arr[i2]=arr[i2],arr[i1]
#     return ra(i1+1,i2-1,arr)

# print(ra(0,n-1,arr))
# import re
# s1="A man, a plan, a canal: Panama"
# s1=s1.lower()
# s1=re.sub(r'[^A-Za-z0-9 ]+', '', s1)
# n=len(s1)
# ps=""
# for i in range(n):
#     ps= ps+ s1[n-i-1]
#     # s1=s1[:n-i]
# print(ps)
# if s1==ps:
#     print("true")
# else:
#     print("false")
# def isPalindrome(s):
#     def isp(l,r):
#         if l>=r:
#             return True
        
#         if s[l].isalnum()!=True: 
#             return isp(l+1,r)
            
#         if s[r].isalnum()!=True: 
#             return isp(l,r-1)

#         if s[l].lower()!=s[r].lower(): 
#             return False
            
#         return isp(l+1,r-1)
#     return isp(0,len(s)-1)
# print(isPalindrome(s1))
# x = ''.join([char for char in s1.lower() if char.isalnum()])
# if x == x[::-1]:
#     print(True)
# print(False)
# def fib(n: int) -> int:
#     if n==0:
#         return 0
#     if n==1:
#         return 1
#     sum = (n-1)+ fib(n-2)
#     return sum 
# print(fib(4))

# a=list(input())
# print(a)
# def isprime(n)->bool:
#     import math
#     if n==1:
#         return False
    
#     for i in range(2,int(math.sqrt(n))+1):
#         if n%i==0:
#             return False
#     return True
# print(isprime(8))


# def fact(n):
#     if n==1:
#         return 1
    
#     return (n*fact(n-1))

# print(fact(4))

# def floorSqrt(n): 
#     # code here
#     n=n**0.5
#     if type(n)==int:
#         return n
#     else:
#         return int(n)
# print(floorSqrt(n=37))  

# arr=[2,3,4]
# arr.append(5)
# print(arr)
# def fibonacciNumbers(n):
#         arr=[0]
#         if n==0:
#             return arr
        
#         if n==1:
#             return arr.append(1)
#         a=0
#         b=1
#         for i in range(2,n+1):
#             temp=a+b
#             a=b
#             b=temp
#             arr.append(a)
#         return arr
# print(fibonacciNumbers(5))


