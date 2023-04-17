<?php
require_once('Car.php');
require_once('Account.php');

$car = new Car("HIF344", Account("Andres Herrera", "JFD342"));
$car->printDataCar;