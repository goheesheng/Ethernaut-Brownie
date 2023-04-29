from brownie import accounts, GatekeeperOne, AttackGateKeeper, config


def main():
    contract = '0xC39E9A019F5060E4ca110102F1273F7547df7373'
    hacker = accounts.add(config['wallets']['from_key'])

    print(hacker.balance())
    # gate = GatekeeperOne.deploy({'from': owner})
    attack = AttackGateKeeper.deploy(contract, {'from': hacker})
    tx = attack.attack({'from': hacker})
    assert len(tx.events['key_value']) > 0
    print(tx.events)