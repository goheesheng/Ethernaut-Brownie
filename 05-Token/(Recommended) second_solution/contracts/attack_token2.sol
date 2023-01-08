// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

// import 'OpenZeppelin/openzeppelin-contracts@3.0.0/contracts/math/SafeMath.sol';
import 'interfaces/Itoken.sol';

contract AttackToken2 {
// The contract uses solidity 0.6.0 which is subject to overflow.
  address public owner;

  constructor() public {
    owner = msg.sender;
  }

}