//BCMETH means Blockchain Match Ethereum 
pragma solidity ^0.4.24;

contract BCMETH {
    String currentStatus;
    constructor () public {
        currentStatus="[1]";
    }

    function Ture-aas(String actionStr) public returns(bool){
        if(currentStatus=="[1]" && action=="Ture-aas"){
            currentStatus="[2]";
            return true;
        }
        else
            return false;
    }

    function Timeout-aas(String actionStr) public returns(bool){
        if(currentStatus=="[1]" && action=="Ture-aas"){
            currentStatus="[2]";
            return true;
        }
        else
            return false;
    }

    function Ture-assault(String actionStr) public returns(bool){
        if(currentStatus=="[1]" && action=="Ture-aas"){
            currentStatus="[2]";
            return true;
        }
        else
            return false;
    }

    function Timeout-assault(String actionStr) public returns(bool){
        if(currentStatus=="[1]" && action=="Ture-aas"){
            currentStatus="[2]";
            return true;
        }
        else
            return false;
    }

}