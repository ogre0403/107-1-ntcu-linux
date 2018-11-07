# 1.關於連結檔案的建置行為:
![](https://i.imgur.com/2ioaCi5.png)
* ## 圖中可見inode為3173595,且有一個檔名在使用
![](https://i.imgur.com/GGxFhI7.png)
* ## 複製實體連結
![](https://i.imgur.com/bjRqrEK.png)
* ## inode也為3173595,有2檔名在使用,因為實體連結和原文件共享inode
![](https://i.imgur.com/j1BmQSR.png)
* ## 複製符號連結
* ## inode為551644,有一個檔名使用,因為符號連結是獨立檔案,有自己的inode