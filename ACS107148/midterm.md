## Midterm

* 第一題:
   * 1.輸入"echo $ver"顯示變數，用"變數=變數內容"，修改變數內容，用"uname -r"看要輸入的知訊，最後再用"echo $ver"看內容。

![](https://i.imgur.com/Q41L18Z.png)
* 2.![](https://i.imgur.com/S5CEBbE.png)
* PATH 功用：執行檔搜尋的路徑~目錄與目錄中間以冒號(:)分隔，由於執行檔/指令的搜尋是依序由PATH的變數內的目錄來查詢，所以，目錄的順序也是很重要的。



* 第二題:
     * drwxrwsr-x 3 root mail 4096 2月 16 2017 mail/，前面的"d"代表後面的檔名為目錄檔，後面的英文字母表示權限，此檔案為所有人接可讀( r )、可寫(w)、可執行(x)。
     * 數字法：輸入"chmod 755 script.sh"即可讓所有人執行該檔。
     * 符號法：輸入"chmod a+x script.sh"即可讓所有人執行該檔。

* 第三題:
* 1. 
   * 下圖為實體連結
![](https://i.imgur.com/5H9P7xP.png)

     下圖為符號連結
![](https://i.imgur.com/twcvH5t.png)


  差異：建立出來的符號連結是一個獨立的檔案，所以不會像實體連結一樣共用同一個inode。

* 2.
   
   * 輸入"ln /etc/hosts /srv/hosts.real"即可做實體連結。
* 3. 
   * 輸入"ln -s /etc/host /srv/hosts.symbo"即可做符號連結。 

* 第四題:
* 1.
![](https://i.imgur.com/BQGI4pq.png)
* 2.

* 3.
![](https://i.imgur.com/YjH9xfb.png)
* 4.
![](https://i.imgur.com/51u34Xh.png)
* 5.