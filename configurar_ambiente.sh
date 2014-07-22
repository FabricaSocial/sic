echo "Configuração do ambiente SIC"
echo "-----------------------------------------"
echo "Instalando MySQL Server"
yum update
yum install -y mysql-server mysql-devel
echo ""
echo "Instalando development tools"
yum group -y install "development tools"
echo ""
echo "Instalando Python-PIP"
easy_install pip
echo ""
echo "Instalando dependencias do projeto"
sudo pip install -r requirements.txt
