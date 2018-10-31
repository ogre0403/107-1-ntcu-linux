#Homework 4
###1.  
首先使用 groupadd 指令新增   
-mygroup  
-nogroup   
這兩個群組  
  
然後再使用 useradd 指令加入  
-myuser1  
-myuser2  
-myuser3  
三個使用者   
  
使用 passwd 指令增加密碼  
EX **:** passwd myuserX  
  
接著使用 usermod -a -G mygroup 將使用者新增至群組中  
Ex **:** usermod -a -G mygroup myuserX 。
  
而 nouserX 使用者的創建和加入nogroup群組的方法與上面  
只是名子不同而已 。
  
使用 mkdir 的指令來創造文件
(創造文件必須依著資料夾一個一個創 ，  
不能一次創完 。除非加入-p這個參數 ，只是一打錯字就要全部重創所以用時要小心 。)
  
而這個目錄可以讓 mygroup 群組內的使用者完整使用 ，不過其他人不能有任何權限 。  
  
Ex **:** mkdir -m 070 /srv/myproject    
  
使用 su - myuser1 這個指令登入 myuser1   
並使用 cd /srv/myproject 前往目的目錄  
(同創建文件必須一層一層的進行)  
最後成功建立一個名為 myuser1.data的檔案  
  
接著一樣使用 su - root 這個指令來以 root 進行登錄  
  
然後使用cp複製目要求的東西到要求的區域   
然後確認 nouser1 這隻帳號的權限能不能使用   
###2.   

用 ps aux | grep rsyslog>/root/process_syslog.txt 此指令找到跟 rsyslog 相關的東西 , 並且存取。   
 
###3.  
  
用 find/usr/bin -prem /u=s -exec is -l {} \ ; > /root/findsuidsgid.txt 這個指令去找出有 suid 特殊檔名的檔案 , 並且列出 , 之後轉存到指令上的路徑。
 
用 find/usr/bin -prem /u=s -exec is -l {} \ ; **>>** /root/findsuidsgid.txt 這支指令去找出有 suid 特殊檔名的檔案,並且列出, 之後轉存到指令上的路徑  
  
之後用 cat /root/findsuidsgid.txt 檢查上述操作有沒有成功


