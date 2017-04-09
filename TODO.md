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
