+ 新建Host-only網段為192.168.100.1/24
![GITHUB](https://imgur.com/Ut1jdvF.jpg"gitｹﾏ･ﾜ")
+ 用ifconfig enp0s8 192.168.100.100/24 192.168.100.200/24改ip
![GITHUB](https://imgur.com/YegxdaC.jpg"gitｹﾏ･ﾜ")
+ 用ifconfig看是否改成功
![GITHUB](https://imgur.com/26MugvU.jpg"gitｹﾏ･ﾜ")
+ 改vi /etc/sysconfig/network-scripts/ifcfg-enp0s8
![GITHUB](https://imgur.com/F0BGaam.jpg"gitｹﾏ･ﾜ")
+ 重開機後用ifconfig看ip
![GITHUB](https://imgur.com/ulzRmFG.jpg"gitｹﾏ･ﾜ")
+ 用ping 192.168.100.200 ping 192.168.100.100確認是否連通
![GITHUB](https://imgur.com/3ptEd2A.jpg"gitｹﾏ･ﾜ")