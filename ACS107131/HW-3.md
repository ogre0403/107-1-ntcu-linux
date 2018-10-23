### 1-1 建立三個用戶，帳號名稱分別為： examuser1, examuser2, examuser3 ，同時三個用戶的密碼都是『 ItIsExam 』  
     
 useradd 帳號   
 passwd 帳號    
 輸入密碼      
![1](https://github.com/edmundabc/107-1-ntcu-linux/blob/HW-3/ACS107131/1.png?raw=true)  
 
### 1-2 請刪除系統中的 examuser3 這個帳號，同時將這個帳號的家目錄與郵件檔案同步刪除   
 
 userdel -r examuser3  
![2](https://github.com/edmundabc/107-1-ntcu-linux/blob/HW-3/ACS107131/2.png?raw=true)  
 
### 1-3 examuser1 不小心被管理員刪除了，但是這個帳號的家目錄與相關郵件都還存在。請參考這個帳號可能的家目錄所保留的 UID 與 GID， 並嘗試以該帳號原有的 UID/GID 資訊來重建該帳號。而這個帳號的密碼請給予 ItIsExam 的樣式  
   
 userdel examuser1  
 ll /home/ 會看到1001    
 useradd -u 1001 -U examuser1     
![3](https://github.com/edmundabc/107-1-ntcu-linux/blob/HW-3/ACS107131/3.png?raw=true) 
 
### 2-1 建立examuser4使用者帳號，密碼任意 
 
  useradd 帳號   
  passwd 帳號   
  輸入密碼    
![4](https://github.com/edmundabc/107-1-ntcu-linux/blob/HW-3/ACS107131/4.png?raw=true)  
 
### 2-2 使用 root 將 /etc/securetty 複製給 examuser4，且這個帳號要能夠完整使用該檔案才行  
#### 複製     
  cp /etc/securetty /home/examuser4     
  cd examuser4      
  ls 會看到securetty    
![5](https://github.com/edmundabc/107-1-ntcu-linux/blob/HW-3/ACS107131/5.png?raw=true) 
   
#### 更改權限    
  切換到root su - root     
  chmod u=rwx,g=rwx,o=rwx /home/examuser4/securetty       
![6](https://github.com/edmundabc/107-1-ntcu-linux/blob/HW-3/ACS107131/6.PNG?raw=true) 
 
### 2-3 建立一個名為 /examdata/change.txt 的空檔案，這個檔案的擁有者為 sshd，擁有群組為 users，sshd 可讀可寫，users 群組成員可讀， 其他人沒權限。且這個檔案的修改日期請調整成 2012 年 12 月 21 日 (日期正確即可，時間隨便) 
 
  cd /      
  mkdir examdata     
  cd examdata      
  ls 查看檔案    
  touch change.txt    
  ll 查看權限     
  這個檔案的擁有者為 sshd:chown sshd change.txt      
  擁有群組為 users:chgrp users change.txt       
  sshd 可讀可寫，users 群組成員可讀， 其他人沒權限:chmod u=rw,q=r,0= change.txt      
  ll 確認         
![7](https://github.com/edmundabc/107-1-ntcu-linux/blob/HW-3/ACS107131/7.PNG?raw=true) 

#### 修改日期請調整成 2012 年 12 月 21 日 touch -t 201212210000 change.txt        
  ll確認               
![8](https://github.com/edmundabc/107-1-ntcu-linux/blob/HW-3/ACS107131/8.PNG?raw=true) 
 
### 3-1 請使用 root 的身份建立底下的檔案與權限：              
 drwxrwxr-x  root root /dev/shm/unit05/    
 drwxr-xr--  root root /dev/shm/unit05/dir1/       
 -rw-r--r--  root root /dev/shm/unit05/dir1/file1 (複製來自 /etc/hosts)         
 drwxr-x--x  root root /dev/shm/unit05/dir2/            
 -rw-r--r--  root root /dev/shm/unit05/dir2/file2 (複製來自 /etc/hosts)         
 drwxr-xr-x  root root /dev/shm/unit05/dir3/           
 -rw-rw-rw-  root root /dev/shm/unit05/dir3/file3 (複製來自 /etc/hosts)       
 drwxrwxrwx  root root /dev/shm/unit05/dir4/          
 -rw-------  root root /dev/shm/unit05/dir4/file4 (複製來自 /etc/hosts)          
 
 cd /dev/shm     
![9](https://github.com/edmundabc/107-1-ntcu-linux/blob/HW-3/ACS107131/9.PNG?raw=true)  
 
 建立unit05: mkdir unit05      
 設定unit05的權限:chmod u=rwx,g=rwx,o=rx unit05         
 cd unit05/     
#### 建立資料夾        
 mkdir dir1      
 mkdir dir2    
 mkdir dir3   
 mkdir dir4     
![10](https://github.com/edmundabc/107-1-ntcu-linux/blob/HW-3/ACS107131/10.PNG?raw=true) 
  
#### 設定dir 1-4的權限       
 chmod u=rwx,g=rx,o=r dir1   
 chmod u=rwx,g=rx,o=x dir2  
 chmod u=rwx,g=rx,o=rx dir3  
 chmod u=rwx,g=rwx,o=rwx dir4  
![11](https://github.com/edmundabc/107-1-ntcu-linux/blob/HW-3/ACS107131/11.PNG?raw=true)  
 
#### 複製 
 cp /etc/hosts /dev/shm/unit05/dir1/file1        
 cp /etc/hosts /dev/shm/unit05/dir2/file2       
 cp /etc/hosts /dev/shm/unit05/dir3/file3         
 cp /etc/hosts /dev/shm/unit05/dir4/file4         
![12](https://github.com/edmundabc/107-1-ntcu-linux/blob/HW-3/ACS107131/12.PNG?raw=true) 
 
#### 設定file 1-4的權限 
 cd dir1/         
 chmod u=rw,g=r,o=r file1        
 cd ..       
 cd dir2/        
 chmod u=rw,g=r,o=r file2      
 cd ..        
 cd dir3/    
 chmod u=rw,g=rw,o=rw file3     
 cd ..      
 cd dir4/     
 chmod u=rw,g=,o=  file4       
![13](https://github.com/edmundabc/107-1-ntcu-linux/blob/HW-3/ACS107131/13.png?raw=true) 
 
### 3-2使用一般使用者 的身份進行各項工作：        
  
### 1.請使用 ls -l /dev/shm/unit05/dir[1-4] 依據輸出的結果說明為何會產生這些問題？   
![14](https://github.com/edmundabc/107-1-ntcu-linux/blob/HW-3/ACS107131/14.PNG?raw=true) 
       
### 2.請使用 ls -l /dev/shm/unit05/dir1/file1 ，依序將上述的檔名由 dir1/file1 ~ dir4/file4 執行，依據產生的結果說明為何會如此？         
![15](https://github.com/edmundabc/107-1-ntcu-linux/blob/HW-3/ACS107131/15.PNG?raw=true)  
          
### 3.請使用 vim /dev/shm/unit05/dir1/file1 ~ vim /dev/shm/unit05/dir4/file4，嘗試儲存 (或強制儲存)，說明為何可以/不可以儲存？      
 vim /dev/shm/unit05/dir1/file1 無法儲存 因為沒有權限           
 vim /dev/shm/unit05/dir2/file2 無法儲存 因為沒有權限       
 vim /dev/shm/unit05/dir3/file3 可以儲存 因為有權限     
 vim /dev/shm/unit05/dir4/file4 無法儲存 因為沒有權限          