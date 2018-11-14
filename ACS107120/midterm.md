# 第一題
  1.uname -r ver="my kernel version is 3.xx"
  
    uname -r $ver 
    
	3.10.0-862.e17.x86_64
	
	
  2.
  (1)echo $PATH
     /usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/bin:/root/bin
     
  (2)作業系統會依據PATH環境變數中所設定的路徑順序
     依序尋找個路徑下是否有要使用的指令

# 第二題
  1.
  (1)這個檔案名稱叫做mail
  
  (2)是屬於root的
  
  (3)屬於mail群組
  
  (4)他是個目錄檔
  
  (5)最後一次被修改的時間為2017/2/16
  
  (6)檔案容量為4096KB
  
  (7)檔案的連結數為3個
  
  (8)擁有者可讀可寫可執行
  
  (9)群組成員可讀可寫可執行
  
  (10)其他人可讀可執行
  
  2.
  (1)數字法
  
     chmod  755 script.sh 
     
  (2)符號法
  
     chmod u=rwx,g=rx,o=rx script.sh
     

# 第三題
  1.實體連結與符號連結的差異
  
    實體連結:
    
    (1)每個檔案都會占用一個inode
    
    (2)使用hard link設定連結檔時
    
	   磁碟的空間與inode的數目都不會改變
	   
	符號連結:
	
	(1)建立一個獨立的檔案
	
	(2)會占用到一個inode和block
	
  2.ll -i /etc/hosts
  
    ln /etc/hosts.real
    
	ll -i /etc/hosts.real hosts
	
  3.ln -s /etc/hosts hosts.symbo
  
    ll -i /etc/hosts /root/hosts.symbo
    

# 第四題
  1.建立一個容量為1GB的xfs檔案系統
  
    mkfs.xfs /dev/sdb
    
  2.建立一個名為mailuser的帳號，並加入 mailgroup 群組，且此帳號不可使用shell登入系統
  
    useradd maildir
    
	passwd 設定密碼
	
	chgrp maildir mailgroup
	
	usermod maildir /sbin/nologin
	
  3.mkdir /srv/linux /srv/maildir
  
    mount /dev/maildir /srv/linux
    
	df -T /srv/linux /srv/maildir
	
  4.ps aux |grep maildir
  
    ls -al /srv/maildir
    
	id mailuser
	
	ps aux |grep mailuser
	
	https://github.com/CHANGYUNEN/107-1-ntcu-linux/blob/midterm/picture.PNG
