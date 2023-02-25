# ler a string do usuário
s = input("Digite algo a ser invertido: ")

# criar uma string vazia para armazenar o resultado
s_invertido = ""

# percorrer a string de trás para frente
for i in range(len(s)-1, -1, -1):
    # adicionar cada caractere na nova string
    s_invertido += s[i]

# imprimir o resultado
print(s_invertido)