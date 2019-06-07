entrada = int(input("Numero: "))
divisores = []
for i in range(1, entrada):
    calc = entrada%i 
    if calc == 0:
        divisores.append(i)
if len(divisores)==1:
    divisores.append(entrada)
    print("Primo")
    print(divisores)
else:
    print("Nao primo")
    
