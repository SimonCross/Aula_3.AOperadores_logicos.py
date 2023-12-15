"""
    Operadores lógicos

    Certamente! Em Python, os operadores lógicos são usados para realizar
    operações de lógica booleana em valores booleanos
    (True ou False).Existem três operadores lógicos principais em
    Python: and, or e not. Aqui está uma breve explicação de cada um:

    1- Operador "and"
    # Retorna True se ambas as condições forem verdadeiras.

    2- Operador or
    # Retorna True se pelo menos uma das condições for verdadeira.

    3- Operador not:
    #Inverte o valor de verdadeiro para falso e vice-versa.

    4- Operadores IF ELIF ELSE
    # Esses operadores são frequentemente usados em estruturas condicionais (if, elif, else) para
    controlar o fluxo do programa com base em expressões lógicas.

Maior ou igual (>=):

resultado = 18 >= 18
print(resultado)  # Saída: True (porque 18 é igual a 18)
Menor ou igual (<=):


resultado = 18 <= 18
print(resultado)  # Saída: True (porque 18 é igual a 18)
Igual (==):

resultado = 18 == 18
print(resultado)  # Saída: True (porque 18 é igual a 18)
Diferente (!=):


resultado = 18 != 18
print(resultado)  # Saída: False (porque 18 não é diferente de 18)

Esses exemplos mostram o uso desses operadores de comparação de uma maneira mais
simples na linguagem Python. Eles retornam True se a comparação for verdadeira e False se for falsa.

"""
A = True
B = True

Resultado = A and B
print(f"O resultado mostrado agora referente a variavel AND e o  Resultado é: {Resultado} ")

# para fins de fixação a variavel And SEMPRE  Retorna True se ambas as condições forem verdadeiras.

print("\n")

C = True
D = False

resultado = C and D

print(f"O resultado  nesse caso é: {resultado}"f" devido a uma das variveis receberem o valor \n"
      f"FALSE a regra faz com que o retorno do operador logico seja False")

print("\n")

codigo = C or D


print(f"O resultado usando a varivel OR por regra "
      f"define que se uma das variveis \nestiver com o "
      f"valor TRUE o operador logico retornara: {codigo}")

print("\n")

reverso = not A

print(f"No caso do uso da variavél Not implica que o valor do operador logico \nsempre sera o reverso dele"
      f" por exemplo se A receber o valor True logo quando o\ncodigo for complidado ele sera: {reverso}")

# A = True

print("\n")

"""
Altura = float(input("Digite sua Altura: "))
tamanhoMinimo = True

if Altura >= 1.50 and tamanhoMinimo: # tem que por os : se não n funciona
      print(f"Acesso permitido")

else:
      print(f"Acesso negado")
"""

"""
codigo = int(input(f"Favor introduza o codigo: "))
senha = 1234

if codigo == senha:
      print("Acesso permitido")

else:
      print("Acesso negado")
      
"""

"""
numero = int(input("Favor introduzir o tamanho do calçado: "))
tamanho = 40

if numero <= 40:
      print("Lamentamos informar mas não temos o numero selecionado ")
else:
      print("Temos o numero selecionado favor ir na prateleira A gaveta B ")

"""

idade = int (input(f" Favor informar a idade: "))

if idade >= 18:
      print("acesso permitido")

else:
      print("Acesso negado")

