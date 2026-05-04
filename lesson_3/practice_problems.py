def has_an_exclamation(string):
    if string.endswith("!"):
        return True
    else:        
        return False

str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False

print(has_an_exclamation(str1))
print(has_an_exclamation(str2))

famous_words = "seven years ago..."
new_string = f"Four score and {famous_words}"
new_string = "Four score and " + famous_words

munsters_description = "the Munsters are CREEPY and Spooky."
# => 'The munsters are creepy and spooky.'
print(munsters_description[0].capitalize() + munsters_description[1:].lower())


munsters_description = "The Munsters are creepy and spooky."
"tHE mUNSTERS ARE CREEPY AND SPOOKY."
print(munsters_description.swapcase())


str1 = "Few things in life are as important as house training your pet dinosaur."
str2 = "Fred and Wilma have a pet dinosaur named Dino."
'Dino' in str1
'Dino' in str2

flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
flintstones.append("Dino")
print(flintstones)

flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
flintstones.extend(["Dino", "Hoppy"])
print(flintstones)

advice = "Few things in life are as important as house training your pet dinosaur."
advice.split("house")[0]

advice = "Few things in life are as important as house training your pet dinosaur."
advice.replace("important", "urgent")

numbers = [1, 2, 3, 4, 5]
reversed_numbers = list(reversed(numbers))
print(reversed_numbers)


numbers = [1, 2, 3, 4, 5, 15, 16, 17, 95, 96, 99]

number1 = 8  # False (not in numbers)
number2 = 95 # True (in numbers)

number1 in numbers
number2 in numbers

42 in range(10, 101)          # True
100 in range(10, 101)         # True
101 in range(10, 101)         # False

numbers = [1, 2, 3, 4, 5]
del numbers[2]
print(numbers)

numbers = [1, 2, 3, 4]
table = {'field1': 1, 'field2': 2, 'field3': 3, 'field4': 4}
type(numbers)  # <class 'list'>
type(table)    # <class 'dict'>

statement1 = "The Flintstones Rock!"
statement2 = "Easy come, easy go."

statement1.count('t')  # 2
statement2.count('t')  # 0

def is_color_valid(color):
    if color == "blue" or color == "green":
        return True
    else:
        return False
    
def is_color_valid(color):
    return color == "blue" or color == "green"