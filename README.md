# 107(1) UNIX應用實務

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

## HW1: Deadline: 2018/10/3 00:00 
建立和自己學號相同的目錄，在目錄下用Markdown 寫自我介紹，並練習透過github發pull request (PR)

## HW2: 安裝Linux, Deadline: 2018/10/11 00:00 

請依下列要求練習安裝Linux，並詳細記錄說明安裝過程。
採用`Markdown`文件格式撰寫，檔名請命名為README.md，將檔案放於自己學號的目錄下，發PR至HW-2 branch。

1. 建立一個新的虛擬機器

2. distribution & image 任選

3. 至少建立二個分割區，分別掛載 / 與 /home

4. 登入後用 `df` 驗證是否有掛載二個分割區


