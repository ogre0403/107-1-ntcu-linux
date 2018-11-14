##1

1. 
```
#ver=$(uname -r)
``` 
2.
```
#echo $ver
``` 
*顯示3.10.0-862.e17.x86_64
3.
```
#ver="my kernel version is 3.10"
```
4.(檢查)
```
#echo $ver
```
*出現my kernel version is 3.10

*![](https://i.imgur.com/nfNcAVQ.png)
*作業系統會依照PATH環境變數中所設定的路徑順序，依序尋找各路徑下是否有這個指令。

##2

*root和同群組的帳號具有rwx權限，其他帳號則只有rx權限

1.
```
#chmod 777 ~/script.sh
```
2.
```
#chmod u=rwx,g=rwx,o=rwx ~/script.sh
```

##3

*實體連結是在目錄裡加一筆inode與檔名對應
*符號連結是建立獨立檔案指向目的檔案

*實體連結
1.
```
#ll -i /etc/hosts
``` 
2.
```
#ln /etc/hosts .
```
3.(檢查) 
```
ll -i /etc/hosts hosts.real
```

*符號連結
1.
```
#ln -s /etc/hosts hosts.symbo
```
2.(檢查) 
```
#ll -i /etc/hosts /root/hosts.symbo
```

##4
*重啟測試系統打不開
