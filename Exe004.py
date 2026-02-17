valor = input("Digite alguma coisa: ")

print("O tipo de dado digitado é: ", type(valor))
print("O tipo de dado digitado é numérico? ", valor.isnumeric())
print("O tipo de dado digitado é alfabético? ", valor.isalpha())
print("O tipo de dado digitado é alfanumérico? ", valor.isalnum())
print("O tipo de dado digitado é decimal? ", valor.isdecimal())
print("O tipo de dado digitado é um espaço? ", valor.isspace())