+ ��ifconfig�]�wens37��192.168.200.100 ��ifconfig����
![GITHUB](https://imgur.com/CiTRQWB.jpg"git�ϥ�")
+ �w��nginx���systemctl�Ұ�
![GITHUB](https://imgur.com/Y11JqNG.jpg"git�ϥ�")
+ �ϥ�netstat -tulpn�T�{port80��nginx
![GITHUB](https://imgur.com/yLhCknL.jpg"git�ϥ�")
+ �]�i��netstat -ant |grep:80�ˬd 
+ ��curl 192.168.200.100�s�u
![GITHUB](https://imgur.com/h4WjzRb.jpg"git�ϥ�")
+ ��google�s��IP ���ڦn���ο����d�F�ҥHIP�O�t�@�i��
![GITHUB](https://imgur.com/wpPL4Ra.jpg"git�ϥ�")
+ �]���ڦA��curl�s��192.168.174.128
![GITHUB](https://imgur.com/J1TZE5y.jpg"git�ϥ�")
+ ��cut -d , -f 2 /var/log/nginx/error.log |sort|uniq -c�d�ݿ��~�T��
![GITHUB](https://imgur.com/SUW9pWe.jpg"git�ϥ�")