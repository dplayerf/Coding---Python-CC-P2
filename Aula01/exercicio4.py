palavra = input("Digite uma palavra palíndromo: ")

def eh_palindromo(texto):
    texto_limpo = texto.replace(" ", "").lower()
    return texto_limpo == texto_limpo[::-1]
print(eh_palindromo(palavra))