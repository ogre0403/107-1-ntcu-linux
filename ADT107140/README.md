#systemctl status sshd確認sshd執行狀態

![](./1.png)

#進入/etc/ssh並複製sshd_config成sshd2_config

![](./2.png) 

#vim sshd2_config 把port改成2222(要將port那行的#刪掉不然無法執行)

![](./3.png)

#進入/etc/systemd/system複製sshd.service成sshd2.service

![](./4.png)

#vim sshd2.service把description最後面加上2 execstart加上-f /etc/ssh/sshd2_config

![](./5.png)

#安裝semanage

![](./7.png)

#將system重開

![](./9.png)

#netstat -alntp即可查詢ssh狀態

![](./10.png)
