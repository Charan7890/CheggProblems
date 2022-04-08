import java.util.Scanner;
abstract class Job{
	String name;
	double salary;
	String description;
	int length;
	abstract void getSalary(double salary);
	abstract void getLengthOfName(int length);
}

class Definition extends Job{
	void getSalary(double salary){
		super.salary=salary;
	}
	void getLengthOfName(int length){
		super.length=length;
	}
	void getName(String name){
		super.name =name;
	}
	void getDescription(String description){
		super.description=description;
	}
	void display(){
		System.out.println("Name:"+super.name+"  salary:"+super.salary+"  description:"+super.description);
	}
}
public class MainClass{
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		// Taking inputs of name,salary and description
		double salary;
		String name,description;

		System.out.println("enter your name:");
		name=sc.nextLine();

		
		System.out.println("enter description:");
		description = sc.nextLine();

		System.out.println("enter your salary:");
		salary = sc.nextDouble();


		// Creating object to the child class named Definition:
		Definition obj = new Definition();
		obj.getSalary(salary);
		obj.getName(name);
		obj.getDescription(description);

		// Finding length of name

		int length = name.length();

		obj.getLengthOfName(length);

		// displaying the scanned inputs

		obj.display();
	}
}