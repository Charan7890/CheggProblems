import java.util.ArrayList;  // imported ArrayList class from util package.

// creating Rainfall class Template
class Rainfall{
    ArrayList<Double> rain = new ArrayList<>();  // to store constructor values in this list.
    int len; // to store the length of list.
    double total = 0.0; // to store the sum of rainfalls
    
    // Rainfall constructor adds value to the instance list named rain. Since, the names are same I used 
    // this keyword. I hope you may get that.
    Rainfall(ArrayList<Double> rain){    
        this.len = rain.size();
        for(int i=0;i<rain.size();i++){
            this.rain.add(rain.get(i));
        }
    }
    
    // getTotalRainFall method is used to calculate the total rainfall of all 12 months.
    public double getTotalRainFall(){
    for(int i=0;i<len;i++){
        total+=rain.get(i);
    }
    return total;
    }
    
    //getAverageRainFall method is used to calculate the average rainfall of all 12 months.
    public double getAverageRainFall(){
        return(total/len);
    }
    
    //getHighestMonth return the month which has highest rainfall.
    public int getHighestMonth(){
        int ind=-1;
        Double max = rain.get(0);
        for(int i=1;i<len;i++){
            if(max<rain.get(i)){
                max = rain.get(i);
                ind = i;
            }
        }
        return ind+1;
    }
    
    //getLowestMonth return the month which has least rainfall.
    public int getLowestMonth(){
        int ind=-1;
        Double min = rain.get(0);
        for(int i=1;i<len;i++){
            if(min>rain.get(i)){
                min = rain.get(i);
                ind = i;
            }
        }
        return ind+1;
    }
    
    //getRainAt method return the rainfall data at particular month.
    public double getRainAt(int e){
        return(rain.get(e-1));
    }
    
}

public class Main
{
	public static void main(String[] args) {
	    
	    // Using arraylist concept to slove this problem.
		ArrayList<Double> rain = new ArrayList<>();
		
		//Adding values to the list named rain.
		rain.add(3.0);
		rain.add(2.0);
		rain.add(3.0);
		rain.add(0.15);
		rain.add(0.2);
		rain.add(0.1);
		rain.add(0.02);
		rain.add(2.5);
		rain.add(1.6);
		rain.add(4.0);
		rain.add(5.0);
		rain.add(4.5);
		
		// passing list rain using constructors concept.
		Rainfall rainfall = new Rainfall(rain);
		
		// These are the printing statemets to know thw answer for each of the case.
		System.out.println("Total Rainfall:"+rainfall.getTotalRainFall());
		System.out.println("Average Rainfall:"+rainfall.getAverageRainFall());
		System.out.println("Highest Rainfall in month of:"+rainfall.getHighestMonth());
		System.out.println("Lowest Rainfall in month of:"+rainfall.getLowestMonth());
		System.out.println("Rainfall at month number:"+rainfall.getRainAt(4));
	
		
		
	}
}
