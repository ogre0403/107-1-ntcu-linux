##  1.</br>
###  �إߤT�ӥΤ�A�b���W�٤��O���G examuser1, examuser2, examuser3 �A�P�ɤT�ӥΤ�</br>
###  ���K�X���O�y ItIsExam �z�C(�аѦҮѤWpasswd --stdin������)</br></br>

####  �`�N"useradd"�n��root�Ӱ���</br>
![Alt text](https://github.com/ad8902210302/107-1-ntcu-linux/blob/master/ACS107127/123/1.jpg)</br>
###  �ЧR���t�Τ��� examuser3 �o�ӱb���A�P�ɱN�o�ӱb�����a�ؿ��P�l���ɮצP�B�R��</br></br>

####  ��"-r"���ѼƱN�a�ؿ��B�l���ɮפ@�֧R���C</br>
![Alt text](https://github.com/ad8902210302/107-1-ntcu-linux/blob/master/ACS107127/123/2.jpg)</br>
###  examuser1 ���p�߳Q�޲z���R���F�A���O�o�ӱb�����a�ؿ��P�����l���٦s�b�C�аѦ�</br>
###  �o�ӱb���i�઺�a�ؿ��ҫO�d�� UID �P GID�A �ù��եH�ӱb���즳��UID/GID��T�ӭ���</br>
###  �ӱb���C�ӳo�ӱb�����K�X�е��� ItIsExam ���˦��C</br></br>

####  �ϥ�"useradd -u (uid) �b���W "�i�H�N�s�b���P�¦���uid���s���C</br>
![Alt text](https://github.com/ad8902210302/107-1-ntcu-linux/blob/master/ACS107127/123/4.jpg)</br>
##  2.</br>
###  �إ�examuser4�ϥΪ̱b���A�K�X���N�C</br>
###  �ϥ� root �N /etc/securetty �ƻs�� examuser4�A�B�o�ӱb���n�������ϥθ��ɮ�</br>
###  �~��A(�Y���Ҧ����v��)�C</br>
![Alt text](https://github.com/ad8902210302/107-1-ntcu-linux/blob/master/ACS107127/123/6.jpg)</br>

###  �إߤ@�ӦW�� /examdata/change.txt �����ɮסA�o���ɮת��֦��̬� sshd�A�֦��s��</br>
###  �� users�Asshd �iŪ�i�g�Ausers �s�զ����iŪ�A ��L�H�S�v���C�B�o���ɮת��ק�����</br>
###  �վ㦨2012�~12��21��(������T�Y�i�A�ɶ��H�K)</br></br>

####  �ϥ�touch�s�W�@�Ӥ��C��chmod�ӧ���ɮ��v���C�ק����ɶ���00:00 touch -d 20150101 (filename)</br>
![Alt text](https://github.com/ad8902210302/107-1-ntcu-linux/blob/master/ACS107127/123/7.jpg)</br>
##  3.</br>
###  �Шϥ� root �������إߩ��U���ɮ׻P�v���G</br>
####  drwxrwxr-x  root root /dev/shm/unit05/</br>
####  drwxr-xr--  root root /dev/shm/unit05/dir1/</br>
####  -rw-r--r--  root root /dev/shm/unit05/dir1/file1 (�ƻs�Ӧ� /etc/hosts)</br>
####  drwxr-x--x  root root /dev/shm/unit05/dir2/</br>
####  -rw-r--r--  root root /dev/shm/unit05/dir2/file2 (�ƻs�Ӧ� /etc/hosts)</br>
####  drwxr-xr-x  root root /dev/shm/unit05/dir3/</br>
####  -rw-rw-rw-  root root /dev/shm/unit05/dir3/file3 (�ƻs�Ӧ� /etc/hosts)</br>
####  drwxrwxrwx  root root /dev/shm/unit05/dir4/</br>
####  -rw-------  root root /dev/shm/unit05/dir4/file4 (�ƻs�Ӧ� /etc/hosts)</br></br>

#####  �إߥؿ���"mkdir"�C�إ��ɮץ�"touch"�C����v����"chmod"�C�ƻs��"cp"�C
![Alt text](https://github.com/ad8902210302/107-1-ntcu-linux/blob/master/ACS107127/123/8.jpg)</br>
![Alt text](https://github.com/ad8902210302/107-1-ntcu-linux/blob/master/ACS107127/123/9.jpg)</br>
![Alt text](https://github.com/ad8902210302/107-1-ntcu-linux/blob/master/ACS107127/123/10.jpg)</br>
![Alt text](https://github.com/ad8902210302/107-1-ntcu-linux/blob/master/ACS107127/123/11.jpg)</br>

###  �ϥΤ@��ϥΪ� �������i��U���u�@�G</br>
##### ��"su (username)"���^�ۨ��b��</br>
###  Q:�Шϥ� ls -l /dev/shm/unit05/dir[1-4] �̾ڿ�X�����G��������|���ͳo�ǰ��D�H</br>
![Alt text](https://github.com/ad8902210302/107-1-ntcu-linux/blob/master/ACS107127/123/12.jpg)</br>
###  Q:�Шϥ� ls -l /dev/shm/unit05/dir1/file1 �A�̧ǱN�W�z���ɦW��</br>
###  dir1/file1 ~ dir4/file4 ����A�̾ڲ��ͪ����G��������|�p���H</br>
###  A:�]���@�}�l�����v�����P�A�~�|�y�����G���P�C</br>
![Alt text](https://github.com/ad8902210302/107-1-ntcu-linux/blob/master/ACS107127/123/14.jpg)</br>
###  Q:�Шϥ� vim /dev/shm/unit05/dir1/file1 ~ vim /dev/shm/unit05/dir4/file4�A</br>
�����x�s (�αj���x�s)�A��������i�H/���i�H�x�s�H</br></br>
##  file1 => ���iŪ���i�s��</br>
![Alt text](https://github.com/ad8902210302/107-1-ntcu-linux/blob/master/ACS107127/123/15.jpg)</br>
![Alt text](https://github.com/ad8902210302/107-1-ntcu-linux/blob/master/ACS107127/123/16.jpg)</br></br>
##  file2 => ���iŪ���i�s��</br>
![Alt text](https://github.com/ad8902210302/107-1-ntcu-linux/blob/master/ACS107127/123/17.jpg)</br>
![Alt text](https://github.com/ad8902210302/107-1-ntcu-linux/blob/master/ACS107127/123/18.jpg)</br></br>
##  file3 => �iŪ�i�Q�s��</br>
![Alt text](https://github.com/ad8902210302/107-1-ntcu-linux/blob/master/ACS107127/123/19.jpg)</br>
![Alt text](https://github.com/ad8902210302/107-1-ntcu-linux/blob/master/ACS107127/123/20.jpg)</br></br>
##  file4 => ���iŪ���i�s�� </br>
![Alt text](https://github.com/ad8902210302/107-1-ntcu-linux/blob/master/ACS107127/123/21.jpg)</br>