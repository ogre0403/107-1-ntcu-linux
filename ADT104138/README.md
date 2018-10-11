# 安裝Linux
## ADT104138 羅苡倫
*****
## 一、前置作業
1.安裝[Oracle VM VirtualBox](https://www.virtualbox.org/)虛擬機器軟體。</br>
![安裝VM](
        https://github.com/LoYiLun/107-1-ntcu-linux/blob/HW-2/ADT104138/VM1.png
      )</br>
2.下載[CentOs映像檔](https://www.centos.org/download/)，這邊使用[Minimal版本](http://isoredirect.centos.org/centos/7/isos/x86_64/CentOS-7-x86_64-Minimal-1804.iso)示範。</br>
*****
## 二、安裝過程
1.打開Oracle VM VirtualBox軟體，並且點擊左上角的新增圖示。</br>
![新增](https://github.com/LoYiLun/107-1-ntcu-linux/blob/HW-2/ADT104138/VM2.png)</br>

2.輸入自定義的名稱，類型及版本選擇相對應的選項。</br>
![新增2](https://github.com/LoYiLun/107-1-ntcu-linux/blob/HW-2/ADT104138/VM4.png)</br>

3.依個人喜好選擇配置的記憶體大小。</br>
![mem](https://github.com/LoYiLun/107-1-ntcu-linux/blob/HW-2/ADT104138/VM5.png)</br>

4.選擇「立即建立虛擬硬碟」。</br>
![](https://github.com/LoYiLun/107-1-ntcu-linux/blob/HW-2/ADT104138/VM6.png)</br>

5.選擇「VDI」類型。</br>
![](https://github.com/LoYiLun/107-1-ntcu-linux/blob/HW-2/ADT104138/VM7.png)</br>

6.依照使用者需求，選擇動態配置或固定大小，兩者差異在於前者會依照空間大小配置，而後者依使用者設定配置。</br>
![](https://github.com/LoYiLun/107-1-ntcu-linux/blob/HW-2/ADT104138/VM8.png)</br>

7.依照需求設定大小。</br>
![](https://github.com/LoYiLun/107-1-ntcu-linux/blob/HW-2/ADT104138/VM9.png)</br>

8.基礎設定完後，再點選左上角的設定值圖示。</br>
![](https://github.com/LoYiLun/107-1-ntcu-linux/blob/HW-2/ADT104138/VM11.png)</br>

9.點選 存放裝置 → 屬性，選擇剛剛下載的CentOs的映像檔。</br>
![](https://github.com/LoYiLun/107-1-ntcu-linux/blob/HW-2/ADT104138/VM12.png)</br>

10.勾選 網路 → 介面卡2 → 啟用網路卡，並且選擇附加到 → 「僅限主機」介面卡。</br>
![](https://github.com/LoYiLun/107-1-ntcu-linux/blob/HW-2/ADT104138/VM13.png)</br>

11.接著選擇左上角的啟動圖示。</br>
![](https://github.com/LoYiLun/107-1-ntcu-linux/blob/HW-2/ADT104138/VM14.png)</br>

12.選擇第一個選項安裝。</br>
![](https://github.com/LoYiLun/107-1-ntcu-linux/blob/HW-2/ADT104138/VM15.png)</br>

13.依照使用者需求選擇語言。</br>
![](https://github.com/LoYiLun/107-1-ntcu-linux/blob/HW-2/ADT104138/VM16.png)</br>

14.選擇下方圖示，系統 → 安裝目的地。</br>
![](https://github.com/LoYiLun/107-1-ntcu-linux/blob/HW-2/ADT104138/VM17.png)</br>

15.勾選 其他儲存選項 → 讓我自行配置磁碟分割。</br>
![](https://github.com/LoYiLun/107-1-ntcu-linux/blob/HW-2/ADT104138/VM19.png)</br>

16.在左下角的+號圖示新增/ 和 /home 的掛載點，如下圖。</br>
![](https://github.com/LoYiLun/107-1-ntcu-linux/blob/HW-2/ADT104138/VM20.png)</br>
![](https://github.com/LoYiLun/107-1-ntcu-linux/blob/HW-2/ADT104138/VM21.png)</br>

17.新增完後點擊左上角的完成，並且選擇接受變更。</br>
![](https://github.com/LoYiLun/107-1-ntcu-linux/blob/HW-2/ADT104138/VM22.png)</br>

18.這時候跳回上一個畫面，選擇下方圖示的 系統 → 網路與主機名稱，開啟網路功能。</br>
![](https://github.com/LoYiLun/107-1-ntcu-linux/blob/HW-2/ADT104138/VM23.png)</br>
![](https://github.com/LoYiLun/107-1-ntcu-linux/blob/HW-2/ADT104138/VM24.png)</br>

19.接著就會開始安裝，在此期間我們來順便新增用戶以及設定root密碼，請妥善保管密碼。</br>
![](https://github.com/LoYiLun/107-1-ntcu-linux/blob/HW-2/ADT104138/VM25.png)</br>
![](https://github.com/LoYiLun/107-1-ntcu-linux/blob/HW-2/ADT104138/VM26.png)</br>

20.安裝完後，會要求重開機，這裡的重開機指的是虛擬機器，並非電腦本身。</br>
![](https://github.com/LoYiLun/107-1-ntcu-linux/blob/HW-2/ADT104138/VM27.png)</br>

21.接著會自動進入登入畫面，輸入剛剛建立使用者名稱及密碼即可登入，到此步驟基本上已經大功告成了。</br>
![](https://github.com/LoYiLun/107-1-ntcu-linux/blob/HW-2/ADT104138/VM28.png)</br>
*****
## 三、檢查
1.登入後，輸入指令<pre><code>df</code></pre>檢查分割的磁碟區域大小。
![](https://github.com/LoYiLun/107-1-ntcu-linux/blob/HW-2/ADT104138/VM30.png)</br>

2.使用結束後，記得使用關機指令。
<pre><code>shutdown -h now</code></pre>
# 感謝觀看 The End