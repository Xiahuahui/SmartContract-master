//BCMETH means Blockchain Match Ethereum 
pragma solidity ^0.4.24;

contract BCMETH {
    String currentStatus;
    constructor () public {
        currentStatus="[1]";
    }

    function Ture-w(String actionStr) public returns(bool){
        if(currentStatus=="[1]" && action=="Ture-w"){
            currentStatus="[2]";
            return true;
        }
        else
            return false;
    }

    function Timeout-w(String actionStr) public returns(bool){
        if(currentStatus=="[1]" && action=="Ture-w"){
            currentStatus="[2]";
            return true;
        }
        else
            return false;
    }

    function Ture-缴纳房租(String actionStr) public returns(bool){
        if(currentStatus=="[1]" && action=="Ture-w"){
            currentStatus="[2]";
            return true;
        }
        else
            return false;
    }

    function Timeout-缴纳房租(String actionStr) public returns(bool){
        if(currentStatus=="[1]" && action=="Ture-w"){
            currentStatus="[2]";
            return true;
        }
        else
            return false;
    }

}