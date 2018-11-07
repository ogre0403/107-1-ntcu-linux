#hw5   流程  
##Q1連結檔案建置行為  
###找出 ln /etc/hosts 的 inode 號碼  
 - 用 ls -li /etc/hosts 這條指令找出 Inode 號碼
 - 我的執行指令後顯示的號碼是: 4213160      
###確認 inode 共有幾個檔案使用
 - 第三欄的連結數顯示 1 ,代表只有一個檔名使用這個 inode   
##Q2建立實體連結  
###找出 ln /etc/hosts /srv/hosts.hard 的 inode 號碼  
 - 用 ln /etc/hosts /srv/hosts.hard 建立硬體連結
 - 用 ls -li /srv/hosts.hard 這條指令找出Inode 號碼  
 - 找出的號碼也是4213160  
###確認 inode 共有幾個檔案使用
 - 第三欄的連結數顯示 1 ,代表只有一個檔名使用這個 inode  
###原因
 - 造成此現象的原因,是由於兩個檔案,藉由硬體連結,強制使用相同的inode號碼,這代表,可以用不同的文件名訪問相同的内容;對文件内容進行修改,會影響到所有文件名;但是,刪除一個文件,不影響另一個文件名的訪問  
##Q3建立符號連結  
###找出 ln /etc/hosts /srv/hosts.hard 的 inode 號碼  
 - 用 ln /etc/hosts /srv/hosts.soft 建立符號連結
 - 用 ls -li /srv/hosts.soft 這條指令找出Inode 號碼
 - 找出的結果是 13029050  
###確認 inode 共有幾個檔案使用
 - 13029050 這支 inode 只有 1 個檔案使用  
###原因
 - 符號連結感覺就像是建立一個捷徑,它只負責導引這件事而已,直接幫你導向到連結的檔案,所以他自己是一個獨立檔案,而不是像硬體連結一樣,連 inode 都一樣