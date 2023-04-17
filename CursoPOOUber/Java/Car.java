class Car {
    Integer id;
    String license;
    Account drive;
    Integer passenger;

    public Car(String license, Account driver){
        this.license = license;
        this.drive = driver;
    }

    void printDataCar() {
        System.out.println("License: " + license + " Name Driver: " + drive.name);
    }
}
