第八次作業
＝＝＝＝＝＝＝＝＝＝＝＝＝＝


進入左上角的主機網路管理員 新增一張host-only  的網卡

網段為192.168.100.1

![1](1.png)

然後打開設定值 將他新增至另一個虛擬機

打開網卡設定檔調整設定 在/etc/sysconfig/network-scripts/ifcfg-enp0s3
![2](2.png)

將onboot調整成yes

並調整網路設定

最後讓兩台機器互ping 證實和用nmap實證

![3](3.png)





