#期中考    
##Q1    
 - 1-1  
   + 先以 uname -r 這隻指令知道 kernel 的版本  
   + (**我的是 3.10.0-862.e17.x86_64**)   
   + 再用 ver=3.10.0-862.e17.x86_64 設定變數  
   + 接下來以 echo $ver 確認變數有設定成功  
 - 1-2  
   + 3.10.0-862.e17.x86_64 是我的環境變數的值(**圖Q1-1**)  
   + path 的功用就是搜尋路徑  
##Q2  
 - 2-1  
   +  drwxrwsr-x,d代表的是目錄, rwx 代表 root 的權限,在這裡 root 可讀可寫可執行, rws 代表 group 的權限,原先應該是 rw- 只能讀跟寫而無法執行,但是經由特殊權限 s 則變成可執行, r-x代表 other 的權限, 他們只能讀跟執行  
   +  這個檔案具有 3 個連結  
   +  檔案的擁有者是 root  
   +  檔案的所屬群組是 mail  
   +  檔案的大小為 4096 bytes  
   +  最後的修改時間是 2017/2/16  
   +  它的檔名是 mail/  
 - 2-2  
   +  檔案顯示出的權限是 -rw-r--r-- 這代表了 root 只有讀跟寫的權限, group 只有寫的權限, other 只有寫的權限  
   +  想要大家都能執行它,這時候就要更改權限了,以下有兩種方法  
   +  數字法  
   +  用 chmod 755 script.sh 這個指令來變更這個檔案的權限,使得大家都能執行它(它原本的權限用數字法表示的話是 644,而三個數字全部加1,代表的是大家都能夠執行它)  
   +  (r==4 , w==2 , x==1)  
   +  符號法  
   +  用 chmod u+x script.sh | chmod g+w script.sh |chmod o+x script.sh 這個指令來變更這個檔案的權限,使得大家都能執行它  
##Q3  
 - 3-1   
   +  實體符號是直接將新檔案的 inode 與舊檔案的　inode 共用,代表的是他們所使用的記憶體區域是同一個區塊,因此,就算兩個檔案的檔名不同,它們的執行結果也是一樣的,畢竟是同一個程式。  
   +  符號連結比較沒有實體連結那麼麻煩,它就像是桌面上的捷徑,建立新的檔案,執行後連接上舊的檔案,所以這兩個檔案的 inode 碼不一樣,但是執行的結果依然是舊的檔案。  
   +  (**實體連結的彈性比較不高,符號連結的彈性比較高,所以符號連結的使用度比較高**)  
 - 3-2  
   +  先用 ln /etc/hosts hosts.real 建立硬體連結  
   +  用 ls -ali hosts.real 確認這個檔案的 inode 碼   
   +  用 ls -ali /etc/hosts 確認這個檔案的 inode 碼  
   +  (**兩者的 inode 碼都是 4213106**)  
 - 3-3   
   +  先用 ln -s /etc/hosts hosts.soft 建立軟體連結  
   +  再用 ls -ali /etc/hosts hosts.soft 確認這兩個檔案的 inode 碼  
   +  (**兩者的 inode 碼不同, 前者是 4213160 後者是 8409203**)  
##Q4    
 - 4-1  
   + 先檢查磁碟數量及名稱(圖Q4-1)  
   + 新增硬碟(圖Q4-2)  
   + 增加2G保證空間足夠(圖Q4-3)  
   + 再次檢查磁碟數量 (圖Q4-4)  
   + 檢查磁碟分割狀況 lsblk 指令 (圖Q4-4)  
   + 分割磁碟 fdisk /dev/sda (圖Q4-4)  
   + 建立一個1G的硬碟(圖Q4-5)  
   + 確認分割成功(圖Q4-6)  
   + 以 mkfs.xfs /dev/sdb1 指令建立 xfs 檔案系統(圖Q4-6)  
   + 以 mount dev/sdb1 /srv/maildir 掛載上檔案  
   +  以 useradd mailuser 這隻指令新增 mailuser 這個帳號  
   +  以 groupadd mailgroup 這隻指令新增 mailgroup 這個群組  
   +  以 gpasswd -M mailuser mailgroup 這隻指令將 mailuser 新增進 mailgroup  
   +  題目的要求都是request 為開頭的檔名

##我的解題順序 Q2-Q3-Q4-Q1