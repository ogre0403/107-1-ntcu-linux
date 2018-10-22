HW3

#第一題
1.建立三個用戶examuser1, examuser2, examuser3
  以root的身分登入
  
  useradd examuser1
  passwd examuser1
  設定密碼為ItIsExam
  
  useradd examuser2
  passwd examuser2
  設定密碼為ItIsExam
  
  useradd examuser3
  passwd examuser3
  設定密碼為ItIsExam
  
2.刪除examuser3 同時將這個帳號的家目錄與郵件檔案同步刪除
  userdel -r examuser3
  
3.examuser1 不小心被管理員刪除了
  userdel examuser1
  輸入ll
  觀察出現的一組數字
  利用 useradd -u 那組數字 -U examuser1 來還原

#第二題
1.建立examuser4使用者帳號，密碼任意
  以root的身分登入
  useradd examuser4
  passwd examuser4
  設定密碼為exam4
  
2.使用 root 將 /etc/securetty 複製給 examuser4
  cp /etc/securetty /home/examuser4/
  接下來更改權限
  chmod u=rwx, g=rwx, o=rwx
  
3.建立一個名為 /examdata/change.txt 的空檔案
  cd/ (回到家目錄)
  mkdir examdata (建立examdata資料夾)
  cd examdata (進入examdata)
  touch change.txt(建立檔案)
  
4.設定檔案的擁有者為 sshd
  chown sshd change.txt

5.設定擁有群組為 users
  chgrp users change.txt
  
6.設定權限
  chmod u=rw, g=r, o= change.txt
  
7.修改日期請調整成 2012 年 12 月 21 日
  touch -t 201212210000 change.txt
  
#第三題
1.按照步驟一個個設定

2.使用一般使用者 的身份進行各項工作
  登入剛才僅存的examuser2
   
  ls -l /dev/shm/unit05/dir1
  ls -l /dev/shm/unit05/dir2
  ls -l /dev/shm/unit05/dir3
  ls -l /dev/shm/unit05/dir4

  examuser2為其他人 所以dir1只能讀
  dir2只能執行
  dir3可讀可執行
  dir4可讀可修改可執行
  
  
3.輸入ls -l /dev/shm/unit05/dir1/file1 ，依序將上述的檔名由 dir1/file1 ~ dir4/file4 執行
  dir1只能讀
  dir2只能讀
  dir3可讀可修改
  dir4沒有任何權限
  
4.使用 vim /dev/shm/unit05/dir1/file1 ~ vim /dev/shm/unit05/dir4/file4，嘗試儲存
  dir1 dir2 dir4不能儲存
  dir3因為有修改的權限 所以可以儲存


  
  





























  
  
  
  
