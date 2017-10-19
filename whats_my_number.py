'''Author Anurag Kumar(mailto:anuragkumarak95@gmail.com)
Whats My Number..?

Only one number available from 1 - 1000 that satisfies below rules, 
find it.

RULES:
  - The number has two or more digits.
  - The number is prime.
  - The number does NOT contain a 1 or 7 in it.
  - The sum of all of the digits is less than or equal to 10.
  - The first two digits add up to be odd.
  - The second to last digit is even and greater than 1.
  - The last digit is equal to how many digits are in the number.
'''

# 1, 3, 7, 6, 4, 5, 2 is the rule sequence i used.

def check_prime(num):
    for i in range(num):
        if i==0 or i==1: continue
        if num%i==0:return False
    return True

for i in range(10,1000): # 1
    digits = [int(j) for j in str(i)]
    l = len(digits)
    if 1 in digits or 7 in digits: continue # 3
    if digits[l-1] != l: continue # 7
    if digits[l-2]<=1 or digits[l-2]%2!=0: continue # 6
    if sum(digits)>10: continue # 4
    if sum(digits[:2])%2==0: continue # 5
    if check_prime(i): # 2
        print(i)


