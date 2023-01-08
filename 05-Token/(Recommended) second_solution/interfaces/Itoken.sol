// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;
interface IToken {

  function balanceOf(address _owner) external view returns (uint balance);
  function totalSupply() external view returns(uint);
  function transfer(address _to, uint _value) external returns (bool);

}