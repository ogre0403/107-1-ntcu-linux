## HW10
#### 請仿照課堂上練習，透過systemd管理二個sshd服務，並讓第二個sshd服務的 port 放行於 2222。完成後可以使用指令 netstat -alntp | grep ssh 確認是否啟動二個sshd服務

* 先使用`cd /etc/ssh/`進入資料夾，再使用`cp sshd_config sshd2_config`複製檔案

![](https://i.imgur.com/BY7ymbf.jpg)

* 使`vi sshd2_config`進入編輯模式，將內容**port22**改為**Port 2222**
![](https://i.imgur.com/bS3UWFK.jpg)

* 接著輸入`cd /usr/lib/systemd/system`找到**sshd.service**
![](https://i.imgur.com/wX3yI7Y.png)

* 並將其複製到`/etc/systemd/system`
![](https://i.imgur.com/xVksodq.png)

* 接者使用`vi`編輯該檔案
![](https://i.imgur.com/uNSSmID.jpg)

* 因為最後使用的指令需要安裝一修配件，故在這裡要先輸入`yum provides semanage`u以及`yum install policycoreutils-python`
![](https://i.imgur.com/5rxA7Up.png)

* 最後使用`systemctl stop firewalld.service`關閉防火牆，再輸入`systemctl daemon-reload`，以及`systemctl start sshd2`，最後的最後使用`netstat -alntp | grep ssh`檢查是否成功

![](https://i.imgur.com/hbxNT66.png)


![](https://i.imgur.com/UgkxV5l.jpg)