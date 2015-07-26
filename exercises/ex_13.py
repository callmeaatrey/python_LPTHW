def break_words(stuff):
	words = stuff.split(' ')
	return words

def sort_words(words):
	return sorted(words)

def print_first_word(words):
	first_word = words.pop(0)
	print first_word

def print_last_word(words):
	last_word = words.pop(-1)
	print last_word

def sort_sentence(sentence):
	words = break_words(sentence)
	return sort_words(words)

def print_first_last(sentence):
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_last_sorted(sentence):
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)

