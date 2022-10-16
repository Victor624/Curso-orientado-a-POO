class Main {
    public static void main(String[] args) {
        
        Car car= new Car("AMD325 ",new Account("andres herrera","31253040"));
        car.passegenger= 3;
        car.printDataCar();
        
        Car car2 = new Car("2525 ", new Account("teresa ", "2521252"));
        car2.passegenger=3;
        car2.printDataCar();
    }
    
}