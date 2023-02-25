# Entrada do número informado pelo usuário e que será checado na sequência de fibonacci.

n = int(input("Informe um número inteiro: "))

# Calcula a sequência de Fibonacci até n + 1 termo. Quando o valor alcançar ou ultrapassar o valor de n, o loop será interrompido.

fibonacci = [0, 1]
while fibonacci[-1] < n:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

# Verifica se n pertence à sequência e responde a pergunta juntamente com o print da sequência até n + 1 termo.

if n in fibonacci:
    print(f"{n} faz parte da sequência de Fibonacci. A lista completa da sequência é: {fibonacci} e assim sucessivamente.")
else:
    print(f"{n} não faz parte da sequência de Fibonacci. A lista completa da sequência é: {fibonacci} e assim sucessivamente.")