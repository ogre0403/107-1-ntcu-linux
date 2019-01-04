1.先在相同目錄下(/etc/vsftpd/)複製新的ftp設定檔

![image](https://github.com/boolenboom/107-1-ntcu-linux/blob/HW-10/ADT105136/01.png)

2.修改新的設定檔，將聆聽的端口設定成2222

![image](https://github.com/boolenboom/107-1-ntcu-linux/blob/HW-10/ADT105136/02.png)

3.再去/etc/systemd/system/複製新的vsftpd的Service檔

![image](https://github.com/boolenboom/107-1-ntcu-linux/blob/HW-10/ADT105136/03.png)

4.修改檔案內容，讓它讀到先前修改的vsftpd2.conf

![image](https://github.com/boolenboom/107-1-ntcu-linux/blob/HW-10/ADT105136/04.png)

5.用systemctl將服務檔重新讀取，並確認修改的檔案是否有被抓到

![image](https://github.com/boolenboom/107-1-ntcu-linux/blob/HW-10/ADT105136/05.png)

6.將服務開啟運行

![image](https://github.com/boolenboom/107-1-ntcu-linux/blob/HW-10/ADT105136/06.png)

7.再用netstat -alntp確認端口是否有被正確設定

![image](https://github.com/boolenboom/107-1-ntcu-linux/blob/HW-10/ADT105136/07.png)
