
# personalityNumber function implementation
def personalityNumber(name,numerologies):
    
    # taking an empty list to store the numbers of each letter
    num_lst = []
    
    # applying for loop to know the numbers of each letter. You can look brief into it.The code is easier
    # to understand.
    for k in name:
        for i in range(1,10):
            if k in numerologies[i]:
                num_lst.append(i)
                break
    
    # the total variables stores the sum of the list of num_list.
    # NOTE: sum() is an inbuilt method used to find the sum of all numbers present in the list.
    total = sum(num_lst)
    
    # if the total is belong to below condition, then it get gets returned to called function.
    if((total>=1 and total<=9) or total==11 or total == 22):
        return total
    
    else:
        
        # This case is used to minimize the higher number to lower, by summing up each individual digit 
        # of a number.
        nsum = total
        while(True):

            var = list(map(int,list(str(total))))
            nsum = sum(var)
            
            if nsum==11 or nsum==22 or (nsum>=1 and nsum<=9):
                return nsum
            
    
    
                
# main function implementation
def main():
    # personalityAssociations kept in a dictionary.
    personalityAssociations ={
    1:"initiating action,pioneering,leading,independent,attaining,individual",
    2:"cooperation,adaptability,consideration of others,partnering,mediating",
    3:"expression,verbalization,socialization,the arts,the joy of living",
    4:"a foundation,order,service,struggle against limits,steady growth",
    5:"expansiveness,visionary,adventure,the constructive use of freedom",
    6:"responsibility,protection,nurturing,community,balance,sympathy",
    7:"analysis,understanding,knowledge,awareness,studious,mediating",
    8:"practical endeavors,status oriented,power seeking,material goals",
    9:"humanitarian,giving nature,selflessness,obligations,creative expression",
    11:"higher spiritual plane,intuitive,illumination,idealist,a dreamer",
    22:"the Master Builder,large endeavors,powerful force,leadership"
    }
    
    #numerologies kept in a dictionary named - numerologies
    numerologies = {
        1 : ['A','J','S'],
        2 : ['B','K','T'],
        3 : ['C','L','U'],
        4 : ['D','M','V'],
        5 : ['E','N','W'],
        6 : ['F','O','X'],
        7 : ['G','P','Y'],
        8 : ['H','Q','Z'],
        9 : ['I','R']
    }
    
    # taking name as an input parameter from user.
    #NOTE: stripping whitespaces at the start and end of name as well as converting into upper case.
    name = list(input("Enter your name: ").strip().upper())
    
    # personalityNumber function gets called and it returns personalityNumber to a variable perNum.
    perNum = personalityNumber(name,numerologies)
    
    # display statements.
    print("\nYour personality number is:",perNum)
    
    print("\nYour personality associations are:\n"+personalityAssociations[perNum])
    



# Program execution starts from here
if __name__ == "__main__":
    # calling main function
    main()
