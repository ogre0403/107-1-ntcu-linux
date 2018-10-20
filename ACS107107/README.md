#第一題
##一.建立三個用戶,要先登入root帳戶才能建立喔!利用useradd 帳號以及passwd 密碼來建立
##![](https://i.imgur.com/ay3PESX.jpg)
##二.建立完之後利用id 帳號來確認
##![](https://i.imgur.com/YR2jnv1.jpg)
##三.利用userdel -r examuser3刪除examuser3的資料(包括家目錄及郵件目錄)
##![](https://i.imgur.com/qtiLWYL.jpg)
##四.當用userdel examuser1時,並沒有刪除所有檔案
##![](https://i.imgur.com/eX41DZr.jpg)
##五.利用下圖中的指令來還原
##![](https://i.imgur.com/jz6HHHM.jpg)

#第二題
##一.根據上一題的作法建立examuser4使用者
##二.之後呢就使用root將/etc/securetty複製給examuser4
##![](https://i.imgur.com/BDbJre7.jpg)
##三.然後回到root後再利用chmod u=rwx,g=rwx,o=rwx securetty來更改權限就完成了
##![](https://i.imgur.com/pejTIHE.jpg)
##四.建立一個名為 /examdata/change.txt 的空檔案
##![](https://i.imgur.com/CKNklFx.jpg)
##五.之後依照下圖完成修改使用者,修改群組,修改權限的步驟
##![](https://i.imgur.com/ForURVz.jpg)
##六.最後是時間的調整
##![](https://i.imgur.com/X6fzCtv.jpg)
#第三題
##一.按照步驟把權限給慢慢設定好,詳細方法請看上一題
##![](https://i.imgur.com/9tMgYUi.jpg)
##![](https://i.imgur.com/pozDE0S.jpg)
##二.之後登入一般用戶並開啟ls -l /dev/shm/unit05/dir[1-4]
##![](https://i.imgur.com/4tAbsaK.jpg)
##三.依據結果顯示出,由於examuser2為其他人(others)所以dir1的結果是只能讀而已,dir2只能執行而已,所以什麼都看不到,dir3正常顯示只是不能修改而已,dir4由於權限都開放了所以就能自由使用了
##至於檔案的部分,執行後如圖:
##![](https://i.imgur.com/IXHO4I5.jpg)
##四.可以看出dir1中的檔案要顯示出來是有問題的,其實就跟剛剛的觀念一樣用普通用戶登入由於不屬於user也不屬於group,所以根據前面的調整權限,只有唯讀而已,dir2目錄的檔案也是唯獨,dir3目錄檔案則是可讀可寫的,dir4目錄檔案都沒辦法做任何事情
##五.而在檔案儲存的部分先用了vim /dev/shm/unit05/dir1/hosts,之後要用:w儲存時發生了問題,原因在於使用者權限並沒有開放給其他人可寫的指令
##![](https://i.imgur.com/f2tM3Lo.jpg)
##之後再使用了vim /dev/shm/unit05/dir2/hosts來儲存看看,結果也不行,因為也只有唯讀的權限而已
##再用vim /dev/shm/unit05/dir3/hosts試試,這時由於擁有w得權限,所以非常正常
##最後用vim /dev/shm/unit05/dir4/hosts試,由於什麼權限都沒有,所以也沒辦法正常儲存



