# Kör területe: r^2*PI
# print(math.pi)
import math
d = int(input("Kérem a kör átmérőjet: ")) 
r = d/2
#T = r**2*math.pi
pi = math.pi
T = math.pow(r,2)*pi
x = round(T,2)
print(f"A kör területe: {x} ")
#Kör kerülete: 2*r*PI
K = 2*r*pi
y = round(K,2)
print(f"A kör kerülete: {y}")


