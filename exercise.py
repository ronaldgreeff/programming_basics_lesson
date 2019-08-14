"""
We'll start with a list of the top 100 popular names. *Note that they are all capitalised.*
"""

top_100_names = ["OLIVIA", "RUBY", "EMILY", "GRACE", "JESSICA", "CHLOE", "SOPHIE", "LILY", "AMELIA", "EVIE", "MIA", "ELLA", "CHARLOTTE", "LUCY", "MEGAN", "ELLIE", "ISABELLE", "ISABELLA", "HANNAH", "KATIE", "AVA", "HOLLY", "SUMMER", "MILLIE", "DAISY", "PHOEBE", "FREYA", "ABIGAIL", "POPPY", "ERIN", "EMMA", "MOLLY", "IMOGEN", "AMY", "JASMINE", "ISLA", "SCARLETT", "LEAH", "SOPHIA", "ELIZABETH", "EVA", "BROOKE", "MATILDA", "CAITLIN", "KEIRA", "ALICE", "LOLA", "LILLY", "AMBER", "ISABEL", "LAUREN", "GEORGIA", "GRACIE", "ELEANOR", "BETHANY", "MADISON", "AMELIE", "ISOBEL", "PAIGE", "LACEY", "SIENNA", "LIBBY", "MAISIE", "ANNA", "REBECCA", "ROSIE", "TIA", "LAYLA", "MAYA", "NIAMH", "ZARA", "SARAH", "LEXI", "MADDISON", "ALISHA", "SOFIA", "SKYE", "NICOLE", "LEXIE", "FAITH", "MARTHA", "HARRIET", "ZOE", "EVE", "JULIA", "AIMEE", "HOLLIE", "LYDIA", "EVELYN", "ALEXANDRA", "MARIA", "FRANCESCA", "TILLY", "FLORENCE", "ALICIA", "ABBIE", "EMILIA", "COURTNEY", "MARYAM", "ESME"]


# ---STEP 1----------------------------------------------------------------------------------------
"""
Let's write our first function. As a reminder, a function is structured like this:

def function_name(input_paramaters):
	output = some_processing(input_parameters)
	return output

you can name the function and the input_parameters whatever you want.
"""

# def my_function(my_name, list_of_names):
# 	if my_name in list_of_names:
# 		print(my_name + ' is in the list!')
# 	else:
# 		print(my_name + ' is not in the list')


# ---STEP 2----------------------------------------------------------------------------------------
"""
Now let's create a variable to hold our name:
"""

# my_name = ''


# -------------------------------------------------------------------------------------------------
# lower_cased_names = [name.title() for name in top_100_names]


# ---STEP 3----------------------------------------------------------------------------------------
"""
Now let's see if our name is one of the popular ones.
Let's call our function and pass in the required parameters
"""

# my_function(my_name, lower_cased_names)