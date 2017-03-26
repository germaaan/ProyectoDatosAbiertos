### Crear tablas de la base de datos

```bash
cd /usr/lib/ckan/default/src/ckan
paster db init -c /etc/ckan/default/production.ini
```

### Configurar DataStore

Editar **/etc/ckan/default/production.ini**:

- _ckan.plugins = stats text_view image_view recline_view_ -> **ckan.plugins = stats text_view image_view recline_view datastore**

```bash
sudo -u postgres createuser -S -D -R -P -l datastore_default
sudo -u postgres createdb -O ckan_default datastore_default -E utf-8
```

Editar **/etc/ckan/default/production.ini**:

- *#ckan.datastore.write_url = postgresql://ckan_default:pass@localhost/datastore_default* -> **ckan.datastore.write_url = postgresql://ckan_default:{PASSWORD}@127.0.0.1/datastore_default**
- *#ckan.datastore.read_url = postgresql://datastore_default:pass@localhost/datastore_default* -> **ckan.datastore.read_url = postgresql://datastore_default:{PASSWORD}@127.0.0.1/datastore_default**

```bash
sudo ckan datastore set-permissions | sudo -u postgres psql --set ON_ERROR_STOP=1
```

### Configurar FileStore

```bash
sudo mkdir -p /var/lib/ckan/default
```

Editar **/etc/ckan/default/production.ini**:

- *#ckan.storage_path = /var/lib/ckan* -> **ckan.storage_path = /var/lib/ckan/default**

```bash
sudo chown www-data /var/lib/ckan/default
sudo chmod u+rwx /var/lib/ckan/default
sudo service apache2 reload
```

### Configurar DataPusher

Editar **/etc/ckan/default/production.ini **:

- *#ckan.datapusher.url = http://127.0.0.1:8800/* -> **ckan.datapusher.url = http://0.0.0.0:8800/**
- _ckan.plugins = stats text_view image_view recline_view datastore_ -> **ckan.plugins = stats text_view image_view recline_view datastore datapusher**

```bash
sudo service apache2 restart
```

### Configurar visualizaciones

```bash
git clone https://github.com/ckan/ckanext-viewhelpers.git
cd ckanext-viewhelpers
sudo python setup.py install
```

```bash
git clone https://github.com/ckan/ckanext-dashboard.git
cd ckanext-dashboard
sudo python setup.py install
```

```bash
git clone https://github.com/ckan/ckanext-basiccharts.git
cd ckanext-basiccharts
sudo python setup.py install
```

```bash
git clone https://github.com/ckan/ckanext-mapviews.git
cd ckanext-mapviews
sudo python setup.py install
```

```bash
sudo pip install ckanext-geoview
sudo pip install ckanext-pdfview
```

- _ckan.plugins = stats text_view image_view recline_view datastore_ -> **ckan.plugins = stats viewhelpers resource_proxy dashboard_preview recline_grid_view recline_graph_view recline_map_view text_view image_view webpage_view geo_view pdf_view linechart barchart piechart basicgrid navigablemap choroplethmap datapusher datastore**

### Instalar servidor de correo
```bash
export HOST=opendata.ugr.es
export SERVER=ugr.es
export USER=vagrant

sudo debconf-set-selections <<< "postfix postfix/mailname string $HOST"
sudo debconf-set-selections <<< "postfix postfix/main_mailer_type string 'Internet Site'"
sudo apt install -y postfix
```

Editar **/etc/postfix/main.cf**:
- *myhostname = CKAN* -> **myhostname = $HOST**

Editar **sudo nano /etc/postfix/virtual**:

Añadir **$USER@$HOST $USER**

```
sudo postmap /etc/postfix/virtual
sudo service postfix restart

echo -e '#!/bin/bash\ncd /usr/lib/ckan/default/src/ckan && paster --plugin=ckan post -c /etc/ckan/default/production.ini /api/action/send_email_notifications > /dev/null' | sudo tee /etc/cron.hourly/mail.sh

sudo chmod +x /etc/cron.hourly/mail.sh
```

Editar **/etc/ckan/default/production.ini**:

- *#ckan.activity_streams_email_notifications = true* -> **ckan.activity_streams_email_notifications = true**

- *ckan.site_title = CKAN* -> **ckan.site_title = $SITE**

- *#smtp.server = localhost* -> **smtp.server = $SMTP:$PORT_SMTP**

- *#smtp.starttls = False* -> **smtp.starttls = True**

- *#smtp.user = your_username@gmail.com* -> **smtp.user = $USER@$SERVER**

- *#smtp.password = your_password* -> **smtp.password = $PASSWORD**
va
- *#smtp.mail_from =* -> **smtp.mail_from = $USER@$SERVER**

```bash
sudo service apache2 reload
```

### Instalar worker para trabajos en segundo plano
sudo apt-get install supervisor

### Comenzando
http://docs.ckan.org/en/latest/maintaining/getting-started.html

Crear cuenta de administrador del sistema.

```bash
export USER=vagrant

cd /usr/lib/ckan/default/src/ckan
paster sysadmin add $USER -c /etc/ckan/default/production.ini
paster create-test-data -c /etc/ckan/default/production.ini
```

Configuración de autorización

```bash
sudo sed -i '/^ckan.auth.*/ s/= .*/= false/' /etc/ckan/default/production.ini
sudo sed -i '/^ckan.auth.roles*/ s/= .*/= admin/' /etc/ckan/default/production.ini
```

# PostgreSQL' full-text search parameters
ckan.datastore.default_fts_lang = spanish


## Front-End Settings
ckan.site_title = OpenDataUGR
ckan.site_logo = /base/images/ckan-logo.png
ckan.site_description = Portal para gestionar los datos abiertos de la UGR
ckan.favicon = /images/icons/ckan.ico
ckan.gravatar_default = identicon
ckan.preview.direct = png jpg gif
ckan.preview.loadable = html htm rdf+xml owl+xml xml n3 n-triples turtle plain atom csv tsv rss txt json pdf jpg png


## Internationalisation Settings
ckan.locale_default = es
ckan.locale_order = en pt_BR ja it cs_CZ ca es fr el sv sr sr@latin no sk fi ru de pl nl bg ko_KR hu sa sl lv
ckan.locales_offered =
ckan.locales_filtered_out = en_GB


## Feeds Settings
ckan.feeds.authority_name = Universidad de Granada
ckan.feeds.date =
ckan.feeds.author_name = Oficina de Software Libre
ckan.feeds.author_link =


## Email settings
email_to = opendata@ugr.es
error_email_from = opendata@ugr.es
smtp.server = smtp.ugr.es:587
smtp.starttls = True
smtp.user = opendata.ugr.es
#smtp.password = PASSWORD
smtp.mail_from = opendata@ugr.es
