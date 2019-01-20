第一題

在VirtalBox內建立一個新的Host-only網路卡
網段為192.168.100.1/24

![9](https://user-images.githubusercontent.com/43788227/51441746-90a5a300-1d0f-11e9-9db9-b2044ba89ee0.PNG)

使用ifconfig或ip指令，將網路設定為192.168.100.100/24
ip address add 198.168.100.100/24 broadcast + dev enp0s8
同理再將網路設定為192.168.100.200/24
![10](https://user-images.githubusercontent.com/43788227/51441822-bb442b80-1d10-11e9-8e79-13ed53f73ad0.PNG)
![11](https://user-images.githubusercontent.com/43788227/51441823-bd0def00-1d10-11e9-84a9-d16cc9e2bc04.PNG)

接著把2台虛擬機器的網路相關設定
儲存至/etc/sysconfig/network-scripts/下的相對檔案並使用vi修改

確認網路是否連通

