CONSTANTE_BONUS = 1000

nome = input("Digite seu nome: ")

salario = float(input("Digite o valor do seu salário: "))

bonus = float(input("Digite o valor do seu bônus: "))

valor_bonus = float(CONSTANTE_BONUS + salario * (bonus/100))

print(f"Olá, {nome} você possui um bônus de R${valor_bonus}")
