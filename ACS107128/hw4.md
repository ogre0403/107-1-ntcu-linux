ACS107128 張云榮 第四次作業
-----------------------------
因為原本的電腦是ubuntu
為了不在原本的電腦上刪了又加加了又刪使用者
所以我又安裝了一個centos的小系統
這次的作業在這個小系統上做

1.
建立群組名稱為：mygroup,nogroup
使用groupadd這個指令
2.
建立帳號名稱為：myuser1,myuser2,myuser3,通通加入mygroup
原本想改useradd的參考檔
但後來想想還是算了,直接useradd-G 的參數下去改好像比較快
（真的要好好看鳥哥第十三章呢）
3.
建立帳號名稱為 nouser1,nouser2,nouser3
如第二步驟

4.
mkdir建立一個新的目錄,用chgrp去改變檔案的擁有組別.

5.
到另個tty去登入使用者myuser1,touch一個檔案叫做myuser1.data,然後logout

6.
cp usr/bin/ls 至usr/local/bin/myls 
/*
小補充：
bin   ：這是放例如： ls, mv, rm, mkdir, rmdir, gzip, tar, telnet, 及 ftp 等等常用的執行檔的地方。
*/
當用別的使用者登入時,竟然可以用myls查閱本來不能開的檔名資訊。

7.8.才剛讀完bash但先跳去寫shell
重導向輸出還沒讀完.......剛好作業期限到了呢.....
