def verificar_palindromo(frase):
    frase_limpa = "".join(char.lower() for char in frase if char.isalnum())
    
    if frase_limpa == frase_limpa[::-1]:
        print("Sim")
    else:
        print("Não")

print("Verificando a frase 'Anotaram a data da maratona.'")
verificar_palindromo("Anotaram a data da maratona.")

print("\nVerificando a palavra 'ovo'")
verificar_palindromo("ovo")

print("\nVerificando a frase 'A sacada da casa'")
verificar_palindromo("A sacada da casa")

print("\nVerificando a palavra 'carro'")
verificar_palindromo("carro")

print("\nVerificando a frase 'Socorram-me, subi no ônibus em Marrocos!'")
verificar_palindromo("Socorram-me, subi no ônibus em Marrocos!")