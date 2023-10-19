def s(a,b):
    ss = a+b
    return ss

def d(a,b):
    if a == 0:
        return "no es pussevel"
    else:
        ss = a/b
        return ss
def m(a,b):
    ss = a*b
    return ss

def su(a,b):
    ss = a-b
    return ss

while True:
    a = int(input("Digite um numero: "))
    o = input("digite um operador: ")
    b = int(input("Digite um numero: "))

    if o == "+":
        c = s(a,b)
        print(c)
    elif o == "-":
        c = su(a,b)
        print(c)
    elif o == "*":
        c = m(a,b)
        print(c)
    else:
        c = d(a,b)
        print(c)