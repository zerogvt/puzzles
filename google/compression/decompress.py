
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

def inflate(str):
	inflated = ""
	i = 0
	while i < len(str):
		if str[i].isdigit():
			num = int(str[i])
			token_start = i + 2
			token_end = i + 2 + find_closing_bracket(str[token_start:])
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

if __name__ == "__main__":
	main()
