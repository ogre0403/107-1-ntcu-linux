##�]�wvirtualbox���������A�[�J�@�ihost-only�����d�A�bLinux�̳]�w����������������192.168.200.100/24�C�Х� `ifconfig`���ҡC

**ifconfig enp0s8 192.168.200.100
**ifconfig�Y�i�ݨ������192.168.200.100(��1)

##nginx�O�@�M�������A���n��A�Х�`yum`�w�ˡA�z�L`systemctl`�Ұʫ�A�ϥ�`netstat`����nginx���b�ϥ�Port 80�C

(�w��)
��������ʥ[�Jrepo�]�w�A�ê����z�Lyum�w��
**vi /etc/yum.repos.d/nginx.repo
(�g�J�U��{��)
**
[nginx]
name=nginx repo
baseurl=http://nginx.org/packages/centos/6/$basearch/
gpgcheck=0
enabled=1
(�Y�iyum install nginx)(��2)

(�ҰʡB����)
**systemctl start nginx
**netstat -ant | gerp :80
(�Y�i�X�{�p��3�ҥ�)

##�z�L���� windows �W���s�����A�s�u��192.168.200.100�C��?�����ҥi�H�s�u��Linux�W��nginx�������A���C
(��4)
##�bLinux�̡A��`curl`�s�u��192.168.200.100�C��?�����ҥi�H�s�u��Linux�W��nginx�������A��
(��5)

##
**cd var/log/nginx
**ll�i�H�d�ݨ짹�㪺��T access.log error.log
**cat error.log 
