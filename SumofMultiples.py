"""https://www.codewars.com/kata/57241e0f440cd279b5000829/train/python
Your Job
Find the sum of all multiples of n below m

Keep in Mind
n and m are natural numbers (positive integers)
m is excluded from the multiples
Examples
sumMul(2, 9)   ==> 2 + 4 + 6 + 8 = 20
sumMul(3, 13)  ==> 3 + 6 + 9 + 12 = 30
sumMul(4, 123) ==> 4 + 8 + 12 + ... = 1860
sumMul(4, -7)  ==> "INVALID"

"""

def sum_mul(n, m):
    if n <=0 or m <=0: return "INVALID"
    else:
        multy = 0
        sum = 0
        while multy < m :
            multy +=n
            if multy>=m: break
            sum +=multy
        return sum

print(sum_mul(2,9))
print(sum_mul(3,13))
print(sum_mul(4,123))
print(sum_mul(4,-7))