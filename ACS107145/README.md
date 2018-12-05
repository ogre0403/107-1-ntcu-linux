## 依下列描述完成並說明各項問題：<br>
### 1.請在家目錄下的.bashrc裡新增一個shell變數 HOSTS_PATH=/etc/hosts，(注意不需用export)，說明如何不登出讓HOSTS_PATH變數生效，執行cat $HOST_PATH確認有讀取到檔案內容。<br>

```
vi ~/.bsahrc
將HOSTS_PATH=/etc/hosts打進檔案
esc離開編輯模式
:wq離開並儲存
sourse ~/.bashrc 
cat $HOSTS_PATH
```
![image](https://github.com/percy890713/107-1-ntcu-linux/blob/HW-6/ACS107145/img/HW6-1.PNG)<br>
![image](https://github.com/percy890713/107-1-ntcu-linux/blob/HW-6/ACS107145/img/HW6-2.PNG)<br><br>
### 2.在C語言程式可以用getenv()讀取LINUX的環境變數，範例程式如下。請在Linux裡編譯此範例程式並執行，請問否有讀到HOSTS_PATH以及$?的值為何，請說明。<br>
![image](https://github.com/percy890713/107-1-ntcu-linux/blob/HW-6/ACS107145/img/HW6-3.PNG)<br><br>
```
gcc test.c
./a.out (getenv() return NULL＞＞錯誤)
echo $? (1＞＞錯誤)
```
![image](https://github.com/percy890713/107-1-ntcu-linux/blob/HW-6/ACS107145/img/HW6-4.PNG)<br><br>
### 3.在.bashrc裡要如何修正，讓C語言程式可以讀到環境變數並將檔案內容顯示。<br>

```
vi ~/.bashrc
把export打在HOSTS_PATH=/etc/hosts前面
gcc test.c
./a.out
echo $?
```
![image](https://github.com/percy890713/107-1-ntcu-linux/blob/HW-6/ACS107145/img/HW6-5.PNG)<br>
![image](https://github.com/percy890713/107-1-ntcu-linux/blob/HW-6/ACS107145/img/HW6-6.PNG)<b