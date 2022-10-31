
def main():
    # Taking input from the user.
    sentence = input().upper().split(' ')
    
    # Calling a function named EnglishToPigLatin.
    latin = EnglishToPigLatin(sentence)
    
    # Converting list to string using join method.
    answer = ' '.join(latin)
    
    # printing the output after performing certain actions.
    print(answer)
    
            
    
# function converts english to latin
def EnglishToPigLatin(sentence):
    updated_list,ans = [],'' # updated list stores updated string in list format.
    for item in sentence:
        if len(item)==1:   # If the length of word is 1.
            x_list = list(item)
            x_list.append('S')
            x_list.append('T')
            ans = ''.join(x_list)
            updated_list.append(ans)
        else:  # If the length of word is more than 1.
            x_list = list(item)
            popped_element =x_list.pop()
            x_list.insert(0,popped_element)
            x_list.append('S')
            x_list.append('T')
            ans = ''.join(x_list)
            updated_list.append(ans)
    
    return updated_list




if __name__ == "__main__":  # running of program starts from here.
    main()
