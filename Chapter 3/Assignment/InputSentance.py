#Q1  write a program that takes a sentance and prints the following:
# Total characters in a sentence, convert to uppercase and lowercase

sentence = input("Please enter a sentence: ")
total_Number_of_characters = len(sentence)
print("Total number of characters in the sentence:", total_Number_of_characters)
uppercase_sentence = sentence.upper()
print("Sentence in uppercase:", uppercase_sentence)
lowercase_sentence = sentence.lower()
print("Sentence in lowercase:", lowercase_sentence)