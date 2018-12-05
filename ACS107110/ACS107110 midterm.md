1.
--echo $var(設定一個名為var的變數)
--var=my\ kernel\ version\ is\ $(uname -r)
--echo ${var}(即可顯示var變數內容為何?)
##/usr/local/bin:/bin:/usr/local/sbin::/usr/sbin:/home/yizhen/ .local/bin:/home/yizhen/bin var
(上述的值說明使用$PATH環境變數，可以搜尋執行檔的的路徑~目錄與目錄中間以冒號空格

2.-1drwxrwsr-x 3 root mail 4096 2月 16 2017 mail/
A.drwxrwsr-x --說明權限問題，看到前面為d英文字母顯示後面檔名為標頭檔
使用者可讀可寫可修改，群組有使用到SGID權限，群組所有人都可讀寫修改，其他人可讀可執行但不能寫
B.2 --顯示檔案連結數
C.root --該檔案的擁有者
D.mail --該檔案所屬的群組
E.4096 --該檔案的容量
F.2月 16--剛檔案最後一次被修改的時間日期
G.檔名

2.-2
*符號表示
--chmod u=rwx,g=rwx,o=rwx script.sh
*數字表示
--chmod 777 script.sh

3.
**實體連結--hardlink在某目錄下新增一筆檔名連結到某inode號碼的關聯紀錄，但不能跨filesystem和不能link目錄
**符號連結--symbolic link--在建立一個獨立的檔案，而這個檔案會讓資料的讀取指向他link的那個檔案的檔名，所以當來源檔案被刪除，symbolic link的檔案會開不了
**實體連結
--cd /home(cd回到家目錄)
--touch hosts.real(建立一個檔案)
--cd/(cd回到根目錄)
--ln ~/hosts.real /etc/hosts(建立一個實體連結)
**符號連結
--cd /home(cd回到家目錄)
--touch hosts.symbo(建立一個檔案)
--cd/(cd回到根目錄)
--ln -s ~/host.symbo /etc/hosts(建立一個符號連結)

4.
附圖
