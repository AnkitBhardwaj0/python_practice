#Count vowels and consonants from a text file.
with open("python_fundamental_02/q2.txt",'r') as f:
    vowels_no=0
    consonants_no=0
    for letter in f.read():
        letter=letter.lower()
        if letter in "aeiou":
            vowels_no+=1
        elif letter.isalpha():
            consonants_no+=1
            
print(f"number of vowels in this file : {vowels_no} \nnumber of consonants in this file : {consonants_no}")