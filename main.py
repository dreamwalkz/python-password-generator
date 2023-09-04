#Password Generator Project
import random
import string
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


# using random.choices()
# generating random strings
letterss = ''.join(random.choices(string.ascii_letters, k=nr_letters))
 
# print letter result
print("The generated random string : " + str(letterss))

# random numbers
def randN(N):
	min = pow(10, N-1)
	max = pow(10, N) - 1
	return random.randint(min, max)

#print(randN(nr_numbers))
numberss = randN(nr_numbers)
print("The generated random numbers : " + str(numberss))

# random symbols
symbolss = ''.join(random.choices(symbols, k=nr_symbols))

print("The generated random symbols : " + str(symbolss))

s = str(letterss) + str(numberss) + str(symbolss)
l = list(s)
#print(l)
random.shuffle(l)
result = ''.join(l)
print(f"Your password is {result}")

#combined = ''.join(letterss, numberss, symbolss)
#print(combined)

#Randomizer after choices are made.
# s = "Geeks for"
# l = list(s)
# print(l)

# l = list(s)
# random.shuffle(l)
# result = ''.join(l)
# print(result)

