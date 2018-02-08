from test import testequal
def mirror(input):
    return input + input[::-1]


text = raw_input("Type the string you would like to reverse.")
print("Here is your string, with its mirror: " + mirror(text))

print("Tests:")
testEqual(mirror('good'),'gooddoog')
testEqual(mirror('Python'),'PythonnohtyP')
testEqual(mirror(''), '')
testEqual(mirror('a'),'aa')
