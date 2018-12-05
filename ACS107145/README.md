## 1-1.設定 ver 變數，內容為『 my kernel version is 3.xx 』，其中 3.xx 為 uname -r 輸出的資訊，並顯示出ver變數的值。<br>
### Ans:<br>
![image](https://github.com/percy890713/107-1-ntcu-linux/blob/midterm/ACS107145/exam1-1.PNG)<br>
## 1-2.請顯示目前PATH環境變數的值為何，並說明PATH的功用為何?
### Ans:<br>
![image](https://github.com/percy890713/107-1-ntcu-linux/blob/midterm/ACS107145/exam1-2.PNG)<br>
###就是執行檔搜尋的路徑啦～目錄與目錄中間以冒號(:)分隔， 由於檔案的搜尋是依序由 PATH 的變數內的目錄來查詢，所以，目錄的順序也是重要的喔。<br>
## 2-1.有一個檔案的屬性權限為 drwxrwsr-x 3 root mail 4096 2月 16 2017 mail/，請說明此檔案的特性。<br>
### Ans:此檔名mail/,目錄檔(d).使用者(root)權限為可讀可寫可執行.並擁有SGID的特別權限.其他人為可讀可執行.檔案連結數為3,檔案容量4096,最後一次修改時間為2017/2/16<br>
## 2-2.假設有一個script.sh檔案的權限為-rw-r--r--，若希望讓所有人可以執行該檔案，請問該如何下達指令？請使用數字法與符號法各操作一次。<br>
### Ans:數字法:chmod 755 script.sh<br>  
### Ans:符號法:chmod a+x script.sh<br>
## 3-1.說明實體連結與符號連結的差異。<br>
### Ans:符號連結:一種是類似 Windows 的捷徑功能的檔案，可以讓你快速的連結到目標檔案(或目錄)； 實體連結:是透過檔案系統的 inode 連結來產生新檔名，而不是產生新檔案<br>
## 3-2.在家目錄下建立一個檔名為 hosts.real 的實體連結指到 /etc/hosts？<br>
### Ans:cd ~percy -> touch hosts.real -> ln ~percy/hosts.real /etc/hosts -> ll -i ~percy/hosts.real /etc/hosts<br>
## 3-3.在家目錄下建立一個檔名為 hosts.symbo 的符號連結指到 /etc/hosts？<br>
### Ans:cd ~percy -> touch hosts.symbo -> ln -s ~percy/hosts.symbo /etc/hosts -> ll -i ~percy/hosts.symbo /etc/hosts<br>