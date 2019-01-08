#  請仿照課堂上練習，透過systemd管理二個sshd服務，並讓第二個sshd服務的port放行於2222。完成後可以使用指令netstat -alntp | grep ssh確認是否啟動二個sshd服務
##  先到ssh的目錄下複製ssh_config到ssh2_config
##  ![](https://i.imgur.com/UKF1rNg.jpg)
##  在vim sshd2_config中任一處加上Port 2222
##  再將sshd.service的部分複製到sshd2.service
##  ![](https://i.imgur.com/XdFueXX.jpg)
##  利用vim sshd2.service修改ExecStart=/usr/sbin/sshd -f /etc/ssh/sshd2_config -D $OPTIONS
##  ![](https://i.imgur.com/d0EFwAz.jpg)
##  再來就是使用semanage指令了!!但是command not found，所以我們就要利用yum來裝好它，但他又說找不到package，所以就要利用yum provides semanage來找尋所需的安裝包了
##  ![](https://i.imgur.com/uq2KAJp.jpg)
##  ![](https://i.imgur.com/81nU8VQ.jpg)
##  ![](https://i.imgur.com/LDePdhs.png)
##  最後用netstat -alntp | grep ssh確認，但又command not found 了，之後用yum install net-tools安裝
##  ![](https://i.imgur.com/rK6VEmG.jpg)