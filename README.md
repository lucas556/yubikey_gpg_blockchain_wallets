
### GPG 清空yubikey
```
gpg --card-edit
gpg > admin
gpg > factory-reset
```

### GPG 导入
```
gpg --edit-key <KEYID>
keytocard
save
```
