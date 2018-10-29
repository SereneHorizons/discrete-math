# Finds GCD of 2 numbers
# Numbers have to be relatively prime to have an inverse
from __future__ import print_function

input1 = 1001
input2 = 1331

n1 = max(input1, input2)
n2 = min(input1, input2)

result = 1
while (result != 0):
    result = n1 % n2
    multiple = n1 / n2
    print("%d = (%d)*%d + %d" % (n1, multiple, n2, result))
    n1 = n2
    n2 = result

print()
print("gcd(%d, %d) = %d" % (input1, input2, n1))
