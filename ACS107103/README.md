<strong>第一大題</strong>

<em>1.<em>
+ 用groupadd分別創建mygroup和nogroup群組
+ (這邊可以看到我的系統已經存在一個名為nogroup的群組了,似乎是因為distribution的關係)
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-4/ACS107103/kali-2018-10-30-19-38-15.png)

<em>2.<em>
+ 先用useradd連同"-G"參數創建myuser1~3和nouser1~3
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-4/ACS107103/kali-2018-10-30-19-51-58.png)

<em>3.<em>
+ 再用passwd來修改密碼為MyPassWord
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-4/ACS107103/kali-2018-10-30-19-54-28.png)
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-4/ACS107103/kali-2018-10-30-19-56-34.png)

<em>4.<em>
+ 先用mkdir來創建/srv/myproject目錄
+ 再用chgrp來變更該目錄的所屬群組為mygroup
+ 再用chmod變更目錄的權限讓擁有者和所屬群組有完全的使用權限
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-4/ACS107103/kali-2018-10-30-19-59-43.png)

<em>5.<em>
+ 先用su指令暫時切換到myuser1
+ 再用touch指令創建指定文件到指定目錄(/srv/myproject/myuser1.data)
+ 最後用exit退出myuser1
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-4/ACS107103/kali-2018-10-30-20-07-11.png)

<em>6.<em>
+ 用cp指令複製 /usr/bin/ls 到 /usr/local/bin/myls
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-4/ACS107103/kali-2018-10-30-20-10-26.png)
+ 由於nogroup下的使用者沒有權限所以要設置一下suid讓nouser1~3也能檢視/srv/myproject
+ 用chmod u+s設置suid屬性
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-4/ACS107103/kali-2018-10-30-20-22-47.png)


<strong>第二大題</strong>

+ 用ps指令搭配管線和grep抓出帶有關鍵字的部分
+ 後方搭配用">"將內容輸出到/root/process_syslog.txt
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-4/ACS107103/kali-2018-10-30-20-27-12.png)

<strong>第三大題</strong>

+ 用find -perm /u=s參數來查找符合的檔案
+ 後方搭配管線"|"將查找結果輸出到"ls -l"來列出詳細資訊
+ 注意此處要用">>"來追加檔案內容(用">"的話檔案內容會被覆蓋)
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-4/ACS107103/kali-2018-10-30-20-43-43.png)
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-4/ACS107103/kali-2018-10-30-20-44-15.png)








