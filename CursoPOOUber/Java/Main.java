class Main {
    public static void main(String[] args) {
        Car car = new Car("AMQ123", new Account("Andres Herrera", "AND234"));
        car.passenger = 4;
        car.printDataCar();

        Car car2 = new Car("QWE567", new Account("Andra Herrera", "JFI897"));
        car2.passenger = 3;
        car2.printDataCar();
    }
}
