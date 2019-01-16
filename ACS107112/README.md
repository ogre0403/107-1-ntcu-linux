+ 先切換至ssh並將sshd_config複製到sshd2_config
![](https://i.imgur.com/9PgCQ4X.jpg)
+ 更改裡面內容，在隨便一行加上port 2222
![](https://i.imgur.com/WoqViDm.jpg)
+ 再將sshd.service的部分複製到sshd2.service
![](https://i.imgur.com/egcOBhz.png)
+ 使用yum install policycoreutils-python
+ 安裝完就可以使用semanage 
![](https://i.imgur.com/HpFKKBS.jpg)
+ 使用semanage port -a -t ssh_port_t -p tcp 2222
+ 使用semanage port -l | grep ssh 確認完成
![](https://i.imgur.com/BxB4YRo.jpg)
+ 使用yum whatprovides netstat
![](https://i.imgur.com/5qH1yzH.jpg)
+ 使用yum install net-tools
![](https://i.imgur.com/pEG4nUo.jpg)
+ 使用systemctl daemon-reload
+ 使用systemctl start sshd2.service
+ 使用netstat -alntp | grep ssh
![](https://i.imgur.com/omP2BTY.jpg)




