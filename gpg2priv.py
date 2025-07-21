### 测试 私钥生成的以太坊地址和公钥与PGP公钥生成的的地址进行对比

from pgpy import PGPKey
from eth_keys import keys
from eth_utils import to_checksum_address

# 1. 读取 privkey.asc
with open("privkey.asc", "r") as f:
    blob = f.read()

# 2. 加载私钥
key, _ = PGPKey.from_blob(blob)

# 3. 提取 secp256k1 私钥标量（即 Ethereum 私钥）
d = int(key._key.keymaterial.s)  # 正确字段是 `.s`

eth_privkey = d.to_bytes(32, 'big').hex()
print("Ethereum 私钥 (hex):", eth_privkey)

# 4. 生成 Ethereum 地址
priv_key = keys.PrivateKey(bytes.fromhex(eth_privkey))
print("eth pub",priv_key.public_key)
eth_address = to_checksum_address(priv_key.public_key.to_address())
print("Ethereum address:", eth_address)
