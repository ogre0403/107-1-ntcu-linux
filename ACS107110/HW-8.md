1.點選右上方的全域工具，進入之後建立網卡，在IPV4位址輸入192.168.100.100，即可完成。

2.建立一個虛擬機器abc，在設定值上選擇啟用host-only網路卡
  安裝完成之後，輸入ifconfig enp0s8 192.168.100.100，再輸入ifconfig，如圖所示
  再建立一個虛擬機器def，在設定值上選擇啟用host-only網路卡
  安裝完成之後，輸入ifconfig enp0s8 192.168.100.200，再輸入ifconfig,即可完成
##ifconfig需事先下載yum install net-tools

3. (abc虛擬機器)vi /etc/sysconfig/network-scripts/ifcfg-*
   把ONBOOT=yes(no改yes)，新增ip位址IPADDR=192.168.100.100
   (def虛擬機器)vi /etc/sysconfig/network-scripts/ifcfg-*
   把ONBOOT=yes(no改yes)，新增ip位址IPADDR=192.168.100.200

4.***從虛擬機器-1 ping 虛擬機器-2確認網路是連通，並從虛擬機器-2 ping 虛擬機器-1，確認網路也是連通。
在abc虛擬機器上輸入
ping 192.168.100.200
在def虛擬機器上輸入
ping 192.168.100.100
確認網路是否互通
