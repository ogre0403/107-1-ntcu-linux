+使用echo ${ver}、echo ${kernel}建立變數ver、kernel，然後設定kernel=$(uname -r)
 最後設定ver="my kernel version is $kernel"即可

+使用echo $PATH可以查看路徑相關的環境變數
![GITHUB](https://imgur.com/O8Sk2kq.jpg"git圖示")
 
+drwxrwsr-x 3 root mail 4096 2月 16 2017 mail/
+其檔案特性為:權限為使用者可寫可讀可使用，具有SGID的功能，其他人執行時可獲得群組的權限
+檔案連結數為3個
+擁有者為root
+檔案所屬群組為mail
+檔案大小為4096
+最後修改日期為2017年2月16日
+檔案名為mail/
 
+權限為-rw-r--r--因為都沒有x的權限所以不能只單純設SUID
+數字法:chmod 4755 script.sh
+符號法:chmod u=rwx g=rx o=rx script.sh後chmod u+s script.sh

+hard link的每個檔案都會佔用一個inode而soft link不會
 hard link的需全連結刪除才算刪除檔案，soft link目的檔刪除後連結就不能使用了
 hard link不能跨Filesystem而soft link可
+建立實體連結hosts.real在家目錄:ln /etc/hosts ~hosts.real
+建立符號連結hosts.real在家目錄:ln -s /etc/hosts ~hosts.real

+使用ud -m可知有一個大小為1014mb檔案系統正掛載到/srv/maildir
![GITHUB](https://imgur.com/U5HZQD6.jpg"git圖示")
+使用grep "maildir" /etc/fstab可知已設為開機自動掛載
![GITHUB](https://imgur.com/bovvHXr.jpg"git圖示")
+使用ls -al /srv/maildir可知其群組為mailgrpup
![GITHUB](https://imgur.com/vlYIegs.jpg"git圖示")
+使用id mailuser可知其在mailgroup內
![GITHUB](https://imgur.com/2YyDt9T.jpg"git圖示")
+由下圖可知道mailuser不能登入
![GITHUB](https://imgur.com/jSeJPIH.jpg"git圖示")
