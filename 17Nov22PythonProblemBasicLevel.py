#import random module
from random import randint

# It generates a list of 10 random elements from 1 to 20.
def randList():
    L2 = []
    
    for i in range(10):
        L2.append(randint(1,20))
        
    return L2

# It finds the common name present between the two sets.    
def set_Methods(Set1,Set2):
    return Set1.intersection(Set2)

# It finds the average of given list.
def average(L1):
    total = sum(L1)
    avg = total/len(L1)
    return avg
    
# main definition.
def main():
    L1 = [2,4,6,8,10]
    
    avgResult = average(L1)
    
    print('Average of L1 is:'+str(avgResult))
    
    Set1 = {"Jim","Mary","Bill"}
    Set2 = {"George","Salley","Mary"}
    commonNames = set_Methods(Set1,Set2)
    
    print("Common names:",commonNames)
    
    L2 = randList()
    
    print("The elements in the L2 are:",L2)
    
    L2r = L2.copy()
    
    L2r = L2[::-1]
    
    print("The L2r contains:",L2r)
    
    print("The 4th element of the L2r is:",L2r[3]) 
    

# Program execution starts from here.
if __name__ == "__main__":
    main() #main is called
