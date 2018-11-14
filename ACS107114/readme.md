## 第一題
### 1.設定 ver 變數，內容為『 my kernel version is 3.xx 』，其中 3.xx 為 uname -r 輸出的資訊，並顯示出ver變數的值。
* Ans:  
* 1.使用```uname -r```找出版本為**3.10.0-862.el7.x86_64**
* 2.使用```ver="my kernel version is 3.10"```
* 3.使用```echo $ver```印出變數值 即完成

### 2.請顯示目前PATH環境變數的值為何，並說明PATH的功用為何?
* Ans:
* 1.使用```echo $PATH```顯示出目前環境變數的值為 **usr/local/bin:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/home/kenny/.local/bin:/home/kenny/bin**

* 2.Path環境變數是作業系統外部「命令」搜索路徑 當使用者輸入一指令時 作業系統會至Path中找尋條列其中的路徑 並在資料夾中尋找符合其命令需求的檔案 最終得以啟動並執行。




## 第二題
### 1.有一個檔案的屬性權限為 `drwxrwsr-x  3 root mail   4096  2月 16  2017 mail/`，請說明此檔案的特性。
* Ans:
* 1.一開頭**d**表示此檔案為目錄，而後**rwxrwsr-x**則代表 
* 這個檔案擁有者**root**擁有全部的權限
* 此檔案所存在群組的使用者因為權限為**rws** 具有SGID關係 代表如果群組使用者的權限具有**x**的話 群組使用者則可以進入此目錄 其餘權限則與檔案擁有者一樣
* 而其他人因權限為**r-x** 代表可以讀取並執行此檔案 。

### 2.假設有一個script.sh檔案的權限為-rw-r--r--，若希望讓所有人可以執行該檔案，請問該如何下達指令？請使用數字法與符號法各操作一次。
* Ans:
* 1.**數字法**；使用```chmod 770 script.sh```即可完成
* 2.**符號法**；使用```chmod a=rwx script.sh```即可完成


## 第三題
### 1.說明實體連結與符號連結的差異。
* Ans:
* 1.**實體連結**是在某個目錄下新增一筆檔名連結到 inode 號碼的關連記錄，而**符號連結**就是在建立一個獨立的檔案，而這個檔案會讓資料的讀取指向連結的那個檔案的檔名，類似**捷徑**的概念。
### 2.在家目錄下建立一個檔名為 hosts.real 的實體連結指到 /etc/hosts？ (請用相對路徑表示家目錄)
* Ans:使用 ```cd ~``` 切換到目前使用者的家目錄 再使用 **ln** 指令來建立實體連結```ln /etc/hosts hosts.real``` 即完成
### 3.在家目錄下建立一個檔名為 hosts.symbo 的符號連結指到 /etc/hosts？ (請用相對路徑表示家目錄)
* Ans:使用 ```cd ~``` 切換到目前使用者的家目錄 再使用 **ln -s** 指令來建立符號連結  ```ln -s /etc/hosts hosts.symbo``` 即完成


## 第四題
### 1.請用`df`指令配合`human-readable`選項，顯示有1GB的檔案系統正掛載到`/srv/maildir`
![](https://i.imgur.com/B1bWknZ.png)
### 2. 請用`grep`驗證有設定開機自動掛載。
![](https://i.imgur.com/WynwQXs.png)
### 3. 請用`ls`查詢`/srv/maildir`屬性，確認可以讓`mailgroup`群組共用，而其他人不具任何權限。
![](https://i.imgur.com/bMJdldl.png)
### 4.請用`id`檢查`mailuser`使用者有在`mailgroup`.
![](https://i.imgur.com/e9FNboy.png)
