public class Oven{
    private int maxTemp;
    
    private int currentTemp;
    
    public Oven(int maxTemperature,int startTemperature){
        
        if(maxTemperature> 0 && maxTemperature <= 500){
            maxTemp = maxTemperature;
        }
        else{
            maxTemp = 500;
        }
        
        if(startTemperature>0 && startTemperature<=maxTemperature){
            currentTemp = startTemperature;
        }
        else{
            currentTemp = 0;
        }
    }
    
    public int getMaxTemp(){
        
        return maxTemp;
        
    }
    
    public int getCurrentTemp(){
        
        return currentTemp;
        
        
    }
    
    public void turnOff(){
        
        if(currentTemp>0){
            currentTemp = 0;
        }
            
        
        
    }
    
    public boolean isOn(){
        
        if(currentTemp == 0 || currentTemp<0){
            return false;
        }
        else{
            return true;
        }
    }
    
    public void preheat(int temp){
        if(temp<=maxTemp){
            currentTemp = temp;
        }
        else{
            System.out.println("The current temperature is maximum compared to maximum temperature of oven.");
        }
    }
}
