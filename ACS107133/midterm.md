1.

設定 ver 變數，內容為『 my kernel version is 3.xx 』，其中 3.xx 為 uname -r 輸出的資訊，並顯示出ver變數的值。

>> 1.首先先輸入uname -r 來查看資訊為3.10.0-862.e17.x86_64

>> 2.之後要設定ver這個變數，輸入ver="my kernel version is 3.10"，要加上引號因為字中間有空白符號

>> 3.接著輸入echo $ver 來查看是否更改成功，可發現已顯示為my kernel version is 3.10

請顯示目前PATH環境變數的值為何，並說明PATH的功用為何?

>> 1.輸入echo $PATH還查看環境變數的值為/usr/local/sbin:usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin:/root/bin

>> 2.環境變數PATH的功用是執行檔搜尋的路徑，執行檔或指令的搜尋是依序PATH此環境變數內的目錄來查詢的

2.

有一個檔案的屬性權限為 drwxrwsr-x 3 root mail 4096 2月 16 2017 mail/，請說明此檔案的特性?

>> 由題目中的權限可得知此檔案使用者為『root』其權限為『可讀可寫可執行』，則所屬群組為『mail』權限也為『可讀可寫可執行』，『others』則為『可讀可執行但不可寫』

假設有一個script.sh檔案的權限為-rw-r--r--，若希望讓所有人可以執行該檔案，請問該如何下達指令？請使用數字法與符號法各操作一次。

>> 1.數字法 : 輸入chmod 777 script.sh ，可將此檔案的所有人的權限改為『可讀可寫可執行』，『4』代表可讀，『2』代表可寫入，『1』代表可執行

>> 2.符號法 : 輸入chmod u=rwx,g=rwx,o=rwx script.sh，可將此檔案的所有人的權限改為『可讀可寫可執行』，『u』代表使用者權限，『g』代表群組權限，『o』代表others的權限

3.

說明實體連結與符號連結的差異。

>> 『符號連結』會建立一個獨立檔案和inode，且新建立的檔案會讀取原本檔案的檔名

>>『實體連結』用多個檔案對到一個inode來建立，檔名只與目錄有關，而檔案內容與 inode 有關

在家目錄下建立一個檔名為 hosts.real 的實體連結指到 /etc/hosts？

>> 1.首先輸入 vi ~/hosts.real 建立一個檔案，之後按ESC鍵，退出編輯，輸入 :wq 離開

>> 2.輸入ln hosts.real ./etc/hosts來建立實體連結

在家目錄下建立一個檔名為 hosts.symbo 的符號連結指到 /etc/hosts

>> 1.輸入 vi ~/hosts.symbo 建立一個檔案，之後按ESC鍵，退出編輯，輸入 :wq 離開

>> 2.輸入ln -s hosts.symbo ./etc/hosts來建立符號連結

4.

請依下述情境完成系統操作後再用相關指令進行驗證，請抓驗證指令的圖：

建立一個容量為1GB的xfs檔案系統，每次開機都能夠自動的掛載到 /srv/maildir，且該目錄是給 mailgroup 這個群組共用的，其他人不可具有任何權限。再建立一個名為mailuser的帳號，並加入 mailgroup 群組，且此帳號不可使用shell登入系統。
