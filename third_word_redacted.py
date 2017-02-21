''' this program takes a sentence or paragraph as input and turns all the third
words into all x's. this is a useless function but I couldn't figure out how to 
do it at first, so I made a point of creating this program '''
 
############################################################################### 
#ask user for input
#turn that input into a list
#create a new list which we will turn into a redated sentence at the end
#for each word in the sentence:
#    if you find a third word, convert to a list and it's letters to x
#    then add that word to a new list
#    
#    if you find a non-third word, just add it to the list:
#turn that new sentence list into a sentence
#print that sentence
###############################################################################

import string



# ask user for a passage to convert
s=input("input a sentence: ")

#turn that sentence into a list
s=s.split()

# create a new list where we will add the words and redacted words to
# we do this so we can join the list later and print that out
new_sentence_list=[]


# initialize a variable so we know when were a third word of the sentence
third=0

#if we are on the third word, convert it to a list and turn each letter into x
#then when all the letters are converted, turn it back into a string of x's
# add that new xxx word to the new sentence list
# if its just a normal word, add it to the new sentence list
for word in s:
    third+=1
    if third%3==0:
        word=list(word)
        index=0
        for letter in word:
            if letter in string.punctuation:
                word[index]=letter
                index+=1
            else:
                word[index]='x'
                index+=1
        word=''.join(word)
        new_sentence_list.append(word)
    else:
        new_sentence_list.append(word)
 

#join the new sentence list into a string/sentence  
new_sentence_list=' '.join(new_sentence_list)

#print empty line to separate input and output
print()

#print out the sentence with all the 3rd words converted to all x's
print(new_sentence_list)

        
        
        
        
        
            
            
