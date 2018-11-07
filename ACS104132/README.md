一.關於連結檔案的建置行為:
在 /etc/hosts 檔案，請找出
1.該檔案的 inode 號碼為幾號？
67173736
(如圖1)

2.這個 inode 共有幾個檔名在使用？
1


二.建立實體連結，原始檔案為 /etc/hosts 而新的檔案檔名為 /srv/hosts.hard，請找出

1./srv/hosts.hard的 inode 號碼為幾號？
67173736
(如圖2)

2.這個 inode 共有幾個檔名在使用？
2

3.說明原因。
因為是hard link，磁碟的空間與 inode 的數目都不會
改變,只是在目錄裡加一筆inode與檔名的對應


三.建立符號連結，原始檔案為 /etc/hosts 而新的檔案檔名為 /srv/hosts.soft，請找出
1./srv/hosts.soft的 inode 號碼為幾號？
100673490
(如圖3)

2.這個 inode 共有幾個檔名在使用
1

3.說明原因
因為檔案會指向目的檔案也就是他的link的那個檔案,故inode只會有一個,就是他指向的那個檔案


