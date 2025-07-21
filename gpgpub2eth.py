from pgpy import PGPKey
from eth_utils import keccak, to_checksum_address
import struct

def extract_pubkey_from_gpg_ascii(path: str) -> bytes:
    with open(path, "r") as f:
        blob = f.read()
    key, _ = PGPKey.from_blob(blob)

    # 获取 ECPoint 对象 → 转为 MPI bytes（2字节bitlen + 65字节数据）
    mpi_bytes = key._key.keymaterial.p.to_mpibytes()

    # 解析 MPI → 跳过前2字节bit长度
    bitlen = struct.unpack(">H", mpi_bytes[:2])[0]
    keydata = mpi_bytes[2:]

    if len(keydata) != 65 or keydata[0] != 0x04:
        raise ValueError("不是未压缩 secp256k1 公钥")
    return keydata

def pubkey_to_eth_address(pubkey_bytes: bytes) -> str:
    keccak_digest = keccak(pubkey_bytes[1:])[-20:]
    return to_checksum_address("0x" + keccak_digest.hex())

# 主程序
pubkey_bytes = extract_pubkey_from_gpg_ascii("pubkey.asc")
print("Ethereum Pubkey:",pubkey_bytes.hex())
eth_address = pubkey_to_eth_address(pubkey_bytes)
print("Ethereum address:", eth_address)
