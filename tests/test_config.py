from ape_ethereum.transactions import TransactionType

from ape_polygon_zkevm.ecosystem import PolygonZkEVMConfig


def test_gas_limit(polygon_zkevm):
    assert polygon_zkevm.config.local.gas_limit == "max"


def test_default_transaction_type(polygon_zkevm):
    assert polygon_zkevm.config.mainnet.default_transaction_type == TransactionType.DYNAMIC


def test_mainnet_fork_not_configured():
    obj = PolygonZkEVMConfig.model_validate({})
    assert obj.mainnet_fork.required_confirmations == 0


def test_mainnet_fork_configured():
    data = {"mainnet_fork": {"required_confirmations": 555}}
    obj = PolygonZkEVMConfig.model_validate(data)
    assert obj.mainnet_fork.required_confirmations == 555


def test_custom_network():
    data = {"apenet": {"required_confirmations": 333}}
    obj = PolygonZkEVMConfig.model_validate(data)
    assert obj.apenet.required_confirmations == 333
