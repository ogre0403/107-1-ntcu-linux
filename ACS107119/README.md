#1

1.按全域工具進入全域工具,再按左上角的建立,建立新的網路卡,然後按左上角的內容,更改內容為192.168.100.1/24。
2.用ip address add 192.168.100.100/24 broadcast + dev enp0s8 設定虛擬機器1的網路,並用ip a看是否成功。用ip address add 192.168.100.200/24 broadcast + dev enp0s8 設定虛擬機器2的網路,並用ip a看是否成功。
3.用 vi /etc/sysconfig/network-scripts/ifcfg-* 進入檔案
將 ONBOOT=no 改成 ONBOOT=yes,加入 IPADDR=192.168.100.200 至虛擬機器一,加入 IPADDR=192.168.100.100 至虛擬機器二,確認網路ip設定無誤。
4.用 ping 192.168.100.200 確認虛擬機器1與虛擬機器2的連線,再用 ping 192.168.100.100 確認虛擬機器2與虛擬機器1的連線。






![](https://ppt.cc/fzTSqx@.png)
![](https://ppt.cc/f3bAjx@.png)
![](https://ppt.cc/fUa6px@.png)