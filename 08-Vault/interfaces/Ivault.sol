// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IVault {
    function locked() external returns(bool);
    function unlock(bytes32 _password) external; 
}