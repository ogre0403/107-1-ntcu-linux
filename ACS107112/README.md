## 第一題
+ 在VirtalBox內建立一個新的Host-only網路卡
+ 網段為192.168.100.1/24
![](https://i.imgur.com/RXfNLIi.png)
## 第二題
+ 建立虛擬機器-1
+ 用host-only網路卡
+ 用ifconfig 或 ip指令
+ 設定虛擬機器-1的網路為192.168.100.100/24
![](https://i.imgur.com/sFHmopH.png)

![](https://i.imgur.com/AFdtV0f.png)
## 第三題
+ 建立虛擬機器-2
+ 用host-only網路卡
+ 用ifconfig或ip指令
+ 設定虛擬機器-1的網路為192.168.100.200/24
![](https://i.imgur.com/cIs5QBq.png)
## 第四題
+ 將二台虛擬機器的網路設定存至/etc/sysconfig/network-scripts/下相對應的ifcfg-*檔案
![](https://i.imgur.com/U0lmwul.png)

![](https://i.imgur.com/Ih9AJBB.png)

![](https://i.imgur.com/MQge0Rn.png)

![](https://i.imgur.com/7sBgEeE.png)
+ 重新啟動虛擬機器
+ 確認網路ip設定無誤
## 第五題
+ 從虛擬機器-1 ping虛擬機器-2確認網路是連通
+ 並從虛擬機器-2 ping 虛擬機器-1
+ 確認網路也是連通
![](https://i.imgur.com/jM32Gv1.png)

