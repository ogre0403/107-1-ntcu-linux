#帳號管理任務說明
##操作流程 
 - 1 先以 adduser  指令添加以下三支帳號 examuser1 examuser2 examuser3
 - 2 三隻帳號的密碼接設定為 ltlsExam  
   (**建議一次建立一隻帳號,不然你會變得跟某人一樣一直重複操作,結果自己還不知道XDD**) 
 - 3 用 userdel  指令刪除examuser3這隻帳號  
   (**因為要完全刪除帳號,就是加目錄跟郵件檔案要同步刪除,所以指令要記得加上 -r 這個東東**)  
   ex. userdel -r examuser3
 - 4 接下來,因為管理員首誤,意外刪除了examuser1這隻帳號,要試試看能不能復原  
   (**其實就是管理員在刪除指令中沒有 -r 這個參數**)
 - 5 先以 id examuser1 確認帳號消失了
 - 6 試試重新建立 examuser1 這隻帳號
 - 7 系統跟我說,他的家目錄已經存在,不允許其他帳號資料由外側接入  
   (**就算是用 examuser1 這個名稱也不行**)
 - 8 所以結論是,這個方法好像沒辦法重建XDD
#權限管理任務說明
##操作流程
 - 1 建立examuser4這隻帳號  
   (**建立的流程跟剛剛一樣**)
 - 2 密碼設定為ltlsExam  
   (**想說跟剛剛一樣,肯定不會錯亂XD**)
 - 3 使用 root 將 /etc/securetty 複製給 examuser4
   (**以 cp /etc/securetty /home/examuser4 這個指令執行**)
 - 4 設定完整使用檔案的權限
 - (**以 chmod 777 /home/examuser4/securetty 這個指令執行**) 
 - 5 用 mkdir /examdata 這個指令新增空檔案,再用 mkdir /examdata/change.txt 完成新增目錄
   (**只能一步一步慢慢建,沒辦法一次來**)
 - 6 用 chown sshd /examdata/change.txt 這個指令轉換擁有者
 - 7 用 chgrp users /examdata/change.txt 這個指令轉換群組
 - 8 以 chmod 640 /examdata/change.txt 這個指令轉換權限
 
#文件管理任務說明
##操作流程
 - 1 建立題目要求的檔案  
   drwxrwxr-x  root root /dev/shm/unit05/  
   drwxr-xr--  root root /dev/shm/unit05/dir1/  
   -rw-r--r--  root root /dev/shm/unit05/dir1/file1 (複製來自 /etc/hosts)  
   drwxr-x--x  root root /dev/shm/unit05/dir2/  
   -rw-r--r--  root root /dev/shm/unit05/dir2/file2 (複製來自 /etc/hosts)  
   drwxr-xr-x  root root /dev/shm/unit05/dir3/  
   -rw-rw-rw-  root root /dev/shm/unit05/dir3/file3 (複製來自 /etc/hosts)  
   drwxrwxrwx  root root /dev/shm/unit05/dir4/  
   -rw-------  root root /dev/shm/unit05/dir4/file4 (複製來自 /etc/hosts)  
  (**上述的權限設定,基本上都要用 chmod 指令進行權限變更**)  
  (**如果要新增加檔案,一樣用 mkdir 指令來新增**)
 - 2 以下工作請使用一般工作者進行操作  
  + (1)請使用 ls -l /dev/shm/unit05/dir[1-4] 依據輸出的結果說明為何會產生這些問題？
  + (2)請使用 ls -l /dev/shm/unit05/dir1/file1 ，依序將上述的檔名由 dir1/file1 ~ dir4/file4 執行，依據產生的結果說明為何會如此？
  + (3)請使用 vim /dev/shm/unit05/dir1/file1 ~ vim /dev/shm/unit05/dir4/file4，嘗試儲存 (或強制儲存)，說明為何可以/不可以儲存？  
   以上工作執行完的結果
  - (1)  
輸入cd dir1顯示為Permission denied，因為dir1這個目錄對examuser這個使用者來說權限為r--只可讀取不可執行。  
輸入cd dir2，可進入此目錄，因為他對examuser的權限為--x可執行，但使用ls -l這個指令無法看到他的權限，因為它不可讀。  
輸入cd dir3進入目錄，發現可以進入因為userexam的權限為r-x，使用ls -l也可查看權限，但無法使用vi編輯檔案。  
輸入cd dir4進入目錄，發現可進入也可使用ls -l查看權限因為examuser的權限為rwx
  - (2)  
輸入ls -l /dev/shm/unit05/dir1/file1，跑出permission denied，因為examuser對file1的權限為r--,他沒有執行的權限   
輸入ls -l /dev/shm/unit05/dir2/file2，跑出permission denied，因為examuser對file2的權限為r--,他沒有執行的權限    
輸入ls -l /dev/shm/unit05/dir3/file3，跑出permission denied，因為examuser對file3的權限為rw-,他沒有執行的權限    
輸入ls -l /dev/shm/unit05/dir4/file4，跑出permission denied，因為examuser對file4的權限為---,什麼權限都沒有  
(**基本上,他都沒辦法執行,因為他沒有權限XDD**)
  - (3)  
輸入vim /dev/shm/unit05/dir1/file1，無法儲存，因為權限為r--,他們都只能讀  
輸入vim /dev/shm/unit05/dir2/file2，無法儲存，因為權限為r--,他們都只能讀  
輸入vim /dev/shm/unit05/dir3/file3，可以儲存，因為權限為rw-,他有可以儲存的權限  
輸入vim /dev/shm/unit05/dir4/file4，不可儲存，因為權限為---,什麼事都無法處理 

###反正最後學到了一件事,權限真的超重要,沒有權限很痛苦的