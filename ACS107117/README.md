### (1)在VirtalBox內建立一個新的Host-only 網路卡，網段為192.168.100.1/24  
![image](/ACS107106/1.png)
### (2)建立虛擬機器-1，並啟用host-only網路卡，透過ifconfig 或 ip指令，設定虛擬機器-1的網路為192.168.100.100/24
+ ifconfig enp0s8 192.168.100.100
![image](/ACS107106/2.png)
![image](/ACS107106/3.png)
![image](/ACS107106/4.png)
### (3)建立虛擬機器-2，並啟用host-only網路卡，透過ifconfig 或 ip指令，設定虛擬機器-2的網路為192.168.100.200/24
+ ifconfig enp0s8 192.168.100.200
![image](/ACS107106/5.png)
![image](/ACS107106/6.png)
### (4)將二台虛擬機器的網路設定存至/etc/sysconfig/network-scripts/下相對應的ifcfg-*檔案，重新啟動虛擬機器，確認網路ip設定無誤
+ vi /etc/sysconfig/network-scripts/ifcfg-enp0s8
![image](/ACS107106/7.png)
![image](/ACS107106/8.png)
![image](/ACS107106/9.png)
![image](/ACS107106/10.png)
![image](/ACS107106/11.png)
### (5)從虛擬機器-1 ping 虛擬機器-2確認網路是連通，並從虛擬機器-2 ping 虛擬機器-1，確認網路也是連通
+ ping 192.168.100.100
+ ping 192.168.100.200
![image](/ACS107106/12.png)
![image](/ACS107106/13.png)
