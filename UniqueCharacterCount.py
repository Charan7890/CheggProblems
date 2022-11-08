
# main method definition.
def main():
    # taking input from user and converting it into lowercase and list type.
    text = list(input('Enter text:').lower())
    
    # using set type to eliminate all duplicate elements in the list.
    unique_letters = set(text)
    
    # count is a dictionary stores keys and values of our code.
    count = {}
    
    # Inserting values in dictionary
    for item in unique_letters:
        if item>='a' and item<='z':
            count[item] = text.count(item)
    
    # Condition checking
    if count=={}:
        print('your text doesn\'t contain any letter.')
    else:
        print('The count of letters in text is:[',end='')
        counter = 0
        # Loop to print dictionary in a list format
        for k,v in sorted(count.items()):
            if counter<len(count)-1:
                print(k+':'+str(v),end=',')
                counter+=1
            else:
                print(k+':'+str(v),end='')
                
        print(']')
        

# Execution of code starts from here.
if __name__ == "__main__":
    main()    # main method called.
