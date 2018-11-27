# HW6
## 請在家目錄下的.bashrc裡新增一個shell變數 HOSTS_PATH=/etc/hosts，(注意不需用export)，說明如何不登出讓HOSTS_PATH變數生效，執行cat $HOST_PATH確認有讀取到檔案內容。
### 輸入vi ~/.bashrc後新增變數HOSTS_PATH=/etc/hosts
![1](https://github.com/hfjdgfj/107-1-ntcu-linux/blob/HW-6/ACS107130/1.PNG)
### 輸入source ~/.bashrc即可不登出讓HOSTS_PATH變數生效
![2](https://github.com/hfjdgfj/107-1-ntcu-linux/blob/HW-6/ACS107130/2.PNG)
### 輸入cat $HOSTS_PATH來確認有讀取到檔案內容
![3](https://github.com/hfjdgfj/107-1-ntcu-linux/blob/HW-6/ACS107130/3.PNG)
## 在C語言程式可以用getenv()讀取LINUX的環境變數，範例程式如下。請在Linux裡編譯此範例程式並執行，請問否有讀到HOSTS_PATH以及$?的值為何，請說明。也許需透過yum groupinstall "Development Tools"安裝gcc。
### 輸入vi 檔名.c寫一個C語言程式
![4](https://github.com/hfjdgfj/107-1-ntcu-linux/blob/HW-6/ACS107130/4.PNG)
### 先輸入gcc 檔名.c及ll 檔名.c a.out後，輸入./a.out即可執行
![5](https://github.com/hfjdgfj/107-1-ntcu-linux/blob/HW-6/ACS107130/5.PNG)
### 沒有讀到HOSTS_PATH的值，因為它不在程序中；$?的值為1，表示程式未成功執行
![6](https://github.com/hfjdgfj/107-1-ntcu-linux/blob/HW-6/ACS107130/6.PNG)
### 需再次輸入vi ~/.bashrc，並加入export HOSTS_PATH，完成後仍須輸入source ~/.bashrc；這樣就有讀到HOSTS_PATH的值，且$?的值是0，代表程式成功執行
![9](https://github.com/hfjdgfj/107-1-ntcu-linux/blob/HW-6/ACS107130/9.PNG)
![7](https://github.com/hfjdgfj/107-1-ntcu-linux/blob/HW-6/ACS107130/7.PNG)
![8](https://github.com/hfjdgfj/107-1-ntcu-linux/blob/HW-6/ACS107130/8.PNG)