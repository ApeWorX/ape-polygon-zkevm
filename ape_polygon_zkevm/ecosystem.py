from typing import cast

from ape_ethereum.ecosystem import (
    BaseEthereumConfig,
    Ethereum,
    NetworkConfig,
    create_network_config,
)

NETWORKS = {
    # chain_id, network_id
    "mainnet": (1101, 1101),
    "goerli": (1442, 1442),
}


class PolygonZkEVMConfig(BaseEthereumConfig):
    mainnet: NetworkConfig = create_network_config(block_time=2, required_confirmations=1)
    goerli: NetworkConfig = create_network_config(block_time=2, required_confirmations=1)


class PolygonZkEVM(Ethereum):
    @property
    def config(self) -> PolygonZkEVMConfig:  # type: ignore
        return cast(PolygonZkEVMConfig, self.config_manager.get_config("polygon-zkevm"))
