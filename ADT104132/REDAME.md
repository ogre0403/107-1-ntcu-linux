# HW7
### 使用ubuntu

1.apache log是apache web server的日誌檔</br>
* 先安裝curl
<pre><code>apt install curl</code></pre>
![1](img/1.png)</br>
在使用curl，下在日誌檔</br>
<pre><code>curl -O https://raw.githubusercontent.com/ogre0403/107-1-ntcu-linux/master/resource/web.log</code></pre>
![2](img/2.png)</br>
* 使用cat檢視</br>
<pre><code>cat web.log | grep error</code></pre>
![3](img/3.png)</br>
2.使用 tar cvf 檔案名稱 目錄</br>
<pre><code>tar cvf hw7test.tar /var 2>tar-err.log</code></pre>
![4](img/4.png)</br>
![5](img/5.png)</br>
![6](img/6.png)</br>
