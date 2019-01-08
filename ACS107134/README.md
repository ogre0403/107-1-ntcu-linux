* 的使用
">" 的使用
![](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-10/ACS107134/1.PNG)
`的用法
空四個有另一種用法
### 請仿照課堂上練習，透過systemd管理二個sshd服務，並讓第二個sshd服務的 port 放行於 2222。
### 完成後可以使用指令 netstat -alntp | grep ssh 確認是否啟動二個sshd服務，範例如下：

` $ netstat -alntp | grep ssh `

` tcp        0      0 0.0.0.0:22     0.0.0.0:*     LISTEN      1300/sshd `

` tcp        0      0 0.0.0.0:2222   0.0.0.0:*     LISTEN      15275/sshd `

` tcp6       0      0 :::22          :::*          LISTEN      1300/sshd `

` tcp6       0      0 :::2222        :::*          LISTEN      15275/sshd `

1.找到設定ssh連接埠的設定檔 /etc/ssh/ssh_config。

複製一份取名為 ssh2_config ，將連接埠改為2222
![](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-10/ACS107134/3.PNG)

2.再找到ssh的設定腳本 /usr/lib/systemd/system/sshd.service。

複製一份取名為sshd2.service ，將Execstart增加 -f /etc/ssh/ssh2_config 
![](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-10/ACS107134/4.PNG)

3.systemctl start sshd2 啟動該服務
![](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-10/ACS107134/1.PNG)
