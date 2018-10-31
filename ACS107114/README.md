# HW-4
## 第一題
* (1)使用groupadd建立 mygroup、nogroup群組
![](https://i.imgur.com/dJpTfMx.png)
* (2)建立帳號名稱 myuser1~3 並且加入mygroup 
![](https://i.imgur.com/kah7GFM.png)
* (3)建立帳號名稱 nouser1~3 加入nogroup
![](https://i.imgur.com/KGjRGAy.png)
* (4)使用mkdir 建立目錄 然後使用 (chmod 770)讓mygroup群組內的使用者完整使用 不過其他人不能有任何權限
![](https://i.imgur.com/BD30mUz.png)
* (5)切換至myuser1 在/srv/myproject 目錄中使用 touch myuser1.data建立檔案
![](https://i.imgur.com/M6agCgk.png)
* (6)切換至root 使用(cp /usr/bin/ls /usr/local/bin/myls)    復制/usr/bin/ls至/usr/local/bin/myls![](https://i.imgur.com/kDfE2hx.png)
* (7)使用(chmod u+s /usr/local/bin/myls)更改權限
![](https://i.imgur.com/MNrpDMt.png)
* (8)切換至nouser1 使用(myls /srv/myproject) 執行 檢驗是否成功修改權限
![](https://i.imgur.com/aCU4ssh.png)

## 第二題
* 使用 (ps |grep rsyslog) 找到的 rsyslog 相關的程序的 PID, PRI, NI, COMMAND 再使用(ps aux | grep rsyslog > /root/process_syslog.txt)
![](https://i.imgur.com/o5SKjCq.png)

## 第三題
* (1)使用(find /usr/bin /usr/sbin -perm /4000)找出 /usr/bin 及 /usr/sbin 兩個目錄中 含有 SUID 的特殊檔案檔名
![](https://i.imgur.com/JuBnRKR.png)
* (2)再使用(find /usr/bin /usr/sbin -perm /4000 -exec ls -l {} \;)列出找到的檔案的相關權限
![](https://i.imgur.com/XCBSKrX.png)
* (3)最後使用(find /usr/bin /usr/sbin -perm/4000 -exec ls -l {} \; > /root/findsuidsgid.txt)將螢幕資料轉存到 /root/findsuidsgid.txt 檔案中
![](https://i.imgur.com/sztl9Pq.png)


