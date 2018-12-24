## 在VirtalBox內建立一個新的Host-only 網路卡，網段為192.168.100.1/24。
![](https://i.imgur.com/VaX5ECd.png)
## 使用ifconfig或ip指令，將虛擬機器-1的網路設定為192.168.100.100/24，將虛擬機器-2的網路設定為192.168.100.200/24
(ip address add 198.168.100.100/24 broadcast + dev enp0s3)
(ip address add 198.168.100.200/24 broadcast + dev enp0s3)
![](https://i.imgur.com/QDjxGr4.png)
## 將虛擬機器1&2的網路設定存至/etc/sysconfig/network-scripts/下相對應的ifcfg-*檔案，重新啟動虛擬機器，確認網路ip設定無誤。 
(vi /etc/sysconfig/network-scripts/ifcfg-enp0s3)
![](https://i.imgur.com/nIWT8MJ.png)
## 從虛擬機器-1 ping 虛擬機器-2確認網路是連通，並從虛擬機器-2 ping 虛擬機器-1，確認網路也是連通。
(ping 192.168.100.100)
(ping 192.168.100.200)
![](https://i.imgur.com/eXVLc5m.png)
