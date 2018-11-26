#群組管理權限操作說明
##操作流程 Q1
 - 1 以 groupadd 指令新增 mygroup 以及 nogroup 這兩個群組  
 - 2  以 useradd 指令新增 myuser1, myuser2, myuser3  
 - 3  以 passwd 重設新增帳號的密碼    
   (**是myuserX的**)    
   (**MyPassWord 被認為是不好的密碼設定,所以我改成QwEr4myUSER**)  
   (**X 代表的是數字喔**)  
 - 4  以 usermod -a -G mygroup myuserX 將帳號新增至群組中  
   (**X 代表的是數字喔**)
 - 5  以 useradd 指令新增 nouser1, nouser2, nouser3
 - 6  以 passwd 重設新增帳號的密碼 
 - 7  以 usermod -a -G mygroup myuserX 將帳號新增至群組中
   (**MyPassWord 被認為是不好的密碼設定,所以我改成QwEr4noUSER**)  
   (**5,6,7 三點的注意事項跟前面提過的大致上一樣,除了密碼的部分**)
 - 8 用 mkdir 指令新增 /srv/myproject 這個目錄  
   (**要一層一層建,千萬別一次建完,系統不會給你這麼玩xdd,如果 /srv 這個目錄本來就在的話,那就另當別論囉**)
 - 9 以 chgrp  mygroup /srv/myproject指令變更檔案所屬的群組
 - 10 以 chmod 指令變更 /srv/myproject 的權限
   (**記得是改成770啊......**)
 - 11 以 su - myuser1 這個指令登入 myuser1
 - 12 以 cd /srv/myproject 這個指令前往檔案  
   (**記得一層一層跳,系統不會讓你一次跳完的xdd**)
 - 13 進入之後,嘗試建立一個名為 myuser1.data的檔案   
   (**基本上會成功建立啦,畢竟該有的權限都有**)
 - 14 接下來就用 su - root 這隻指令來以 root 進行登錄
 - 15 用 cp 這隻指令來複製題目要求的東西到要求的區域
 - 16 題目要求的動作記得要執行,確認 nouser1 這隻帳號的權限能不能使用
##操作流程Q2
 - 17 用 ps aux | grep rsyslog>/root/process_syslog.txt 找到跟 rsyslog 相關的東西,並且存取
   (**要記得進資料夾檢查有沒有成功**)
##操作流程Q3
 - 18 用 find/usr/bin -prem /u=s -exec is -l {} \ ; > /root/findsuidsgid.txt 這支指令去找出有 suid 特殊檔名的檔案,並且列出, 之後轉存到指令上的路徑
 - 19 用 find/usr/bin -prem /u=s -exec is -l {} \ ; >> /root/findsuidsgid.txt 這支指令去找出有 suid 特殊檔名的檔案,並且列出, 之後轉存到指令上的路徑  
 (**第二個有兩個>>,是為了不要讓上一個移動的檔案被覆蓋的操作,不然系統只會讓後面加上的檔案覆蓋上去**)
 - 20 之後用 cat /root/findsuidsgid.txt 檢查上述操作有沒有成功
   (**基本上成功,樹入指令且執行之後,有特殊權限的檔案會列在最下方**)