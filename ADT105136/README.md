#特殊檔案權限：SUID、SGID、SBIT
SUID：當使用者對檔案擁有執行權限，執行時會暫時轉換身分成為該檔案的擁有者(owner)
SGID：當使用者對檔案擁有執行權限，執行時就會暫時擁有該檔案群組(group)的權限
SBIT：當使用者對目錄擁有寫入權限，建立的檔案或目錄只有自己或是root才能夠刪除

![image](https://github.com/boolenboom/107-1-ntcu-linux/blob/HW-4/ADT105136/001.PNG)

首先建立測試的帳號及群組

![image](https://github.com/boolenboom/107-1-ntcu-linux/blob/HW-4/ADT105136/002.PNG)

若此目錄不做任何更改，直接建立一個檔案，他的Owner和Group都會是使用者

![image](https://github.com/boolenboom/107-1-ntcu-linux/blob/HW-4/ADT105136/003.PNG)

但是現在更動目錄後...(給予目錄SGID)

![image](https://github.com/boolenboom/107-1-ntcu-linux/blob/HW-4/ADT105136/004.PNG)

新建立的檔案群組會直接變成和目錄同一個群組！

