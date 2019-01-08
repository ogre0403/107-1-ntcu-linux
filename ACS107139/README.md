#1.
關閉firewalld
![Imgur](https://i.imgur.com/zZCVAOd.png)
systemctl start sshd啟動sshd <br>
cd /etc切換到檔案etc<br>
ll | grep ssh確認etc裡面有ssh<br>
![Imgur](https://i.imgur.com/NgKNDPF.png)
cd /etc/ssh再到ssh裡面
![Imgur](https://i.imgur.com/OXIBnHI.png)
cp sshd_config sshd2_config將sshd，sshd2複製進去 
![Imgur](https://i.imgur.com/wyCqfAz.png)
vi sshd2_config，把port從22改成2222
![Imgur](https://i.imgur.com/VFakOWm.png)
yum provides semessage找到下載指令
![Imgur](https://i.imgur.com/HlYqXTE.png)
yum install policycoreutils-python安裝
![Imgur](https://i.imgur.com/RMzQiQf.png)
cp /usr/lib/systemd/system/sshd.service sshd2.service複製<br>
然後不知道為什麼sshd2不行所以我就用sshd做實驗了<br>
vi sshd.service將daemon後面加2，notify改simple
![Imgur](https://i.imgur.com/VZQ8vCp.png)
systemctl start sshd.service啟動
![Imgur](https://i.imgur.com/POwOBqg.png)
systemctl daemon-reload重啟資料
systemctl start sshd.service再啟動
![Imgur](https://i.imgur.com/cqNmqBk.png)
netstat -alntp | grep ssh確認是否啟動二個sshd服務
[Imgur](https://i.imgur.com/8u4QEZ6.png)