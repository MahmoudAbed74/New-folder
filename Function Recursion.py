def clean_word(word,x=0):
    if len(word) == 1:
        return word
    print(f"start the : {word}")    
    if word[0] == word [1]:
        print(f"before the : {word}")
        # Function Recursion
        return clean_word(word[1:]) #clean_world ==for loop in function
    print(x)    
    print(f"after the : {word}")
    return word[0]+clean_word(word[1:])
print(clean_word("wwwoorrld"))
