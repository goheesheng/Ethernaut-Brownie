pragma solidity ^0.8.0;

import "OpenZeppelin/openzeppelin-contracts@4.8.0/contracts/token/ERC20/IERC20.sol";
import "OpenZeppelin/openzeppelin-contracts@4.8.0/contracts/token/ERC20/ERC20.sol";
import 'OpenZeppelin/openzeppelin-contracts@4.8.0/contracts/access/Ownable.sol';
import 'contracts/dex2.sol';


contract AttackDexTwo is ERC20{

    /*
    The "uint256(decimals())" part is used to convert the number of decimals for the token into a uint256 type. 
    Decimals are used to represent fractions of a token, for example, if the token has 18 decimals, 
    1 token can be divided into 10^18 smaller units. 
    This multiplication is used to set the initial supply of tokens with the correct decimal places. 
    */
    constructor() ERC20('PwnToken', 'PWN') public{
        _mint(msg.sender, 400 * (10 * uint256(decimals()))); 
    }

}