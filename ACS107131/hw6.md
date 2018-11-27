## 1.請在家目錄下的.bashrc裡新增一個shell變數 HOSTS_PATH=/etc/hosts，(注意不需用export)，說明如何不登出讓HOSTS_PATH變數生效，執行cat $HOST_PATH確認有讀取到檔案內容。           
                 
####   vi ~/.bashrc           
####   i 編輯         
####   新增HOSTS_PATH=/etc/hosts         
####   esc 離開編輯       
####   :w 儲存           
####   :q 離開  
![1](https://github.com/edmundabc/107-1-ntcu-linux/blob/HW-6/ACS107131/1.PNG?raw=true)     
####   source ~/.bashrc 不登出讓HOSTS_PATH變數生效           
####   cat $ HOSTS_PATH 確認有讀取到檔案內容          
![2](https://github.com/edmundabc/107-1-ntcu-linux/blob/HW-6/ACS107131/2.PNG?raw=true)             
## 2.C語言程式可以用getenv()讀取LINUX的環境變數，範例程式如下。請在Linux裡編譯此範例程式並執行，請問否有讀到HOSTS_PATH以及$?的值為何?                 
                
####   vi 6.c 輸入程式碼    
![3](https://github.com/edmundabc/107-1-ntcu-linux/blob/HW-6/ACS107131/3.PNG?raw=true)              
####   gcc 6.c            
####   ll 6.c a.out          
####   ./a.out            
####   會顯示 getenv() return NULL (錯誤)       
####   echo $?            
####   會顯示 1 (代表沒執行)           
           
#### 正確為 在前面 vi ~/.bashrc裡        
####        HOSTS_PATH=/etc/hosts 前面要加 export        
####    這樣 ./a.out 才會顯示正確         
####    echo $? 也會變成 0         
        