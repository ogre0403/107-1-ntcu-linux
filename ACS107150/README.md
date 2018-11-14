# midterm

## 1.

### 設定 ver 變數，內容為『 my kernel version is 3.xx 』，其中 3.xx 為 uname -r 輸出的資訊，並顯示出ver變數的值。

-   ver="my kernel version is $(uname -r)"
-   echo $ver
-   顯示出值為my kernel version is 3.10.0-862.e17.x86_64

### 請顯示目前PATH環境變數的值為何，並說明PATH的功用為何?

-   用echo $PATH顯示出/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin:/root/bin
-   PATH的功能是用PATH變數內的目錄查詢執行檔搜尋的路徑

## 2.

### 有一個檔案的屬性權限為 drwxrwsr-x 3 root mail 4096 2月 16 2017 mail/，請說明此檔案的特性。

-   drwxrwsr-x代表後面的檔名是目錄檔,user擁有權限是rwx,group擁有的權限也是rwx,但other在執行時因具備x的權限,經SGID後身分轉成group,權限也變成rwx
-   3是檔案連結數
-   root是檔案擁有者
-   mail是檔案所屬群組
-   4096是檔案容量
-   2月 16 2017是檔案最後一次被修改的日期時間
-   mail/是檔名

### 假設有一個script.sh檔案的權限為-rw-r--r--，若希望讓所有人可以執行該檔案，請問該如何下達指令？請使用數字法與符號法各操作一次。

-   數字法:chmod 755 script.sh
-   符號法:chmod a+x script.sh

## 3.

### 說明實體連結與符號連結的差異。

-   使用hard link時,磁碟空間和inode數目都部會改變
-   使用symbolic link時,會建立一個獨立的檔案並占用inode和block

### 在家目錄下建立一個檔名為 hosts.real 的實體連結指到 /etc/hosts？ (請用相對路徑表示家目錄) 

-   ln /etc/hosts ~/hosts.real

### 在家目錄下建立一個檔名為 hosts.symbo 的符號連結指到 /etc/hosts？ (請用相對路徑表示家目錄)

-   ln -s /etc/hosts ~/hosts.symbo

## 4.

### 建立一個容量為1GB的xfs檔案系統，每次開機都能夠自動的掛載到 /srv/maildir，且該目錄是給 mailgroup 這個群組共用的，其他人不可具有任何權限。再建立一個名為mailuser的帳號，並加入 mailgroup 群組，且此帳號不可使用shell登入系統。


#### 請用`df`指令配合`human-readable`選項，顯示有1GB的檔案系統正掛載到`/srv/maildir`

> ![github]()

#### 請用`grep`驗證有設定開機自動掛載。

> ![github]()

#### 請用`ls`查詢`/srv/maildir`屬性，確認可以讓`mailgroup`群組共用，而其他人不具任何權限。

> ![github]()

#### 請用`id`檢查`mailuser`使用者有在`mailgroup`.

> ![github]()

#### 請用`grep`驗證此帳號無法透過shell登入。




