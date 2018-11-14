#設定 ver 變數，內容為『 my kernel version is 3.xx 』，其中 3.xx 為 uname -r 輸出的資訊，並顯示出ver變數的值。

  *uname -r→ver='my kernel version is 3.10'→echo $ver

#請顯示目前PATH環境變數的值為何，並說明PATH的功用為何?

  *顯示:附圖，功用:是讓我們去存取裝在變數裡面的資料，系統會照著PATH中所設定的路徑順序，尋找是否有要用的指令

#有一個檔案的屬性權限為 drwxrwsr-x 3 root mail 4096 2月 16 2017 mail/，請說明此檔案的特性。

  *它是一個檔案，擁有者的權限為可讀可寫可執行，群組的權限為可讀可寫且執行者在執行的過程中將獲得該程式群組的權限，擁有者為root，群組為mail，檔案容量為4096，檔案最後一次被修改的時間為2017年2月16日，檔名較mail/

#假設有一個script.sh檔案的權限為-rw-r--r--，若希望讓所有人可以執行該檔案，請問該如何下達指令？請使用數字法與符號法各操作一次。
  
##數字法

  *chmod 755 script.sh即可修改

##符號法

  *chmod u=rwx,g=r-x,o=r-x script.sh即可修改

#說明實體連結與符號連結的差異。

##差異

  *使用這個指令設定連結檔時，磁碟的空間與inode數目不會改變，只是在目錄裡面增加一筆inode與檔名的對應，但符號連結是在建立一個獨立的檔案，這個檔案會指向目的檔案，當資料讀取時，會指向他link的那個檔案名稱，因為他是獨立建立的檔案，所以會占用inode跟block

#在家目錄下建立一個檔名為 hosts.real 的實體連結指到 /etc/hosts？ (請用相對路徑表示家目錄) 

  *ln /etc/hosts ~/hosts.real→ll -i /etc/hosts ~/hosts.real

#在家目錄下建立一個檔名為 hosts.symbo 的符號連結指到 /etc/hosts？ (請用相對路徑表示家目錄 

  *ln -s /etc/hosts ~/hosts.symbo→ll -i /etc/hosts ~/hosts.symbo

#建立一個容量為1GB的xfs檔案系統，每次開機都能夠自動的掛載到 /srv/maildir，且該目錄是給 mailgroup 這個群組共用的，其他人不可具有任何權限。再建立一個名為mailuser的帳號，並加入 mailgroup 群組，且此帳號不可使用shell登入系統。

  *請用`df`指令配合`human-readable`選項，顯示有1GB的檔案系統正掛載到`/srv/maildir`

  *附圖

  *請用`grep`驗證有設定開機自動掛載。

  *附圖

  *請用`ls`查詢`/srv/maildir`屬性，確認可以讓`mailgroup`群組共用，而其他人不具任何權限。

  *附圖

  *請用`id`檢查`mailuser`使用者有在`mailgroup`. 

  *附圖
   
   我的mailuser1=mailuser

  *請用`grep`驗證此帳號無法透過shell登入。

  *附圖