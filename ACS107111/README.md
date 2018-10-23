# 安裝Linux流程

![GITHUB]( https://imgur.com/boLcaoY.jpg"git圖示")
+ 登入CentOS後建立帳號

![GITHUB](https://imgur.com/rz8sfGL.jpg"git圖示")
+ 設定密碼

![GITHUB](https://imgur.com/fCLTmNi.jpg"git圖示")
+ 完成後重複相同動作設置examuser2和examuser3

![GITHUB](https://imgur.com/dAJM8GL.jpg"git圖示")
+ 完成圖

![GITHUB](https://imgur.com/wAkZn9s.jpg"git圖示")
+ 輸入指令刪除examuser3

![GITHUB](https://imgur.com/faiXmxp.jpg"git圖示")
+ 確認是否成功刪除


![GITHUB](https://imgur.com/7CC5tO1.jpg"git圖示")
+ 刪除examuser1但不加-r，確認後examuser1還沒完全刪除

![GITHUB](https://imgur.com/OUJPF0n.jpg"git圖示")
+ 確認id

![GITHUB](https://imgur.com/PyIdF6h.jpg"git圖示")
+ 使用useradd examuser1-d 修復帳號

![GITHUB](https://imgur.com/kEcCnsz.jpg"git圖示")
+ 重新設置密碼

+這樣第一題就結束了

![GITHUB](https://imgur.com/PIhSd6z.jpg"git圖示")
+ 建立examuser4
![GITHUB](https://imgur.com/GKCmH5f.jpg"git圖示")
+ 使用chgrp將群組改為examuser4
![GITHUB](https://imgur.com/5V6VFUi.jpg"git圖示")
+ 使用chmod更改群組權限
![GITHUB](https://imgur.com/dQnPLY7.jpg"git圖示")
+ 建立examdata的資料夾
![GITHUB](https://imgur.com/LZR2DGC.jpg"git圖示")
+ 改變目錄至exandata
![GITHUB](https://imgur.com/hFt2sCW.jpg"git圖示")
+ 使用指令vi 建立change.txt的檔案
![GITHUB](https://imgur.com/3u9GS6A.jpg"git圖示")
+ 用wq!儲存後離開
![GITHUB](https://imgur.com/0Tqhjc8.jpg"git圖示")
+ 用chown改擁有者為sshd，用chgrp改群組為users
![GITHUB](https://imgur.com/za4hXGN.jpg"git圖示")
+ 使用touch -t改變修改時間

 +這樣第二題就結束了

![GITHUB](https://imgur.com/uQwmqIO.jpg"git圖示")
+ 將目錄改制/dev/shm/
![GITHUB](https://imgur.com/HMypuxR.jpg"git圖示")
+ 建立unit05的資料夾後換此資料夾為目錄
![GITHUB](https://imgur.com/aAu9OWy.jpg"git圖示")
+ 建立dir1的資料夾
![GITHUB](https://imgur.com/t2s1H6p.jpg"git圖示")
+ 以同樣方法建立dir2、dir3、dir4
![GITHUB](https://imgur.com/1oSssuz.jpg"git圖示")
+ 將hosts的檔案用cp複製到dir1-4的資料夾中
![GITHUB](https://imgur.com/AZGlvzu.jpg"git圖示")
+ 將每個hosts檔案名改成file1-4
![GITHUB](https://imgur.com/XT2xnj9.jpg"git圖示")
+ 用chmod跟改權限
![GITHUB](https://imgur.com/l2fBCGM.jpg"git圖示")
+ 切換為一般帳號
![GITHUB](https://imgur.com/SpF4uaB.jpg"git圖示")
+ 依照第一題的指令後的結果，只有dir3和dir4因為權限夠所以能看到內容
![GITHUB](https://imgur.com/yGN3xwA.jpg"git圖示")
+ 依照第二題的指令後的結果，只有file1因為權限不足所以無法觀看
![GITHUB](https://imgur.com/A3Jqt79.jpg"git圖示")
+ 依照第三題的指令後，用:w儲存的結果，因為權限不足所以無法儲存
![GITHUB](https://imgur.com/Ufv4pLZ.jpg"git圖示")
+ 依照第三題的指令後，用:w儲存的結果，因為權限不足所以無法儲存
![GITHUB](https://imgur.com/JKMwxky.jpg"git圖示")
+ 依照第三題的指令後，用:w儲存的結果，因為權限足夠所以可以儲存
![GITHUB](https://imgur.com/kYoNDer.jpg"git圖示")
+ 依照第三題的指令後，用:w儲存的結果，因為權限不足所以無法儲存















