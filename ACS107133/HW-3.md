1.輸入#useradd examuser1建立三個帳號:examuser1, examuser2, examuser3。輸入密碼#passwd examuser1，會冒出new password:，再輸入ItIsExam，會出現Retype new password:，再輸入一次密碼，之後重複動作。
2.使用# userdel -r examuser3，刪除examuser3帳號和家目錄，刪除後未出現敘述，所以我無法確定是否刪除，我再輸入一次一樣的指令，發現她說examuser3不存在，所以我確定我已經刪除examuser3了。
3.輸入# id examuser1 查詢examuser1的id，UID和GID發現為1002，再輸入# userdel examuser1刪除此帳號(未刪除家目錄)。
4.輸入#adduser -u 1002 examuser1，建立帳號，再輸入passwd examuser1更改密碼。


1.輸入#useradd examuser4，再輸入#passwd examuser4，我輸入的密碼為pp22，它顯示說我的密碼是BAD PASSWORD，因為少於七的字。
2.我首先確認是否存在securetty，因此我移動到目錄etc下，然後輸入cd securetty，Not a directory，原本以為不存在這個securetty，但後來發現，是因為securetty根本不是一個資料夾，如果用ls指令就可以看到etc資料夾下存在securetty。
3.接著開始將securetty複製到examuser4，首先確認examuser4的路徑，用cd指令移動到examuser4之後，輸入pwd指令，會顯示出當前的路徑，接著用cd指令移動回etc資料夾下，然後輸入指令cp securetty "剛才複製的examuser4路徑"，就完成了複製securetty。
4.先用ls -l查看securetty的權限，目前是root所擁有，輸入指令chown examuser4 securetty，然後再用ls -l查看一次securetty的權限，可以發現已經變為examuser4所擁有，但對自己的權限仍是rw-，只能讀和寫，但不能執行。
5.為了更改examuser4對securetty的權限，讓examuser4可以執行securetty，輸入chmod 700 securetty，其中7代表使用者可讀取、可寫入、可執行檔案，00代表群組的人和其他人不可讀取、寫入、執行檔案。其中7代表1(執行) + 2(寫入) + 4(讀取)。輸入完指令後用ls -l確認權限是否更改正確，可以看到權限已經更改為700，使用者可讀取、可寫入、可執行。
6.因為原本沒有examdata資料夾，所以要先創建一個，輸入指令mkdir examdata，用ls可以看到創建的資料夾，然後cd examdata，移動到資料夾下，接著創建change.txt，輸入指令vi change.txt，由於原本不存在change.txt，所以會自動創建一個change.txt的檔案，因為沒有要編輯內容，所以直接儲存離開就可以了，先按esc鍵，然後輸入:wq，寫入並離開，結束後輸入ls，確認change.txt已經創建成功。
7.輸入ls -l，可以看到現在的檔案擁有者是root，且其餘人只有讀取的權限。輸入chown sshd change.txt，然後用ls -l查看，發現檔案的擁有者已經變為sshd。
8.雖然擁有者已經更改為sshd，但擁有群組依然是root，輸入指令chgrp users change.txt，更改群組擁有者為users，使用ls -l查看，發現群組擁有者已經正確更改。
9.目前還剩下權限還沒更改，原本的權限是使用者可讀取、可寫入，群組擁有者可讀取，其他人可讀取，但題目要求其他人不可讀取，因此再使用chmod 640 change.txt，將其他人的權限設為不可讀取，使用ls -l檢查發現權限已經正確變更。其中6代表2(寫入) + 4(讀取)，4代表可讀取、不可寫入、不可執行，0代表不可讀取、不可寫入、不可執行。
10.先用ls -l查看原本時間為Oct 22 01:23，再來是要更改時間，輸入touch -t 201212210303 change.txt，再輸日ls -l查看時間，變為Dec 21 2012，這樣就修改成功了。


