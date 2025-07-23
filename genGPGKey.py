from pgpy import PGPKey, PGPUID
from pgpy.constants import PubKeyAlgorithm, EllipticCurveOID, KeyFlags, HashAlgorithm, SymmetricKeyAlgorithm, CompressionAlgorithm

# 生成 secp256k1 主密钥
key = PGPKey.new(PubKeyAlgorithm.ECDSA, EllipticCurveOID.SECP256K1)
uid = PGPUID.new("Your Name", email="you@example.com")

# 绑定 User ID
key.add_uid(uid,
            usage={KeyFlags.Sign, KeyFlags.Certify},
            hashes=[HashAlgorithm.SHA256],
            ciphers=[SymmetricKeyAlgorithm.AES256],
            compression=[CompressionAlgorithm.ZLIB])

# 导出
print("Public Key:\n", key.pubkey)
print("Private Key:\n", key)
