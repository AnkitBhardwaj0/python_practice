#Reverse every word in a sentence.
sentence="Reverse every word in a sentence"
reverse_word=[]
for words in sentence.split():
    reverse_word.append(words[::-1])
sentence=" ".join(reverse_word)
print(sentence)

        
