* �]�wvirtualbox���������A�[�J�@�ihost-only�����d�A�bLinux�̳]�w����������������192.168.200.100/24�C�Х� ifconfig���ҡC(25%)

1.���}virtualbox�I�����u��A�A�I��W�誺�D�������޲z���A�إ߷s�������d�ÿ�JIPv4��}192.168.200.100

2.�A��]�w�ȡA�I������A�N�s�W�����d���ȭ��D�������d�A�èϥέ��s�W�������C

3.���}���������A��Jip a �i�o�{�s�W�Fvirbr0�A��Jip address add 192.168.200.100 broadcast + dev virbr0 label virbr0�A�A��Jifconfig�d��(��1)

* nginx�O�@�M�������A���n��A�Х�yum�w�ˡA�z�Lsystemctl�Ұʫ�A�ϥ�netstat����nginx���b�ϥ�Port 80�C(25%)

1.��J yum install nginx�U��

2.��J systemctl start nginx �Ұ�

3.��Jnetstat -nlp | grep nginx (��2)

* �z�L���� windows �W���s�����A�s�u��192.168.200.100�C������ҥi�H�s�u��Linux�W��nginx�������A���C(10%)

(��3)

* �bLinux�̡A��curl�s�u��192.168.200.100�C������ҥi�H�s�u��Linux�W��nginx�������A���C(10%)

1.��J curl 192.168.200.100 (��4)

* nginx����x�ɦ��/var/log/nginx�ؿ��U�A��s�u���s�b�������ɡAnginx�|�O��������T�A�榡�p�U�C�䤤client��쬰�Ȥ��ip�C (30%)

��5

��6