1.輸入cd dev進入此目錄後，再輸入cd shm，輸入mkdir unit05 建立此目錄，使用ls -l查看權限發現為drwxr-xr-x，輸入chmod 775 unit05，將此更改為drwxrwxr-x。
2.再unit05這個目錄下再建立一個叫做dir1的目錄，輸入mkdir dir1，使用ls -l查看權限，發現為drwxr-xr-x，輸入chmod 754 dir1，將權限更改為drwxr-xr--。
3.使用指令vi file1，在dirl的目錄下建立一個叫做file1的檔案，會跳出編輯檔案，按下ESC鍵退出，在輸入:wq，可退出編輯模式，在使用ls -l查看權限可發現此檔案權限就為-rw-r--r--。
4.輸入cd ..退到unit05的目錄，使用mkdir dir2建立目錄，在此用ls -l查看權限為drwxr-xr-xr--，輸入chmod 751 dir2更改權限為drwxr-x--x。
5.輸入cd dir2進入目錄，輸入vi file2建立檔案，並按ESC退出編輯，在輸入:wq完全退出，輸入ls -l查看權限可發現為-rw-r--r--。
6.輸入cd ..退到unit05的目錄，使用mkdir dir3建立目錄，在此用ls -l查看權限為drwxr-xr-xr--，輸入chmod 755 dir3更改權限，在輸入ls -l查看權限變更為drwxr-xr-x。
7.輸入cd dir3進入目錄，輸入vi file3建立檔案，並按ESC退出編輯，在輸入:wq完全退出，輸入ls -l查看權限可發現為-rw-r--r--，輸入chmod 666 file3更改權限為-rw-rw-rw-。
8.輸入cd ..退到unit05的目錄，使用mkdir dir4建立目錄，在此用ls -l查看權限為drwxr-xr-xr--，輸入chmod 777 dir4更改權限為drwxrwxrwx。
9.輸入cd dir4進入目錄，輸入vi file4建立檔案，並按ESC退出編輯，在輸入:wq完全退出，輸入ls -l查看權限可發現為-rw-r--r--，輸入chmod 600 file4更改權限為-rw-------
10.輸入useradd examuser 創建一般帳號，在輸入passwd examuser，我將密碼設為556677。
11.輸入su examuser更換為一般使用者，使用cd dir1顯示為Permission denied，因為dir1這個目錄對examuser這個使用者來說權限為r--只可讀取不可執行。
12.再來輸入cd dir2，可進入此目錄，因為他對examuser的權限為--x可執行，但使用ls -l這個指令無法看到他的權限，因為它不可讀。
13.輸入cd ..退到unit05的目錄，在輸入cd dir3進入目錄，發現可以進入因為userexam的權限為r-x，使用ls -l也可查看權限，但無法使用vi編輯檔案。
14.輸入cd ..退到unit05的目錄，再輸入cd dir4進入目錄，發現可進入也可使用ls -l查看權限因為examuser的權限為rwx。
15.輸入cd ~退回host ~，輸入ls -l /dev/shm/unit05/dir1/file1，跑出permission denied，因為examuser對file1的權限為r--。
16.輸入ls -l /dev/shm/unit05/dir2/file2，跑出permission denied，因為examuser對file2的權限為r--。
17.輸入ls -l /dev/shm/unit05/dir3/file3，跑出permission denied，因為examuser對file3的權限為rw-。
18.輸入ls -l /dev/shm/unit05/dir4/file4，跑出permission denied，因為examuser對file4的權限為---。
20.輸入vim /dev/shm/unit05/dir1/file1，無法儲存，因為權限為r--
21.輸入vim /dev/shm/unit05/dir2/file2，也無法儲存，權限同為r--
22.輸入vim /dev/shm/unit05/dir3/file3，可以儲存，因為權限為rw-
23.輸入vim /dev/shm/unit05/dir4/file4，不可儲存，因為權限為---