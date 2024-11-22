def somaLista(valores=[]):

    """
    A função somaLista, recebeuma lista de números e 
    faz a soma de todos os números da lista, e retorna
    o resultado da soma.

    Parametrs
    ---------------------------------------

    valores: int[]
        Lista de números para a soma

    Returns
    ---------------------------------------
        Retorna a soma de uma lista

    """

    resultado = 0
    for i in valores:
        resultado+=i

    return resultado


def maiorValor(lista=[]):
  
    """

    A função maiorValor encontra o maior valor
    em uma lista numérica.

    Parameters
    ------------------------------------------
        lista: int[]

    Returns
    ------------------------------------------
        Retorna o maior valor da lista
    """

    m = lista[0]

    for i in lista:
        if i > m:
            m = i

    return m 

def inverter(palavra=""):
    # Vamos utilizar um comando 
    # len(length-comprimento) para o obter
    # a quantidade de caracteres da palavra

    qtd = len(palavra)
    invertida = ""
    
    for i in range(qtd-1, -1,-1):
        invertida+=palavra[i]
    return invertida 

def palindromo(palavra=""):
    org = inverter(palavra).lower()
    if palavra.lower()==org:
        return "E um palindromo"
    else:
        return "Não é um palindromo"
    
