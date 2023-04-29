# Import necessary modules from Brownie
from brownie import accounts, config, First_AttackDexTwo

# Define the main function
def main():

    # Define the contract address of the DEX
    contract = '0xBb8080caBdee22fbF4f0B0d618A334064DB6C241'
    hacker = accounts.add(config['wallets']['from_key'])
    attack_dex2 = First_AttackDexTwo.deploy(contract,{"from":hacker})
