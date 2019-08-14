# THINGS WE'RE GOING TO USE

print() # <- This is the print function. We'll get into functions later, you just need to know that it prints whatever you put into it, into the console.
"CTRL + B" # <- You hit these two together to execute whatever you write in this file (a python script / .py file)

print("""                 __,__\n        .--.  .-"     "-.  .--.\n       / .. \/  .-. .-.  \/ .. \\\n      | |  '|  /   Y   \  |'  | |\n      | \   \  \ 0 | 0 /  /   / |\n       \ '- ,\.-"`` ``"-./, -' /\n        `'-' /_   ^ ^   _\ '-'`\n        .--'|  \._ _ _./  |'--.\n      /`    \   \.-.  /   /    `\\\n     /       '._/  |-' _.'       \\\n    /          ;  /--~'   |       \\\n   /        .'\|.-\--.     \       \\\n  /   .'-. /.-.;\  |\|'~'-.|\       \\\n  \       `-./`|_\_/ `     `\'.      \\\n   '.      ;     ___)        '.`;    /\n     '-.,_ ;     ___)          \/   /\n      \   ``'------'\       \   `  /\n       '.    \       '.      |   ;/_\n     ___>     '.       \_ _ _/   ,  '--.\n   .'   '.   .-~~~~~-. /     |--'`~~-.  \\\n  // / .---'/  .-~~-._/ / / /---..__.'  /\n ((_(_/    /  /      (_(_(_(---.__    .'\n           | |     _              `~~`\n           | |     \'.\n            \ '....' |\n             '.,___.'\n""")


# VARIABLES

""" What is a variable?
	Officially: Variables are used to store information to be referenced and manipulated in a computer program.
	Think of it as a tag / label / container that stores some data. That data may change as you manipulate it,
	but you can always get hold of the container again by calling its tag (the variable name) """


# Without a variable



# print("I have 3 bananas.")
# print("If I eat 1 banana, I now have 2 left.")


# With a variable
bananas = 3

"I have {} bananas".format(bananas)

# s1 = "I have {} bananas".format(bananas)

number_of_bananas_eaten = 1
bananas_remaining = bananas - number_of_bananas_eaten

"If I eat {} banana, I now have {} left".format(number_of_bananas_eaten, bananas_remaining)

# s2 = "If I eat {} banana, I now have {} left".format(number_of_bananas_eaten, bananas_remaining)

bananas_per_banana_tree = 10
banana_trees = 'a'


# STRINGS

string = "Hello, I am a string."


# LISTS

# DICTIONARIES

# FUNCTIONS

def my_function(input_a, input_b):
	output = input_a + input_b
	return output

# FOR LOOPS




# EXERCISE

top_100_names = ["OLIVIA", "RUBY", "EMILY", "GRACE", "JESSICA", "CHLOE", "SOPHIE", "LILY", "AMELIA", "EVIE", "MIA", "ELLA",
				"CHARLOTTE", "LUCY", "MEGAN", "ELLIE", "ISABELLE", "ISABELLA", "HANNAH", "KATIE", "AVA", "HOLLY", "SUMMER",
				"MILLIE", "DAISY", "PHOEBE", "FREYA", "ABIGAIL", "POPPY", "ERIN", "EMMA", "MOLLY", "IMOGEN", "AMY", "JASMINE",
				"ISLA", "SCARLETT", "LEAH", "SOPHIA", "ELIZABETH", "EVA", "BROOKE", "MATILDA", "CAITLIN", "KEIRA", "ALICE", "LOLA",
				"LILLY", "AMBER", "ISABEL", "LAUREN", "GEORGIA", "GRACIE", "ELEANOR", "BETHANY", "MADISON", "AMELIE", "ISOBEL",
				"PAIGE", "LACEY", "SIENNA", "LIBBY", "MAISIE", "ANNA", "REBECCA", "ROSIE", "TIA", "LAYLA", "MAYA", "NIAMH", "ZARA",
				"SARAH", "LEXI", "MADDISON", "ALISHA", "SOFIA", "SKYE", "NICOLE", "LEXIE", "FAITH", "MARTHA", "HARRIET", "ZOE",
				"EVE", "JULIA", "AIMEE", "HOLLIE", "LYDIA", "EVELYN", "ALEXANDRA", "MARIA", "FRANCESCA", "TILLY", "FLORENCE",
				"ALICIA", "ABBIE", "EMILIA", "COURTNEY", "MARYAM", "ESME"]

d = {}
for name in top_100_names:
	first = name[0]

	if not d.get(first):
		d[first] = []

	d[first].append(name)

l = []
for i in d:
	l.append((i, len(d[i])))

l.sort(key=lambda x: x[1], reverse=True)
print(l)