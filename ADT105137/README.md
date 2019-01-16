# ADT105137_final
1.設定virtualbox虛擬機器，加入一張host-only網路卡，在Linux裡設定虛擬機器的網路為192.168.200.100/24。請用 `ifconfig`驗證。(25%)

A:使用ifconfig修改網路ip。

![image](https://github.com/Yubo0826/0116/blob/master/1-2.PNG)

2.nginx是一套網頁伺服器軟體，請用`yum`安裝，透過`systemctl`啟動後，使用`netstat`驗證nginx有在使用Port 80。(25%)

A: 首先先建立檔案 /etc/yum.repos.d/nginx.repo，在檔案內加入下方圖片文字，就可以用yum來安裝nginx囉。

![image](https://github.com/Yubo0826/0116/blob/master/2-1.PNG)

安裝完畫面長下方這樣。

![image](https://github.com/Yubo0826/0116/blob/master/2-2.PNG)

接著啟用nginx的service。

![image](https://github.com/Yubo0826/0116/blob/master/2-3.PNG)

接著netstat -alntp 看nginx service使用到哪個port，就可以看出使用的port是80。

![image](https://github.com/Yubo0826/0116/blob/master/2-4.PNG)

3.透過實體 windows 上的瀏覽器，連線至192.168.200.100。抓�圖驗證可以連線至Linux上的nginx網頁伺服器。(10%)

![image](https://github.com/Yubo0826/0116/blob/master/3.PNG)

4.在Linux裡，用`curl`連線至192.168.200.100。抓�圖驗證可以連線至Linux上的nginx網頁伺服器。(10%)

![image](https://github.com/Yubo0826/0116/blob/master/4.PNG)

5.請使用管線指令，找出每個ip連線錯誤的次數。

這題可能我連線都成功，在error.log裡沒有資料，在access.log是紀錄檔案有成功連線的資料

![image](https://github.com/Yubo0826/0116/blob/master/5-1.PNG)

使用grep -i -o -E "([0-9]{1,3}\.){3}[0-9]{1,3}" test1.txt | sort -n | uniq -c | sort -n -r | head -6 ，找出各個ip連線成功的次數。

![image](https://github.com/Yubo0826/0116/blob/master/5.PNG)
