// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import '@openzeppelin/contracts/utils/math/SafeMath.sol';

contract Telephone {

  address public owner;

  constructor() {
    owner = msg.sender;
  }

  function changeOwner(address _owner) public {
      // msg.sender is the smart contract address
    if (tx.origin != msg.sender) {
      owner = _owner;
    }
  }
}

// Basically the smart contract address of attack_telephone.sol calls the telephone.sol contract function == msg.sender
// and tx.origin is the EOA that calls attack_telephone.sol and which calls the telephone.sol function

// Details indepth:

// The changeOwner function allows the value of owner to be modified, but only if the tx.origin parameter is different from the msg.sender parameter.

// tx.origin is the address that originally created the transaction, while msg.sender is the address of the person or contract that is invoking the function. 
// tx.origin is always an external address, while msg.sender can be either an external address or the address of a smart contract.

// An attacker can exploit this vulnerability by calling the changeOwner function through an intermediate contract. 
// This allows the attacker to fulfill the condition tx.origin != msg.sender, allowing them to become the owner of the contract.

// In Ethereum, every transaction is associated with a msg.sender and a tx.origin. 
// The msg.sender is the address of the person or contract that is calling the current function, while the tx.origin is the address of the person or contract that originally created the transaction.

// Here are some examples to illustrate the difference between tx.origin and msg.sender:

// Alice creates a transaction and signs it with her private key.
// Alice sends the transaction to the Ethereum network.
// The transaction is broadcast to the network and eventually included in a block.
// The transaction is executed, and a smart contract function is called as a result.
// In this example, the tx.origin would be set to Alice's address, because she was the one who originally created the transaction. 
// The msg.sender would also be set to Alice's address, because she is the one calling the contract function.

// Now consider a slightly different example:

// Alice creates a transaction and signs it with her private key.
// Alice sends the transaction to a contract that she owns.
// The contract receives the transaction and executes a function that calls another contract function.
// The second contract function is executed.
// In this example, the tx.origin would still be set to Alice's address, because she was the one who originally created the transaction. 
// However, the msg.sender would be set to the address of the contract that Alice owns, because the contract is the one calling the second contract function.
