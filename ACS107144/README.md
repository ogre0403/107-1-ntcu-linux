# 第一題
* 設定 ver 變數，內容為『 my kernel version is 3.xx 』，其中 3.xx 為 uname -r 輸出的資訊，並顯示出ver變數的值
1. 輸入`ver=“my kernel version is $(uname -r)”`
2. 輸入`echo $ver`

* 請顯示目前PATH環境變數的值為何，並說明PATH的功用為何?
1. 輸入`echo $PATH`
> ![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/midterm/ACS107144/midterm%201.png)
2. 設定執行檔的尋找路徑

# 第二題
* 有一個檔案的屬性權限為 drwxrwsr-x 3 root mail 4096 2月 16 2017 mail/，請說明此檔案的特性。
1. 檔名：mail
2. 檔案所有者：root 
3. 檔案所有群組：mail
4. 檔案權限：所有者：rwx，群組成員：rwx，其他人：rx
5. 屬性：目錄
6. inode共用檔案數：3
7. 建立時間：2017/02/16

* 假設有一個script.sh檔案的權限為-rw-r--r--，若希望讓所有人可以執行該檔案，請問該如何下達指令？請使用數字法與符號法各操作一次。
1. 數字法：`chmod 755 script.sh`
2. 符號法：`chmod u=rwx,g=rx,o=rx script.sh`

# 第三題
* 說明實體連結與符號連結的差異。
1. 實體連結：實體連結是指向的實際文件的精確副本。實體連結和原文件共享相同的inode。
2. 符號連結：符號連結會產生一個獨立的檔案，所以會有自己的 inode。
3. 實體連結限制較多，不能跨Filesystem，所以較常使用符號連結。

* 在家目錄下建立一個檔名為 hosts.real 的實體連結指到 /etc/hosts
1. 輸入`ln cd ../hosts /hosts.real`

*  在家目錄下建立一個檔名為 hosts.symbo 的符號連結指到 /etc/hosts
1. 輸入`ln -s cd ../hosts /hosts.symbo`

# 第四題
* 建立一個容量為1GB的xfs檔案系統，每次開機都能夠自動的掛載到 /srv/maildir，且該目錄是給 mailgroup 這個群組共用的，其他人不可具有任何權限。再建立一個名為mailuser的帳號，並加入 mailgroup 群組，且此帳號不可使用shell登入系統。

1. 使用`mkfs.xfs -b 1GB /dev/sdb1`建立好xfs檔案系統
2. 輸入`mkdir /srv/maildir`
3. 輸入 `mount /dev/sdb1 /srv/maildir`

* 請用`df`指令配合`human-readable`選項，顯示有1GB的檔案系統正掛載到`/srv/maildir`
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/midterm/ACS107144/midterm%202.png)

* 請用`grep`驗證有設定開機自動掛載
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/midterm/ACS107144/midterm%203.png)

* 請用`ls`查詢`/srv/maildir`屬性，確認可以讓`mailgroup`群組共用，而其他人不具任何權限。
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/midterm/ACS107144/midterm%204.png)

* 請用`id`檢查`mailuser`使用者有在`mailgroup`.
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/midterm/ACS107144/midterm%205.png)

* 請用`grep`驗證此帳號無法透過shell登入
1. 於vi內修改mailuser 成 /sbin/nologin
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/midterm/ACS107144/midterm%206.png)
 
