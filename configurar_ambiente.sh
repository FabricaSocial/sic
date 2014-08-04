echo "Configuração do ambiente SIC"
echo "-----------------------------------------"
echo "Atualizando gerenciador de pacotes"
yum update
echo "Instalando MySQL Server"
yum install -y mysql-server mysql-devel
echo ""
echo "Instalando development tools"
yum group -y install "development tools"
echo ""
echo "Instalando Python-PIP"
wget http://peak.telecommunity.com/dist/ez_setup.py
python ez_setup.py
easy_install pip
echo ""
echo "Instalando dependencias do projeto"
sudo pip install -r requirements.txt
