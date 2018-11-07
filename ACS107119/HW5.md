
#1
1.輸入ls -li /etc/hosts 後出現4213160 -rw-r--r--. "2" 表示這個inode只有2個檔名在使用。

2.輸入ln /etc/hosts/ /srv/hosts.hard建立實體連結，再打ll -i /etc/hosts/ /srv/hosts.hard來查看inode，而inode為4213160。

3.輸入ls -ali /srv/hosts.hard出現4213160 -rw-r--r--. "2" 表示這個inode有2個檔名在使用。

4.因為實體連結是用多個檔案對同一個inode建立，所以剛剛建立的新檔案的inode會和之前的一樣。

5.輸入ln -s /etc/hosts /srv/hosts.soft建立符號連結。

6.輸入ll -i /srv/hosts.soft 顯示為13026252 lrwxrwxrwx. 1。

7.由上點可得知inode為130226252，且只有1個檔名在使用這個inode。

8.因為文件A和文件B的inode號碼雖然不一樣，但是文件A的內容是文件B的路徑。讀取文件A時，系統會自動將訪問者導向文件B.因此，無論打開哪一個文件，最終讀取的都是文件B。


![](https://ppt.cc/f5W84x@.png)
  