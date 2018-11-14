## 第一題
1.
+ 用PATH=$:${my kernel version is 3.xx}來設定 ver 變數，內容為『 my kernel version is 3.xx 』
2.
+ 用env來顯示顯示目前PATH環境變數的值
+ PATH的能功為執行檔案搜尋的路徑
## 第二題
1.
+ 第一個字元d代表後面的檔名為目錄檔
+ owner的權限為可讀，可寫入、編輯、修改，可執行
+ group的權限為可讀，可寫入、編輯、修改，並在執行者執行的過程中獲得該程式群組的權限
+ others的權限為可讀，可執行
2.
數字法
+ 用chmod 744 script.sh 使"所有人"可執行該檔案
符號法
+ 用chmod u+x script.sh 使"所有人"可執行該檔案
## 第三題
1.
+ 實體連結:hard link 只是在某個目錄下新增一筆檔名連結到某 inode 號碼的關連記錄而已，只要有任何一個目錄下存在著關連資料，那麼該檔案就不會不見，用 ln 如果不加任何參數的話，那麼就是 Hard Link。不能跨Filesystem，link目錄會有問題
+ 符號連結:Symbolic link 是在建立一個獨立的檔案，而這個檔案會讓資料的讀取指向他 link 的那個檔案的檔名
2.
+ 實體連結
+ 先用cd ../home 更換至家目錄
+ 用mkdir hosts.real 建立一個新的目錄
+ 用ln /etc/hosts hosts.real 建立實體連結
3.
+ 符號連結
+ 先用cd ../home 更換至家目錄
+ 用mkdir hosts.real 建立一個新的目錄
+ ln -s /etc/hosts hosts.real 建立實體連結
## 第四題
1.
+ 用mkfs.xfs建立檔案系統
+ 用mount  
 ![](https://i.imgur.com/H55p6ul.jpg)
 
 ![](https://i.imgur.com/rVxmWor.jpg)

