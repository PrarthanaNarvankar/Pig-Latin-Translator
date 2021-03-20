#get the sentence from user

orignal=input("Enter the sentence: ").strip().lower()

# split the sentence into words

words=orignal.split()

new_words=[]

#loop through words and convert into pig latin

#If the word starts with vowel  add "yay"
for word in words:
    if  word[0] in "aeiou":
        new_word=word + "yay"
        new_words.append(new_word)
    else:
        vowel_pos=0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos=vowel_pos + 1
            else:
                break
        cons=word[:vowel_pos]
        the_rest=word[vowel_pos:]
        new_word=the_rest + cons + "ay"
        new_words.append(new_word)

#now join the word

output=" ".join(new_words)

#print the output

print(output)
