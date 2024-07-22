#1) Calculando a média de dois números
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
media = (num1 + num2) / 2
print("Média dos números", media)

# 2) Covertendo a temperatura de Celsius para Farenheit
celsius = float(input("Digite a temperatura em celsius: "))
farenheit = ((9 * celsius + 32) / 5) + 32
print("A temperatura em Farenheit", farenheit)

# 3) Calculando média de três números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
media = (num1 + num2 + num3) / 3
print("A média dos núemros é: ", media)

# 4) Convertendo dólares em euros
dolar = float(input("Digite o valor em dolar: "))
euro = float(input("Qual é a cotação do dia do euro?: "))
conversão = dolar * euro
print("O resultado da conversão é: ", conversão)

# 5) Determinando se um número é positivo ou negativo
num1 = float(input("Digite um número: "))
if num1>0:
    print("É positivo")
elif num1<0:
    print("É negativo")

# 6) Determinando aprovação ou não do aluno
bim1 = float(input("Digite a média do 1º bimestre: "))
bim2 = float(input("Digite a média do 2º bimestre: "))
bim3 = float(input("Digite a média do 3º bimestre: "))
bim4 = float(input("Digite a média do 4º bimestre: "))
media = (bim1 + bim2 + bim3 + bim4) / 4
if media >= 7:
    aprov = ("APROVADO")
    print(aprov)
elif media < 7:
    reprov = ("REPROVADO")
    print(reprov)

# 7) Determinando se um ano é bissexto ou não
ano = int(input("Digite um ano: "))
if ano % 4 == 0:
    print("É bisexto")
else:
    print("Não é bisexto")

# 8) Qual dos três números é maior?
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
if num1 > num2 and num1 > num3:
    print("O primero número é maior")
elif num2 > num1 and num2 > num3:
    print("O segundo número é maior")
else:
    print("O terceiro número é maior")

# 9) Pode votar ou não?
idade = int(input("Digite a idade: "))
if idade >= 16:
    print("Você pode votar")
else:
    print("Você não pode votar. Aguarde ter 16 anos")

# 10) Calculando média considerando pesos
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))
media = ((nota1 * 3) + (nota2 * 2) + (nota3 * 1) + (nota4 * 2)) / (3 + 2 + 1 + 2)
print("A média é", media)

# 11) Determinando se é criança, adolescente, adulto ou idoso
idade = int(input("Digite a idade: "))
if idade <=12:
    print("Você é criança")
elif idade <=18:
    print("Você é adolescente")
elif idade <= 60:
    print("Você é adulto")
else:
    print("Você é idoso")

# 12) Determine se é par ou impar 
for cat  in range(1,31):
    if cat % 2 == 0:
         print("É par",cat)
    else:
        print("É ímpar", cat)