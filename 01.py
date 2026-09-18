aluno = input("Digite o nome do aluno: ")
ano_nascimento = int(input("Digite o ano de nascimento do aluno: "))
nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))

media = (nota1 + nota2) / 2


if media >= 7:
    situacao = "Aprovado"
elif media >=5:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

ano_atual = 2026
idade = (ano_atual - ano_nascimento)

print (f"Aluno: {aluno}")
print (f"Idade: {idade}")
print (f"A média das notas é: {media}")
print (f"Situação do aluno: {situacao}")