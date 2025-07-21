
### GPG 清空yubikey
```
gpg --card-edit
gpg > admin
gpg > factory-reset
```

### GPG 导入
```
gpg --edit-key <KEYID>
gpg > keytocard
gpg > save

# 查询yubikey
gpg --card-status
```
