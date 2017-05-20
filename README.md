# Datos abiertos en la universidad

Proyecto sobre un portal de datos abiertos de máxima categoría.

## Instalación CKAN (versión 2.6, Ubuntu 14.04 64 bits)

- Generar clave SSH:

```bash
ssh-keygen -t rsa -b 4096 -C EMAIL
```

- Copiar clave SSH a nuestro servidor:

```bash
ssh-copy-id -i ~/.ssh/id_rsa.pub USUARIO@HOST
```

- Establecer variables de entorno para los datos confidenciales:

```bash
export CKAN_PASSWD="PASSWD_CKAN"
export DATASTORE_PASSWD="PASSWD_DATASTORE"
export SYSADMIN_PASSWD="PASSWD_SYSADMIN"
```

- [_**OPCIONAL**_] En el caso de usar una máquina _Vagrant_, cambiar la configuración del archivo **Vagrantfile**.

- Cambiar la dirección IP de nuestro servidor en el archivo **hosts**.

- Desplegar la configuración con _Ansible_:

```bash
ansible-playbook --inventory-file=./hosts -become ckan.yml
```

## En qué consiste un portal de datos abiertos de máxima categoría

En un portal de datos abiertos como podemos suponer lo principal es que se publiquen datos bajo una licencia libre de forma que cualquiera pueda trabajar con ellos; pero además, en función de la facilidad que nos presenten los formatos en los que están publicados dichos datos y la información semántica que los acompañe, podemos distinguir entre portales con una distinta valoración según una escalada definida como las 5 estrellas del Open Linked Data según Tim Berners-Lee, inventor de la World Wide Web.

- <img  src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Star_full.svg/2000px-Star_full.svg.png" height="15">
Los datos está publicados bajo un licencia libre, independientemente de que el formato sea poco práctico para la reutilización de los datos (como puede ser un documento escaneado o un archivo PDF).

- <img  src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Star_full.svg/2000px-Star_full.svg.png" height="15">
<img  src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Star_full.svg/2000px-Star_full.svg.png" height="15">
Los datos está publicados de una forma estructurada (como puede ser una hoja de cálculo en formato propietario de Microsoft Excel).

- <img  src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Star_full.svg/2000px-Star_full.svg.png" height="15">
<img  src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Star_full.svg/2000px-Star_full.svg.png" height="15">
<img  src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Star_full.svg/2000px-Star_full.svg.png" height="15">
Los datos están publicados están publicados en archivos con un formato abierto (como puede ser un archivo CSV).

- <img  src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Star_full.svg/2000px-Star_full.svg.png" height="15">
<img  src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Star_full.svg/2000px-Star_full.svg.png" height="15">
<img  src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Star_full.svg/2000px-Star_full.svg.png" height="15">
<img  src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Star_full.svg/2000px-Star_full.svg.png" height="15">
Los datos publicados son accesibles mediante una URI que permita describir las propiedades de dichos datos mediante el uso de un estándar RDF.

- <img  src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Star_full.svg/2000px-Star_full.svg.png" height="15">
<img  src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Star_full.svg/2000px-Star_full.svg.png" height="15">
<img  src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Star_full.svg/2000px-Star_full.svg.png" height="15">
<img  src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Star_full.svg/2000px-Star_full.svg.png" height="15">
<img  src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Star_full.svg/2000px-Star_full.svg.png" height="15">
Los datos publicados son enlazados con otros datos mediante consultas semánticas de forma que puedan proveer un contexto, pero sobretodo lo más importante, que la información sea lo más reusable posible e interpretable por máquinas.

## Vamos a crear un *Linked Data site*

Como hemos dicho, el objetivo es tener un portal de datos abiertos en el que además de tener nuestros datos libremente accesibles de forma estructurada y en formatos abiertos, queremos que los datos sea interpretables por máquinas para que se facilite su reutilización.

Con este fin en mente, una de las primeras cosas que tenemos que hacer es precisamente hacer que nuestros datos sean entendibles por máquinas, por lo que el primer paso será convertir todos nuestros datos estructurados con formato CSV a un modelo de datos RDF en forma de expresiones sujeto-predicado-objeto, lo que usualmente recibe un nombre de "triple". Por otro lado, también deberemos definir un vocabulario y una ontología que facilite la intepretación por parte de las máquinas del significado de los datos enlazados.
