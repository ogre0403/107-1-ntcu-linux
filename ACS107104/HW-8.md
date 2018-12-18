#請依說明完成下列操作讓虛擬機器彼此間能夠透過網路相互溝通：

##在VirtalBox內建立一個新的Host-only 網路卡，網段為192.168.100.1/24

*進入virtuallbox點選右上角全域工具→點選主機網路管理員→點選建立→在位址 輸入192.168.100.1;網路遮罩 輸入255.255.255.0→按後方啟用即可完成

![image]()

##建立虛擬機器-1，並啟用host-only網路卡，透過ifconfig 或 ip指令，設定虛擬機器-1的網路為192.168.100.100/24

*先下載ifconfig

>輸入yum install net-tools

*輸入ip address add 192.168.100.100/24 broadcast + dev enp0s8

##建立虛擬機器-2，並啟用host-only網路卡，透過ifconfig 或 ip指令，設定虛擬機器-2的網路為192.168.100.200/24

*輸入ip address add 192.168.100.200/24 broadcast + dev enp0s8

![image]()

##將二台虛擬機器的網路設定存至/etc/sysconfig/network-scripts/下相對應的ifcfg-*檔案，重新啟動虛擬機器，確認網路ip設定無誤。

*開啟虛擬機器1

*輸入vi /etc/sysconfig/network-scripts/ifcfg-enp0s3

*輸入a

>啟用編輯

*把ONBOOT=no改成yes

>開機時即會自動開啟

*IPADDR=192.168.100.100

>新增對應IP位址

*按esc→:wq

>儲存離開

![image]()

*開啟虛擬機器2

*輸入vi /etc/sysconfig/network-scripts/ifcfg-enp0s3

*輸入a

>啟用編輯

*把ONBOOT=no改成yes

>開機時即會自動開啟

*IPADDR=192.168.100.200

>新增對應IP位址

*按esc→:wq

>儲存離開

![image]()

##從虛擬機器-1 ping 虛擬機器-2確認網路是連通，並從虛擬機器-2 ping 虛擬機器-1，確認網路也是連通。

*重新開啟虛擬機器1

*輸入ping 192.168.100.200

>確認跟虛擬機器二網路有連通

![image]()

*重新開啟虛擬機器2

*輸入ping 192.168.100.100

>確認跟虛擬機器一網路有連通

![image]()
