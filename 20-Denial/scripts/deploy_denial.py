# Import necessary modules
from brownie import accounts, config, AttackDenial


# Define main function
def main():
    # Instance Address
    contract = '0xAC0484CD54b5092e9663bFb7bA403d1B16d78D63'
    # Create a new account using the private key stored in the config file
    hacker = accounts.add(config['wallets']['from_key'])
    
    AttackDenial.deploy(contract,{'from': hacker})
