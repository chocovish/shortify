def gen(last):
	digits = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_"
	last = list(last)
	if last[-1] != digits[-1]:
		index = digits.index(last[-1]) +1
		last[-1] = digits[index]
	else:
		if len(last) ==last.count(digits[-1]):
			last.insert(0, digits[0])
			for i in range(len(last)): last[i] = digits[0]
		else:
			for i in range(len(last)-1,-1,-1):
				if last[i] == digits[-1]:
					last[i] = digits[0]
					if last[i-1]!=digits[-1]:
						last[i-1] = digits[digits.index(last[i-1])+1]
						break
	result = ""
	for i in last: result+=i
	return result

