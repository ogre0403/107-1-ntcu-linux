## 1. 在 /etc/hosts 檔案  
  
#### ‧該檔案的 inode 號碼為幾號？ 2129800  
  
####‧這個 inode 共有幾個檔名在使用？ 1   
   
## 2.建立實體連結，原始檔案為 /etc/hosts 而新的檔案檔名為 /srv/hosts.hard    
      
####‧/srv/hosts.hard的 inode 號碼為幾號？ 2129800   
   
####‧這個 inode 共有幾個檔名在使用？ 2   
  
####‧說明原因     
##### hard link 只是在某個目錄下新增一筆檔名連結到某 inode 號碼的關連記錄，
 所以這個 inode有2個檔名在使用   
   
## 3.建立符號連結，原始檔案為 /etc/hosts 而新的檔案檔名為 /srv/hosts.soft   
####‧/srv/hosts.soft的 inode 號碼為幾號？ 3148481    
      
####‧這個 inode 共有幾個檔名在使用 1   
     
####‧說明原因   
##### Symbolic link 就是在建立一個獨立的檔案，而這個檔案會讓資料的讀取指向他 link 的那個檔案的檔名，所以這個 inode只有1個檔名使用   
       
![5](https://github.com/edmundabc/107-1-ntcu-linux/blob/HW-5/5.png?raw=true)

