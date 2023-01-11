a = int(input("Primeiro número: "))
b = int(input("Segundo número: "))
c = int(input("Terceiro número: "))

if a < b and a < c:
    print(f"{a} é o número menor")
if b < a and b < c:
    print(f"{b} é o número menor")
if c < a and c < b:
    print(f"{c} é o número menor")
if a > b and a > c:
    print(f"{a} é o número maior")
if b > a and b > c:
    print(f"{b} é o número maior")
if c > a and c > b:
    print(f"{c} é o número maior")
