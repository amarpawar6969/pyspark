# # ====================================================================================================================
# a = 'amar ravindra pawar'
# l = a.split(' ')
# s = ''
# for i in l:
#     for j in range(len(i)-1, -1, -1):
#         s += i[j]
#     s += ' '
# print(s)

# # ====================================================================================================================
# p = 98743334434
# s = str(p)
# l = len(s)
# a = 1
# b = 0
# c = 0
# x = len(s)
# while x > 0:
#     for j in range(0,a):
#         b = b + int(s[j])
#     for k in range(a+1,l):
#         c = c + int(s[k])
#     if c == b:
#         print(f'LHS {b} RHS {c} middle {s[a]}')
#         break
#     else:
#         a+=1
#         x -= 1
#         b = 0
#         c = 0

# ======================================================================================================================
# -- revers the number
# x = 12345
# y = str(x)
# z = ''
# for i in range(len(y)-1,-1,-1):
#     z+=y[i]
# print(int(z))

# ======================================================================================================================
# # -- prime number
# x = int(input('enter number to check: '))
# y = True
# z = []
# for i in range(2,x//2+1):
#     if x%i==0:
#         y = False
#         z.append(i)
# if y:
#     print(f'{x} is prime number')
# else:
#     print(f'{x} is non-prime and is divisible by {z}')

# ======================================================================================================================
# # -- find largest number
# z = [5, 9, 62, 1, 3, 59]
# from functools import reduce
# y = reduce(lambda x,y: x if x>y else y, z)
# print(y)

# ======================================================================================================================
# -- binary or not
# x = str(input('enter number: '))
# y = True
# for i in x:
#     if int(i) != 0 and int(i) != 1:
#         print(f'{x} is not binary')
#         y = False
#         break
# if y:
#     print(f'{x} is binary')

# ======================================================================================================================
# -- swap variables
# a = input('a: ')
# b = input('b: ')
# a,b = b,a
# print('a:', a)
# print('b:', b)

# ======================================================================================================================
# -- add 2 numbers without '+' operator
# a = 10
# b = 21
# x = [a,b]
# print(sum(x))

# ======================================================================================================================
# -- is given number is perfect number
# x = int(input('enter number: '))
# y = []
# for i in range(1,x//2 + 1):
#     if x%i==0:
#         y.append(i)
# if sum(y) == x:
#     print(f"sum {sum(y)} equal to x {x} is perfect number")
# else:
#     print(f"sum {sum(y)} not equal to x {x} is not-perfect number")

# ======================================================================================================================
# -- factorial using recursion
# def func(x):
#     if x == 0:
#         return 1
#     else:
#         return x * func(x-1)
# print(func(5))

# ======================================================================================================================
# -- decimal to binary
# x = 128
# s = ''
# while x > 1:
#     amod = x%2
#     s+= str(amod)
#     adiv = x//2
#     x = adiv
#     if adiv < 2:
#         s += str(adiv)
# print(s[::-1])

# ======================================================================================================================
# -- binary to dacimal
# x = 101
# y = 0
# z = 0
# x = str(x)[::-1]
# for i in x:
#     if int(i) == 1:
#         y+=2**z
#     z+=1
# print(y)

# ======================================================================================================================
# -- Write a Python program to find a list of integers with exactly two occurrences of nineteen and at least three
# -- occurrences of five. Return True otherwise False.
# x = [19, 19, 15, 5, 3, 5, 5, 2]
# y = True
# if x.count(5) != 3 or x.count(19) != 2:
#     y = False
#     print(y)
# if y:
#     print(y)


# ======================================================================================================================
# -- Write a Python program that accepts a list of integers and calculates the length and the fifth element. Return
# -- true if the length of the list is 8 and the fifth element occurs thrice in the said list.
# x = [19, 19, 15, 5, 5, 2, 5, 1]
# y = False
# if len(x) == 8 and x.count(x[4]) == 3:
#     y = True
#     print(y)
# if not y:
#     print(y)

# ======================================================================================================================
# -- factorial
# x = int(input('enter number: '))
# y = 1
# for i in range(1,x+1):
#     y *= i
# print(y)

# ======================================================================================================================
# -- pyramid pattern
# x = int(input('enter number: '))
# for i in range(1,x+1):
#     print((x-i) * ' ', i*' *')

# ======================================================================================================================
# -- Seperate out cube od odd number using list comphrehension
# l = [1,2,3,4,5,6,7,8,9]
# l1 = [i**3 for i in l if i%2==1]
# print(l1)

# ======================================================================================================================
# -- even and odd number
# a = []
# b = []
# for i in range(1,21):
#     if i%2 == 0:
#         a.append(i)
#     else:
#         b.append(i)
# print('Even number', a)
# print('odd number', b)

# ======================================================================================================================
# x = int(input('enter number: '))
# b = 5 if x<10 else 'invalid'
# print(b)

# ======================================================================================================================
l = [6,7,8,9]
l1 = []
for i in range(len(l)-1,-1,-1):
    l1.append(l[i])
print(l1)

print(l[::-1])




