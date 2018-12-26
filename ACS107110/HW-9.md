HW-9

(root環境下)
##Install Extra Packages for Enterprise Linux repository configuration (recommended)
→sudo yum install epel-release(如圖1)

##List your new repos
→sudo yum repolist(如圖2)

##Search and install package
→yum --disablerepo="*" --enablerepo="epel" list available(如圖3)

##Search and install htop package from epel repo on a CentOS/RHEL 7.x
→yum search htop(如圖4)
→yum info htop(如圖5)
→yum install htop(如圖6)
