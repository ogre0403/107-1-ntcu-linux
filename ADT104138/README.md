# HW5
## ADT104138 羅苡倫
*****
## 一、關於連結檔案的建置行為：
在 /etc/hosts 檔案，請找出</br>
*	該檔案的 inode 號碼為幾號？</br>
*	這個 inode 共有幾個檔名在使用？</br>
建立實體連結，原始檔案為 /etc/hosts 而新的檔案檔名為 /srv/hosts.hard，請找出</br>
*	/srv/hosts.hard的 inode 號碼為幾號？</br>
*	這個 inode 共有幾個檔名在使用？</br>
*	說明原因。</br>
建立符號連結，原始檔案為 /etc/hosts 而新的檔案檔名為 /srv/hosts.soft，請找出</br>
*	/srv/hosts.soft的 inode 號碼為幾號？</br>
*	這個 inode 共有幾個檔名在使用</br>
*	說明原因</br>

1.利用	ls -li /etc/hosts
	指令，可以達成需求，結果顯示此檔案的inode號碼為6311995號，且連結數為1。</br>
![新增](https://i.imgur.com/8AjzCXr.jpg)</br>

2.利用
		ln /etc/hosts /srv/hosts.hard
	指令，可以達成需求，結果顯示此實體連結之檔案的inode號碼為6311995，且連結數為2。</br>
![新增](https://i.imgur.com/kvy7OwS.jpg)</br>
	因為hardlink是在某個目錄下新增一筆檔名連結到某inode號碼的關聯紀錄，也就是說此連結跟原檔案是連結到同一個inode號碼，所以兩個檔案資訊自然都一樣。</br>

3.利用
		ln -s /etc/hosts /srv/hosts.soft
	指令，可以達成需求，結果顯示此符號連結之檔案的inode號碼為416115，且連結數為1。</br>
![新增](https://i.imgur.com/S3zKVdH.jpg)</br>
	因為softlink是單純建立一個獨立的檔案，來指向其連結檔案，由於只是利用檔案作為指向的動作，所以inode號碼及檔案連結數就不相同了，且作為指向的原檔案若刪除，那麼這個符號連結是開啟不了的。</br>

# 參考資料：[點擊這裡](http://linux.vbird.org/linux_basic/0230filesystem.php#link "參考資料")
# 感謝觀看 The End
