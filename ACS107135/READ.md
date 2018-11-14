## 1.<br>
### (Q1): 設定 ver 變數，內容為『 my kernel version is 3.xx 』，其中 3.xx 為 uname -r 輸出的資訊，並顯示出ver變數的值。(10%)<br>
Ans:<br>
1.指令:" uname -r "觀察其輸出的資訊( 3.xx ) <br>
2.指令:" ver= my kernel version is 3.xx "(變數='變數內容')，設定ver變數。 <br>
3.指令:" echo $ver "顯示 ver 變數的值<br><br>

### (Q2):請顯示目前PATH環境變數的值為何，並說明PATH的功用為何? (10%)<br>
Ans:<br>
指令:" echo $PATH " (注意"PATH"必須皆為大寫!) 顯示目前PATH環境變數的值。<br>
說明: 環境變數" PATH "為執行檔搜尋的路徑~目錄與目錄中間以冒號(:)分隔，由於執行檔/指令的搜尋是依序由 PATH 的變數內的目錄來查詢，所以，目錄的順序也是重要的。<br><br>

## 2.<br>
### (Q1):有一個檔案的屬性權限為 drwxrwsr-x 3 root mail 4096 2月 16 2017 mail/，請說明此檔案的特性。(10%)<br><br>
Ans:<br>
此檔案的擁有者為' root '，群組設定為' mail '。<br><br>
最前面'd'代表橫面的檔名為目錄檔。<br>
中間的" 'rwx''rws''r-x' "以每3個為一組，由左而右分別為擁有者(root)、群組(mail)、其他人(非root、非mail)的權限，其中:<br>
' r '代表閱讀權限，<br>
' w '代表修改權限，<br>
' x '代表執行權限，<br>
' s '代表為" SUID "，在此題代表只要任何人擁有x的權限，當用戶執行這個檔案時，就會自動透過 SUID 轉換身分成為 group 的一員，亦即變成了 群組' mail '的一員。 (雖然other的權限只有 r 與 x ，但是當other執行此檔案時會自動轉換為擁有群組 mail 的身分，所以此時就暫時擁有了 w 的權限。)<br><br>
此檔案的容量為4096(bits)。
此檔案的最後修修改時間為2017 2月 16日。<br>
此檔案的檔名為mail。<br><br>

### (Q2):假設有一個script.sh檔案的權限為-rw-r--r--，若希望讓所有人可以執行該檔案，請問該如何下達指令？請使用數字法與符號法各操作一次。(10%)<br><br>
Ans:<br>
數字法:" chmod 755 script.sh " ( r=4 , w= 2 , x=1 )<br>
符號法:" chmod u=rwx, g=rx, o=rx script.sh "  (u= user, g= group, o= other)<br><br>

## 3.<br>
### (Q1):說明實體連結與符號連結的差異。(10%)<br>
Ans: <br>
" Hard Link "是把一個檔案新增出一個不同的檔名，但是這2個不同的檔名所開啟的是同一個檔案，所以他們的inode會是相同的(為同一檔案)。<br>
" Symbolic Link "是建立一個新檔案做為另一個檔案開啟的捷徑，2者為不同的檔案，所以自然inode就不會相同(為不同檔案)。<br><br>

### (Q2):在家目錄下建立一個檔名為 hosts.real 的實體連結指到 /etc/hosts？ (請用相對路徑表示家目錄) (5%)<br>
Ans; <br>
用指令"ln"來建立實體連結(這裡會先發現一般使用者會產生權限不足的問題，所以必須先把使用者切換為root再來進行)<br>
指令:" In /etc/hosts /home/hosts.real "<br>

### (Q3):在家目錄下建立一個檔名為 hosts.symbo 的符號連結指到 /etc/hosts？ (請用相對路徑表示家目錄 (5%)<br>
Ans:<br>
用 ln -s 指令來建立符號連結(Symbolic Link) (要切換為root)<br>
指令:"　In -s /etc/hosts /home/hosts.symbo "<br><br>

## 4.<br>
### (Q1):請用`df`指令配合`human-readable`選項，顯示有1GB的檔案系統正掛載到`/srv/maildir` (8%)<br>
Ans:<br>
human-readablevm選項:"-h"<br>
![image](https://github.com/ACS107135/107-1-ntcu-linux/blob/midterm/ACS107135/photo/1.PNG)<br>






