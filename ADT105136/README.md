經歷了千辛萬苦，總算是成功了...


1.首先用systmectl觀察sshd的狀態

![image](https://github.com/boolenboom/107-1-ntcu-linux/blob/HW-10/ADT105136/010.png)

2.用locate查找sshd的相關檔案，跟設定相關的有兩個，先去看/etc/ssh/sshd_config

![image](https://github.com/boolenboom/107-1-ntcu-linux/blob/HW-10/ADT105136/011.png)

3.可以看到檔案中的#port 22，複製新的檔案後將#去除，並將數字改成2222

![image](https://github.com/boolenboom/107-1-ntcu-linux/blob/HW-10/ADT105136/012.png)

4.接下來到/etc/systemd/system/下，把/usr/lib/systemd/system/sshd.service複製到此，此處的檔案可以放修改過的系統服務檔

![image](https://github.com/boolenboom/107-1-ntcu-linux/blob/HW-10/ADT105136/020.png)

5.並將新複製的檔案修改，重要的ExecStart增加參數和剛剛新增的sshd的設定檔

![image](https://github.com/boolenboom/107-1-ntcu-linux/blob/HW-10/ADT105136/021.png)

![image](https://github.com/boolenboom/107-1-ntcu-linux/blob/HW-10/ADT105136/022.png)

6.使用systemctl daemon-reload後再使用systemctl start sshd2後，會發現無法順利開啟

![image](https://github.com/boolenboom/107-1-ntcu-linux/blob/HW-10/ADT105136/030.png)

![image](https://github.com/boolenboom/107-1-ntcu-linux/blob/HW-10/ADT105136/031.png)

![image](https://github.com/boolenboom/107-1-ntcu-linux/blob/HW-10/ADT105136/032.png)

7.上網搜尋會發現SELinux只允許ssh的端口是22，用semanage(如果沒有必須要用yum安裝，且需要特殊設定https://n.sfs.tw/content/index/11039  )設定

![image](https://github.com/boolenboom/107-1-ntcu-linux/blob/HW-10/ADT105136/040.png)

8.最後再重新運行一次，就完成了！

![image](https://github.com/boolenboom/107-1-ntcu-linux/blob/HW-10/ADT105136/050.png)
