# HW6
-----------------------------------------
## 請在家目錄下的` .bashrc `裡新增一個shell變數` HOSTS_PATH=/etc/hosts `，(注意不需用export)，說明如何不登出讓` HOSTS_PATH `變數生效，執行` cat $HOST_PATH `確認有讀取到檔案內容。
* 在家目錄下的` .bashrc `裡新增一個shell變數` HOSTS_PATH=/etc/hosts `
  * ` vim .bashrc `。
   > 進入後使用編輯模式。
  * 在最末行新增shell變數` HOSTS_PATH=/etc/hosts `。
   > 儲存後離開。


![image](https://github.com/YANGshujun1110/107-1-ntcu-linux/blob/HW-6/ACS107109/img/1.png)


* 如何不登出讓` HOST_PATH `便入生效?
  * 輸入` source .bashrc `可不用登出即可讀到此新的設定。
   > 使用` echo $HOSTS_PATH `確認。
  * 執行` cat $HOSTS_PATH `確認有讀取到檔案內容。


![image](https://github.com/YANGshujun1110/107-1-ntcu-linux/blob/HW-6/ACS107109/img/2.png)


-----------------------------------------
## 在C語言程式可以用getenv()讀取LINUX的環境變數，範例程式如下。請在Linux裡編譯此範例程式並執行，請問否有讀到HOSTS_PATH以及$?的值為何，請說明。也許需透
過yum groupinstall "Development Tools"安裝gcc。
* 安裝gcc。
  > ` yum groupinstall "Development Tools" `。


![image](https://github.com/YANGshujun1110/107-1-ntcu-linux/blob/HW-6/ACS107109/img/3.PNG)


* 編譯範例程式。
  > ` vim test.c `。
  > >進入後使用編譯模式。

  > 儲存後離開。


![image](https://github.com/YANGshujun1110/107-1-ntcu-linux/blob/HW-6/ACS107109/img/4.PNG)


* 執行範例程式。
  > ` gcc test.c `。

  > ` ./a.out `。
  

* 有無讀到` HOSTS_PATH ` 及 ` $? `的值為何?
  * 沒有讀到` HOSTS_PATH `的值。
   > getenv() return NULL。

  * ` $? `的值為1。(**有誤**)
    > ` echo $? `。


![image](https://github.com/YANGshujun1110/107-1-ntcu-linux/blob/HW-6/ACS107109/img/5.png)

----------------------------------------
## 在.bashrc裡要如何修正，讓C語言程式可以讀到環境變數並將檔案內容顯示。


* 進入` .bashrc `中修正。
  > ` vim .bashrc `。

* 在原本的` HOSTS_PATH `加上**export**。
  > `export HOSTS_PATH `。

  > 儲存後離開。


![image](https://github.com/YANGshujun1110/107-1-ntcu-linux/blob/HW-6/ACS107109/img/6.png)


* **記得要使用 `source HOSTS_PATH `使變數生效。**
* 執行test.c。
  > ` gcc test.c `。

  > ` ./a.out。

* 即可讀到環境變數並將檔案內容顯示。
  > 如圖。

* $?的值為0。(**無誤**)
  > ` echo $? `。
  

![image](https://github.com/YANGshujun1110/107-1-ntcu-linux/blob/HW-6/ACS107109/img/7.png)
