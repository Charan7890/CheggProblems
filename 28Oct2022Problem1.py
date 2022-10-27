
def main():
    WindowSpeed = int(input("Enter the peak windspeed(mph):"))
    
    tornadoCategory = ''
    if(WindowSpeed<=72):
        tornadoCategory='F0'
        
    elif(WindowSpeed>=73 and WindowSpeed<=112):
        tornadoCategory='F1'
        
    elif(WindowSpeed>=113 and WindowSpeed<=157):
        tornadoCategory='F2'
        
    elif(WindowSpeed>=158 and WindowSpeed<=206):
        tornadoCategory='F3'
        
    elif(WindowSpeed>=207 and WindowSpeed<=260):
        tornadoCategory='F4'
        
    elif(WindowSpeed>=261 and WindowSpeed<=318):
        tornadoCategory='F5'
        
    elif(WindowSpeed>=319):
        tornadoCategory='F6'
        
    print(f'Top windspeed ={WindowSpeed} MPH, The tornodo category is:{tornadoCategory}')

if __name__ == "__main__":
    main()
        
