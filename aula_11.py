# -*- coding: utf-8 -*-
"""Aula 11

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1juudwXaGOPXioXLksg8s2IdCKl3Z5U4_

Uma função lambda em Python é uma função anônima, ou seja, uma função que não possui um nome. Ela é uma forma concisa de definir funções simples e pode ser muito útil em situações em que você precisa de uma função temporária e não quer criar uma função completa usando a definição tradicional com a palavra-chave def.

A sintaxe básica de uma função lambda é a seguinte:
"""

quadrado = lambda x: x ** 2
print(quadrado(5))

soma = lambda lista: sum(lista)
numeros = [1, 5, 10, 50]
total = soma(numeros)
print(total)
numeros = [80, 74, 25]
total = soma(numeros)
print(total)

"""Neste exemplo, `lambda x:` define a função lambda com um único argumento `x` e a expressão `x ** 2` calcula o quadrado de `x`.

As funções lambda são frequentemente usadas com funções embutidas como `map()`, `filter()`, `reduce()`, entre outras, para realizar operações em coleções de dados.

exemplos com: **map()**
"""

numeros = [1, 2, 3, 4, 5]
quadrados = list(map(lambda x: x ** 2, numeros))
print(quadrados)  # # Saída: [1, 4, 9, 16, 25]

"""exemplo com: **filter()**"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Saída: [2, 4, 6, 8, 10]



"""exemplo com: **reduce()**"""

from functools import reduce

numeros = [1, 2, 3, 4, 5]
soma = reduce(lambda x, y: x + y, numeros)
print(soma)  # Saída: 15

"""Lembre-se de que as funções lambda são mais adequadas para funções simples e curtas. Para funções mais complexas, é preferível usar a definição tradicional de função (`def`) para tornar o código mais legível e manutenível.
`map()`, `filter()`, e `reduce()` são funções de ordem superior em Python que permitem operar em coleções de dados, como listas ou tuplas, de maneira eficiente e concisa. Aqui está uma explicação de cada uma delas:

1. **`map()`**:
    - A função `map()` (mapeamentp) é usada para aplicar uma função a cada elemento de uma sequência (por exemplo, uma lista) e retorna um objeto `map`, que pode ser convertido em uma lista ou outra sequência.
    - Sintaxe: `map(função, sequência)`
    
    Exemplo:
"""

numeros = [1, 2, 3, 4, 5, 6]
quadrados = list(map(lambda x: x ** 2, numeros))
print(quadrados)  # Saída: [1, 4, 9, 16, 25]

lista = [1, 2, 3, 4, 5, 6]
lista1 = list(map(lambda x: x ** 2, lista))
print("lista =", lista,"\n\nlista1 =", lista1)  # Saída: [1, 4, 9, 16, 25]

def calculaQuadrado(numero):
  return f'O quadrado de {numero} é: {numero**2}'
lista_numeros = [1, 2, 3, 4, 5, 6]
calculo = map(calculaQuadrado, lista_numeros)
for n in calculo:
  print(n)

"""2. **`filter()`**:
    - A função `filter()` é usada para filtrar elementos de uma sequência com base em uma função de teste (predicado) e retorna um objeto `filter`, que pode ser convertido em uma lista ou outra sequência.
    - Sintaxe: `filter(predicado, sequência)`
    
    Exemplo:
"""

lista = [1, 2, 3, 4, 5, 6]
lista1 = list(filter(lambda x: x % 2 != 0, lista))
print('lista =', lista,'\n\nlista1 =', lista1)    # retorna a lista de números ímpares

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Saída: [2, 4, 6, 8, 10]

"""3. **`reduce()`**:
    - A função `reduce()` é usada para aplicar uma função acumuladora a uma sequência de elementos, reduzindo-a a um único valor acumulado. Para usar `reduce()`, você precisa importá-lo do módulo `functools`.
    - Sintaxe: `reduce(função, sequência)`
    
    Exemplo:
"""

lista = [1, 2, 3, 4, 5, 6]
protudo = reduce(lambda x,y: x * y, lista)
print('lista =', lista,'\n\nproduto =', protudo)

from functools import reduce

numeros = [1, 2, 3, 4, 5]
soma = reduce(lambda x, y: x + y, numeros)
print(soma)  # Saída: 15

"""Essas funções são poderosas e podem simplificar o código ao evitar a necessidade de loops explícitos. Elas são especialmente úteis quando você deseja aplicar operações a todos ou a alguns elementos de uma coleção de dados.
No entanto, lembre-se de que funções lambda ou predicados devem ser usados com parcimônia e clareza para manter o código legível. Para operações complexas, é preferível usar funções nomeadas com `def` para melhor documentação e compreensão do código.

| Operator | Name | Example |
| --- | --- | --- |
| + | Adição | x + y |
| - | Subtração | x - y |
| * | Multiplicação | x * y |
| / | Divisão | x / y |
| % | Modulo | x % y |
| ** | Potenciação | x ** y |
| // | Floor division | x // y |

1 - Crie uma função lambda que retorne o dobro de um número.
"""

numero = [16]
dobro = list(map(lambda x: x * 2, numero))
print(dobro)

"""2 - Crie uma função lambda que calcule a soma de dois números."""

numeros = [4, 5]
soma = reduce(lambda x, y: x + y, numeros)
print(soma)

"""3 - Crie uma função lambda que verifique se um número é par."""

numeros = [1, 5, 8, 13]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)

"""4 - Crie uma função lambda que converta uma string em maiúsculas."""

maiusculas = lambda s: s.upper()
print(maiusculas('caroline'))

"""5 - Crie uma função lambda que calcule o produto de três números."""

lista = [4, 5, 6]
produto = reduce(lambda x,y,: x * y, lista)
print('lista =', lista,'\n\nproduto =', produto)

#ou

produto = lambda x, y, z: x * y * z
print(produto(5, 3, 10))

#ou

produto = lambda x, y, z:print(x * y * z)
produto(5, 3, 10)
