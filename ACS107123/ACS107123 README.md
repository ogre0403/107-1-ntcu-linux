(一)連結檔案的建置行為:
(1)輸入 ls -ali /etc/hosts*
(2)inode號碼: 5848692  
(3)僅其中一個檔名需要用inode

(二)建立實體連結
原始檔案:  /etc/hosts 
新案檔名:  /srv/hosts.hard  
(1)輸入ln /etc/hosts /srv/hosts.hard建立實體連結
(2)輸入cd /srv進入srv 
(3)輸入ls -ali hosts.hard
(4)inode號碼: 12810757   
(5)其中兩個檔名用inode
(6)實體連結和原始文件會共用相同inode
  
(三)建立符號連結
原始檔案:  /etc/hosts
新案檔名:  /srv/hosts.soft  
(1)輸入ln -s /etc/hosts /srv/ hosts.soft建立符號連結
(2)輸入ls -ali /srv/hosts.soft
(3)inode號碼: 12625702 
(4)與/etc/hosts的inode名稱不同
(5)重新建立新的inode   