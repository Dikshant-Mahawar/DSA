n=int(input('Enter the number: '))

# Pattern 1
# * * * 
# * * *
# * * *

# for i in range(n):
#     for j in range(n):
#         print('* ',end='')
#     print('\n')


# Pattern 2
# *
# * *
# * * *

# for i in range(n):
#     for j in range(i+1):
#         print('* ',end='')
#     print('\n')

# Pattern 3
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(str(j)+' ',end='')
#     print('\n')

# Pattern 4
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(str(i)+' ',end='')
#     print('\n')

# Pattern 5
# 1 2 3
# 1 2
# 1

# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(str(j)+' ',end='')
#     print('\n')

# Pattern 6

#   *
#  ***
# *****

# for i in range(1, n + 1):
#     # Print leading spaces
#     for j in range(n - i):
#         print(' ', end='')
#     # Print stars
#     for k in range(2 * i - 1):
#         print('*', end='')
#     # Move to the next line
#     print()

# Pattern 7

#   *
#  ***
# *****
# *****
#  ***
#   *

# for i in range(n):
#     for j in range(n-i):
#         print(' ',end='')
#     for k in range(2*i-1):
#         print('*',end='')
#     print()

# for a in range(n,0,-1):
#     for b in range(n-a):
#         print(' ',end='')
#     for c in range(2*a-1):
#         print('*',end='')
#     print()

# Pattern 8
# *
# **
# ***
# **
# *

# for i in range(n):
#     for j in range(i+1):
#         print('*',end='')
#     print()

# for a in range(n,0,-1):
#     for b in range(a-1):
#         print('*',end='')
#     print()

# Pattern 9

# Aryan and his friends are very fond of the pattern. For a given integer ‘N’, they want to make the N-Binary Number Triangle.
# You are required to print the pattern as shown in the examples below.
# Example:
# Input: ‘N’ = 3

# Output: 

# 1
# 0 1
# 1 0 1

# for i in range(1,n+1):
#     for j in range(i):
#         if(j%2==0):
#             print(0,end='')
#         else:
#             print(1,end='')
#     print()


# Pattern 10

# 1         1
# 1 2     2 1
# 1 2 3 3 2 1
# space=2*n-2
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(str(j),end='')

#     for sp in range(space):
#         print(' ',end='')
#     space-=2

#     for k in range(i,0,-1):
#         print(str(k),end='')
#     print()

# Pattern 11
# 1
# 2 3
# 4 5 6
# c=1
# for i in range(1,n+1):
#     for j in range(i):
#         print(str(c)+' ',end='')
#         c+=1
#     print()

# Pattern 12

# Sample Input  :
# 7
# Sample Output  :
# A
# A B
# A B C 
# A B C D
# A B C D E
# A B C D E F
# A B C D E F G

# ch = 'A'
# print(ord(ch))  # Output: 65

# for i in range(1,n+1):
#     ch='A'
#     for j in range(i):
#         print(ch,end='')
#         ch=chr(ord(ch)+1) #Increment character
#     print()

# Pattern 13

# Sample Input  :
# 7
# Sample Output  :
# A B C D E F G 
# A B C D E F 
# A B C D E 
# A B C D 
# A B C 
# A B 
# A 

# for i in range(n,0,-1):
#     ch='A'
#     for j in range(i):
#         print(ch,end='')
#         ch=chr(ord(ch)+1) #Increment character
#     print()
        
# Pattern 14

# A
# B B
# C C C
# ch='A'
# for i in range(1,n+1):
#     for j in range(i):
#         print(ch,end='')
#     ch=chr(ord(ch)+1)
#     print()

# Pattern 15
#     A
#   A B A
# A B C B A





