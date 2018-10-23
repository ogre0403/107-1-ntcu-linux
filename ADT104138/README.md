# HW3
## ADT104138 羅苡倫
*****
## 一、請『依序』進行如下的帳號管理任務, 並以Markdown 格式 詳細整理記錄說明 每一個步驟，若太精簡成績以50分記。
*	建立三個用戶，帳號名稱分別為： examuser1, examuser2, examuser3 ，同時三個用戶的密碼都是『 ItIsExam 』。(請參考書上passwd --stdin的說明)</br>
*	請刪除系統中的 examuser3 這個帳號，同時將這個帳號的家目錄與郵件檔案同步刪除。</br>
*	examuser1 不小心被管理員刪除了，但是這個帳號的家目錄與相關郵件都還存在。請參考這個帳號可能的家目錄所保留的 UID 與 GID， 並嘗試以該帳號原有的 UID/GID 資訊來重建該帳號。而這個帳號的密碼請給予 ItIsExam 的樣式。(相關建置帳號的指令，請參考 man useradd 等線上文件的說明)</br>

1.分別建立examuser1、2、3，並一併設定密碼ItIsExam，--stdin方法可以不用再重複輸入一次，對於大量建置很方便。</br>
![新增](https://i.imgur.com/eXKLxFw.jpg)</br>

2.用userdel -r userexam3指令，刪除包括userexam3家目錄以及郵件檔案。</br>

3.用userdel userexam1指令，刪除帳號但不刪除其他相關檔案，再利用useradd -u UID examuser1指令，指定ID創建帳號。</br>
![新增](https://i.imgur.com/QEljpgl.jpg)</br>

*****
## 二、請進行如下的權限管理任務, 以Markdown 格式 詳細整理記錄說明 每一個步驟，若太精簡成績以50分記。
*	建立examuser4使用者帳號，密碼任意。</br>
*	使用 root 將 /etc/securetty 複製給 examuser4，且這個帳號要能夠完整使用該檔案才行，(即有所有的權限)。</br>
*	建立一個名為 /examdata/change.txt 的空檔案，這個檔案的擁有者為 sshd，擁有群組為 users，sshd 可讀可寫，users 群組成員可讀， 其他人沒權限。且這個檔案的修改日期請調整成 2012 年 12 月 21 日 (日期正確即可，時間隨便)</br>

1.建立userexam4帳號及設定密碼。</br>
![新增](https://i.imgur.com/U1IYVO9.jpg)</br>

2.使用cp指令，將 /etc/securetty 複製給 examuser4，並且利用chmod指令設定權限。</br>
![新增](https://i.imgur.com/TPk81Ow.jpg)</br>

3.建立 /examdata/change.txt 空檔案，並且利用chown指令設定sshd為擁有者，chgrp指令設定群組為users，chmod指令設定權限，最後再用touch -t 設定規定時間。</br>
![新增](https://i.imgur.com/kPy5L8A.jpg)</br>

*****
## 三、請進行如下說明操作, 以Markdown 格式 詳細整理記錄說明 每一個步驟，若太精簡成績以50分記。
*	請使用 root 的身份建立底下的檔案與權限：</br>
![新增](https://i.imgur.com/cfQrjf1.jpg)</br>

*	使用一般使用者 的身份進行各項工作：</br>
*	請使用 ls -l /dev/shm/unit05/dir[1-4] 依據輸出的結果說明為何會產生這些問題？</br>
*	請使用 ls -l /dev/shm/unit05/dir1/file1 ，依序將上述的檔名由 dir1/file1 ~ dir4/file4 執行，依據產生的結果說明為何會如此？</br>
*	請使用 vim /dev/shm/unit05/dir1/file1 ~ vim /dev/shm/unit05/dir4/file4，嘗試儲存 (或強制儲存)，說明為何可以/不可以儲存？</br>

1.這部分的作法，基本上大同小異，利用mkdir指令創建目錄之後，再利用cp指令複製file1~4，創建及複製途中順便利用chmod指令設定規定的權限。</br>
![新增](https://i.imgur.com/ux9CTB2.jpg)</br>
![新增](https://i.imgur.com/9dPvEeN.jpg)</br>
![新增](https://i.imgur.com/A4FCD2n.jpg)</br>

2.dir1在other權限上是r--，代表一般使用者只能查看，dir2在other權限上是--x，代表一般使用者不能查看但可以執行，dir3在other權限上是r-x，代表一般使用者可以查看執行，但不能修改，dir4在other權限上是rwx，代表一般使用者可以查看以及讀寫。</br>
![新增](https://i.imgur.com/68T7RxS.jpg)</br>

3.file1即使other能查看，但他的上一層dir1是不可執行，所以整體而言無法執行，file2的上一層dir2可執行，而本身只有r--所以只能查看，file3的上一層dir3可執行，故依照權限此使用者可讀可寫，file4的上一層dir4可執行，但本身沒有任何權限。</br>
![新增](https://i.imgur.com/RqDtS8D.jpg)</br>

4-1.file1無法儲存，因為在other權限上沒有修改權限。</br>
![新增](https://i.imgur.com/XBiaybv.jpg)</br>

4-2.file2無法儲存，因為在other權限上沒有修改權限。</br>
![新增](https://i.imgur.com/dzq1nbi.jpg)</br>

4-3.file3可以儲存，因為在other權限上有修改權限。</br>
![新增](https://i.imgur.com/4zKbI3L.jpg)</br>

4-4.file4無法儲存，因為在other權限上沒有修改權限。</br>
![新增](https://i.imgur.com/DS8k65k.jpg)</br>

# 感謝觀看 The End
