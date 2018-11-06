##1-1在 /etc/hosts 檔案，請找出
#該檔案的 inode 號碼為幾號？
*"ls -ali /etc/hosts"→ inode 號碼為+16816552
#這個 inode 共有幾個檔名在使用？
*1個

##1-2建立實體連結，原始檔案為 /etc/hosts 而新的檔案檔名為 /srv/hosts.hard，請找出
#/srv/hosts.hard的 inode 號碼為幾號？
*"ln /etc/hosts /srv/hosts.hard"→"ls -ali /srv/hosts.hard"→ inode 號碼為+16816552
#這個 inode 共有幾個檔名在使用？
*2個
#說明原因
*因為建立的是實體連結，所以inode號碼是一樣的

##1-3建立符號連結，原始檔案為 /etc/hosts 而新的檔案檔名為 /srv/hosts.soft，請找出
#/srv/hosts.soft的 inode 號碼為幾號？
*"ln -s /etc/hosts /srv/hosts.soft"→"ls -ali /srv/hosts.soft"→ inode 號碼為+25245520
#這個 inode 共有幾個檔名在使用
*1個
#說明原因
*符號連結=>建立捷徑，建立一個獨立的檔案，而這個檔案會讓資料的讀取指向他link的那個檔案的檔名！