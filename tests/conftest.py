import ape
import pytest


@pytest.fixture
def networks():
    return ape.networks


@pytest.fixture
def accounts():
    return ape.accounts


@pytest.fixture
def polygon_zkevm(networks):
    return networks.get_ecosystem("polygon-zkevm")


@pytest.fixture
def eth_tester_provider():
    if not ape.networks.active_provider or ape.networks.provider.name != "test":
        with ape.networks.get_ecosystem("polygon-zkevm").local.use_provider("test") as provider:
            yield provider
    else:
        yield ape.networks.provider
