salario = float (input("Digite o salário do colaborador: R$ "))

if salario <= 280:
    aumento = 0.20
elif salario <= 700:
    aumento = 0.15
elif salario <= 1500:
    aumento = 0.10
else:
    aumento = 0.05

novo_salario = salario* ( 1 + aumento)

print(f"Salário antes: R$ {salario:.2f}")
print(f"Porcentual de aumento: {aumento*100:.0f}%")
print(f"Valor do aumento: R$ {salario * aumento:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")