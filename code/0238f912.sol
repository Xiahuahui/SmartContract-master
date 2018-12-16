//BCMETH means Blockchain Match Ethereum 
pragma solidity ^0.4.24;

contract BCMETH {
    String currentStatus;
    constructor () public {
        currentStatus="[1]";
    }

    function event(String actionStr) public returns(bool){
        if(currentStatus=="[1]" && action=="event"){
            currentStatus="[2]";
            return true;
        }
        else
            return false;
    }

    function event(String actionStr) public returns(bool){
        if(currentStatus=="[1]" && action=="event"){
            currentStatus="[2]";
            return true;
        }
        else
            return false;
    }

    function event(String actionStr) public returns(bool){
        if(currentStatus=="[1]" && action=="event"){
            currentStatus="[2]";
            return true;
        }
        else
            return false;
    }

    function event(String actionStr) public returns(bool){
        if(currentStatus=="[1]" && action=="event"){
            currentStatus="[2]";
            return true;
        }
        else
            return false;
    }

}