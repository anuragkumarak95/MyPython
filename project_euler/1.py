'''Question:

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

'''

N=1000
threes = list(range(3,N,3))
fives = list(range(5,N,5))
out = set(threes)
out = out.union(fives)
print("answer is : "+str(sum(out)))
