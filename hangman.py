from random_word import RandomWords as get_word
import math

def welcome(name_input):
	print("Hello," , name_input)

def get_word():
	return get_word.get_random_word(hasDictionaryDef = True ,min_Length = 4)


def main():
	name = str(input("Hello, what's your name? I'm "))
	\
	welcome(name)
	loop_status = True
	while True:
		word = str(get_word())


main()