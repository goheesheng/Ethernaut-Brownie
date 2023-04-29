// SPDX-License-Identifier: MIT
pragma solidity ^0.8;

import 'contracts/magicnum.sol';

contract Hack {
    constructor(MagicNum target) {
        bytes memory bytecode = hex"69602a60005260206000f3600052600a6016f3";
        address addr;
        assembly {
            // create(value, offset, size)
            // Pointer in memeory where code is store at slot 0
            // Dynamic Array (First 32 bytes = Array Length)

            //Size of code:
            // 69602a60005260206000f3600052600a6016f3 = 38 characters
            // Bytecode = 38 / 2 =19
            // Bytecode to Hex = 13
            addr := create(0, add(bytecode, 0x20), 0x13)
        }
        require(addr != address(0));

        target.setSolver(addr);
    }
}
