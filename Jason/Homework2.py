print("01: 2020-20" , (2020-20))
print("02: 494+118" , ( 494+118))
print("03: the tens digit of 1296",9)
print("04: 60/5",(60/5)) 
print("05: 14*50",(14*50)) 
print("06: 66&4", (66%4))
print("07: theproduct of 14 and 3 is", 42)
print("08: 8*11+8", (8*11+8))
print("09: 53+12+7",(53+12+7)) 
x=201+402+804+603
print("10: answer is", (x//100)*100)
print("11: 1987 rounded to the nearest ten is",1990)
print("12: 17*17", (17*17))
print ("13: 578-361-2 7",(578-361-27))
print("14: 11*48",(11*48))
print("15: 681-292",(681-292))
print("45*18",(45*18))
print("37+41+45", (37+41+45))

print("19: 32*28", (32*28))
x=398*202
print("20: answer is ",(x//100)*100)
print("19: 38*25", (38*25))
print("21: 36*25" , (36*25))
print("22: 44*3/33" ,(44*3/33))
print("24: 342/18",(342/18))
print("25: 63 feet is equal to", 21)
print("26: 24*24",(24*24))
print("28: 5/8+1/24",(5/8+1/24))
print("29: 17*7",(17*7))
x=29*41*61
print("30: 29*41*61 =",(x/10)*10)
print("9+13+17+21+25 =",(9+13+17+21+25))
print("65*65 =",(65*65))
D=500
C=100
L=50
X=10
V=5
I=1
print("17: DCLXXVI in Roman Numeral  is",D+C+L+X+X+V+I)

def roman_to_int(s):
    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_val = 0
    for i in range(len(s)):
        if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
            int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
        else:
            int_val += rom_val[s[i]]
    return int_val

print("17: DCLXXVI in Roman Numeral  is",roman_to_int("DCLXXVI"))
