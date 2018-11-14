一.
1.https://ppt.cc/fl08qx

2.PATH說簡單點就是一個字串變數，當輸入命令的時候LINUX會去查詢PATH裡面記錄的路徑。
   而執行檔搜尋的路徑，目錄目錄間會以冒號分隔

二.
1.
    drwxrwsr-x 3 指的是該檔案有3個連結，檔案的擁有者為root，然後所屬群組為mail，
    檔案大小為4096 bytes，最後的修改時間為2017年2月16日，最後他的檔名為mail。

2.
(1)數字:先輸入ls -al script.sh，然後再輸入chmod [-R] 755
(2)符號: 輸入 chmod u+x,g+x,o+x script.sh



三.

1.
(1)實體連結的每個文件都會有一個inode來記錄文件內容的block號碼，想要讀取一個文件，
必須要通過目錄記錄的文件名來指向該文件正確的inode號碼

(2)而符號連結在創建一個獨立的文件，而這個文件會讓數據的讀取指向他 link 的那個文件的文件名！
由於只是利用文件來做為指向的動作， 所以，當來源文件被刪除之後，symbolic link 
的文件會「開不了」， 會一直說「無法打開某文件！」。實際上就是找不到原始「文件名」而已

(3)也就是說實體連結相對於符號連結比較安全，即使某一個目錄下的關連數據被刪除了， 也沒有關係
但實體連結的限制較多，無法做「目錄」的連結，所以在用途上面是比較受限的
反而是符號連結的使用方面較廣。

2.
首先先輸入touch hosts.real建立一個叫hosts.real的檔案
然後輸入 ls -ali 確認該檔案的inode碼



3.
首先先輸入touch hosts.symbol建立一個叫hosts.symbol的檔案




四.
1.使用 gdisk /dev/vda 進入 gdisk 的界面
按下 p 取得目前的分割表，按下 n 進行新增的動作：
在 Partition number 的地方"4"；
在 First sector 的地方也可以直接按下 Enter；
在 Last sector 的地方輸入 +1G 來提供 1G 的容量；
在 Hex code or GUID) 的地方，因此直接按下 [enter] 即可
按下 p 來查閱一下是否取得正確的容量
上述動作觀察後，若沒有問題，按下『 w 』來儲存後離開
系統會詢問『 Do you want to proceed? (Y/N): 』按下 y 來確認即可 
圖片:https://ppt.cc/f61rRx