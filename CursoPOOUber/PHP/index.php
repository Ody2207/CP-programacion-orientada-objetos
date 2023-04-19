<?php
require_once('car.php');
require_once('UberX.php');
require_once('account.php');

$uberX = new UberX('CVE234', new Account('Andres Herrera', 'DAD234'), 'Chevrolet', 'Sparl');
$uberX->printDataCar();

$uberPool = new UberPool('JFK342', new Account('Andrea Fernanda', 'KJD342'), 'Dodge', 'Attitude');
$uberPool->printDataCar();
?>