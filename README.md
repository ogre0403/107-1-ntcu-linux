# 107(1) UNIX應用實務


## HW3: Deadline: 2018/10/23 23:59 

1. 請『依序』進行如下的帳號管理任務, 並以Markdown 格式 **詳細整理記錄說明** 每一個步驟，若太精簡成績以50分 記。

    * 建立三個用戶，帳號名稱分別為： examuser1, examuser2, examuser3 ，三個人都加入 examgroup 的次要群組支援，同時三個用戶的密碼都是『 ItIsExam 』。(i 與 e 都是大寫字元)

    *  建立一個用戶，帳號名稱為 examuser4，密碼為『 ItIsExam 』但這個帳號沒加入 examgroup 群組

    * 請刪除系統中的 examuser5 這個帳號，同時將這個帳號的家目錄與郵件檔案同步刪除。

    * 有個帳號 myuser1 不小心被管理員刪除了，但是這個帳號的家目錄與相關郵件都還存在。請參考這個帳號可能的家目錄所保留的 UID 與 GID， 
並嘗試以該帳號原有的 UID/GID 資訊來重建該帳號。而這個帳號的密碼請給予 ItIsExam 的樣式。(相關建置帳號的指令，請參考 man useradd 等線上文件的說明)
    
    * 讓 examuser1 額外加入 student 這個群組，亦即 examuser1 至少有加入 examgroup 與 student 群組


2. 請進行如下的權限管理任務, 以Markdown 格式 **詳細整理記錄說明** 每一個步驟，若太精簡成績以50分 記。

    * 使用 root 將 /etc/securetty 複製給 examuser4，且這個帳號要能夠完整使用該檔案才行。
    
    * 建立一個空的檔案，檔名為 /srv/examcheck.txt，這個檔案可以讓 examuser1 完整的使用，而 examuser2 與 examuser3 可以讀取，但不能執行與寫入， 至於 examuser4 什麼權限都沒有。

    * examgroup 群組的成員想要共用 /srv/examdir 目錄，而沒有加入 examgroup 的其他人不具備任何權限，應該如何處理？

    * /usr/local/bin/mymore 複製來自 /bin/more，但我只想要讓 examgroup 的成員能夠執行 /usr/local/bin/mymore 這個指令，其他人不能執行這個指令。

    * 建立一個名為 /examdata/change.txt 的空檔案，這個檔案的擁有者為 sshd，擁有群組為 users，sshd 可讀可寫，users 群組成員可讀， 其他人沒權限。且這個檔案的修改日期請調整成 2012 年 12 月 21 日 (日期正確即可，時間隨便)

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

