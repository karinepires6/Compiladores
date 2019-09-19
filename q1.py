import re

texto = "abbbbbba,aaaaa,bababa,bbbbbbbb, ababababa,b"
#padrao = "(abc)*a*"
#padrao = "(ab)*|a*"
#padrao = "(ba|bb)*|(ab|aa)*"
padrao = "(ab+a)+"
texto_separado = re.split("\W+", texto)


for palavra in texto_separado:
	resultado = re.fullmatch(padrao,palavra)
	
	if(resultado is None):
		print("{} palavra nao pertence".format(palavra))
	else:
		print("{} palavra pertence".format(palavra))
