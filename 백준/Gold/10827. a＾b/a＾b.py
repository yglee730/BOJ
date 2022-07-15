from decimal import Decimal, getcontext

a, b = input().split()

getcontext().prec = 1101
print("{0:f}".format(Decimal(a)**Decimal(b)))