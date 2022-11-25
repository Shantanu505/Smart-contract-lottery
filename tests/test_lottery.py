from brownie import Lottery, accounts, config, network
from web3 import Web3


def test_get_entrance_fee():
    account = accounts[0]
    lottery = lottery.deploy(
        config["networks"][network.show_active()]["eth_usd_price_feed"],
        {"from": account},
    )
    assert lottery.getGetEntranceFee() > Web3.roWei(0.018, "ether")
    assert lottery.getGetEntranceFee() < Web3.roWei(0.022, "ether")
