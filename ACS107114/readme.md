# HW7

### 第一題；
* 因未安裝過wget，故使用`yum -y install wget`，安裝wget環境。
* 安裝完成後依照題目所給網址，輸入`wget https://raw.githubusercontent.com/ogre0403/107-1-ntcu-linux/master/resource/web.log`即可下載檔案。
![](https://i.imgur.com/JVJYBwT.png)


* 檢查是否成功下載
![](https://i.imgur.com/UkjK8OF.png)


* 接著輸入指令`cat web.log | grep error`，即可顯示出現error的原因。
![](https://i.imgur.com/KXhmMnd.png)

### 第二題

* 使用`tar -cvf var.tar /var 2> tar-err.log`，製造一個壓縮檔，並以**tar-err.log**存在當前目錄裡。
* 檢查是否儲存成功
![](https://i.imgur.com/RJpCgMk.png)

* 因為上述動作將錯誤資料轉存入**tar-err.log**檔案中，所以要以`cat tar-err.log`，抓出存在檔案中的錯誤訊息。
![](https://i.imgur.com/BJ4GLdI.png)
