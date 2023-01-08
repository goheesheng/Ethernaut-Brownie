// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface Icoinflip {
    function flip(bool _guess) external returns(bool);
    function consecutiveWins() external view returns(address);

}