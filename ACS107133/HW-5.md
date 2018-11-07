1.輸入cd ..退到host /，輸入cd etc進入此目錄，再輸入ls -ali hosts，發現inode為4213160，權限為-rw-r--r--

2.輸入ls -ali hosts後出現4213160 -rw-r--r--. "1" --->表示這個inode只有1個檔名在使用

3.輸入ln /etc/hosts/ /srv/hosts.hard來建立實體連結，再輸入ll -i /etc/hosts/ /srv/hosts.hard來查看inode，而inode為4213160

4.輸入ls -ali /srv/hosts.hard出現4213160 -rw-r--r--. "2" --->表示這個inode有2個檔名在使用

5.原因:實體連結是用多個檔案對到一個inode來建立，所以剛剛建立的新檔案的inode會和原本的一樣

6.輸入ln -s /etc/hosts /srv/hosts.soft建立符號連結

7.輸入ll -i /srv/hosts.soft 顯示為13028838 lrwxrwxrwx. 1

8.由上點可得知inode為13028838，且只有1個檔名在使用這個inode

9.原因:如果使用符號連結會另外建立一個inode，所以還是只有一個檔名在使用
