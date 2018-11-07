1.關於連結檔案的建置行為:
    
(1)輸入 ls -ali /etc/hosts*找到incode號碼為5848692  
(2)只有一個檔名在使用該inode
      
2.建立實體連結，原始檔案為 /etc/hosts 而新的檔案檔名為 /srv/hosts.hard，請找出  
   
(1)輸入ln /etc/hosts /srv/hosts.hard去建立實體連結，然後再輸入 cd /srv進入srv 
然後再輸入ls -ali hosts.hard就可以找到incode號碼為12810757   
(2)有兩個檔名在使用該inode
(3)實體連結和原文件共享相同的inode
  
3.建立符號連結，原始檔案為 /etc/hosts 而新的檔案檔名為 /srv/hosts.soft，請找出  
(1)輸入 ln -s /etc/hosts /srv/ hosts.soft來建立符號連結，然後再輸入ls -ali /srv/hosts.soft就可以找到incode號碼為12625702。
(2)一個   
(3)因為跟/etc/hosts的inode名稱不同，所以會重新建立新的inclode   