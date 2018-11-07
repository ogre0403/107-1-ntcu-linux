# 第一題
 1.在 /etc/hosts 檔案，請找出
   (1)該檔案的 inode 號碼為幾號？
      ls -ali /etc/hosts*
      4237992
   (2)這個 inode 共有幾個檔名在使用？
      1個
 2.建立實體連結，原始檔案為 /etc/hosts 而新的檔案檔名為 /srv/hosts.hard，請找出
   (1)/srv/hosts.hard的 inode 號碼為幾號？
      建立實體連結
	  ll -i /etc/hosts
	  ln /etc/hosts /srv/hosts.hard
	  ll -i /etc/hosts /srv/hosts.hard
	  4237992
   (2)這個 inode 共有幾個檔名在使用？
      2個
   (3)說明原因
      使用hard link設定連結檔時，磁碟空間與inode的數目都不會改變
	  只是在目錄裡加一筆inode與檔名對應
 3.建立符號連結，原始檔案為 /etc/hosts 而新的檔案檔名為 /srv/hosts.soft，請找出
   (1)/srv/hosts.soft的 inode 號碼為幾號？
      ln -s /etc/hosts /srv/hosts.soft
	  ll -i /etc/hosts /root/srv/hosts.soft
	  6291566
   (2)這個 inode 共有幾個檔名在使用
      1個
   (3)說明原因
      soft link所建立的檔案為一個獨立的新檔案，會佔用掉inode