import sys

def find_closing_bracket(str):
	depth = 0
	for i in range(0, len(str)):
		if str[i] == "[":
			depth += 1
		if str[i] == "]":
			depth -= 1
		if depth < 0:
			return i

def get_num(str, start):
	numstr = ""
	for i in range(start, len(str)):
		if str[i].isdigit():
			numstr += str[i]
		else:
			break
	return int(numstr), i+1

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

