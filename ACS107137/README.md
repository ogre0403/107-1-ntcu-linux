## 1.<br>
### 設定 ver 變數，內容為『 my kernel version is 3.xx 』，其中 3.xx 為 uname -r 輸出的資訊，並顯示出ver變數的值。<br>

```
ver=my\ kernel\ version\ is\ $(uname -r)
echo $ver
```

### 請顯示目前PATH環境變數的值為何，並說明PATH的功用為何?<br>

```
echo $PATH
```

PATH是執行檔搜尋的路徑，目錄與目錄中間以冒號(:)分隔，由於檔案的搜尋是依序由 PATH 的變數內的目錄來查詢，因此目錄的順序也是重要的喔。<br>

## 2.<br>
### 有一個檔案的屬性權限為 drwxrwsr-x 3 root mail 4096 2月 16 2017 mail/，請說明此檔案的特性。<br>
此檔案檔名為mail/，目錄檔(d)。使用者(root)權限為可讀可寫可執行。群組(mail)權限為可讀可寫可執行，並擁有SGID的特殊權限。其他人權限為可讀可執行。<br>
檔案連結數為3，檔案容量4096，最後一次修改時間為2017年2月16日。<br>

### 假設有一個script.sh檔案的權限為-rw-r--r--，若希望讓所有人可以執行該檔案，請問該如何下達指令？請使用數字法與符號法各操作一次。<br>

```
chmod 755 script.sh
或是
chmod u=rwx,g=rx,o=rx script.sh
```

## 3.<br>
### 說明實體連結與符號連結的差異。
實體連結會建立與連結檔同inode碼的檔案，而符號連結則會建立與連結檔不同inode碼的獨立檔案<br>

### 在家目錄下建立一個檔名為 hosts.real 的實體連結指到 /etc/hosts。(請用相對路徑表示家目錄)<br>

```
cd ~bill0330
touch hosts.real
ln ~bill0330/hosts.real /etc/hosts
ll -i ~bill0330/hosts.real /etc/hosts
```

### 在家目錄下建立一個檔名為 hosts.symbo 的符號連結指到 /etc/hosts。(請用相對路徑表示家目錄)<br>

```
cd ~bill0330
touch hosts.symbo
ln -s ~bill0330/hosts.symbo /etc/hosts
ll -i ~bill0330/hosts.symbo /etc/hosts
```

## 4.
### 建立一個容量為1GB的xfs檔案系統，每次開機都能夠自動的掛載到 /srv/maildir，且該目錄是給 mailgroup 這個群組共用的，其他人不可具有任何權限。再建立一個名為mailuser的帳號，並加入 mailgroup 群組，且此帳號不可使用shell登入系統。
![image](https://github.com/bill0330/107-1-ntcu-linux/blob/midterm/ACS107137/img/4-1.PNG?raw=true)<br>
![image](https://github.com/bill0330/107-1-ntcu-linux/blob/midterm/ACS107137/img/4-2.PNG?raw=true)<br>


