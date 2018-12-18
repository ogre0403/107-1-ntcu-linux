* ##  在VirtalBox內建立一個新的Host-only 網路卡，網段為192.168.100.1/24
### 進入全域工具內選擇主機網路管理員，然後按建立，再按內容調整IPv4 位址192.168.100.1
![](https://i.imgur.com/OPMsAzC.png)
* ## 建立虛擬機器-1，並啟用host-only網路卡，透過ifconfig 或 ip指令，設定虛擬機器-1的網路為192.168.100.100/24
### 建立名為net的虛擬機器
![](https://i.imgur.com/Sh6c8OF.png)
### 輸入ip address add 192.168.100.100/24 broadcast + dev enp0s3改變ip位址,並用ip address show確認有改
![](https://i.imgur.com/0pTPkAl.png)
* ## 建立虛擬機器-2，並啟用host-only網路卡，透過ifconfig 或 ip指令，設定虛擬機器-2的網路為192.168.100.200/24
### 一樣使用ip address add 192.168.100.200/24 broadcast + dev enp0s3改變ip位址,並用ip address show確認有改
![](https://i.imgur.com/dEaE8XN.png)
* ## 將二台虛擬機器的網路設定存至/etc/sysconfig/network-scripts/下相對應的ifcfg-*檔案，重新啟動虛擬機器，確認網路ip設定無誤。
### 輸入vi /etc/sysconfig/network-scripts/ifcfg-,然後輸入IPADDR=192.168.100.100
![](https://i.imgur.com/ZQYNOX9.png)
### 於另一台虛擬機器輸入IPADDR=192.168.100.200
![](https://i.imgur.com/NmP1oD6.png)
* ## 從虛擬機器-1 ping 虛擬機器-2確認網路是連通，並從虛擬機器-2 ping 虛擬機器-1，確認網路也是連通。
### 用ping 192.168.100.200和ping 192.168.100.100確認網路有連通
![](https://i.imgur.com/LJHhQ0J.png)