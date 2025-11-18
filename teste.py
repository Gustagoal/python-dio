peso = 8
valor = 600
percentual_de_desconto = 0
cliente = input("Digite o tipo do cliente :  ")   #("Novo cliente", "Cliente fidelizado", "Cliente premium")
if cliente == "Novo cliente":
    pass
if cliente == "Cliente fidelizado":
    percentual_de_desconto = 0.05
elif cliente == "Cliente premium":
    percentual_de_desconto = 0.10

valor_total = peso*valor
valor_final =  valor_total - (valor_total*percentual_de_desconto) 

print(percentual_de_desconto)
print(valor_total)
print(f"{valor_final:.2f}")
