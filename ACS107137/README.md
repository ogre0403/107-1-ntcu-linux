# 如何安裝Linux    
請先安裝模擬器VirtualBox並開啟,然後點選新增,建立虛擬模擬器    
![image](https://github.com/bill0330/107-1-ntcu-linux/blob/HW-2/ACS107137/1.PNG?raw=true)    
設定記憶體大小(大小自訂)    
![image](https://github.com/bill0330/107-1-ntcu-linux/blob/HW-2/ACS107137/2.PNG?raw=true)    
點選建立    
![image](https://github.com/bill0330/107-1-ntcu-linux/blob/HW-2/ACS107137/3.PNG?raw=true)    
點選下一步    
![image](https://github.com/bill0330/107-1-ntcu-linux/blob/HW-2/ACS107137/4.PNG?raw=true)    
點選動態配置,然後按下一部    
![image](https://github.com/bill0330/107-1-ntcu-linux/blob/HW-2/ACS107137/5.PNG?raw=true)    
設定虛擬硬碟大小(大小自訂),然後按建立,這樣你的虛擬機器就裝好了喔!    
![image](https://github.com/bill0330/107-1-ntcu-linux/blob/HW-2/ACS107137/6.PNG?raw=true)    
點選剛剛建立的虛擬機器,按下設定,然後找到存放位置    
在畫面的右方有個小小的光碟圖示,按下去之後,點選剛剛下載的虛擬光碟檔    
![image](https://github.com/bill0330/107-1-ntcu-linux/blob/HW-2/ACS107137/7.PNG?raw=true)    
接下來找到網路    
介面一請點選"啟用網路卡",然後選取"NAT"    
介面二請點選"啟用網路卡",然後選取"僅限主機介面卡"    
![image](https://github.com/bill0330/107-1-ntcu-linux/blob/HW-2/ACS107137/8.PNG?raw=true)    
![image](https://github.com/bill0330/107-1-ntcu-linux/blob/HW-2/ACS107137/9.PNG?raw=true)    
按下確定後就可以開始啟動模擬器了,畫面是這樣的    
![image](https://github.com/bill0330/107-1-ntcu-linux/blob/HW-2/ACS107137/10.PNG?raw=true)    
系統跑一段時間後,就會出現以下畫面,進行語言設定    
![image](https://github.com/bill0330/107-1-ntcu-linux/blob/HW-2/ACS107137/11.PNG?raw=true)    
設定語言後,會跑進安裝摘要的畫面,正常情況下,"本地化設定"和"軟體"都會設定好    
接下來就是最重要的磁碟分割了,請點選"系統"裡的"安裝目的地"    
![image](https://github.com/bill0330/107-1-ntcu-linux/blob/HW-2/ACS107137/12.PNG?raw=true)    
點選"其他儲存選項"的"自行配置磁碟分割",後按完成    
![image](https://github.com/bill0330/107-1-ntcu-linux/blob/HW-2/ACS107137/13.PNG?raw=true)    
磁碟分割格式預設是"LVM",請改成"標準分割區"    
按+加入新掛載點,本人作法:/和/home和swap分別為5/4/1GB    
![image](https://github.com/bill0330/107-1-ntcu-linux/blob/HW-2/ACS107137/14.PNG?raw=true)    
![image](https://github.com/bill0330/107-1-ntcu-linux/blob/HW-2/ACS107137/15.PNG?raw=true)    
按完成後,點選接受變更    
![image](https://github.com/bill0330/107-1-ntcu-linux/blob/HW-2/ACS107137/16.PNG?raw=true)    
接下來請點選"系統"裡的"網路與主機名稱",因為預設是關的,因此要記得打開,完成後就可以開始安裝了    
![image](https://github.com/bill0330/107-1-ntcu-linux/blob/HW-2/ACS107137/17.PNG?raw=true)    
進入安裝畫面後要記得設置"使用者"與"ROOT"的帳密,安裝和設定都完成後就可以重新開機了    
![image](https://github.com/bill0330/107-1-ntcu-linux/blob/HW-2/ACS107137/18.PNG?raw=true)    
![image](https://github.com/bill0330/107-1-ntcu-linux/blob/HW-2/ACS107137/19.PNG?raw=true)    
重新開機後,輸入使用者帳密,並"df"指令檢視是否有剛剛設置的分割區    
如果有就代表你完成了!    
![image](https://github.com/bill0330/107-1-ntcu-linux/blob/HW-2/ACS107137/20.PNG?raw=true)    
![image](https://github.com/bill0330/107-1-ntcu-linux/blob/HW-2/ACS107137/21.PNG?raw=true)    
# 恭喜你完成了Linux虛擬機器的設定!!!



