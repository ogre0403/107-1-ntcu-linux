2.
(1)此為一個目錄信件，檔案擁有者可讀可寫可執行，加入此群組之帳號可可讀可寫可執行，其他
非本人且沒有加入本群組之其他帳號的權限可讀可執行

(2)-rw-r--r-- 應改成-rwx-r-xr-x
   數字法為ls -al script.sh
           chmod 755 script.sh
   符號法為 chmod u=rwx,go=rx script.sh

3.
(1)hard link 限制較多
 不能跨filesystem
 link目錄有問題
 hard link 設定連結檔時，磁碟空間與inode數不變，只在目錄加inode與檔名對應
 而soft link 是建立一個新的獨立檔案，而且會占用inode跟block
(2)ln /etc/hosts /host.real
(3)ln -s /etc/hosts /hosts.symbg
