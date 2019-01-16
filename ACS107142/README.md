# HW-10
---
## 請仿照課堂上練習，透過systemd管理二個sshd服務，並讓第二個sshd服務的 port 放行於 2222。完成後可以使用指令 netstat -alntp | grep ssh 確認是否啟動二個sshd服務。
### 使用cp複製sshd_config至sshd2_config
![](https://i.imgur.com/7nytye7.png)
### 用vi進入sshd2_config並將port 22改為port 2222
![](https://i.imgur.com/prN0VcK.png)
### 用cp複製cp /usr/lib/systemd/system/sshd.service 至sshd2.service
![](https://i.imgur.com/K8JXLCX.png)
### 用vi將type改為simple且將ExecStart改成/usr/sbin/sshd -f /etc/ssh/sshd2_config -D
![](https://i.imgur.com/X3cApR3.png)
### 用yum下載指令包
![](https://i.imgur.com/uC1OcRz.png)
![](https://i.imgur.com/iIKabOP.png)
### 用semanage port -a -t ssh_port_t -p tcp 2222設定,然後用semanage port -l | grep ssh確認
![](https://i.imgur.com/3qy4VRv.png)
### 用systemctl daemon-reload和systemctl start sshd2.service重新啟動sshd2_service
![](https://i.imgur.com/kqM4nHD.png)
### 最後用netstat -alntp | grep ssh查看