* �]�wvirtualbox���������A�[�J�@�ihost-only�����d�A�bLinux�̳]�w����������������192.168.200.100/24�C�Х� `ifconfig`���ҡC(25%)</br></br>

�bvirtual box ������u��W�[�J�@�ihost-only�����d�A�æb������������J`ifconfig enp0s3 192.168.200.100`�A
��J`ifconfig`�i�H�b�̭��o�{�h�F�@��192.168.200.100�A�̫��`ping 192.168.200.100`���ճs�����\�C
![1](https://github.com/ad8902210302/107-1-ntcu-linux/blob/final/ACS107127/screen/1.png)</br>
![1](https://github.com/ad8902210302/107-1-ntcu-linux/blob/final/ACS107127/screen/2.png)</br>
![1](https://github.com/ad8902210302/107-1-ntcu-linux/blob/final/ACS107127/screen/3.png)</br>
![1](https://github.com/ad8902210302/107-1-ntcu-linux/blob/final/ACS107127/screen/4.png)</br></br>

* nginx�O�@�M�������A���n��A�Х�`yum`�w�ˡA�z�L`systemctl`�Ұʫ�A�ϥ�`netstat`����nginx���b�ϥ�Port 80�C(25%)</br></br>

��J`vi /etc/yum.repos.d/nginx.repo`�A�æb���e�s�W</br>
`[nginx] 
name=nginx repo 
baseurl=http://nginx.org/packages/centos/7/$basearch/ 
gpgcheck=0 
enabled=1 `
���۴N�i�H�U���O�w��`yum install nginx`</br>
![1](https://github.com/ad8902210302/107-1-ntcu-linux/blob/final/ACS107127/screen/5.png)</br></br>

�Ұ� Nginx �A�ȡG`systemctl start nginx`</br>
�ˬd Nginx �O�_���`�ҰʡG`systemctl status nginx`</br>
��`netstat -ano | grep 0.0:80`����nginx���b�ϥ�Port 80</br>
![1](https://github.com/ad8902210302/107-1-ntcu-linux/blob/final/ACS107127/screen/6.png)</br></br>

* �z�L���� windows �W���s�����A�s�u��192.168.200.100�C��?�����ҥi�H�s�u��Linux�W��nginx�������A���C(10%)
![]()</br></br>

* �bLinux�̡A��`curl`�s�u��192.168.200.100�C��?�����ҥi�H�s�u��Linux�W��nginx�������A���C(10%)
![1](https://github.com/ad8902210302/107-1-ntcu-linux/blob/final/ACS107127/screen/9.png)</br></br>

* nginx����x�ɦ��`/?var/log/nginx`�ؿ��U�A��s�u���s�b�������ɡAnginx�|�O��������T�A�榡�p�U�C�䤤client��쬰�Ȥ��ip�C (30%)