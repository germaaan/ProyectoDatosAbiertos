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
