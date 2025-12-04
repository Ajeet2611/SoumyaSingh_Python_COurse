#Q2 write a python program that takes any words or sentance as input and prints the following:
#the first charecter
#the last charecter
#the total number of characters
input = input ("Enter any words or sentance: ")

total_number_of_characters=print("Total number of characters is: ", len(input))
first_character = print("The first character is: ", input[0])

last_character = print("The last character is: ", input[-1])