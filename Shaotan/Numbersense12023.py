print('1. 2020 - 20 =', 2020-20)
print('2. %d + %d = %d' % (494, 118, 494+118))
print('3. The tens digit of 1296 is', int(1296/10)-int(1296/100)*10)
print('4. %d / %d = %d' % (60, 5, 60/5))
print('5. 14 * 50 = ', 14 * 50)
print('6. The remainder of 66 / 4 is', 66 - int(66/4)*4)
print('7. The product of 14 * 3 is', 14 * 3)
print('8. %d * %d + %d = %d' % (8, 11, 8, 8*11+8))
print('9. 53 + 12 + 28 + 7 = ', 53 + 12 + 28 + 7)
print('*10. 201 + 402 + 804 + 603 =', 201 + 402 + 804 + 603)
print('11. 1987 rounded to the nearest ten is', int(1987/10+0.5)*10)
print('12. 17 ^ 2 =', 17*17)
print('13. %d - %d - %d = %d' % (578, 361, 27, 578-361-27))
print('14. 11 * 48 =', 11 * 48)
print('15. %d - %d = %d' % (681, 292, 681-292))
print('16. 45 * 18 =', 45 * 18)
class py_solution:
    def roman_to_int(self, s):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(s)):
            if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
            else:
                int_val += rom_val[s[i]]
        return int_val

print('17. DCLXXVI in Arabic Numerals is',(py_solution().roman_to_int('DCLXXVI')))
print('18. 37 + 41 + 45 =', 37 + 41 + 45)
print('19. %d * %d = %d' % (32, 28, 32*28))
print('*20. 398 * 202 =', 398 * 202)
print('21. 36 * 25 =', 36*25)
print('22. %d * %d / %d = %d' % (44, 3, 33, 44*3/33))
from math import gcd
print('23. The GCD of 28 and 21 is', gcd(28, 21))
print('24. %d / %d = %d' % (342, 18, 342/18))
print('25. If 1 yard is equal to 3 feet, then 63 feet is equal to', int(63/3), 'yards.')
print('26. 24 ^ 2 =', 24 * 24)
print('27. The smaller of 5/8 and 3/5 is', end=' ')
ans = min(5/8, 3/5)
from fractions import Fraction
print(Fraction(ans))
print('28. 5/8 + 1/24 =', Fraction(5/8 + 1/24), '(fraction).')
print('29. Seventeen weeks is', 17 * 7, 'days.')
print('*30. %d * %d * %d = %d' % (29,41,61,29*41*61))
print('31. 9 + 13 + 17 + 19 + 25 =', 9+13+17+19+25)
print('32. 65 ^ 2 =', 65 * 65)
print('33. 1.444 * 10 ^ 3 =', int(1.444*(10*10*10)))
def lcm(x, y):
   if x > y:
       z = x
   else:
       z = y

   while(True):
       if((z % x == 0) and (z % y == 0)):
           lcm = z
           break
       z += 1

   return lcm

print('34. The LCM of 28 and 21 is', end=' ')
print(lcm(28, 21))
print('35. 54 * 101 =', 54*101)
l = []
for n in range(11, 52):
    if n%5==0:
        l.append(n)
print('36. The number of multiples of 5 between 11 and 51 is', l)
print('36. The number of multiples of 5 between 11 and 51 is', int((51-11)/5))
print('37. %d * %d = %d' % (67,63,67*63))
# Python program to display all the prime numbers within an interval

lower = 40
upper = 50
count = 0
for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
               break
        else:
            count = count + 1
print('38. The number of prime numbers that are between 40 and 50 is', count)
print('39. %d * %d = %d' % (99,42,99*42))
print('*40. The cubic root of 511111 is', int(511111**(1/3)+0.5))
print('41. 32^2 - 21^2 =', 32*32 - 21*21)
print('42. The square root of 784 is', int(784**(1/2)))
