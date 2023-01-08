pragma solidity ^0.8.0;

interface Itelephone {
    function changeOwner(address _owner) external; 
    function owner() external view returns (address); 

}