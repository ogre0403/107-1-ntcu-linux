##HW8
 1. 請依說明完成下列操作讓虛擬機器彼此間能夠透過網路相互溝通
 
 + 在VirtalBox內建立一個新的Host-only 網路卡，網段為192.168.100.1/24
 ![GITHUB](https://imgur.com/243S3dl.jpg"git圖示")
 ![GITHUB](https://imgur.com/UBMT3Ck.jpg"git圖示")
 + 建立虛擬機器-1，並啟用host-only網路卡，透過ifconfig 或 ip指令，設定虛擬機器-1的網路為192.168.100.100/24。
 ![GITHUB](https://imgur.com/pyNq4pb.jpg"git圖示")
 + 建立虛擬機器-2，並啟用host-only網路卡，透過ifconfig 或 ip指令，設定虛擬機器-2的網路為192.168.100.200/24。
 ![GITHUB](https://imgur.com/LvJT5Fe.jpg"git圖示")
 + 將二台虛擬機器的網路設定存至/etc/sysconfig/network-scripts/下相對應的ifcfg-*檔案，重新啟動虛擬機器，確認網路ip設定無誤。
 ![GITHUB](https://imgur.com/hnIJhM4.jpg"git圖示")
 + 從虛擬機器-1 ping 虛擬機器-2確認網路是連通，並從虛擬機器-2 ping 虛擬機器-1，確認網路也是連通。
 ![GITHUB](https://imgur.com/5yaLp6P.jpg"git圖示")
 
 ![GITHUB](https://imgur.com/dK62tS6.jpg"git圖示")