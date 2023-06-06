import random

phrase = input("Enter the sentence you'd like to mix up: ")
phrase = phrase.split()
random_phrase = ""

for word in phrase:
  row = ""
  wordMixed = ""
  
  for letter in word:
      wordMixed += letter

  wordMixed = wordMixed[1:-1]
  jumbled = random.sample(wordMixed, len(wordMixed))
  
  for i in jumbled:
    row += i
  random_phrase += (word[0] + row + word[-1]) + " "

print(random_phrase)
