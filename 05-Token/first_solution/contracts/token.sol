// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;


contract Token {
// The contract uses solidity 0.6.0 which is subject to underflow/overflow.
  mapping(address => uint) balances;
  uint public totalSupply; // 256 bits in size
  // int public totalSupply; // 256 bits in size // There is no such thing as negative tokens supply

  constructor(uint _initialSupply) public {
    balances[msg.sender] = totalSupply = _initialSupply;
  }

  function transfer(address _to, uint _value) public returns (bool) {
    // 0 - 1 = 2**256- 1
    // maximum value of 2^256-1 = 115792089237316195423570985008687907853269984665640564039457584007913129639935 //78 decimal digits
    require(balances[msg.sender] - _value >= 0);
    balances[msg.sender] -= _value;
    balances[_to] += _value;
    return true;
  }

  function balanceOf(address _owner) public view returns (uint balance) {
    return balances[_owner];
  }
}