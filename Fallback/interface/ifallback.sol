// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IFallback{
    function owner() external view returns(address);
    function contribute() external;
    function withdraw() external;
}
