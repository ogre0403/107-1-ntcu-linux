# (I)
+ 使用*useradd -G mygroup*建立使用者 myuser1,myuser2,myuser3,nouser1,nouser2,nouser3。
+ 此指令可以讓使用者原本就所屬指定群組。
![GITHUB](https://imgur.com/lVSZYPB.jpg "git圖示")
![GITHUB](https://imgur.com/CYpfHDa.jpg "git圖示")
+ 使用 *id* 確認使用者是否存在以及群組所屬
![GITHUB](https://imgur.com/4eQb3rx.jpg "git圖示")
+ 在 /srv 建立myproject資料夾。
+ 使用 *ll* 指令作確認資料夾屬性以及是否存在
![GITHUB](https://imgur.com/WG13MUB.jpg "git圖示")
+ (1)登入myuser1帳號並進入/srv/myproject
+ 使用 *touch* 指令新建myuser1.data之檔案
+ (2)將/usr/bin/ls 複製至/usr/local/bin/myls
+ (3)使用 *ll* 查看 /usr/local/bin 之屬性為(-rwxr)
+ 接著修改其屬性為(-rwsr)
![GITHUB](https://imgur.com/pG5SdJO.jpg "git圖示")
# (II)
+ 使用*grep*尋找rsyslog相關程序資料。
![GITHUB](https://imgur.com/cA30mdP.jpg "git圖示")
+ 使用*top*指令列出相關程序資料
+ 可以得知 PID=1002;NI=0;PR=20。
![GITHUB](https://imgur.com/2ZSVnJ1.jpg "git圖示")
# (III)
+ 使用*find*指令找出/bin及/sbin目錄中，含有 SUID 的特殊檔案檔名。
![GITHUB](https://imgur.com/FAJN0eR.jpg "git圖示")
+ 使用*ls -l*指令列出檔案相關權限後，將資料轉存至 findsuidsgid.txt檔案中。並使用*vi findsuidsgid.txt* 可以發現資料已經儲存到檔案中。
![GITHUB](https://imgur.com/UUdD11u.jpg "git圖示")

