<strong>第一大題</strong>

<em>1.<em>
+ 執行wget https://raw.githubusercontent.com/ogre0403/107-1-ntcu-linux/master/resource/web.log即可下載目標檔案
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-7/ACS107103/kali-2018-12-04-20-32-15.png)

<em>2.<em>
+ 執行cat web.log | grep error把帶有error的內容抓出來
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-7/ACS107103/kali-2018-12-04-20-35-30.png)

<strong>第二大題</strong>

<em>1.<em>
+ 執行tar -czf var.tgz /var 2> tar-err.log
+ (後面使用 2> 是將錯誤訊息重新導向到tar-err.log)
+ 關於tar的用法以及參數請參考http://www.vixual.net/blog/archives/127
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-7/ACS107103/kali-2018-12-04-20-48-08.png)
+ 之後執行cat tar-err.log來查看重新導向後的錯誤訊息(還滿多的...)
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-7/ACS107103/kali-2018-12-04-20-48-46.png)
