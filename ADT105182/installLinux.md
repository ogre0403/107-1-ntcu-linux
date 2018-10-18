#UBUNTU到官網下載iso檔
	Download version: 16.04LTS

#製作開機USB
	windows環境底下使用rufus

#按照系統指示安裝
	無雙系統/虛擬機, 故無須分割硬碟
	無顯示卡故無須安裝顯卡驅動
	因為鍵盤改為日文, 故鍵盤設定為日規, 並安裝ibus-anthy
	安裝vim並編輯vimrc
		https://imgur.com/BkQh8vF
	
#修改界面
	將Unity界面修改為XFCE
		Uninstall Unity
			sudo apt purge unity*
		Install XFCE4
			sudo apt install xfce4
			sudo apt install xfce4-goodies
	
	修改theme和icon
		https://www.opendesktop.org/s/XFCE
		安裝路徑：
		/usr/share/icons
		/usr/share/themes

#完成
	https://imgur.com/rWqmANh	

