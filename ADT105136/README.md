1.\\ver="my kernel version is $(uname -r)"\\
  \\echo $ver\\

\\echo $PATH\\的結果是/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
而變數PATH的主要功能是會在這些路徑中依序(/usr/local/sbin開始)尋找使用者要執行的程式名稱，若全部都沒有找到則回傳command not found

2.drwxrwsr-x 3 root mail 4096 2月 16 2017 mail/ 可以知道這是一個目錄，權限為775，連結3個檔案，擁有者為root，群組為mail，檔案大小4096，2017/2/16時建立，檔案名稱為mail/

\chmod +x script.sh  or  \chmod 755 script.sh
3.實體連結(hard link)類似於備份，inode和block相同，檔案連結數+1，而符號連結(symbolic link)則類似於捷徑，使用不同的inode和block，儲存連結的檔名，原本檔案連結數不會增加

\\ln /etc/hosts ~/hosts.real
\\ln -s /etc/hosts ~/hosts.symbo
4.
![image](https://github.com/boolenboom/107-1-ntcu-linux/blob/midterm/ADT105136/001.PNG)
![image](https://github.com/boolenboom/107-1-ntcu-linux/blob/midterm/ADT105136/002.PNG)
![image](https://github.com/boolenboom/107-1-ntcu-linux/blob/midterm/ADT105136/003.PNG)
![image](https://github.com/boolenboom/107-1-ntcu-linux/blob/midterm/ADT105136/004.PNG)
![image](https://github.com/boolenboom/107-1-ntcu-linux/blob/midterm/ADT105136/005.PNG)
