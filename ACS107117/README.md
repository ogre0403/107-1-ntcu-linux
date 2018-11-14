#期中考
###1.
(1)  
使用 uname -r 來確認自己的版本 發現為3.10.0-862.17.x86_64
接著使用變數="變數內容"
**ver="my kernel version is 3.10.0-862.17.x86_64"**  
(2)  
使用 **set** 指令來查看目前環境變數，
PATH環境變量中存放的是：執行文件命令搜索路徑。

###2.
(1)  
可以知道  
此檔案類型為目錄，使用者有全部權限，群組也有全部權限且有SGID的功能(讓程式執行者在執行的過程中將會獲得該程式群組的權限。)  
該檔案有3個檔案連結，擁有者為root,並且屬於mail群組。  
容量為4096，檔案最後一次修改時間為2017/2/16，檔名為mail/  
(2)  
使用 **chmod** 指令來修改權限  
數字法:**chmod 777 script.sh**  
符號法:**chmod a=rwx script.sh** 
###3.    
(1)  
實體連結為不論你使用哪個「文件名」來編輯， 最終的結果都會寫入到相同的 inode 與 block 中，因此均能進行數據的修改，並且磁碟的空間與 inode 的數目都不會改變。  
符號連結則是在創建一個獨立的文件，而這個文件會讓數據的讀取指向他 link 的那個文件的文件名，他們的 inode 並不會相同。  
(2)  
使用 **cd ~** 切換到目前使用者家目錄  
使用 **ln** 指令來建立實體連結
**ln /etc/hosts hosts.real**   
(3)  
使用 **cd ~** 切換到目前使用者家目錄  
使用 **ln -s** 指令來建立符號連結  
**ln -s /etc/hosts hosts.symbo**  
###4.  
使用mkfs.xfs 建立檔案系統然後使用vi進入/etc/fstab加入  
/dev/sdb1 /srv/maildir xfs defaults 0 0  
![](https://ppt.cc/fFsnwx@.png)  
![](https://ppt.cc/fodyqx@.png)  
使用groupadd 建立mailgroup  
groupadd mailgroup    
  
使用useradd –m  增加不能登入的使用者 mailuser  
useradd -m mailuser    
  
接著使用usermod -g mailgroup mailuser 把mailuser的群組修改為mailgroup    
![](https://ppt.cc/f91lgx@.png)
  
然後使用chgrp  
chgrp -r mailgroup /srv/maildir  
  
使用chmod 070 /srv/maildir    
並且使用chown更改檔案所屬群組    

使用ls -ld 查詢檔案是否屬於mailgroup且其他人沒有權限
d---rwx---  
  
  
![](https://ppt.cc/fFnwtx@.png)  
    
mailuser 屬於mailgroup群組
![](https://ppt.cc/fJFgVx@.png)
   

確認開機自動掛載  
![](https://ppt.cc/fd5kyx@.png)

