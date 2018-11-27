# HW4
### 使用ubuntu

1</br>
* 利用vi .bashrc 指令，在最後面增加變數</br>
![0](img/0.png)</br>
新增 HOSTS_PATH=/etc/hosts</br>
![1](img/1.png)</br>
利用source ~/.bashrc 讓變數生效</br>
![2](img/2.png)</br>
使用cat $HOSTS_PATH 來檢查</br>
![3](img/3.png)</br>
* 先使用touch 建立一個c檔案</br>
![4](img/4.png)</br>
在使用 vi abc.c 來修改內容</br>
![5](img/5.png)</br>
使用gcc 編譯</br>
![6](img/6.png)</br>
回傳getenv() return NULL 及 1</br>
代表s為獲取其變數</br>
* 在 .bashrc 裡再加一條 export ，讓變數變成環境變數</br>
![7](img/7.png)</br>
![8](img/8.png)</br>
