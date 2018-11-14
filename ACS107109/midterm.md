# 期中考上機題目


-----------------------------------------------------
## 第一題
* 設定 ver 變數，內容為『 my kernel version is 3.xx 』，其中 3.xx 為 uname -r 輸出的資訊，並顯示出ver變數的值。(10%)


  1/. ver="my kernel version is 3.xx"
  2/. echo $ver顯示出ver變數的值
> my kernel version is 3.xx

  3. ver="my kernel version is 3.xx" uname -r
> 3.10.0-862.e17.x86_64


![image](https://github.com/YANGshujun1110/107-1-ntcu-linux/blob/midterm/ACS107109/001.PNG)


* 請顯示目前PATH環境變數的值為何，並說明PATH的功用為何? (10%)

  1. /usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin:/root/bin
  2. PATH的功用:
    * 作業系統會依照PATH環境變數中所設定的路徑順序，依序尋找個路徑下是否有藥使用的指令。
    * 若找不到，就會顯示command not found。
    * 偌多個目錄下都有指令，以優先找的為主。  


![image](https://github.com/YANGshujun1110/107-1-ntcu-linux/blob/midterm/ACS107109/002.PNG)

-----------------------------------------------------
## 第二題
* 有一個檔案的屬性權限為 drwxrwsr-x 3 root mail 4096 2月 16 2017 mail/，請說明此檔案的特性。(10%)


為檔案mail，權限:rwx` (user可讀可寫可執行) ` rws` (group可讀可寫可執行，且為SGID的權限，執行者可暫時擁有該程式mail群組的權限) ` r-x` (other可讀可執行) `，user為root，group為mail，容量為4096，最後更改日期為2017/02/16。


* 假設有一個script.sh檔案的權限為-rw-r--r--，若希望讓所有人可以執行該檔案，請問該如何下達指令？請使用數字法與符號法各操作一次。(10%)


  * 數字法:chmod 755 script.sh
  * 符號法:chmod u=rwx,g=r-x,o=r-x script.sh

-----------------------------------------------------
## 第三題
* 說明實體連結與符號連結的差異。(10%)

  1. 實體連結:建立的每個檔案會占用一個inode，檔案內容有inode的紀錄來指向；符號連結:所建立的檔案為一個獨立的新的檔案，會占用一個inode和block。
  2. 實體連結:將任何一個**檔名**刪除，inode和block都還是存在；符號連結:目的檔案被刪除後，因為找不到原始檔名，所以link會變成死link，而無法開啟檔案。
  3. 實體連結:限制較多；符號連結:限制較少，一般常使用。
  4. 實體連結:若想要讀取該檔案，必須要經過目錄紀錄的檔名來指向正確的inode號碼才能讀取；符號連結:為一個獨立的檔案，這個獨立的檔案會指向目的檔案，當資料讀取時，會指向他link的那個檔案的檔名。


* 在家目錄下建立一個檔名為 hosts.real 的實體連結指到 /etc/hosts？ (請用相對路徑表示家目錄) (5%)

  1. ` ln /home/hosts.real /etc/hosts `:建立實體連結。
  2. 相對路徑:/home/hosts.real cd ../etc/hosts

* 在家目錄下建立一個檔名為 hosts.symbo 的符號連結指到 /etc/hosts？ (請用相對路徑表示家目錄 (5%)

  1. ` ln -s /home/hosts.symbo /etc/hosts `:建立符號連結。(/etc/hosts -> /home/hosts.symbo)
  2. 相對路徑:/home/etc/hosts cd ../home/hosts.symbo


-----------------------------------------------------
## 第四題


請依下述情境完成系統操作後再用相關指令進行驗證，請抓驗證指令的圖：


建立一個容量為1GB的xfs檔案系統，每次開機都能夠自動的掛載到 /srv/maildir，且該目錄是給 mailgroup 這個群組共用的，其他人不可具有任何權限。再建立一個名為mailuser的帳號，並加入 mailgroup 群組，且此帳號不可使用shell登入系統。


![image](https://github.com/YANGshujun1110/107-1-ntcu-linux/blob/midterm/ACS107109/003.PNG)
![image](https://github.com/YANGshujun1110/107-1-ntcu-linux/blob/midterm/ACS107109/004.PNG)
![image](https://github.com/YANGshujun1110/107-1-ntcu-linux/blob/midterm/ACS107109/005.PNG)
![image](https://github.com/YANGshujun1110/107-1-ntcu-linux/blob/midterm/ACS107109/006.PNG)
![image](https://github.com/YANGshujun1110/107-1-ntcu-linux/blob/midterm/ACS107109/007.PNG)
![image](https://github.com/YANGshujun1110/107-1-ntcu-linux/blob/midterm/ACS107109/008.PNG)
