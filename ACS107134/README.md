1.
### Q:�إߤT�ӥΤ�A�b���W�٤��O���G examuser1, examuser2, examuser3 �A�P�ɤT�ӥΤ᪺�K�X���O�y ItIsExam �z�C(�аѦҮѤWpasswd --stdin������) 
  �`�N"useradd"�����O�n��root�Ӱ���@�A�p�G�@�}�l�S����"-p"���ܡC�ƫ�]�K�X�n��"passwd+username"�C
![1](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-3/ACS107134/1.JPG)

---------------------------------------���j�u-----------------------------------------

### Q:�ЧR���t�Τ��� examuser3 �o�ӱb���A�P�ɱN�o�ӱb�����a�ؿ��P�l���ɮצP�B�R���C 
  �Y�n�N�a�ؿ��B�l���ɮקR�����ܭn�O�o�n�[ "-r" ���M�|�ܳ·СC
![2](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-3/ACS107134/2.JPG)

---------------------------------------���j�u-----------------------------------------

### Q:examuser1 ���p�߳Q�޲z���R���F�A���O�o�ӱb�����a�ؿ��P�����l���٦s�b�C�аѦҳo�ӱb���i�઺�a�ؿ��A�ҫO�d�� UID �P GID�A �ù��եH�ӱb���즳�� UID/GID ��T�ӭ��ظӱb���C�ӳo�ӱb�����K�X�е���ItIsExam���˦��C(�����ظm�b�������O�A�аѦ� man useradd ���u�W��󪺻���) 
  �ϥ�"useradd -u (uid) �b���W "�i�H�N�s�b���P�¦���uid���s���C
![3](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-3/ACS107134/3.JPG)

---------------------------------------���j�u-----------------------------------------

2.
### Q:�إ�examuser4�ϥΪ̱b���A�K�X���N�C 
### Q:�ϥ� root �N /etc/securetty �ƻs�� examuser4�A�B�o�ӱb���n�������ϥθ��ɮפ~��A(�Y���Ҧ����v��)�C 
  �o�̡A�ڱN/etc/securetty�ɮ��v���W�[��examuser4�A�H�U�O�ڪ��覡�A���I���j�C
![4](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-3/ACS107134/4.JPG)

---------------------------------------���j�u-----------------------------------------

### Q:�إߤ@�ӦW�� /examdata/change.txt �����ɮסA�o���ɮת��֦��̬� sshd�A�֦��s�լ� users�Asshd �iŪ�i�g�Ausers �s�զ����iŪ�A ��L�H�S�v���C�B�o���ɮת��ק����нվ㦨 2012 �~ 12 �� 21 �� (������T�Y�i�A�ɶ��H�K) 
> �ϥ�touch�s�W�@�Ӥ��A�ç��֦��̬�sshd�A�s�է令users�C ��chmod�ӧ���ɮ��v���C 
> ���ק������覡��: 
-	1.�u�����ɶ��ܬ�00:00 	touch -d 20150101 (filename) 
-	2.����&�ɶ�		touch -t 201501150821.32 (filename) 

![5](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-3/ACS107134/5.JPG)

---------------------------------------���j�u-----------------------------------------

3.
### Q:�Шϥ� root �������إߩ��U���ɮ׻P�v���G 
#### drwxrwxr-x  root root /dev/shm/unit05/ 
#### drwxr-xr--  root root /dev/shm/unit05/dir1/ 
#### -rw-r--r--  root root /dev/shm/unit05/dir1/file1 (�ƻs�Ӧ� /etc/hosts) 
#### drwxr-x--x  root root /dev/shm/unit05/dir2/ 
#### -rw-r--r--  root root /dev/shm/unit05/dir2/file2 (�ƻs�Ӧ� /etc/hosts) 
#### drwxr-xr-x  root root /dev/shm/unit05/dir3/
#### -rw-rw-rw-  root root /dev/shm/unit05/dir3/file3 (�ƻs�Ӧ� /etc/hosts) 
#### drwxrwxrwx  root root /dev/shm/unit05/dir4/ 
#### -rw-------  root root /dev/shm/unit05/dir4/file4 (�ƻs�Ӧ� /etc/hosts) 
> �إ��ɮץ�"touch"�B�إߥؿ���"mkdir"�C	�ƻs��"cp (���ƻs���ɮ�) (�мg���ɮ�)" 
> ����v����"chmod"�@�Achmod���Ϊk�O chmod (ugoa)(+-=)(rwx-)(,) filename or chmod ??? filename(?�O�W�ߪ��Ʀr) 
![6](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-3/ACS107134/6.JPG)
![7](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-3/ACS107134/7.JPG)

---------------------------------------���j�u-----------------------------------------

### Q:�ϥΤ@��ϥΪ� �������i��U���u�@�G 
  �ڤ�����ۤv���b����"su username" 
### Q:�Шϥ� ls -l /dev/shm/unit05/dir[1-4] �̾ڿ�X�����G��������|���ͳo�ǰ��D�H 
  �̷ӭn�D������O 
![8](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-3/ACS107134/8.JPG)

---------------------------------------���j�u-----------------------------------------

### Q:�Шϥ� ls -l /dev/shm/unit05/dir1/file1 �A�̧ǱN�W�z���ɦW�� dir1/file1 ~ dir4/file4 ����A�̾ڲ��ͪ����G��������|�p���H 
  �̷Ӥ@�}�l< �v�� >�]�w�����P�y�N�����G�]�N���@�ˡC 
![9](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-3/ACS107134/9.JPG)

---------------------------------------���j�u-----------------------------------------

### Q:�Шϥ� vim(or vi) /dev/shm/unit05/dir1/file1 ~ vim /dev/shm/unit05/dir4/file4�A�����x�s (�αj���x�s)�A��������i�H/���i�H�x�s�H 
-  file1��� -> (Permission Denied) ���iŪ���i�s�� 
-  file2��� -> �L�k��tab����X��(��Ū�ɤ��i���) 
-  file3��� -> �i�Q�s�� 
-  file4��� -> (Permission Denied) ���iŪ���i�s�� 
![10](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-3/ACS107134/10.JPG)
![11](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-3/ACS107134/11.JPG)
![12](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-3/ACS107134/12.JPG)
![13](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-3/ACS107134/13.JPG)

