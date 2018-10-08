# Linux Centos-7 安裝心得
==========================


### 所有圖片接來自[鳥哥](http://linux.vbird.org/linux_basic/0157installcentos7.php)


***	首先要確認安裝後希望達成的效果

>因為我這次的安裝只是在個人電腦的一個練習，而非要用到更為複雜的功能來做更複雜的事情，所以我的基本硬體配備一定夠我使用Linux CentOS-7 minimal系統。這次主要的練習是區塊分割，因此其他更複雜的設定部分沒動到。

**	確認檢查清單
>根據鳥哥提供的[檢查清單](http://linux.vbird.org/linux_basic/0157installcentos7.php#design)來確認事前準備的完成度

*	是，ISO檔

*	CentOS 7-x86_64-Minimal-1804

*	x86_64

*	是

*	已決定硬碟分割方法

*	沒

*	X

*	自動設定，應該也在MBR

*	使用DHCP

*	Virtualbox

***	開始進入安裝環節

>先開啟Virtualbox並利用左上角新增圖示建立一個新的虛擬機器，名稱就設定CentOS_7，*類型*選擇Linux、*版本*選擇Other Linux(64-bit)、設定讓記憶體有基本大小以免突然用完，接著建立。
>建立完成後再次選擇並點選右上方_設定_值進行設定。點選設定中的_存放裝置_，點選控制器旁的新增圖示，點擊選擇磁碟並在瀏覽中選擇已經下載完成的CentOS-7-x86_64-Minimal-1804映像檔(ISO檔)。完成後再根據老師的建議點選_設定_的_網路_進行設定，點擊介面卡2並勾選啟用網路卡，在_附加到_中選擇「僅限主機」介面卡，下方名稱則自動設定好Virtualbox了。
>接著回Virtualbox首頁啟動建立好的虛擬機器。

===========================

***	進入啟動畫面

![id](http://linux.vbird.org/linux_basic/0157installcentos7/centos7_01.jpg)

![id](http://linux.vbird.org/linux_basic/0157installcentos7/centos7_04.jpg)

>因為是在模擬器上練習、檔案也是官網抓的，所以就直接選擇Install CentOS 7，接著經過一段等待時間後進入語言安裝的選擇介面，選擇中文 _繁體中文(台灣)_，接著進入安裝摘要，等待系統的自動設定結束後再手動調整設定。

![id](http://linux.vbird.org/linux_basic/0157installcentos7/centos7_05.jpg)

>確認時間、支援語言、鍵盤配置正確後記得設定鍵盤配置中的配置切換來協助輸入語言切換。

![id](http://linux.vbird.org/linux_basic/0157installcentos7/centos7_10.jpg)

>安裝來源會自動設定，軟體選擇可自行選擇安裝但Minimal只有最小型安裝。

***	磁碟分割

![id](http://linux.vbird.org/linux_basic/0157installcentos7/centos7_11.jpg)

>點選進入安裝目的地後，在本機標準磁碟中選擇Virtualbox預設的CentOS_7磁碟，下方的其他儲存選項中的_分割硬碟_點選_我將配置分頁_，然後點擊左上方完成。

![id](http://linux.vbird.org/linux_basic/0157installcentos7/centos7_14.jpg)

>進入分割頁面後，選擇_標準分割區_再點選左下角的加號，掛在點選擇_biosboot_、輸入2M容量後按新增，再依相同步驟建立_/boot_的掛載點、輸入1G容量。

![id](http://linux.vbird.org/linux_basic/0157installcentos7/centos7_21.jpg)

>同樣步驟新增_/_和_/home_的掛載點，只是根據鳥哥的建議，將前兩者的裝置類型由標準分割區更改為_LVM_。

![id](http://linux.vbird.org/linux_basic/0157installcentos7/centos7_24.jpg)

>確認以上步驟完成後確認biosboot下方的_vda1_、/boot下方的_vda2_、/下方的_centos-root_和/home下方的_centos-home_。結束後點擊左上方完成，會跳出變更摘要的視窗，看過之後選擇左下方接受變更即完成手動分割硬碟。

**	回到安裝摘要

>最後的KDUMP和網路(DHCP)系統都已經自動設定好了，所以選擇左下方開始安裝

***	用戶設定

![id](http://linux.vbird.org/linux_basic/0157installcentos7/centos7_32.jpg)

>設定_root密碼_並記好
>建立用戶，並根據鳥哥的建議將用戶升級成管理員，萬一真的忘記root密碼才有救。

![id](http://linux.vbird.org/linux_basic/0157installcentos7/centos7_35.jpg)

>完成設定後選擇左下方重新開機，重啟後即完成安裝，但是Minimal沒有圖形介面。