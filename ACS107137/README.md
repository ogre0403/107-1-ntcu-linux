## 請仿照課堂上練習，透過systemd管理二個sshd服務，並讓第二個sshd服務的 port 放行於 2222。完成後可以使用指令 netstat -alntp | grep ssh 確認是否啟動二個sshd服務，範例如下：
```
$ netstat -alntp | grep ssh
tcp        0      0 0.0.0.0:22     0.0.0.0:*     LISTEN      1300/sshd
tcp        0      0 0.0.0.0:2222   0.0.0.0:*     LISTEN      15275/sshd
tcp6       0      0 :::22          :::*          LISTEN      1300/sshd
tcp6       0      0 :::2222        :::*          LISTEN      15275/sshd
```
```
Note 1: CentOS有使用SELinux ，故預設只允許 SSH 使用埠號 22，若要使用埠號 2222，使請用下列指開啟並檢查


$ semanage port -a -t ssh_port_t -p tcp 2222
$ semanage port -l | grep ssh
ssh_port_t tcp 2202, 22


Note 2: CentOS預設的防火牆firewalld會禁止訪問埠號2222，若要透過2222埠連ssh，請先關閉firewalld。
```

### Ans:
```
cd /etc/ssh
cp sshd_config sshd2_config (將sshd_config的內容複製到sshd2_config)
```
![image](https://github.com/bill0330/107-1-ntcu-linux/blob/HW-10/ACS107137/img/1.PNG?raw=true)


```
vi sshd2_config (編輯sshd2_config)
將 (Port 22) 改為 (Port 2222)
```
![image](https://github.com/bill0330/107-1-ntcu-linux/blob/HW-10/ACS107137/img/2.PNG?raw=true)
![image](https://github.com/bill0330/107-1-ntcu-linux/blob/HW-10/ACS107137/img/3.PNG?raw=true)

```
cd /etc/systemd/system
cp /usr/lib/systemd/system/sshd.service sshd2.service (將sshd.service的內容複製到sshd2.service)
```
![image](https://github.com/bill0330/107-1-ntcu-linux/blob/HW-10/ACS107137/img/4.PNG?raw=true)

```
vi sshd2.service (編輯sshd2.service)
將 "Type" 改成 simple (原為notify)
將 "ExecStart" 的內容改成 /usr/sbin/sshd -f /etc/ssh/sshd2_config -D $OPTIONS
```
![image](https://github.com/bill0330/107-1-ntcu-linux/blob/HW-10/ACS107137/img/5.PNG?raw=true)
![image](https://github.com/bill0330/107-1-ntcu-linux/blob/HW-10/ACS107137/img/6.PNG?raw=true)

```
yum install policycoreutils-python (完成後就能使用 semanage 了)
```
![image](https://github.com/bill0330/107-1-ntcu-linux/blob/HW-10/ACS107137/img/7.PNG?raw=true)
![image](https://github.com/bill0330/107-1-ntcu-linux/blob/HW-10/ACS107137/img/8.PNG?raw=true)

```
semanage port -a -t ssh_port_t -p tcp 2222
semanage port -l | grep ssh
```
![image](https://github.com/bill0330/107-1-ntcu-linux/blob/HW-10/ACS107137/img/9.PNG?raw=true)

```
systemctl daemon-reload (重新讀取設定檔)
systemctl start sshd2.service (開啟 sshd2.service 之服務)
netstat -alntp | grep ssh
```
![image](https://github.com/bill0330/107-1-ntcu-linux/blob/HW-10/ACS107137/img/10.PNG?raw=true)