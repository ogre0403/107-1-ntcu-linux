# 1.
## 設定 ver 變數，內容為『 my kernel version is 3.xx 』，其中 3.xx 為 uname -r 輸出的資訊，並顯示出ver變數的值。
### export ver="my kernel version is 3.10.0-862.e17.x86_64"
### echo $ver
### my kernel version is 3.10.0-862.e17.x86_64
## 請顯示目前PATH環境變數的值為何，並說明PATH的功用為何?
### echo $PATH
### 在執行一個指令的時候，系統會依照PATH的設定去每個PATH定義的路徑下搜尋檔案，先搜尋到的指令檔案先被執行。
# 2.
## 有一個檔案的屬性權限為 drwxrwsr-x 3 root mail 4096 2月 16 2017 mail/，請說明此檔案的特性。
### 此檔案擁有者及群組成員權限皆為可讀可寫可執行，而其他人只能讀跟執行。
## 假設有一個script.sh檔案的權限為-rw-r--r--，若希望讓所有人可以執行該檔案，請問該如何下達指令？請使用數字法與符號法各操作一次。
### chmod 777 /script.sh
### chmod a=rwx /script.sh
# 3.
## 說明實體連結與符號連結的差異。
### 實體連結是以多個檔案對應到同一個inode的方式建立的連結，而符號連結會占用另一個inode跟空間。
## 在家目錄下建立一個檔名為 hosts.real 的實體連結指到 /etc/hosts？ (請用相對路徑表示家目錄)
### ln ./etc/hosts /hosts.real
## 在家目錄下建立一個檔名為 hosts.symbo 的符號連結指到 /etc/hosts？ (請用相對路徑表示家目錄)
### ln ./etc/hosts /hosts.symbo
# 4.請依下述情境完成系統操作後再用相關指令進行驗證，請抓驗證指令的圖：
    建立一個容量為1GB的xfs檔案系統，每次開機都能夠自動的掛載到 /srv/maildir，且該目錄是給 mailgroup 這個群組共用的，其他人不可具有任何權限。再建立一個名為mailuser的帳號，並加入 mailgroup 群組，且此帳號不可使用shell登入系統。
### 