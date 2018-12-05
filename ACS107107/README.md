#  1.
##  Q:設定 ver 變數，內容為『 my kernel version is 3.xx 』，其中  3.xx 為 uname -r 輸出的資訊，並顯示出ver變數的值。
##  A:利用ver="my kernal version is"再利用y="uname -r"最後執行
##  ![](https://i.imgur.com/RbSfsAe.jpg)
##  Q:請顯示目前PATH環境變數的值為何，並說明PATH的功用為何? 
##  A:PATH的功能:作業系統會依照PATH環境變數中所設定的的路徑順序，依序尋找各路徑下是否有要使用的指令
#  2.
##  Q:有一個檔案的屬性權限為 drwxrwsr-x 3 root mail 4096 2月 16 2017 mail/，請說明此檔案的特性。
##  A:第一個字母d其實是目錄的意思，之後的九個字母中，前三個代表著它的owner(也就是root)可以執行的權限，之後三個代表著它的group(也就是mail)可以執行的權限，最後三個則表示著其他使用著的權限r代表可讀，w代表可寫可修改，x則代表著可執行，但是在group的執行全限不是x而是s，這代表著特殊權限SUID，執行者在執行時將會獲得group的權限。
##  Q:假設有一個script.sh檔案的權限為-rw-r--r--，若希望讓所有人可以執行該檔案，請問該如何下達指令？請使用數字法與符號法各操作一次。
##  A:數字法:chmod 777 script.sh
##  A:符號法:chmod u=rwx,g=rwx,o=rwx script.sh
#  3.
##  Q:說明實體連結與符號連結的差異。
##  A:使用實體連結設定連結檔時,磁碟空間與inode的數目都不變，但使用符號連結時由於是建立一個獨立的檔案，磁碟空間與inode的數目會改變
##  Q:在家目錄下建立一個檔名為 hosts.real 的實體連結指到 /etc/hosts？ (請用相對路徑表示家目錄)
##  A:使用ln/etc/hosts ~/hosts.real 
##  Q:在家目錄下建立一個檔名為 hosts.symbo 的符號連結指到 /etc/hosts？ (請用相對路徑表示家目錄)
##  A:使用ln/etc/hosts ~/hosts.symbo
#  4.請依下述情境完成系統操作後再用相關指令進行驗證，請抓驗證指令的圖：

##  Q:建立一個容量為1GB的xfs檔案系統，每次開機都能夠自動的掛載到 /srv/maildir，且該目錄是給 mailgroup 這個群組共用的，其他人不可具有任何權限。再建立一個名為mailuser的帳號，並加入 mailgroup 群組，且此帳號不可使用shell登入系統。
##  A:先確定有掛載到/srv/maildir
##  ![](https://i.imgur.com/8QsQteb.jpg)
##  Q:請用`df`指令配合`human-readable`選項，顯示有1GB的檔案系統正掛載到`/srv/maildir`
##  ![](https://i.imgur.com/FY4mzmU.jpg)
##  Q:請用`grep`驗證有設定開機自動掛載。
##  ![](https://i.imgur.com/IF2ra79.jpg)
##  Q:請用`ls`查詢`/srv/maildir`屬性，確認可以讓`mailgroup`群組共用，而其他人不具任何權限。
##  ![](https://i.imgur.com/orWDmYB.jpg)
##  Q:請用`id`檢查`mailuser`使用者有在`mailgroup`.
##  ![](https://i.imgur.com/uV4F56S.jpg)
##  Q:請用`grep`驗證此帳號無法透過shell登入。