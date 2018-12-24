# HW-8

## 第一題


>在VirtalBox內建立一個新的Host-only 網路卡，網段為192.168.100.1/24


![1](https://thumbs2.imgbox.com/ef/49/g3B61DGp_t.png)


首先開啟virtualbox，點選右上角全域工具的網路卡設定，右鍵建立新的網路卡。


![2](https://images2.imgbox.com/6b/f1/p626dKAo_o.png)


設定手動組態IPv4位址為192.168.100.1，網路遮罩設為255.255.255.0。



>建立虛擬機器-1，並啟用host-only網路卡，透過ifconfig 或 ip指令，設定虛擬機器-1的網路為192.168.100.100/24

>建立虛擬機器-2，並啟用host-only網路卡，透過ifconfig 或 ip指令，設定虛擬機器-2的網路為192.168.100.200/24


![3](https://images2.imgbox.com/e5/60/KpKgUtor_o.png)


首先建立新的虛擬機器。


![4](https://images2.imgbox.com/8e/86/6LVKMX8G_o.png)


-----
使用指令: **ip addr add 192.168.100.10/24 dev enp0s8**
-----

將網卡enp0s8重設並利用指令 **ip a** 進行查看，同此步驟設定另一個虛擬器。


>將二台虛擬機器的網路設定存至/etc/sysconfig/network-scripts/下相對應的ifcfg-*檔案，重新啟動虛擬機器，確認網路ip設定無誤。


![5](https://images2.imgbox.com/ff/ae/Po4fXs7m_o.png)


-----
使用指令: **vi /etc/sysconfig/network-scripts/ifcfg-enp0s8**
-----

對網卡enp0s8進行設定。


![6](https://images2.imgbox.com/56/91/6jOilgkW_o.png)


將 BOOTPROTO 設為 static 
新增  IPADDR=192.168.100.10  /  NETMASK=255.255.255.0
將 ONBOOT 設為 yes
最後儲存離開
同理設定另一台虛擬機器


![7](https://images2.imgbox.com/b1/33/OYs5jBb0_o.png)

![8](https://images2.imgbox.com/02/04/NYDaCqdU_o.png)


重新開機並利用指令 **ip a** 檢察網卡 enp0s8 是否設定成功


>從虛擬機器-1 ping 虛擬機器-2確認網路是連通，並從虛擬機器-2 ping 虛擬機器-1，確認網路也是連通。


![9](https://images2.imgbox.com/82/b3/eNKhWcvI_o.png)

![10](https://images2.imgbox.com/07/62/mpsBxcm5_o.png)


利用指令ping讓兩台虛擬機器十次測試，分別ping 192.168.100.10 和 192.168.100.20 ，結果正確接收 packets 。

