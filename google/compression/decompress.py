import sys

def find_closing_bracket(str):
	"""
	input: "[[string]]"
	output: 9 (i.e. the closing bracket of the bracket at pos. 0 is at index 9)
	"""
	if str[0] != "[":
		return None
	depth = 0
	for i in range(1, len(str)):
		if str[i] == "[":
			depth += 1
		if str[i] == "]":
			depth -= 1
		if depth < 0:
			return i

def get_num(str, start):
	"""
	input: "100[ala]", 0  (i.e. get number starting off at index 0)
	output: 100, 3 (i.e. number is 100 and token starts off at index 3)
	"""
	numstr = ""
	for i in range(start, len(str)):
		if str[i].isdigit():
			numstr += str[i]
		else:
			break
	return int(numstr), i

def inflate(str):
	inflated = ""
	i = 0
	while i < len(str):
		if str[i].isdigit():
			num, token_start = get_num(str, i)
			token_end = token_start + find_closing_bracket(str[token_start:])
			token = str[token_start : token_end]
			inflated += inflate(token) * num
			i = token_end
		elif str[i] == '[' or str[i] == ']':
			i += 1
		else:
			inflated += str[i]
			i += 1
	return inflated


def main():
	assert(inflate("2[ab]3[c]2[2[2[d]]]") == "ababcccdddddddd" )
	assert(inflate("2[a2[c]b]") == "accbaccb" )
	assert(inflate("10[a]2[b]") == "aaaaaaaaaabb" )

if __name__ == "__main__":
	main()

