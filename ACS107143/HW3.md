### HW3

## 一

# <ol>
<li>用"useradd"建立三個帳號，名稱分別為： examuser1, examuser2, examuser3 ，用"passwd"建立密碼，三個用戶都是"itisexam"</li>
<li>用"userdel -r"刪除"examuser3"，"-r"可將帳號連同家目錄與相關郵件都刪掉</li>
<li>用"id examuser3"確定帳號已經刪除，去/home確定它的家目錄跟去/vac/mail確認相關郵件已被刪除</li>
<li>用"userdel"刪除"examuser1"，但是家目錄與相關郵件不會被刪除</li>
<li>用"id examuser1"發現帳號還沒被刪除，去/home也會發現examuser1的家目錄還在，去/vac/mail也還是會看到相關郵件還存在</li>
<li>這時使用UID創立帳號，輸入"useradd -u 1001 -U examuser1"，因為我原本被刪除的examuser1的UID是1001。"-u"可指定UID，"-U"可建立和帳號相同的群組。</li>
<li>然後再用"passwd"建立密碼"itisexam"，就完成了</li>
</ol>

## 二

# <ol>
<li>使用"useradd"建立一個帳號"examuser4"，密碼我設定為"itisexam"</li>
<li>先使用root使用者，進入/etc然後將securetty複製給examuser4，指令是"cp securetty /home/examuer4/"</li>
<li>然後進去/home/examuser4，按ll後，發現root的權限是"rw-"，要將它改為"rwx"，所以輸入這個指令"chmod 700 securetty"</li>
<li>然後將owner更改為examuser4，輸入"chown examuser4 securetty"，這樣examuser4就擁有這個檔案的所有權限</li>
<li>進入/home/examuser4，創立一個資料夾"examdata"，指令是"mkdir examdata"</li>
<li>在examdata這個資料夾中，使用"touch change.txt"建立一個檔案</li>
<li>然後使用"chown"更改擁有者為"sshd"，接著打"grep users /etc/group"確定users這個群組存在，然後將change.txt的群組更改為user，指令為"chgrp users change.txt"</li>
# <li>用chmod更改這個檔案的權限，"chmod 640 change.txt"，代表sshd可讀可寫，群組成員可讀，其他人無權限。</li>
# <li>然後更改這個檔案的修改日期，改為2012年12月21日，時間隨便，指令為"touch -t 201212211111.11 change.txt"</li>
</ol>

## 三

# <ol>
<il>進入/dev/shm，建立一個資料夾unit05，然後更改unit05的權限，輸入指令"chmod 775 unit05/"</il>
<il>在unit05中創立一個資料夾"dir1"，然後更改它的權限，指令為"chmod 754 dir1/"</il>
<il>再創立3個資料夾，分別為dir2,dir3,dir4，他們的權限分別為751,755,777</il>
<il>進入/etc找到hosts這個檔案，分別將它複製到/dev/shm/uni05/dir1,dir2,dir3,dir4，檔名分別為file1,file2,file3,file4</il>
<il>更改file3,file4的權限，輸入"chmod 666 file3"、"chmod 600 file4"</il>
<il>切換為一般使用者，指令為"su 帳號"</il>
<il>接著輸入"ls -l /dev/shm/unit05/dir[1-4]"，會發現dir1和dir2都不會正常顯示，dir2更是沒出現多少東西，可以推測出dir1沒辦法讓一般使用者執行，但是可以讀取，而dir2是讀取與執行都沒辦法</il>
<il>接著依序輸入"ls -l /dev/shm/unit05/dir1/file1",dir2/file2,dir3/file3,dir4/file4，會發現file1沒辦法顯示，可以推測這個檔案沒辦法讀取，而其他三個檔案都可以讀取</il>
<il>輸入"vi dev/shm/uni05/dir1/file1"~"vi dev/shm/uni05/dir4/file4"，試著去強制儲存檔案，在file1,file2中我隨便輸入一段文字後，打上":wq!"，它顯示這個檔案無法被書寫，表示對一般使用者來說權限不足，而file3和file4都可以修改，表示對於一般使用者來說是有修改的權限的</il>
</ol>
