import re

text = input("Digite: ")

splitted_text = re.split("\s", text)

for word in splitted_text:
	if(re.fullmatch("[a-z]{3}|[a-z]{4}", word)):
		print("Tipo primitivo: {}".format(word))
	elif(re.fullmatch("[a-zA-Z]+\w*", word)):
		print("Identificador: {}".format(word))
	elif(re.fullmatch("=", word)):
		print("Atribuicao: {}".format(word))
	elif(re.fullmatch("[0-9]+", word)):
		print("Inteiro: {}".format(word))
	elif(re.fullmatch("[0-9]+.[0-9]+", word)):
		print("Real: {}".format(word))
