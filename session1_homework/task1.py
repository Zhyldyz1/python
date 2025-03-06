# Task 1: Word Counter
#Ask the user to enter a sentence. Calculate the length of the sentence.

sent = input("Please write your sentence: ")

wordcount= len (sent.split())
print("The number of word(s) in your sentence: ", wordcount)
