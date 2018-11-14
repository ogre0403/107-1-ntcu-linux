## 1.(20%)    
   
### 1-1設定 ver 變數，內容為『 my kernel version is 3.xx 』，其中 3.xx 為 uname -r 輸出的資訊，並顯示出ver變數的值。(10%)    
    
#### ver=my\ kernel\ version\ is\ 3.xx    
#### echo $ver    
    
### 1-2請顯示目前PATH環境變數的值為何，並說明PATH的功用為何? (10%)   
     
#### env 就是執行檔搜尋的路徑啦～目錄與目錄中間以冒號(:)分隔， 由於檔案的搜尋是依序由 PATH 的變數內的目錄來查詢     
       
## 2.(20%)    
    
### 2-1有一個檔案的屬性權限為 drwxrwsr-x 3 root mail 4096 2月 16 2017 mail/，請說明此檔案的特性。(10%)     
     
#### user 和 group 皆可讀寫執行，其他人只能讀執行，不能寫    
#### 有3個連結數    
#### user-root   
#### group-mail    
#### 檔案容量是4096    
#### 最後修改時間2月 16 2017   
#### 檔名mail/    
    
### 2-2假設有一個script.sh檔案的權限為-rw-r--r--，若希望讓所有人可以執行該檔案，請問該如何下達指令？請使用數字法與符號法各操作一次。(10%)     
    
#### chmod u=rwx,g=rx,o=x script.sh    
#### chmod 751 script.sh   
   
## 3(20%)     
     
### 3-1說明實體連結與符號連結的差異。(10%)     
     
#### 實體連結 只是在某個目錄下新增一筆檔名連結到某 inode 號碼的關連記錄    
#### 符號連結 就是在建立一個獨立的檔案，而這個檔案會讓資料的讀取指向他 link 的那個檔案的檔名     
     
### 3-2在家目錄下建立一個檔名為 hosts.real 的實體連結指到 /etc/hosts？ (請用相對路徑表示家目錄) (5%)     
      
#### ln /etc/hosts  ~/hosts.real    
      
### 3-3在家目錄下建立一個檔名為 hosts.symbo 的符號連結指到 /etc/hosts？ (請用相對路徑表示家目錄 (5%)     
       
#### ln -s /etc/hosts ~/hosts.symbo   
    
## 4.(40%)     
      
### 請依下述情境完成系統操作後再用相關指令進行驗證，請抓驗證指令的圖：     
       
### 建立一個容量為1GB的xfs檔案系統，每次開機都能夠自動的掛載到 /srv/maildir，且該目錄是給 mailgroup 這個群組共用的，其他人不可具有任何權限。再建立一個名為mailuser的帳號，並加入 mailgroup 群組，且此帳號不可使用shell登入系統。      
        
#### mkfs.xfs /dev/sdb1      
#### mkdir /srv/maildir      
#### mount -t xfs /dev/sdb1 /srv/maildir      
#### groupadd mailgroup      
#### chgrp mailgroup /srv/maildir        
#### useradd -G mailgroup mailuser　-s　/sbin/nologin    
#### chmod u=rwx,g=rwx,o= /srv/maildir       
           
                
### 4-1 請用`df`指令配合`human-readable`選項，顯示有1GB的檔案系統正掛載到`/srv/maildir` (8%)        
![1](https://github.com/edmundabc/107-1-ntcu-linux/blob/midterm/ACS107131/1.PNG?raw=true)  
        
### 4-2 請用`grep`驗證有設定開機自動掛載。(8%)         
        
### 4-3 請用`ls`查詢`/srv/maildir`屬性，確認可以讓`mailgroup`群組共用，而其他人不具任何權限。(8%)        
![3](https://github.com/edmundabc/107-1-ntcu-linux/blob/midterm/ACS107131/3.PNG?raw=true)                 
### 4-4 請用`id`檢查`mailuser`使用者有在`mailgroup`. (8%)        
![4](https://github.com/edmundabc/107-1-ntcu-linux/blob/midterm/ACS107131/4.PNG?raw=true)                   
### 4-5 請用`grep`驗證此帳號無法透過shell登入。(8%) 
                            