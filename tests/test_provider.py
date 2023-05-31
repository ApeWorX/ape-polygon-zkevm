def test_basic(accounts, local_network):
    a = accounts.test_accounts[0]
    receipt = a.transfer(a, 100)

    assert not receipt.failed
    assert receipt.value == 100


def test_get_receipt(accounts, networks, local_network):
    transfer = accounts.test_accounts[0].transfer(accounts.test_accounts[1], 1)
    assert transfer.txn_hash
    tx = networks.provider.get_receipt(transfer.txn_hash)
    assert tx.data.hex()
