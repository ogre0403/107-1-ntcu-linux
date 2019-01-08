1. 輸入cd /etc/ssh，然後輸入sshd*切換至ssh，使用cp指令將sshd_config複製到sshd2_config。
![](https://i.imgur.com/ps2B6Rs.png)
2. 輸入vi sshd2_config 將#Port 22改成Port 2222
![](https://i.imgur.com/xebT5Ls.png)
![](https://i.imgur.com/wZpwtr4.png)
3. 使用cp指令將sshd.service複製到sshd2.service
![](https://i.imgur.com/o6TylDj.png)
4. vi ssh2.service修改內容
![](https://i.imgur.com/gWyqdtk.png)
5. 輸入yum provides semanage查詢指令
![](https://i.imgur.com/zRv54Qr.png)
![](https://i.imgur.com/RS93j3v.png)
6. 輸入yum install policycoreutils-python安裝semanage
![](https://i.imgur.com/zV3cGNT.png)
![](https://i.imgur.com/1rocupS.png)
7. 輸入semanage port -a -t ssh_port_t -p tcp 2222 
![](https://i.imgur.com/rLpucEm.png)
8. 輸入semanage port -l | grep ssh 
![](https://i.imgur.com/EwPip1a.png)
![](https://i.imgur.com/PGO1sLt.png)
9. 輸入netstat -alntp | grep ssh
![](https://i.imgur.com/lwsxNcX.png)
![](https://i.imgur.com/rU1wdi5.png)
10. 完成