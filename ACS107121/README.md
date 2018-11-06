## 連結檔案建置行為
###找出 ln /etc/hosts 的 inode 號碼
使用指令找出inode編碼 ls -li /etc/hosts
得到inode 編碼 1066954
###確認 inode 共有幾個檔案使用
顯示1,只有1個
##Q2建立實體連結
###找出 ln /etc/hosts /srv/hosts.hard 的 inode 號碼
先建立硬體連結ln /etc/hosts /srv/hosts.hard 然後ls -li /srv/hosts.hard找inode編碼
編碼 1066954
###確認 inode 共有幾個檔案使用
顯示2,有2個
###原因
因為inode碼被hosts跟hosts.hard共用 所以有兩個
##Q3建立符號連結
###找出 ln /etc/hosts /srv/hosts.hard 的 inode 號碼
ln /etc/hosts /srv/hosts.soft 建立符號連結接著用ls -li /srv/hosts.soft找出Inode
編碼 1066954
###確認 inode 共有幾個檔案使用
顯示3,有3個
###原因
因為inode碼被hosts跟hosts.hard跟hosts.soft共用 所以有三個