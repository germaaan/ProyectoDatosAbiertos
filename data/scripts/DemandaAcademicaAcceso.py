#!/usr/bin/python3

'''
  Copyright (C) 2017 Germán Martínez Maldonado

  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program. If not, see <http://www.gnu.org/licenses/>.
'''

import csv

files = ["DemandaAcademicaAcceso1213", "DemandaAcademicaAcceso1314", "DemandaAcademicaAcceso1415"]

for file in files:
    id = 0

    with open('../origin/' + file + '.csv', 'r') as ifile:
      reader = csv.reader(ifile)
      data = list(reader)

    ofile = open('../converted/rdf/' + file + '.rdf', 'w')
    ofile.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n\n"+
    "<!DOCTYPE rdf:RDF [\n"+
    "\t<!ENTITY rdf \"http://www.w3.org/1999/02/22-rdf-syntax-ns#\" >\n"+
    "\t<!ENTITY rdfs \"http://www.w3.org/2000/01/rdf-schema#\" >\n"+
    "\t<!ENTITY xsd \"http://www.w3.org/2001/XMLSchema#\" >\n"+
    "\t<!ENTITY owl \"http://www.w3.org/2002/07/owl#\" >\n"+
    "\t<!ENTITY ugr \"http://cabas.ugr.es/ontology/ugr#\" >\n"+
    "]>\n\n"+
    "<rdf:RDF\n"+
    "\txmlns=\"http://cabas.ugr.es/resources/\"\n"+
    "\txmlns:rdf=\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\"\n"+
    "\txmlns:rdfs=\"http://www.w3.org/2000/01/rdf-schema#\"\n"+
    "\txmlns:xsd=\"http://www.w3.org/2001/XMLSchema#\"\n"+
    "\txmlns:owl=\"http://www.w3.org/2002/07/owl#\"\n"+
    "\txmlns:ugr=\"http://cabas.ugr.es/ontology/ugr#\">\n\n")
    ofile.close()

    with open('../converted/rdf/' + file + '.rdf', 'a') as ofile:
            for lines in data:
                if id > 0:
                    ofile.write("<rdf:Description rdf:about=\"" + file + "#"+str(id)+"\">\n"+
                    "\t<rdf:type rdf:resource=\"#DemandaAcademicaAcceso\" />\n"+
                    "\t<ugr:tipoProcedimiento>"+lines[0]+"</ugr:tipoProcedimiento>\n"+
                    "\t<ugr:estado>"+lines[1]+"</ugr:estado>\n"+
                    "\t<ugr:hombres rdf:datatype=\"&xsd;nonNegativeInteger\">"+lines[2]+"</ugr:hombres>\n"+
                    "\t<ugr:mujeres rdf:datatype=\"&xsd;nonNegativeInteger\">"+lines[3]+"</ugr:mujeres>\n"+
                    "\t<ugr:curso>2012/2013</ugr:curso>\n"+
                    "</rdf:Description>\n\n")
                id += 1

    ofile = open('../converted/rdf/' + file + '.rdf', 'a')
    ofile.write("</rdf:RDF>")
    ofile.close()
