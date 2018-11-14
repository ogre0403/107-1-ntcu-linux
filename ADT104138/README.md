# 期中考
## ADT104138 羅苡倫
*****
##上機考題目
*****
#1.(20%)
*設定 ver 變數，內容為『 my kernel version is 3.xx 』，其中 3.xx 為 uname -r 輸出的資訊，並顯示出ver變數的值。(10%)</br>

利用$(指令)，在設定變數中存入變數資訊，最後用echo顯示出變數的值。</br>
![新增](https://i.imgur.com/4V7HG9y.png)</br>

*請顯示目前PATH環境變數的值為何，並說明PATH的功用為何? (10%)</br>

利用echo指令顯示出PATH變數的值。</br>
PATH的功用就是，當使用者作出命令的時候，linux會去PATH變數裡面的路徑找其輸入的命令。因此，也可以自定義路徑，在某些情況下自定義路徑會方便許多。</br>
![新增](https://i.imgur.com/7eKupxa.png)</br>

#2.(20%)
*有一個檔案的屬性權限為 drwxrwsr-x 3 root mail 4096 2月 16 2017 mail/，請說明此檔案的特性。(10%)</br>

從左到右依序是 1.檔案屬性 2.檔案數 3.擁有者 4.所有者群組 5.大小 6.建檔日期 7.檔名</br>
以下分述：</br>
drwxrwsr-x，此為檔案屬性，可分別用1/3/3/3分開看，第一個字代表這個檔案為目錄或者其他檔案，此例d極為目錄的意思。而後面三個分別是在擁有人、同群組使用者、其他使用者的權限，r代表可以讀，w代表可以寫，x代表可以執行。</br>

3，檔案數，表示有多少檔案在這個目錄。(若為1通常是檔案)</br>

root，代表此檔案(目錄)的擁有人，此例即為root。</br>

mail，代表此檔案的群組。</br>

4096，代表此檔案的大小。</br>

2月 16 2017，代表此檔案的建檔日期。</br>

mail/，代表檔案(目錄)名。</br>

*假設有一個script.sh檔案的權限為-rw-r--r--，若希望讓所有人可以執行該檔案，請問該如何下達指令？請使用數字法與符號法各操作一次。(10%)</br>

利用chmod指令。(因為題目要求執行而已，所以用改成全部人所有權線統一)</br>
數字法：chmod 777 script.sh</br>
符號法：chmod u=rwx g=rwx o=rwx script.sh</br>

#3.(20%)
*說明實體連結與符號連結的差異。</br>

hardlink是在某個目錄下新增一筆檔名連結到某inode號碼的關聯紀錄，也就是說此連結跟原檔案是連結到同一個inode號碼。</br>
softlink是單純建立一個獨立的檔案，來指向其連結檔案，由於只是利用檔案作為指向的動作，所以inode號碼及檔案連結數就不相同了，且作為指向的原檔案若刪除，那麼這個符號連結是開啟不了的。</br>

*在家目錄下建立一個檔名為 hosts.real 的實體連結指到 /etc/hosts？ (請用相對路徑表示家目錄) (5%)</br>
利用ln以及ln -s 指令即可完成，另外相對路徑家目錄符號是 ~ 。</br>

![新增](https://i.imgur.com/2phgRq3.png)</br>

#4.(40%)
#請依下述情境完成系統操作後再用相關指令進行驗證，請抓驗證指令的圖：
#建立一個容量為1GB的xfs檔案系統，每次開機都能夠自動的掛載到 /srv/maildir，且該目錄是給 mailgroup 這個群組共用的，其他人不可具有任何權限。再建立一個名為mailuser的帳號，並加入 mailgroup 群組，且此帳號不可使用shell登入系統。

在虛擬機器設定值裡新增一個虛擬硬碟配置1GB，然後利用mkfs.xfs建立XFS系統，mkdir創建好maildir目錄後，chgrp設定群組，chmod更改權限，useradd建立帳號並指定群組。</br>
自動掛載需要改寫/etc/fstab才能實現，可以利用vim編輯。</br>
利用更改shell成nologin就可以達成不可使用shell登入系統。</br>

![新增](https://i.imgur.com/Ign3z6q.png)</br>
![新增](https://i.imgur.com/ECbDop0.png)</br>
![新增](https://i.imgur.com/vvh376L.png)</br>
![新增](https://i.imgur.com/mQfDcMO.png)</br>


*請用`df`指令配合`human-readable`選項，顯示有1GB的檔案系統正掛載到`/srv/maildir` (8%)</br>
![新增](https://i.imgur.com/PezU7yu.png)</br>

*請用`grep`驗證有設定開機自動掛載。(8%)</br>
![新增](https://i.imgur.com/I55mE0z.png)</br>

*請用`ls`查詢`/srv/maildir`屬性，確認可以讓`mailgroup`群組共用，而其他人不具任何權限。(8%)</br>
![新增](https://i.imgur.com/cYvM0yY.png)</br>

*請用`id`檢查`mailuser`使用者有在`mailgroup`. (8%)</br>
![新增](https://i.imgur.com/cgfG9vL.png)</br>

*請用`grep`驗證此帳號無法透過shell登入。(8%)</br>
![新增](https://i.imgur.com/deZOhex.png)</br>
