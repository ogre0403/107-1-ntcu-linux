## HW10
#### 請仿照課堂上練習，透過systemd管理二個sshd服務，並讓第二個sshd服務的 port 放行於 2222。完成後可以使用指令 netstat -alntp | grep ssh 確認是否啟動二個sshd服務。

+ systemctl status sshd ，查看sshd的狀態
![GITHUB]( https://imgur.com/55E9tRz.jpg"git圖示")

+ 切換到目錄cd /etc/ssh。複製檔案，cp sshd_config sshd2_config。
![GITHUB]( https://imgur.com/FgH0M4P.jpg"git圖示")

+ 更改內容，Port=22 -> Port=2222，vi sshd2_config 。
![GITHUB]( https://imgur.com/vgpVFMo.jpg"git圖示")

+ 切換到目錄cd /etc/systemd/system 。複製檔案，cp /usr/lib/systemd/system/sshd.service sshd2.service。
![GITHUB]( https://imgur.com/3BuEEwA.jpg"git圖示")

+ 更改內容，vi sshd2.service。
![GITHUB]( https://imgur.com/SZfm1oc.jpg"git圖示")

+ 開啟工具，yum provides semanage。
![GITHUB]( https://imgur.com/UAUta9G.jpg"git圖示")

+ 安裝policycoreutils-python，yum install policycoreutils-python。
![GITHUB]( https://imgur.com/uHeJjPE.jpg"git圖示")
![GITHUB]( https://imgur.com/2SJvF4D.jpg"git圖示")

+ semanage port -a -t ssh_port_t -p tcp 2222修正。semanage port -l | grep ssh查看。
![GITHUB]( https://imgur.com/VMSDAx3.jpg"git圖示")

+ systemctl daemon-reload，讓其重新讀取，啟動sshd2_service，systemctl start sshd2.service。
![GITHUB]( https://imgur.com/Y92l5Ub.jpg"git圖示")

+ netstat -alntp | grep ssh，查看結果。
