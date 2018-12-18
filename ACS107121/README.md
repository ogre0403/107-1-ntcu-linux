#hw8  
 ##1  
 ###在VirtalBox建一個Host-only的網路卡，IP 92.168.100.1/24  
  - 按右上角的全域工具,按建立,建立新的網路卡,左上角的內容,從手動組態介面卡更改內容
 ###建立虛擬機器-1，並啟用host-only網路卡，透過ifconfig 或 ip指令，設定虛擬機器-1的網路為192.168.100.100/24  
  - 以 ip address add 192.168.100.100/24 broadcast + dev enp0s8 設定虛擬機器1的網路
 ###建立虛擬機器-2，並啟用host-only網路卡，透過ifconfig 或 ip指令，設定虛擬機器-2的網路為192.168.100.200/24  
  - 以 ip address add 192.168.100.200/24 broadcast + dev enp0s8 設定虛擬機器2的網路
 ###將二台虛擬機器的網路設定存至/etc/sysconfig/network-scripts/下相對應的ifcfg-*檔案，重新啟動虛擬機器，確認網路ip設定無誤。  
  - vi /etc/sysconfig/network-scripts/ifcfg-*
  - ONBOOT=no 改成 ONBOOT=yes
  - IPADDR=192.168.100.200 虛擬機器一, IPADDR=192.168.100.100 虛擬機器二 
 ###從虛擬機器-1 ping 虛擬機器-2確認網路是連通，並從虛擬機器-2 ping 虛擬機器-1，確認網路也是連通  
  - 重新開機後 ping 192.168.100.200 確認虛擬機器1與虛擬機器2的連線,ping 192.168.100.100 確認虛擬機器2與虛擬機器1的連線    
