# HW8_ADT105137

1.在VirtalBox內建立一個新的Host-only 網路卡，網段為192.168.100.1/24

A: 點選VirtalBox右上方全域工具，建立一個網路卡，在下方設定裡的IPv4位置打上192.168.100.1。

![image](https://github.com/Yubo0826/1217/blob/master/1.PNG)

2.建立虛擬機器-1，並啟用host-only網路卡，透過ifconfig 或 ip指令，設定虛擬機器-1的網路為192.168.100.100/24

3.建立虛擬機器-2，並啟用host-only網路卡，透過ifconfig 或 ip指令，設定虛擬機器-2的網路為192.168.100.200/24

A: 打開虛擬主機-1(2)，先用ip addr show指令查看現在host-only網路卡的IP(enp0s8)。

![image](https://github.com/Yubo0826/1217/blob/master/2.PNG)

再用config指令修改IP。

![image](https://github.com/Yubo0826/1217/blob/master/3.PNG)

最後檢查看看IP是否符合需要。

![image](https://github.com/Yubo0826/1217/blob/master/4.PNG)

4.將二台虛擬機器的網路設定存至/etc/sysconfig/network-scripts/下相對應的ifcfg-*檔案，重新啟動虛擬機器，確認網路ip設定無誤。

A:打開文件，加入兩行文字，分別為

IPADDR=192.168.100.100

NETMASK=255.255.255.0

另外ONBOOT改成yes，確保開機時網路卡的IP都是192.168.100.100。

![image](https://github.com/Yubo0826/1217/blob/master/7.PNG)

5.從虛擬機器-1 ping 虛擬機器-2確認網路是連通，並從虛擬機器-2 ping 虛擬機器-1，確認網路也是連通。

A:使用其中一台虛擬主機，利用ping+另一台虛擬主機的網路卡，看看是否能連線成功，出現下方文字即是成功連接。

![image](https://github.com/Yubo0826/1217/blob/master/6.PNG)




