#!/bin/bash

# Borramos todos los datos existentes
isql 1111 dba $VIRTUOSO_PASSWD exec="RDF_GLOBAL_RESET ();"

# Cargamos ontología
isql 1111 dba $VIRTUOSO_PASSWD exec="SPARQL LOAD <cabas.ugr.es/ontology/ugr#>;"

# Cargamos los datos
isql 1111 dba $VIRTUOSO_PASSWD exec="ld_dir ('/usr/local/share/virtuoso/vad/bulk_loading', '*.rdf', 'http://cabas.ugr.es/resources/');"
isql 1111 dba $VIRTUOSO_PASSWD exec="rdf_loader_run();"
