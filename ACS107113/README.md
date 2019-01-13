## HW3

1. 
   
+ 建立三個用戶，帳號名稱分別為： examuser1, examuser2, examuser3 ，同時三個用戶的密碼都是『 ItIsExam 』。(請參考書上passwd --stdin的說明)
        
    + 設立使用者。

        ![GITHUB]( https://imgur.com/NulUtwO.jpg"git圖示")
    
    + 設定密碼，密碼為ItIsExam。

        ![GITHUB]( https://imgur.com/YhVn1Sm.jpg"git圖示")

+ 請刪除系統中的 examuser3 這個帳號，同時將這個帳號的家目錄與郵件檔案同步刪除。
    + 徹底摻除examuser3，刪完再檢查。
![GITHUB]( https://imgur.com/Qj7OxZT.jpg"git圖示")
![GITHUB]( https://imgur.com/XIskxGY.jpg"git圖示")

+ examuser1 不小心被管理員刪除了，但是這個帳號的家目錄與相關郵件都還存在。請參考這個帳號可能的家目錄所保留的 UID 與 GID， 並嘗試以該帳號原有的 UID/GID 資訊來重建該帳號。而這個帳號的密碼請給予 ItIsExam 的樣式。(相關建置帳號的指令，請參考 man useradd 等線上文件的說明)
    + 不小心刪除examuser1，檢視其UID跟GID。
![GITHUB]( https://imgur.com/p9WbVOx.jpg"git圖示")
    + 使用groupadd跟useradd的指令修復使用者資料。
![GITHUB]( https://imgur.com/8pZJFju.jpg"git圖示")
    + 完成後再檢驗。
![GITHUB]( https://imgur.com/MrXM83H.jpg"git圖示")
    + 最後再設密碼。
![GITHUB]( https://imgur.com/V8a7j9i.jpg"git圖示")
2.
+ 建立examuser4使用者帳號，密碼任意。
    + 建立examuser4。
    ![GITHUB]( https://imgur.com/n17nxGM.jpg"git圖示")

+ 使用 root 將 /etc/securetty 複製給 examuser4，且這個帳號要能夠完整使用該檔案才行，(即有所有的權限)。。
    + 複製檔案。
![GITHUB]( https://imgur.com/awdJuda.jpg"git圖示")
    + 改變權限，使其擁有全部權限。
![GITHUB]( https://imgur.com/gSXr6LJ.jpg"git圖示")
    + 驗證結果。
![GITHUB]( https://imgur.com/YXLN7li.jpg"git圖示")

+ 建立一個名為 /examdata/change.txt 的空檔案，這個檔案的擁有者為 sshd，擁有群組為 users，sshd 可讀可寫，users 群組成員可讀， 其他人沒權限。且這個檔案的修改日期請調整成 2012 年 12 月 21 日 (日期正確即可，時間隨便)
    + 建立一個名為 /examdata/change.txt 的空檔案。
![GITHUB]( https://imgur.com/1oDaBlt.jpg"git圖示")
    + 使其擁有者為 sshd，擁有群組為 users，並改變權限，使其可讀可寫。
![GITHUB]( https://imgur.com/BGKv6Je.jpg"git圖示")
    + 再將修改日期改為2012 年 12 月 21 日。
![GITHUB]( https://imgur.com/B3aMl3s.jpg"git圖示")

3.
+ 依照題目設立各檔案。
    + 建立分區並設定權限。 
![GITHUB]( https://imgur.com/B3aMl3s.jpg"git圖示")
    + 檢驗。
![GITHUB]( https://imgur.com/Ghavfrb.jpg"git圖示")
    + 複製檔案到/dir1/file1，並改變權限。
![GITHUB]( https://imgur.com/u4eom9h.jpg"git圖示")
    + 複製檔案到/dir2/file2，並改變權限。
![GITHUB]( https://imgur.com/2vBNLym.jpg"git圖示")
    + 複製檔案到/dir3/file3，並改變權限。
![GITHUB]( https://imgur.com/4qB2fvf.jpg"git圖示")
    + 複製檔案到/dir4/file4，並改變權限。
![GITHUB]( https://imgur.com/CSLl5L0.jpg"git圖示")
+ 前置作業設定完成。

+ 請使用 ls -l /dev/shm/unit05/dir[1-4] 依據輸出的結果說明為何會產生這些問題？
    + ls -l /dev/shm/unit05/dir1，權限可讀但不能執行。
![GITHUB]( https://imgur.com/3f5FJz9.jpg"git圖示")
    + ls -l /dev/shm/unit05/dir2，權限不可讀。
![GITHUB]( https://imgur.com/cpveIZW.jpg"git圖示")
    + ls -l /dev/shm/unit05/dir3，權限可讀可執行。
![GITHUB]( https://imgur.com/THGS2bG.jpg"git圖示")
    + ls -l /dev/shm/unit05/dir4，權限可讀可寫可執行。
![GITHUB]( https://imgur.com/Z6YTgda.jpg"git圖示")


+ 請使用 ls -l /dev/shm/unit05/dir1/file1 ，依序將上述的檔名由 dir1/file1 ~ dir4/file4 執行，依據產生的結果說明為何會如此？
    + ls -l /dev/shm/unit05/dir1/file1，dir1權限不能執行。
![GITHUB]( https://imgur.com/QV668dD.jpg"git圖示")
    + ls -l /dev/shm/unit05/dir2/file2，dir2權限可執，所以可讀。
![GITHUB]( https://imgur.com/cYt512j.jpg"git圖示")
    + ls -l /dev/shm/unit05/dir3/file3，權限可讀。
![GITHUB]( https://imgur.com/h4r5LOt.jpg"git圖示")
    + ls -l /dev/shm/unit05/dir4/file4，所有權限都可。
![GITHUB]( https://imgur.com/ffkQMoM.jpg"git圖示")

+ 請使用 vim /dev/shm/unit05/dir1/file1 ~ vim /dev/shm/unit05/dir4/file4，嘗試儲存 (或強制儲存)，說明為何可以/不可以儲存？
    + vim /dev/shm/unit05/dir1/file1，權限不可以讀。
![GITHUB]( https://imgur.com/N2pCWZS.jpg"git圖示")
    + vim /dev/shm/unit05/dir2/file2，權限可讀不可寫。
![GITHUB]( https://imgur.com/6i63hio.jpg"git圖示")
    + vim /dev/shm/unit05/dir3/file3，權限可讀不可寫。
![GITHUB]( https://imgur.com/mx2y5dD.jpg"git圖示")
    + vim /dev/shm/unit05/dir4/file4，權限可讀可寫。
![GITHUB]( https://imgur.com/SnD9HoZ.jpg"git圖示")
