# ProyectoDatosAbiertos
Proyecto sobre datos abiertos de la UGR

### Instalación CKAN (versión 2.5, Ubuntu 14.04 64 bits)

Pasos de instalación que luego habrá que automatizar:

##### Instalar dependencias:
```
sudo apt-get update && apt-get install -y apache2 git-core libapache2-mod-wsgi libpq-dev libpq5 nginx openjdk-7-jdk postgresql python-dev python-pastescript python-pip redis-server solr-jetty
```

##### Instalar CKAN
```
wget http://packaging.ckan.org/python-ckan_2.5-trusty_amd64.deb
sudo dpkg -i python-ckan_2.5-trusty_amd64.deb
sudo pip install -r /usr/lib/ckan/default/src/ckan/requirements.txt
```

##### Instalar base de datos PostgreSQL
```
sudo -u postgres createuser -S -D -R -P ckan_default
```

Introducir **PASSWORD**.

```
sudo -u postgres createdb -O ckan_default ckan_default -E utf-8
```

##### Instalar Solr

Editar **/etc/default/jetty**:
* *NO_START=1* -> **NO_START=0**
* *#JETTY_HOST=$(uname -n)* -> **JETTY_HOST=127.0.0.1**
* *#JETTY_PORT=8080* -> **JETTY_PORT=8983**

```
sudo service jetty start
sudo mv /etc/solr/conf/schema.xml /etc/solr/conf/schema.xml.bak
sudo ln -s /usr/lib/ckan/default/src/ckan/ckan/config/solr/schema.xml /etc/solr/conf/schema.xml
sudo service jetty restart
```

Editar **/etc/ckan/default/production.ini**:
* *sqlalchemy.url = postgresql://ckan_default:pass@localhost/ckan_default* -> **sqlalchemy.url = postgresql://ckan_default:PASSWORD@localhost/ckan_default**
* *#solr_url = http://127.0.0.1:8983/solr* -> **solr_url=http://127.0.0.1:8983/solr**
* *ckan.site_url = * -> **ckan.site_url = http://opendata.ugr.es**

Acceder a **http://localhost:8983/solr/**.

##### Crear tablas de la base de datos

```
cd /usr/lib/ckan/default/src/ckan
paster db init -c /etc/ckan/default/production.ini
```
