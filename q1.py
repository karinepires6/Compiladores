import re

text = "abbbbbba,aaaaa,bababa,bbbbbbbb, ababababa,b"
#pattern = "(abc)*a*"
#pattern = "(ab)*|a*"
#pattern = "(ba|bb)*|(ab|aa)*"
pattern = "(ab+a)+"
splitted_text = re.split("\W+", text)


for word in splitted_text:
	result = re.fullmatch(pattern,word)
	
	if(result is None):
		print("{} palavra nao pertence".format(word))
	else:
		print("{} palavra pertence".format(word))
