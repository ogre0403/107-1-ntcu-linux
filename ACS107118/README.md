###HW10
1.systemctl status sshd，查看sshd的狀態   
![](https://i.imgur.com/S6H0S7E.png)
2.使用yum install vsftpd 安裝vsftpd    
![](https://i.imgur.com/dq5TUri.png)
3.使用 yum install policycoreutils-python 安裝policycoreutils-python   
![](https://i.imgur.com/66wH1oO.png)
4.切換到目錄cd / etc / ssh 並複製檔案，cp sshd_config sshd2_config   
![](https://i.imgur.com/POTr5X2.png)
5.使用vi sshd2_config 更改內容，Port = 22 - > Port = 2222    
![](https://i.imgur.com/qJXq6eY.png)
6.使用 cd / etc / systemd / system切換到目錄,並使用cp /usr/lib/systemd/system/sshd.service sshd2.service 複製檔案     
![](https://i.imgur.com/tcpBzZf.png)
7.使用vi sshd2.service 更改內容 
![](https://i.imgur.com/0Ryc0rS.png)
8.semanage port -a -t ssh_port_t -p tcp 2222修正.semanage port -l | grep ssh查看。  
![](https://i.imgur.com/FILZIxG.png)
9.使用systemctl daemon-reload，讓其重新讀取，啟動sshd2_service，systemctl start sshd2.service   
![](https://i.imgur.com/wPfWCqs.png)
10.使用netstat -alntp | grep ssh查看結果    
