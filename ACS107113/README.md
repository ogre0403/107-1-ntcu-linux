# Final Exam

1. �]�wvirtualbox���������A�[�J�@�ihost-only�����d�A�bLinux�̳]�w����������������192.168.200.100/24�C�Х� `ifconfig`���ҡC
 + �إ߷s�����d�A�]�wIP��}��192.168.200.100/24�C

    ![GITHUB]( https://imgur.com/vNZv7O9.jpg"git�ϥ�")
    
 + �]�w���������d�C

    ![GITHUB]( https://imgur.com/OVEL3gT.jpg"git�ϥ�")
    
+ �i�J�������A��ifconfig���O�]�wIP�A�A����C

    ![GITHUB]( https://imgur.com/DixBVkg.jpg"git�ϥ�")
    
2. nginx�O�@�M�������A���n��A�Х�`yum`�w�ˡA�z�L`systemctl`�Ұʫ�A�ϥ�`netstat`����nginx���b�ϥ�Port 80�C
    
+ ���w�� epel�A��J���O yum install epel-release�C
    
    ![GITHUB]( https://imgur.com/69egiSt.jpg"git�ϥ�")
    
    ![GITHUB]( https://imgur.com/qPMrh1J.jpg"git�ϥ�")
    
+ �A�w�� nginx�A��J���O yum install nginx�C

    ![GITHUB]( https://imgur.com/ryk0KKG.jpg"git�ϥ�")
    
    ![GITHUB]( https://imgur.com/axgkqUV.jpg"git�ϥ�")
    
+ �w�˧���� systemctl start nginx �����O�A�Ұ� nginx�A�A�� systemctl status nginx ����C

    ![GITHUB]( https://imgur.com/nq1a9LW.jpg"git�ϥ�")
    
+ �A�z�L netstat �����O����nginx���b�ϥ�Port 80�C
    + ��J netstat -ap | grep nginx �A�T�{ nginx ���s�u�C
    + �A��J netstat -a�� | grep �G80 �A�T�{ Port 80 ���s�u���p�C

    ![GITHUB]( https://imgur.com/dp6VhNz.jpg"git�ϥ�")


3. �z�L���� windows �W���s�����A�s�u��192.168.200.100�C��?�����ҥi�H�s�u��Linux�W��nginx�������A���C

+ 
    
    ![GITHUB]( .jpg"git�ϥ�")
    
    
4. �bLinux�̡A��`curl`�s�u��192.168.200.100�C��?�����ҥi�H�s�u��Linux�W��nginx�������A���C

+ ��J���O curl 192.168.200.100 �A�p�U�ϡC

    ![GITHUB]( https://imgur.com/lIqdugn.jpg"git�ϥ�")
    
    ![GITHUB]( https://imgur.com/k2Zrm7k.jpg"git�ϥ�")

5. nginx����x�ɦ��`/?var/log/nginx`�ؿ��U�A��s�u���s�b�������ɡAnginx�|�O��������T�A�榡�p�U�C�䤤client��쬰�Ȥ��ip�C

+ 