# HW9
### 使用ubuntu

#### 1.yum 是透過設定檔的規範去找到安裝/升級伺服器，預設的 CentOS 7 的設定檔的檔名為 /etc/yum.repos.d/CentOS-Base.repo。Red Hat 提供了 EPEL 的計畫，提供額外打包好的軟體，提供給用戶使用。但這些軟體並非官網提供， 因此其軟體庫並沒有在預設的設定檔內。</br>

#### 請閱讀 https://www.cyberciti.biz/faq/installing-rhel-epel-repo-on-centos-redhat-7-x/ 後，依照其作法，啟用epel repo�isitory，並安裝htop</br>

ubuntu 應該無法安裝epel第三方包</br>

[資料來源1](https://laibulai.iteye.com/blog/1416536?fbclid=IwAR3szwrDAeyYrT296xOwM--uFoL9kWz5BLILMC4o-OokbIrO34gnBeYDZC4)</br>
[資料來源2](https://askubuntu.com/questions/720952/impossible-to-install-epel-5-4-on-ubuntu-14-04)</br>

安裝htop</br>
<pre><code>sudo apt-get install htop</code></pre>
![1](img/1.png)</br>
檢查htop</br>
<pre><code>htop</code></pre>
![1](img/2.png)</br>
