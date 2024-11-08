from ape import plugins


@plugins.register(plugins.Config)
def config_class():
    from ape_polygon_zkevm.ecosystem import PolygonZkEVMConfig

    return PolygonZkEVMConfig


@plugins.register(plugins.EcosystemPlugin)
def ecosystems():
    from ape_polygon_zkevm.ecosystem import PolygonZkEVM

    yield PolygonZkEVM


@plugins.register(plugins.NetworkPlugin)
def networks():
    from ape.api.networks import (
        LOCAL_NETWORK_NAME,
        ForkedNetworkAPI,
        NetworkAPI,
        create_network_type,
    )

    from ape_polygon_zkevm.ecosystem import NETWORKS

    for network_name, network_params in NETWORKS.items():
        yield "polygon-zkevm", network_name, create_network_type(*network_params)
        yield "polygon-zkevm", f"{network_name}-fork", ForkedNetworkAPI

    # NOTE: This works for local providers, as they get chain_id from themselves
    yield "polygon-zkevm", LOCAL_NETWORK_NAME, NetworkAPI


@plugins.register(plugins.ProviderPlugin)
def providers():
    from ape.api.networks import LOCAL_NETWORK_NAME
    from ape_node import Node
    from ape_test import LocalProvider

    from ape_polygon_zkevm.ecosystem import NETWORKS

    for network_name in NETWORKS:
        yield "polygon-zkevm", network_name, Node

    yield "polygon-zkevm", LOCAL_NETWORK_NAME, LocalProvider


def __getattr__(name: str):
    import ape_polygon_zkevm.ecosystem as module

    return getattr(module, name)
