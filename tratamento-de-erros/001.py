

try:
    nome = float("Gustavo")
    print(nome)
except Exception as e:
    print("Deu erro no código")
    print(f"Erro de {e}")
finally:
    print("Fim do programa!")


