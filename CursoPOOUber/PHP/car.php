<?php
class Car 
{
    public id;
    public license;
    public driver;
    public passanger;

    public function __construc($license , $driver) {
        $this->license = $license;
        $this->driver = $driver;
    }

    public function printDataCar() {
        echo "license: $this->license, conductor: {$this->driver->name}, document: {$this->driver->document}"
    }
}