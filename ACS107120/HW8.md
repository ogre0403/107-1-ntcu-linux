### 請依說明完成下列操作讓虛擬機器彼此間能夠透過網路相互溝通

1. 在VirtualBox內建立一個新的Host-only網路卡，網段為192.168.100.1/24

   ip a

2. 建立虛擬機器-1，並啟用host-only網路卡，透過ifconfig 或 ip指令，設定虛擬機器-1的網路為192.168.100.100/24

   ip address add 192.168.100.100/24 broadcast +dev enp0s8 label 
   ip a

3. 建立虛擬機器-2，並啟用host-only網路卡，透過ifconfig 或 ip指令，設定虛擬機器-2的網路為192.168.100.200/24

   ip address add 192.168.100.200/24 broadcast +dev enp0s8 label 
   ip a

4. 將二台虛擬機器的網路設定存至/etc/sysconfig/network-scripts/下相對應的ifcfg-*檔案，重新啟動虛擬機器，確認網路ip設定無誤。

   重新啟動機器，用root登入
   輸入ip a

5. 從虛擬機器-1 ping 虛擬機器-2確認網路是連通，並從虛擬機器-2 ping 虛擬機器-1，確認網路也是連通。

   ping 192.168.100.100
   ping 192.168.100.200
