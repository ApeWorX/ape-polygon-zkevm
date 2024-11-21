from typing import cast

from ape_ethereum import TransactionType
from ape_ethereum.ecosystem import (
    BaseEthereumConfig,
    Ethereum,
    NetworkConfig,
    create_network_config,
)

NETWORKS = {
    # chain_id, network_id
    "mainnet": (1101, 1101),
    "cardona": (2442, 2442),
}


class PolygonZkEVMConfig(BaseEthereumConfig):
    mainnet: NetworkConfig = create_network_config(
        block_time=2,
        required_confirmations=1,
        default_transaction_type=TransactionType.STATIC.value,
    )
    cardona: NetworkConfig = create_network_config(
        block_time=2,
        required_confirmations=1,
        default_transaction_type=TransactionType.STATIC.value,
    )


class PolygonZkEVM(Ethereum):
    @property
    def config(self) -> PolygonZkEVMConfig:  # type: ignore
        cfg = self.config_manager.get_config("polygon-zkevm")
        return cast(PolygonZkEVMConfig, cfg)
