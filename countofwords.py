#Write a Python program to find the list of words that are longer than n from a given list of words.
def find_longer_words(words,n):
    longer_words=[]
    for i in words:
        if len(i)>n:
            longer_words.append(i)
    return longer_words

#to find the same for string
def find_longer_words_in_String(input_string,n):
    word_list=input_string.split()
    for word in word_list:
        if(len(word)>n):
            return word_list

words=['apple','banana','grapes','on']
long=find_longer_words(words,3)
print(long)

input_string= "The Quick brown fox jumping on a tree"
long_string=find_longer_words_in_String(input_string,2)
print(long_string)

