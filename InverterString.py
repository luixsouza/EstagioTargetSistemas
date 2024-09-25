def inverter_string(s):
    invertida = ''
    for char in s:
        invertida = char + invertida  # Adiciona o caractere no início da nova string
    return invertida

# Entrada de string
entrada = input("Informe uma string: ")  # Exemplo de entrada
resultado = inverter_string(entrada)
print(f"String invertida: {resultado}")
