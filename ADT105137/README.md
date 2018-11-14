# ADT105137_周柏諭_1114期中考
1-1. 設定 ver 變數，內容為『 my kernel version is 3.xx 』，其中 3.xx 為 uname -r 輸出的資訊，並顯示出ver變數的值。(10%)
![image](https://github.com/Yubo0826/1114/blob/master/1-1-1.PNG)
![image](https://github.com/Yubo0826/1114/blob/master/1-1-2.PNG)

1-2. 請顯示目前PATH環境變數的值為何，並說明PATH的功用為何? (10%)
![image](https://github.com/Yubo0826/1114/blob/master/1-2.PNG)

A: 依照PATH環境變數中所設定的路徑順序，依序尋找個路徑下是否有要使用的指令。

2-1. 有一個檔案的屬性權限為 drwxrwsr-x 3 root mail 4096 2月 16 2017 mail/，請說明此檔案的特性。(10%)

A: d代表是這個檔案是目錄檔，owner、group使用者擁有所有權限，others使用者只有讀和執行的權限，沒有寫入的權限，與這個檔案連接的檔案有三個，
檔案擁有者是root，檔案所屬群組是mail，4096是該檔案的容量，檔案最後修改日期為2017/2/16，最後mail/是該檔案的檔名。

2-2. 假設有一個script.sh檔案的權限為-rw-r--r--，若希望讓所有人可以執行該檔案，請問該如何下達指令？請使用數字法與符號法各操作一次。(10%)

A: 數字法: chmod 777 script.sh
   符號法: chomd u=rwx,g=rwx,o=rwx script.sh
   
3-1. 說明實體連結與符號連結的差異。(10%)

A: 1.使用實體連結時，inode和磁碟空間不會改變，而符號連結因為會建立一個獨立的檔案，所以會占用到磁碟空間，然後inode會不同。

   2.實體連結link目錄會有問題
   
3-2. 在家目錄下建立一個檔名為 hosts.real 的實體連結指到 /etc/hosts？ (請用相對路徑表示家目錄) (5%)
![image](https://github.com/Yubo0826/1114/blob/master/3-2.PNG)

3-3. 在家目錄下建立一個檔名為 hosts.symbo 的符號連結指到 /etc/hosts？ (請用相對路徑表示家目錄 (5%)
![image](https://github.com/Yubo0826/1114/blob/master/3-3.PNG)

4-1. 請用`df`指令配合`human-readable`選項，顯示有1GB的檔案系統正掛載到`/srv/maildir` (8%)
![image](https://github.com/Yubo0826/1114/blob/master/4-1.PNG)

4-2. 請用`grep`驗證有設定開機自動掛載。(8%)
![image](https://github.com/Yubo0826/1114/blob/master/4-2.PNG)

4-3.請用`ls`查詢`/srv/maildir`屬性，確認可以讓`mailgroup`群組共用，而其他人不具任何權限。(8%)
![image](https://github.com/Yubo0826/1114/blob/master/4-3.PNG)

4-4.請用`id`檢查`mailuser`使用者有在`mailgroup`. (8%)
![image](https://github.com/Yubo0826/1114/blob/master/4-4.PNG)

4-5.請用`grep`驗證此帳號無法透過shell登入。(8%)
![image](https://github.com/Yubo0826/1114/blob/master/4-5.PNG)
