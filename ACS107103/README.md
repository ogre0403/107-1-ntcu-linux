﻿<strong>第一大題</strong>

<em>1.<em>
+ 用vi編輯.bashrc
+ 加上一行HOSTS_PATH="etc/hosts"
+ 儲存後執行source ~/.bashrc來套用設定
+ 最後用cat $HOSTS_PATH測試確認有讀取到檔案內容
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-6/ACS107103/centos-2018-11-27-18-52-01.png)
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-6/ACS107103/centos-2018-11-27-18-53-53.png)

<em>2.<em>
+ 請先執行yum groupinstall "Development Tools"安裝gcc
+ 安裝過程有點久，請耐心等候
+ 由於我懶著打code所以這邊我選擇先將code上傳到github然後再clone下來
+ 執行gcc env.c來編譯
+ 執行./a.out
+ 執行echo $?來查看上個指令的回傳值
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-6/ACS107103/centos-2018-11-27-19-07-21.png)
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-6/ACS107103/centos-2018-11-27-19-10-47.png)
+ 由以上兩圖可得知程式讀取不到$HOSTS_PATH且$?回傳值為1
+ 因為$HOSTS_PATH為區域變數，所以程式無法讀取到這個變數
+ 從程式碼可以看出當讀取到空值時會return 1

<em>3.<em>
+ 再次用vi編輯.bashrc
+ 加上一行export HOSTS_PATH
+ 儲存後執行source ~/.bashrc來套用設定
+ 再執行一次./a.out發現可以正常讀取了!!
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-6/ACS107103/centos-2018-11-27-19-28-32.png)
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-6/ACS107103/centos-2018-11-27-19-30-13.png)
