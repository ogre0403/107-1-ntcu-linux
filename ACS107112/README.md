![](https://i.imgur.com/csrQVyj.png)
+ 創建三個使用者
![](https://i.imgur.com/FphnW1X.png)
+ 設定密碼 ItIsExam
![](https://i.imgur.com/No2z7V9.png)
+ 刪掉examuser3
![](https://i.imgur.com/V9CuIdj.png)
+ 刪掉examuser1
![](https://i.imgur.com/txeLUY0.png)
![](https://i.imgur.com/FLx9ZYZ.png)
![](https://i.imgur.com/kpQj1Xb.png)
![](https://i.imgur.com/8rF4N84.png)
+ 把examuser1創建回來
+ 並設定密碼
![](https://i.imgur.com/fd02Jdx.png)
+ 創建examuser4
![](https://i.imgur.com/N25tID9.png)
+ 並設定密碼
![](https://i.imgur.com/UPljQpU.png)
+ 使用 root 將 /etc/securetty 複製給 examuser4
![](https://i.imgur.com/GQmGIRt.png)
![](https://i.imgur.com/YJTcS9r.png)
![](https://i.imgur.com/3RLrLn8.png)
+ 建立一個名為 /examdata/change.txt 的空檔案，這個檔案的擁有者為 sshd，擁有群組為 users，sshd 可讀可寫，users 群組成員可讀， 其他人沒權限。且這個檔案的修改日期請調整成 2012 年 12 月 21 日



+ 因為忘了截圖，沒有圖片請見諒
#root身分建立檔案與權限 
+ 輸入cd /dev/shm/進入資料夾
+ 輸入mkdir unit05建立檔案
+ 輸入chmod u=rwx,g=rwx,o=rx unit05</li>
+ 輸入cd unit05進入</li>
+ 輸入mkdir 分別加上建立四個資料夾 </li>
+ 修改dir1,dir2,dir3,dir4權限如下
	dir1→chmod u=rwx,g=rx,o=r dir1
	dir2→chmod u=rwx,g=rx,o=x dir2 
	dir3→chmod u=rwx,g=rx,o=rx dir3
	dir4→chmod u=rwx,g=rwx,o=rwx dir4 </li>
<li>複製/etc/hosts至 dir1,dir2,dir3,dir4，將檔名改為 file1,file2,file3,file4
	dir1→cp /etc/hosts /dev/shm/unit05/dir1/file1
	dir2→cp /etc/hosts /dev/shm/unit05/dir2/file2
	dir3→cp /etc/hosts /dev/shm/unit05/dir3/file3
	dir4→cp /etc/hosts /dev/shm/unit05/dir4/file4 </li>
#修改file1權限
<li>輸入cd unit05/dir1/</li>
<li>輸入chmod u=rw,g=r,o=r file1</li>
#修改file2權限
<li>輸入cd unit05/dir2/</li>
<li>輸入chmod u=rw,g=r,o=r file2</li>
#修改file3權限
<li>輸入cd unit05/dir3/</li>
<li>輸入chmod u=rw,g=rw,o=rw file3</li>
#修改file4權限
<li>輸入cd unit05/dir4/</li>
<li>輸入chmod u=rwx,g=rwx,o=rwx file4</li>
#請使用 ls -l /dev/shm/unit05/dir[1-4] 依據輸出的結果說明為何會產生這些問題？
<li>dir1唯讀</li>
<li>dir2是只能執行，無法讀</li>
<li>dir3無法修改</li>
<li>dir4可以任意執行</li>
#用 ls -l /dev/shm/unit05/dir1/file1，依序將上述的檔名由 dir1/file1 ~ dir4/file4 執行，依據產生的結果說明為何會如此？
<li>dir1,dir2唯讀</li>
<li>dir3可讀可修改</li>
<li>dir4無法使用</li>
#用 vim /dev/shm/unit05/dir1/file1 ~ vim /dev/shm/unit05/dir4/file4，嘗試儲存 (或強制儲存)，說明為何可以/不可以儲存？
<li>other沒有改動unit05內4個資料夾的修改權限</li>
</ol> 
