## 📦 准备工作

- 一枚 **支持 OpenPGP 和 ECC 的 YubiKey**（如 YubiKey 5C/5NFC/5Ci）
- 已安装 GnuPG ≥ 2.2.27（支持 `secp256k1` 曲线）
- 可选工具：YubiKey Manager (`ykman`)

###

- 创建 secp256k1 主私钥（签名）+ 子私钥（加密、认证）
```
gpg --expert --full-generate-key
Please select what kind of key you want:
(11) ECC (set your own capabilities)

Current allowed actions: Sign Certify 
q

Please select which elliptic curve you want:
(9) secp256k1

```
### GPG 导入
```
gpg --edit-key <KEYID>
gpg > keytocard
gpg > save

# 查询yubikey
gpg --card-status
```

### GPG 清空yubikey
```
gpg --card-edit
gpg > admin
gpg > factory-reset
```

