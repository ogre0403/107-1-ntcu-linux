# HW-9
1. Install Extra Packages for Enterprise Linux repository configuration (recommended)
  
  sudo yum install epel-release
  
2. List your new repos
  
  sudo yum repolist

3. Search and install package
  
  sudo yum --disablerepo="*" --enablerepo="epel" list available
  
4. Search and install htop package from epel repo on a CentOS/RHEL 7.x
  
  yum search htop
  
  yum info htop
  
  yum install htop
