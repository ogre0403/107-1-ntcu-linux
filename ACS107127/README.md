###  1. 請仿照課堂上練習，透過systemd管理二個sshd服務，並讓第二個sshd服務的 port 放行於 2222。完成後可以使用指令 `netstat -alntp | grep ssh` 確認是否啟動二個sshd服務，範例如下：

```sh
$ netstat -alntp | grep ssh
tcp        0      0 0.0.0.0:22     0.0.0.0:*     LISTEN      1300/sshd
tcp        0      0 0.0.0.0:2222   0.0.0.0:*     LISTEN      15275/sshd
tcp6       0      0 :::22          :::*          LISTEN      1300/sshd
tcp6       0      0 :::2222        :::*          LISTEN      15275/sshd
```

    Note 1: CentOS有使用SELinux ，故預設只允許 SSH 使用埠號 22，若要使用埠號 2222，使請用下列指開啟並檢查

    ```sh
    $ semanage port -a -t ssh_port_t -p tcp 2222
    $ semanage port -l | grep ssh
    ssh_port_t tcp 2202, 22
    ```  

    Note 2: CentOS預設的防火牆firewalld會禁止訪問埠號2222，若要透過2222埠連ssh，請先關閉firewalld。

####  先用`cd /etc/ssh`進入ssh。
####  用`cp sshd_config sshd2_config`將sshd_config的內容複製至sshd2_config。
![1](https://github.com/ad8902210302/107-1-ntcu-linux/blob/master/ACS107127/screen/1.png)</br>

####  輸入`vi sshd2_config`進入編輯。
![1](https://github.com/ad8902210302/107-1-ntcu-linux/blob/master/ACS107127/screen/2.png)</br>
####  將"Port 22"改為"Port 2222"
![1](https://github.com/ad8902210302/107-1-ntcu-linux/blob/master/ACS107127/screen/3.png)</br></br>

####  輸入`cd /etc/systemd/system`。
####  輸入`cp /usr/lib/systemd/system/sshd.service sshd2.service`將sshd.service的內容複製至sshd2.service。
![1](https://github.com/ad8902210302/107-1-ntcu-linux/blob/master/ACS107127/screen/4.png)</br></br>

####  `vi sshd2.service`進入編輯。
![1](https://github.com/ad8902210302/107-1-ntcu-linux/blob/master/ACS107127/screen/5.png)</br>
####  將"Type"改成"simple"，方便之後閱讀。
####  將"ExecStart"的內容改成"/usr/sbin/sshd -f /etc/ssh/sshd2_config -D $OPTIONS"。
![1](https://github.com/ad8902210302/107-1-ntcu-linux/blob/master/ACS107127/screen/6.png)</br></br>

####  使用`yum`指令，查詢需要使用的相關指令包並進行安裝。
####  <li>`yum provides semanage`</br>
![1](https://github.com/ad8902210302/107-1-ntcu-linux/blob/master/ACS107127/screen/7.png)</br>
####  <li>`yum install policycoreutils-python`</br>
![1](https://github.com/ad8902210302/107-1-ntcu-linux/blob/master/ACS107127/screen/8.png)</br></br>

####  使用`semanage`指令確認已經設定成功。
#####  <li>`semanage port -a -t ssh_port_t -p tcp 2222`</br>
#####  <li>`semanage port -l | grep ssh`</br>
![1](https://github.com/ad8902210302/107-1-ntcu-linux/blob/master/ACS107127/screen/9.png)</br></br>

####  <li>用`systemctl daemon-reload`重新讀取。
####  <li>用`systemctl start sshd2.service`開啟。
####  最後執行`netstat -alntp | grep ssh`。
![1](https://github.com/ad8902210302/107-1-ntcu-linux/blob/master/ACS107127/screen/10.png)</br></br>

完成~~~