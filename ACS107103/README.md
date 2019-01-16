﻿<strong>第一大題</strong>

<em>1.<em>
+ 先執行cd /etc/ssh切換到設定檔所在目錄
+ 再執行cp ./sshd_config ./sshd_config2222
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-10/ACS107103/centos-2019-01-08-20-29-43.png)
+ 之後執行vi sshd_config2222編輯內容(注意要去掉井字號)
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-10/ACS107103/centos-2019-01-08-20-30-57.png)
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-10/ACS107103/centos-2019-01-08-20-32-16.png)
+ 再來執行cd /usr/lib/systemd/system切換到啟動腳本的所在目錄
+ 然後執行cp ./sshd.service ./sshd2222.service
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-10/ACS107103/centos-2019-01-08-20-36-03.png)
+ 之後執行vi sshd2222.service編輯內容
+ (加上-f /etc/ssh/sshd_config2222)
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-10/ACS107103/centos-2019-01-08-20-36-38.png)
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-10/ACS107103/centos-2019-01-08-20-42-53.png)
+ 接著執行semanage port -a -t ssh_port_t -p tcp 2222開放2222port通行
+ (如果系統沒有該指令，請執行yum install policycoreutils-python安裝相關套件)
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-10/ACS107103/centos-2019-01-08-21-01-28.png)
+ 緊接著再執行systemctl start sshd2222來啟動另外一個ssh
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-10/ACS107103/centos-2019-01-08-21-07-23.png)
+ 最後記得要執行systemctl stop firewalld關閉防火牆
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-10/ACS107103/centos-2019-01-08-21-17-46.png)
