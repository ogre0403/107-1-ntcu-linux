#1.
首先左上角有一個檔案,點下去以後有一個主機網路管理員(H)，然後進入後在左上角有一個建立，再點進去就有新的網卡了。
![](https://ppt.cc/f2rRtx@.png)
#2.
ip address add 192.168.100.100/24 broadcast + dev enp0s3設定虛擬機器1的網路
![](https://ppt.cc/fNnYpx@.png)
#3.
ip address add 192.168.100.200/24 broadcast + dev enp0s3設定虛擬機器2的網路
![](https://ppt.cc/f8GeUx@.png)
#4.
vi /etc/sysconfig/network-scripts/ifcfg-*進入檔案以後，將ONBOOT=no改成ONBOOT=yes，在虛擬機器1上寫下IPADDR=192.168.100.200。在虛擬機器2上寫下IPADDR=192.168.100.100
![](https://ppt.cc/fpTYMx@.png)
#5.
ping 192.168.100.200從虛擬機器-1 ping 虛擬機器-2確認網路是連通ping 192.168.100.100並從虛擬機器-2 ping 虛擬機器-1，確認網路也是連通。
![](https://ppt.cc/fXy7ax@.png)