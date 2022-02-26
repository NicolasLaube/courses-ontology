"""Economy modules"""
from src.builder import ONTOLOGY
from src.construction.micro_learning.classes import Module
from src.instances.micro_learning.information_technologies.courses import (
    networks,
    cryptography,
    blockchain,
)

with ONTOLOGY:
    # Networks course

    devices = Module("Devices")

    addressing = Module("Addressing")
    routing = Module("Routing")
    internet_protocol = Module("InternetProtocol")

    addressing.requires_module.extend([devices])
    routing.requires_module.extend([addressing])
    internet_protocol.requires_module.extend([routing])

    networks_modules = [devices, addressing, routing, internet_protocol]

    networks.has_as_module.extend(networks_modules)

    # Cryptography course

    encryption = Module("Encryption")
    hashing = Module("Hashing")
    secret_sharing = Module("SecretSharing")

    merklte_tree = Module("MerklteTree")
    zero_knowledge_proof = Module("ZeroKnowledgeProof")
    homomorphic_encryption = Module("HomomorphicEncryption")

    historical_cryptography = Module("HistoricalCryptography")
    modern_cryptography = Module("ModernCryptography")

    merklte_tree.requires_module.extend([hashing])
    zero_knowledge_proof.requires_module.extend([merklte_tree])
    historical_cryptography.requires_module.extend([encryption])
    homomorphic_encryption.requires_module.extend([encryption])
    modern_cryptography.requires_module.extend([secret_sharing])

    cryptography_modules = [
        encryption,
        hashing,
        secret_sharing,
        merklte_tree,
        zero_knowledge_proof,
        homomorphic_encryption,
        historical_cryptography,
        modern_cryptography,
    ]

    cryptography.has_as_module.extend(cryptography_modules)

    # Blockchain course

    consensus = Module("Consensus")

    distributed_ledger = Module("DistributedLedger")
    proof_of_work = Module("ProofOfWork")
    proof_of_stake = Module("ProofOfStake")

    distributed_ledger.requires_module.extend([consensus])
    proof_of_work.requires_as_module.extend([consensus])
    proof_of_stake.requires_as_module.extend([distributed_ledger, consensus])

    blockchain_modules = [consensus, distributed_ledger, proof_of_work, proof_of_stake]

    blockchain.has_as_module.extend(blockchain_modules)
