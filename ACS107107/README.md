#  1.請依說明完成下列操作讓虛擬機器彼此間能夠透過網路相互溝通：
##  在VirtalBox內建立一個新的Host-only 網路卡，網段為192.168.100.1/24
##  ![](https://i.imgur.com/CH7lwDD.jpg)
##  建立虛擬機器-1，並啟用host-only網路卡，透過ifconfig 或 ip指令，設定虛擬機器-1的網路為192.168.100.100/24
##  ![](https://i.imgur.com/AuWsHOR.jpg)
##  ![](https://i.imgur.com/ErO0FPt.jpg)
##  建立虛擬機器-2，並啟用host-only網路卡，透過ifconfig 或 ip指令，設定虛擬機器-2的網路為192.168.100.200/24
##  ![](https://i.imgur.com/velsDqq.jpg)
##  ![](https://i.imgur.com/HVKLZ6o.jpg)
##　將二台虛擬機器的網路設定存至/etc/sysconfig/network-scripts/下相對應的ifcfg-*檔案，重新啟動虛擬機器，確認網路ip設定無誤。
##  將第一台虛機的設定存在/etc/sysconfig/network-scripts/下相對應的ifcfg-*檔案(利用vi /etc/sysconfig/network-scripts/ifcfg-*)
##  ![](https://i.imgur.com/Qus8owM.jpg)
##  將第二台虛機的設定存在/etc/sysconfig/network-scripts/下相對應的ifcfg-*檔案(利用vi /etc/sysconfig/network-scripts/ifcfg-*)
##  ![](https://i.imgur.com/JzRbcpQ.jpg)
##  重新啟動虛擬機器，確認網路ip設定無誤。
##  ![](https://i.imgur.com/pNNaMqW.jpg)
##  ![](https://i.imgur.com/5IYs3uY.jpg)
