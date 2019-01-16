#1.
首先左上角有一個檔案,點下去以後有一個主機網路管理員(H)，然後進入後在左上角有一個建立，再點進去就有新的網卡了。
![](https://ppt.cc/f20ERx@.png)

ip address add 192.168.200.100 broadcast + dev enp0s3設定虛擬機器的網路
![](https://ppt.cc/fFJgtx@.png)
vi /etc/sysconfig/network-scripts/ifcfg-*進入檔案以後，，在虛擬機器上寫下IPADDR=192.168.200.100。
![](https://ppt.cc/fWP8zx@.png)
![](https://ppt.cc/f817Jx@.png)
ifconfig驗證
![](https://ppt.cc/fNzVMx@.png)
#2
yum install nginx
![](https://ppt.cc/fXblTx@.png)
systemctl start nginx
![](https://ppt.cc/fhWHax@.png)
netstat -alntp |  grep nginx
![](https://ppt.cc/f0RSZx@.png)
#3.
跑不出來......
![](https://ppt.cc/foMWax@.png)
#4.
連不上去......
![](https://ppt.cc/fLTTyx@.png)