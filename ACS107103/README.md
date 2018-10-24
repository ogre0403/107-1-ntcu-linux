<strong>第一大題</strong>

<em>1.<em>
+ 用adduser分別創建三個使用者
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-3/ACS107103/kali-2018-10-23-19-16-21.png)
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-3/ACS107103/kali-2018-10-23-19-18-04.png)
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-3/ACS107103/kali-2018-10-23-19-18-37.png)

<em>2.<em>
+ 用"-r"參數刪除帳戶(連同家目錄和郵件)
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-3/ACS107103/kali-2018-10-23-19-28-57.png)

<em>3.<em>
+ 先用id指令查看examuser1的uid並記下來
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-3/ACS107103/kali-2018-10-23-19-40-43.png)
+ 刪除examuser1(不用"-r"參數)
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-3/ACS107103/kali-2018-10-23-19-46-56.png)
+ 用"useradd -u"參數加指令重新創建examuser1
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-3/ACS107103/kali-2018-10-23-19-48-46.png)
+ 再用passwd設定密碼
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-3/ACS107103/kali-2018-10-23-19-49-42.png)

<strong>第二大題</strong>

<em>1.<em>
+ 用adduser創建examuser4帳戶
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-3/ACS107103/kali-2018-10-23-19-54-18.png)

<em>2.<em>
+ 用cp指令複製/etc/securetty到/home/examuser4
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-3/ACS107103/kali-2018-10-23-19-59-08.png)
+ 用chown和chgrp改變擁有者和群組為examuser4
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-3/ACS107103/kali-2018-10-23-20-01-26.png)

<em>3.<em>
+ 用mkdir創建/examdata/目錄並且用touch指令創建change.txt
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-3/ACS107103/kali-2018-10-23-20-04-28.png)
+ 用chown和chgrp改變擁有者與群組為sshd和users
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-3/ACS107103/kali-2018-10-23-20-09-18.png)
+ 用chmod指令改變change.txt的權限
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-3/ACS107103/kali-2018-10-23-20-12-24.png)
+ 再用"touch YYMMDDhhmm"來改時間戳記
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-3/ACS107103/kali-2018-10-23-20-15-13.png)

<strong>第三大題</strong>

<em>1.<em>
+ 以root登入建立指定的目錄和檔案
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-3/ACS107103/kali-2018-10-23-20-26-09.png)
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-3/ACS107103/kali-2018-10-23-20-28-39.png)
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-3/ACS107103/kali-2018-10-23-20-34-39.png)
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-3/ACS107103/kali-2018-10-23-20-37-29.png)
+ 然後我一開始沒注意到檔名，這邊用mv指令來改檔案名稱
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-3/ACS107103/kali-2018-10-23-20-51-47.png)

<em>2.<em>
+ 以一般帳戶登入並執行"ls -l"指令
+ dir1和dir2存取被拒絕(因為--x)
+ dir3和dir4可看見其下的檔案與權限狀態
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-3/ACS107103/kali-2018-10-23-21-23-15.png)

<em>3.<em>
+ 用"ls -l"指令檢視file[1~4]
+ file1存取被拒絕(因為--x)
+ file[2~4]可存取
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-3/ACS107103/kali-2018-10-23-21-24-38.png)

<em>4.<em>
+ file1無法讀取並寫入
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-3/ACS107103/kali-2018-10-23-21-25-47.png)
+ file2可讀取但無法寫入
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-3/ACS107103/kali-2018-10-23-21-26-35.png)
+ file3可讀取並寫入
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-3/ACS107103/kali-2018-10-23-21-27-20.png)
+ file4無法讀取並寫入
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-3/ACS107103/kali-2018-10-23-21-27-47.png)
