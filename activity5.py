#words_file = open('CROSSWD.txt' , 'r')

#print([x for x in dir(words_file) if '_' != x [0]]
# 
# = 0

#Function 1 

def more_than_20(file):
    open_file = open(file)
    list = []
     
    for i in open_file:
        x = (i.strip())
        if len(x) > 20:
            list.append(x)
    return list

#Function 2 

def has_no_e(word):

    return 'e' not in word 


#Function 3 

def uses_only(word,letters):

    for letter in word:
        if letter not in letters:
            return False
    return True


#Function 4 

def all_uses_only(file, letters):

    open_file = open(file)


    valid_words = []
    for line in open_file:
        word = line.strip()
        if uses_only(word, letters):
       
            valid_words.append(word)
 
    
    print(valid_words[:10])
    
    return valid_words

        

























































