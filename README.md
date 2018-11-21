# 107(1) UNIX應用實務

*公告:* 

請同學至[作業成績](https://github.com/ogre0403/107-1-ntcu-linux/tree/score)確認自己的作業成績，若HW-1沒有成績(0分)，請至[HW-1 分支](https://github.com/ogre0403/107-1-ntcu-linux/tree/HW-1)確認是否有你的作業，若HW-2沒有成績，請至[HW-2分支](https://github.com/ogre0403/107-1-ntcu-linux/tree/HW-2)確認是否有你的作業，之後的作業依此類推。有些同學作業送到錯分支，一樣以0分記，請重新送一次。

## HW6: Deadline: 2018/11/27 23:59

*注意:* 請依[Git繳交作業流程](#Git繳交作業流程), 唯一不同處是作業2用HW-2的地方在作業6改用HW-6分支

*注意:* HW-6之後遲交以及線上繳交不合規定有錯，一率不接受補交。

TBD

## HW5: Deadline: 2018/11/6 23:59

*注意:* 請依[Git繳交作業流程](#Git繳交作業流程), 唯一不同處是作業2用HW-2的地方在作業5改用HW-5分支

*注意:* 以Markdown 格式 **詳細整理記錄說明** 每一個步驟，若太精簡成績以50分 記。


1. 關於連結檔案的建置行為: 
    
    * 在 /etc/hosts 檔案，請找出
        
        * 該檔案的 inode 號碼為幾號？
        
        * 這個 inode 共有幾個檔名在使用？
    
    * 建立實體連結，原始檔案為 /etc/hosts 而新的檔案檔名為 /srv/hosts.hard，請找出
        
        * /srv/hosts.hard的 inode 號碼為幾號？
        
        * 這個 inode 共有幾個檔名在使用？

        * 說明原因。

    * 建立符號連結，原始檔案為 /etc/hosts 而新的檔案檔名為 /srv/hosts.soft，請找出
    
        * /srv/hosts.soft的 inode 號碼為幾號？
        
        * 這個 inode 共有幾個檔名在使用

        * 說明原因


## HW4: Deadline: 2018/10/30 23:59 

*注意:* 請依[Git繳交作業流程](#Git繳交作業流程), 唯一不同處是作業2用HW-2的地方在作業4改用HW-4分支

*注意:* 題目已修改完成，都是10/24的進度內容。

*注意:* 以Markdown 格式 **詳細整理記錄說明** 每一個步驟，若太精簡成績以50分 記。

1. 管理群組共用資料的權限設計：

    * 建立群組名稱為： mygroup, nogroup

    * 建立帳號名稱為： myuser1, myuser2, myuser3 ，通通加入 mygroup，且密碼為 MyPassWord

    * 建立帳號名稱為： nouser1, nouser2, nouser3 ，通通加入 nogroup，且密碼為 MyPassWord

    * 建立一個名為 /srv/myproject 的目錄，這個目錄可以讓 mygroup 群組內的使用者完整使用，且【新建的檔案擁有群組】為 mygroup 。不過其他人不能有任何權限

    * 暫時切換成為 myuser1 的身分，並前往 /srv/myproject 目錄，嘗試建立一個名為 myuser1.data 的檔案，之後登出 myuser1。

    * 復制/usr/bin/ls至/usr/local/bin/myls後，完成下列操作

        * 雖然 nogroup 群組內的用戶對於 /srv/myproject 應該沒有任何權限，但當 nogroup 內的用戶執行 /usr/local/bin/myls 時，可以產生與 ls 相同的資訊，且暫時擁有 mygroup 群組的權限，因此可以查詢到 /srv/myproject 目錄內的檔名資訊。 也就是說，當你使用 nouser1 的身分執行【myls /srv/myproject】時，應該是能夠查閱到該目錄內的檔名資訊。


2. 使用程序觀察的指令，搭配 grep 的關鍵字查詢功能，將找到的 rsyslog 相關的程序的 PID, PRI, NI, COMMAND 等資訊轉存到 /root/process_syslog.txt 檔案中。(搭配`>`重導向輸出)

3. 使用 find 找出 /usr/bin 及 /usr/sbin 兩個目錄中，含有 SUID 的特殊檔案檔名，並使用 ls -l 去列出找到的檔案的相關權限後，將螢幕資料轉存到 /root/findsuidsgid.txt 檔案中。(自行查詢find指令用法，以及使透過重導向符號`>`輸出檔案)



## HW3: Deadline: 2018/10/23 23:59 

*注意:* 題目已修改完成，都是10/17的進度內容。

*注意:* 請依[Git繳交作業流程](#Git繳交作業流程), 唯一不同處是作業2用HW-2的地方在作業3改用HW-3分支

1. 請『依序』進行如下的帳號管理任務, 並以Markdown 格式 **詳細整理記錄說明** 每一個步驟，若太精簡成績以50分 記。

    * 建立三個用戶，帳號名稱分別為： examuser1, examuser2, examuser3 ，同時三個用戶的密碼都是『 ItIsExam 』。(請參考書上passwd --stdin的說明)

    * 請刪除系統中的 examuser3 這個帳號，同時將這個帳號的家目錄與郵件檔案同步刪除。

    * examuser1 不小心被管理員刪除了，但是這個帳號的家目錄與相關郵件都還存在。請參考這個帳號可能的家目錄所保留的 UID 與 GID， 並嘗試以該帳號原有的 UID/GID 資訊來重建該帳號。而這個帳號的密碼請給予 ItIsExam 的樣式。(相關建置帳號的指令，請參考 man useradd 等線上文件的說明)
    

2. 請進行如下的權限管理任務, 以Markdown 格式 **詳細整理記錄說明** 每一個步驟，若太精簡成績以50分 記。

    * 建立examuser4使用者帳號，密碼任意。

    * 使用 root 將 /etc/securetty 複製給 examuser4，且這個帳號要能夠完整使用該檔案才行，(即有所有的權限)。
    
    * 建立一個名為 /examdata/change.txt 的空檔案，這個檔案的擁有者為 sshd，擁有群組為 users，sshd 可讀可寫，users 群組成員可讀， 其他人沒權限。且這個檔案的修改日期請調整成 2012 年 12 月 21 日 (日期正確即可，時間隨便)


3. 請進行如下說明操作, 以Markdown 格式 **詳細整理記錄說明** 每一個步驟，若太精簡成績以50分 記。 

    * 請使用 root 的身份建立底下的檔案與權限：

    ```sh
    drwxrwxr-x  root root /dev/shm/unit05/
    drwxr-xr--  root root /dev/shm/unit05/dir1/
    -rw-r--r--  root root /dev/shm/unit05/dir1/file1 (複製來自 /etc/hosts)
    drwxr-x--x  root root /dev/shm/unit05/dir2/
    -rw-r--r--  root root /dev/shm/unit05/dir2/file2 (複製來自 /etc/hosts)
    drwxr-xr-x  root root /dev/shm/unit05/dir3/
    -rw-rw-rw-  root root /dev/shm/unit05/dir3/file3 (複製來自 /etc/hosts)
    drwxrwxrwx  root root /dev/shm/unit05/dir4/
    -rw-------  root root /dev/shm/unit05/dir4/file4 (複製來自 /etc/hosts)
    ```

    * 使用一般使用者 的身份進行各項工作：
    
    * 請使用 ls -l /dev/shm/unit05/dir[1-4] 依據輸出的結果說明為何會產生這些問題？
    
    * 請使用 ls -l /dev/shm/unit05/dir1/file1 ，依序將上述的檔名由 dir1/file1 ~ dir4/file4 執行，依據產生的結果說明為何會如此？
    
    * 請使用 vim /dev/shm/unit05/dir1/file1 ~ vim /dev/shm/unit05/dir4/file4，嘗試儲存 (或強制儲存)，說明為何可以/不可以儲存？


## HW2: 安裝Linux, Deadline: 2018/10/11 00:00 

請依下列要求練習安裝Linux，並詳細記錄說明安裝過程。
採用`Markdown`文件格式撰寫，檔名請命名為README.md，將檔案放於自己學號的目錄下，發PR至HW-2 branch。

1. 建立一個新的虛擬機器

2. distribution & image 任選

3. 至少建立二個分割區，分別掛載 / 與 /home

4. 登入後用 `df` 驗證是否有掛載二個分割區


## HW1: Deadline: 2018/10/3 00:00 
建立和自己學號相同的目錄，在目錄下用Markdown 寫自我介紹，並練習透過github發pull request (PR)


## **Git繳交作業流程**
目錄/檔案建立操作為使用command，若使用gui，請自行變通。

Step 1: clone 你 fork 後的git project，注意網址會與我的不同，請換成你的網址

```
$ git clone https://github.com/<YOUR-FORKED-REPO>/107-1-ntcu-linux.git
```

Step 2: checkout a76aa3121679a6d67e3456c0798a080c78b920d3 commit, 並查看目錄下內容，會有`123456`目錄與`README.md`檔案。

**注意**: 請不要刪除或修改`123456`目錄與`README.md`檔案。


```
$ cd 107-1-ntcu-linux
$ git checkout a76aa3121679a6d67e3456c0798a080c78b920d3 -b HW-2
$ ll -al
total 8
drwxr-xr-x  3 jimmy  wheel   102B Oct 10 11:21 123456
-rw-r--r--  1 jimmy  wheel    12B Oct 10 11:21 README.md
```


Step 3: 建立你自己的學號的目錄(如: `ACS107XXXXX`)，並在裡面建立`README.md`，目錄名稱每人都會不同，但目錄內的檔名一定要為`README.md`。
```
$ mkdir ACS107XXXXX
$ touch ACS107XXXXX/README.md

$ ls -al
total 8
drwxr-xr-x   6 jimmy  wheel  204 Oct 10 11:25 .
drwxrwxrwt   7 root   wheel  238 Oct 10 11:18 ..
drwxr-xr-x  12 jimmy  wheel  408 Oct 10 11:25 .git
drwxr-xr-x   3 jimmy  wheel  102 Oct 10 11:21 123456
drwxr-xr-x   3 jimmy  wheel  102 Oct 10 11:25 ACS107XXXXX
-rw-r--r--   1 jimmy  wheel   12 Oct 10 11:21 README.md

$ls -al ACS107XXXXX/
total 0
drwxr-xr-x  3 jimmy  wheel  102 Oct 10 11:25 .
drwxr-xr-x  6 jimmy  wheel  204 Oct 10 11:25 ..
-rw-r--r--  1 jimmy  wheel    0 Oct 10 11:25 README.md
```

Step 4: 將您的報告撰寫在你的目錄內的`README.md`，例如`ACS107XXXXX/READMD.md`，若有圖片或其他檔案，也一併放在你的目錄內(如: `ACS107XXXXX`)，不要放到別的地方

Step 5: 完成後，commit & push你的目錄到你的github repo。 *若你coomit包含你目錄以外的資料，表示你做錯，之後會被退回。*

```
$ git add ACS107XXXXX/
$ git commit -m "hw-2 commit"
$ git push --set-upstream origin HW-2
```

若你push後，有下列訊息，表示你太晚fork我的repo，
```
$ git push --set-upstream origin HW-2

Username for 'https://github.com': ogre0403.public@gmail.com
Password for 'https://ogre0403.public@gmail.com@github.com':
To https://github.com/Jimmy-Chuang/107-1-ntcu-linux.git
 ! [rejected]        HW-2 -> HW-2 (non-fast-forward)
error: failed to push some refs to 'https://github.com/Jimmy-Chuang/107-1-ntcu-linux.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```

解決方法為執行`git push origin :HW-2`，之後再執行`git push --set-upstream origin HW-2`。

```
$ git push origin :HW-2
...
To https://github.com/Jimmy-Chuang/107-1-ntcu-linux.git
 - [deleted]         HW-2
```

SETP 6: push後，請至github檢查是否只有把自己的目錄上傳，若有push其他的目錄，請重新操作，不然繳交時會被退回。

**注意**: 因為沒有刪除或修改`123456`目錄與`README.md`檔案，所以這二個存在是正確的。
![](./img/fig1.png)

STEP 7: 建立pr，注意從你的HW-2到我的HW-2，標題請註明你的`學號-HW-2`
![](./img/fig2.png)

STEP 8: PR建立後，請再三確認是否有動到別的目錄的檔案，正確結果只會上傳你目錄的資料，若有修改或上傳其他目錄/檔案，皆會被退回。
![](./img/fig3.png)
![](./img/fig4.png)

