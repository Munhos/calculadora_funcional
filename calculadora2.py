conta = 0
lst = []
for c in range(0,999):

    if c == 0: 
        numeros = float(input("Digite o numero: "))
        lst.append(numeros)

        operação = input("""Digite a operação 
        [+] SOMAR
        [-] SUBTRAIR
        [*] MULTIPLICAR
        [/] DIVIDIR
        [**] EXPOENTE: """)
        lst.append(operação)

        numeros = float(input("Digite o numero: "))
        lst.append(numeros)

    if c >= 1:
        operação = input("""Digite a operação 
        [+] SOMAR
        [-] SUBTRAIR
        [*] MULTIPLICAR
        [/] DIVIDIR
        [**] EXPOENTE: """)
        lst.append(operação)

        numeros = float(input("Digite o numero: "))
        lst.append(numeros)

    
        
    print(lst)
    
    if input("Deseja continuar? \033[0;32m[S] \033[0;31m[N]\033[m") == "n":
        break
    

for a1 in range(lst.count("**")):
    for c in lst:
        if c == "**":
            if c == "**":
                index = lst.index("**")
                mult = lst[index-1] ** lst[index+1]
                lst.insert(index+2, mult)

                del lst[index-1:index+2]


for a1 in range(lst.count("*") + lst.count("/")):
    for c in lst:
        if c == "*" or c == "/":
            if c == "*":
                index = lst.index("*")
                mult = lst[index-1] * lst[index+1]
                lst.insert(index+2, mult)

                del lst[index-1:index+2]

            if c == "/":
                index = lst.index("/")
                mult = lst[index-1] / lst[index+1]
                lst.insert(index+2, mult)

                del lst[index-1:index+2]

for a1 in range(lst.count("+") + lst.count("-")):
    for c in lst:
        if c == "+" or c == "-":
            if c == "+":
                index = lst.index("+")
                mult = lst[index-1] + lst[index+1]
                lst.insert(index+2, mult)

                del lst[index-1:index+2]

            if c == "-":
                index = lst.index("-")
                mult = lst[index-1] - lst[index+1]
                lst.insert(index+2, mult)

                del lst[index-1:index+2]

    


print(f"O resultado da conta é \033[0;33m{mult}\033[m")