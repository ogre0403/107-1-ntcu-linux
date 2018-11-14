# midterm
## 1.

```
利用 變數="變數內容" 來設定ver
利用 echo $變數 顯示ver的值
```
![](https://i.imgur.com/di10UrJ.png)

* OS會根據PATH設定的路徑順序尋找是否有需要使用的指令

![](https://i.imgur.com/uB7nEjj.png)
## 2.
* d=>此為目錄檔

* rwxrwsr-x =>擁有者有讀寫和執行的權限,檔案所屬的群組的人有讀寫和執行的權限,其他人有讀和執行的權限(因為s,其他人在執行此檔時,權限會暫時升為檔案所屬的群組的人)

* 3 =>此檔案有三個連結數

* root => 此檔的擁有者

* mail => 此檔的所屬群組

* 4096 => 此檔的容量

* 2月 16 2017 => 最後一次修改的日期

*  mail/ => 檔名 

若希望所有人皆可以執行script.sh則要把權限從 -rw-r--r-- 變更為 -rws-r--r-- 
需用到的指令為:
```
chmod u+s script.sh 或 chmod 4000 script.sh
```
## 3.
* 實體連結和原文件共享inode,而符號連結是獨立檔案,有自己的inode

![](https://i.imgur.com/vAWNKMn.png)
* "~"為家目錄的相對路徑,建立實體連結後,因為實體連結和原文件共享inode,故應有兩個檔名在使用(三個是因為之前的功課建立過另一個實體連結)

![](https://i.imgur.com/7XGIiyl.png)

* 建立符號連結後,因為而符號連結是獨立檔案,有自己的inode,所以可以看到/etc/hosts 的檔名數不變,而~hosts.symbo擁有自己的inode

## 4.
* 


* 


* 


* mailuser在mailgroup群組中
![](https://i.imgur.com/649OHCZ.png)

* 

