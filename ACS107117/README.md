### (1)在VirtalBox內建立一個新的Host-only 網路卡，網段為192.168.100.1/24
![Imgur](https://i.imgur.com/D0wcQxr.png)
### (2)建立虛擬機器-1，並啟用host-only網路卡，透過ifconfig 或 ip指令，設定虛擬機器-1的網路為192.168.100.100/24
+ ifconfig enp0s8 192.168.100.100
![Imgur](https://i.imgur.com/Gj6gwkN.png)
![Imgur](https://i.imgur.com/LIo2wPt.png)
![Imgur](https://i.imgur.com/x5UTpL4.png)
### (3)建立虛擬機器-2，並啟用host-only網路卡，透過ifconfig 或 ip指令，設定虛擬機器-2的網路為192.168.100.200/24
+ ifconfig enp0s8 192.168.100.200
![Imgur](https://i.imgur.com/X2zYfAc.png)
![Imgur](https://i.imgur.com/uplwUwk.png)
### (4)將二台虛擬機器的網路設定存至/etc/sysconfig/network-scripts/下相對應的ifcfg-*檔案，重新啟動虛擬機器，確認網路ip設定無誤
+ vi /etc/sysconfig/network-scripts/ifcfg-enp0s8
![Imgur](https://i.imgur.com/LkqNM8o.png)
![Imgur](https://i.imgur.com/6nI2f2T.png)
![Imgur](https://i.imgur.com/AFwTHRK.png)
![Imgur](https://i.imgur.com/nfQJJ8M.png)
![Imgur](https://i.imgur.com/XFQCNmQ.png)
### (5)從虛擬機器-1 ping 虛擬機器-2確認網路是連通，並從虛擬機器-2 ping 虛擬機器-1，確認網路也是連通
+ ping 192.168.100.100
+ ping 192.168.100.200
![Imgur](https://i.imgur.com/S4Y0vZW.png)
![Imgur](https://i.imgur.com/JPHgRYU.png)
