matrix = [['7','T','h'],['i','s','$'],['#','i',' '],['s','%',' '],['M','a','t'],['r','3','i'],['x','#',' '],[' ','%','!']]
neo = []

alphabet ='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
characters = '0123456789@#$%!'

for item in matrix:
	for i in item:
		if i in alphabet:
			print(i)
			neo.append(i)
		elif i in characters:
			neo.append(" ")

neos_matrix = "".join(neo)

print(neos_matrix)
