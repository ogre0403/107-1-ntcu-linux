###�@.

##�bVirtalBox���إߤ@�ӷs��Host-only �����d�A���q��192.168.100.1/24

* ���k�W��**����u��**->**�D�������޲z��**->**�إ�**
* ��**���e**�վ���إߪ������d�A��ܤ�ʲպA�����d�A�N**IPv4 ��}�אּ192.168.100.1**

![1]


##�إߵ�������-1�A�ñҥ�host-only�����d�A�z�Lifconfig �� ip���O�A�]�w��������-1��������192.168.100.100/24

**�إߵ�������(1)**
* ��J` ip address add 192.168.100.100/24 broadcast + dev enp0s3 `�]�w1������

![2]



##�إߵ�������-2�A�ñҥ�host-only�����d�A�z�Lifconfig �� ip���O�A�]�w��������-2��������192.168.100.200/24

**�إߵ�������(2)**
* ��J` ip address add 192.168.100.200/24 broadcast + dev enp0s3 `�]�w2������

![3]



##�N�G�x���������������]�w�s��/etc/sysconfig/network-scripts/�U�۹�����ifcfg-*�ɮסA���s�Ұʵ��������A�T�{����ip�]�w�L�~�C

#1

* ��J` vi /etc/sysconfig/network-scripts/ifcfg-* `
> ��I�i�J�s��
1. �N**ONBOOT�令yes**
2. �s�WIPADDR=192.168.100.200
> Esc->:wq�x�s���}
> ���s�}��

![4]

#2

* ��J` vi /etc/sysconfig/network-scripts/ifcfg-* `
> ��I�i�J�s��
1. �N**ONBOOT�令yes**
2. �s�WIPADDR=192.168.100.100
> Esc->:wq�x�s���}
> ���s�}��

![5]


##�q��������-1 ping ��������-2�T�{�����O�s�q�A�ñq��������-2 ping ��������-1�A�T�{�����]�O�s�q�C

#1

* ��J` ping -c 3 192.168.100.200 `�T�{�s�u
> �O�o�n�[-c���Ѽƭ�����檺���� **���M�|�o�͸�ڤ@�˪��G��QQ**
> �u���ѰO�[�F�N����ctrl��c�N�i�H�X�h�F

![6]

#2

* ��J` ping -c 3 192.168.100.100 `�T�{�s�u

![7]