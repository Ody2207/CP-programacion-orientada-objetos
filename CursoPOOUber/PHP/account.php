<?php
class Account
{
    public $id;
    public $name;
    public $document;
    public $email;
    public $password;

    public function __construc($name, $document) {
        $this->name = $name;
        $this->document = $document;
    }
}