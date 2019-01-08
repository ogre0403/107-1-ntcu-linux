# HW10
## ADT104138 羅苡倫
*****
## 一、請仿照課堂上練習，透過systemd管理二個sshd服務，並讓第二個sshd服務的 port 放行於 2222。完成後可以使用指令 netstat -alntp | grep ssh 確認是否啟動二個sshd服務，範例如下：
```
$ netstat -alntp | grep ssh
tcp        0      0 0.0.0.0:22     0.0.0.0:*     LISTEN      1300/sshd
tcp        0      0 0.0.0.0:2222   0.0.0.0:*     LISTEN      15275/sshd
tcp6       0      0 :::22          :::*          LISTEN      1300/sshd
tcp6       0      0 :::2222        :::*          LISTEN      15275/sshd
```

首先，要複製出第二個sshd的資料，所以使用指令cp把sshd複製到一個新的sshd2裡面，然後再使用vi指令，把port編輯成2222。</br>
![新增](https://i.imgur.com/0Np0LsN.jpg)</br>
![新增](https://i.imgur.com/yPWZve8.jpg)</br>
![新增](https://i.imgur.com/ugyGucc.jpg)</br>

完成後再去system資料夾內，複製sshd.service給sshd2.service，並把裡面的資料編輯成給sshd2能使用的，以辨識出來。</br>
![新增](https://i.imgur.com/vj1riC2.jpg)</br>
![新增](https://i.imgur.com/l5HwRYc.jpg)</br>

最後利用systemd的指令systemctl進行重啟的動作，再利用semanage port -a -t ssh_port_t -p tcp 2222指令定義port2222，檢查過後發現成功完成題目需求。</br>
![新增](https://i.imgur.com/4RksOZK.jpg)</br>
![新增](https://i.imgur.com/Nid4bbE.jpg)</br>

P.S Centos迷你版安裝並沒有安裝SE指令，要解決安裝其他套件即可。
![新增](https://i.imgur.com/HkgAB5J.jpg)</br>

# 參考資料：
[點擊這裡](http://linux.vbird.org/linux_basic/0560daemons.php "參考資料1")</br>
[點擊這裡](https://www.opencli.com/linux/fix-semanage-command-not-found "參考資料2")</br>
# 感謝觀看 The End
