# HW7
----------------------------------------
## apache log是apache web server的日誌檔
### 請查詢` curl `或` wget `的用法後，用其中一個指令下載此日誌檔。
#### 我使用的為` wget `指令。
* 先下載安裝` wget `。
  > ` yum -y install wget `

![image](https://github.com/YANGshujun1110/107-1-ntcu-linux/blob/HW-7/ACS107109/img/1.PNG)


##### **再來記得切換成一般使用者身分 並使用一般使用者身分操作**
* 下載日誌檔。
  > ` wget https://raw.githubusercontent.com/ogre0403/107-1-ntcu-linux/master/resource/web.log `

![image](https://github.com/YANGshujun1110/107-1-ntcu-linux/blob/HW-7/ACS107109/img/2.png)


### 使用bash的pipe指令，例如` grep ` 、 ` cat `...等等，將此日誌中error發生的原因輸出至螢幕，但其他資訊不需要呈現。
* **由於下在日誌檔的位置儲存於` web.log `，所以要從` web.log `中抓資訊。**
* 利用` cat web.log | grep error `抓出error，並將發生之原因輸出至螢幕(其他資訊不會出現)。

![image](https://github.com/YANGshujun1110/107-1-ntcu-linux/blob/HW-7/ACS107109/img/3.png)


----------------------------------------
## ` tar `是linux下用來打包壓縮目錄的工具，請自行查詢` tar `的用法後，用` 一般使用者 `身份打包並壓縮` /var `目錄。在` tar `執行過程中，忽略正常輸出結果，但需將錯誤訊息輸出至` tar-err.log `檔案。
* 輸入指令` tar -jcv -f filename.tar.bz2 /var 2> tar-err.log `，將` /var `的目錄打包並壓縮後，並將標準錯誤輸出導入` tar-err.log `的檔案中。
  > -j:透過 bzip2 的支援進行壓縮/解壓縮，附檔名為` .tar.bz2 `。

  > -c:建立打包檔案，可搭配` -v `來察看過程中被打包的檔名(filename)。

  > -v:在壓縮/解壓縮的過程中，將正在處理的檔名顯示出來。

  > -f filename:-f 後面要立刻接要被處理的檔名。

![image](https://github.com/YANGshujun1110/107-1-ntcu-linux/blob/HW-7/ACS107109/img/4.png)


* 利用` cat tar-err.log `將tar-err.log檔案內容輸出至螢幕。

![image](https://github.com/YANGshujun1110/107-1-ntcu-linux/blob/HW-7/ACS107109/img/5.png)

![image](https://github.com/YANGshujun1110/107-1-ntcu-linux/blob/HW-7/ACS107109/img/6.PNG)


-----------------------------------------
##### 補充
* curl和wget都是能用來下載網頁檔案的指令，但他們的差別我蠻好奇的，所以就查了一下覺得還不錯的解說附在補充的部分。
* curl和wget兩者間最大的差別:


   curl 有 Library 的版本，所以，可以方便程式利用 curl 來當做 HTTP Client 用，而 Wget 就是個單純的命令列程式，沒有程式庫版本，除此之外，再來，大概就是 curl 支援更多比較新的網路協定 (Protocol)， 因此，curl 可以下載的網站類型就比 Wget來的多，還有，curl 官方支援的作業系統比Wget多很多。


   不過，這並不表示Wget沒有curl好用!Wget有一個最利害和最方便的，而就是可以遞迴式的下載檔，就是Wget可以自動去掃整個資料夾的檔案，然後，把它裡面的子資料夾和子子資料夾的檔案都給下載下來，所以，用 Wget來抓FTP或HTTP站上的某個資料夾的所有檔案是很方便的事!


* 來源: <https://www.arthurtoday.com/2015/01/what-is-the-different-between-curl-and-wget.html>
 
