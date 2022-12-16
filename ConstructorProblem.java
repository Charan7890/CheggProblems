import java.util.Scanner;

class Circle{
    // radius variable declared as a private data member.
    private int R;
    
    // pi is a constant variable.
    final double pi = 3.1416;
    
    // It is default Constructor.
    Circle(){
        this.R = 0;  // Radius is initialized with zero value, to avoid error if we call function memebers.
        System.out.println("Default constructor of Circle class is called");
    }
    
    // It is a parameterized constructor.
    Circle(int R){
        this.R = R;
    }
    
    // below method is used to calculate are of circle.
    public double areaOfCircle(){
        if(R!=0)
        return(pi*R*R);
        else
        return 0.0;
    }
    
    // below method is used to calculate the circumference of the circle. 
    public double circumferenceOfCircle(){
        if(R!=0)
        return(2*pi*R);
        else
        return 0.0;
    }
}

public class Main{
    
    public static void main(String args[]){
        
        // Creating Circle Object with no parameters to call default constructor.
        Circle circle = new Circle();
        System.out.println(circle.areaOfCircle());
        System.out.println(circle.circumferenceOfCircle());
        
        // Creating Circle Object with parameter to call parameterized constructor.
        Circle pCircle = new Circle(5); // pass any value as your wish to know the area/circumference of the circle.
        System.out.println(pCircle.areaOfCircle());
        System.out.println(pCircle.circumferenceOfCircle());
        
    }
}
