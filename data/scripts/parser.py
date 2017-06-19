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

id = 0

with open('matriculas_grado_1516.csv', 'r') as ifile:
  reader = csv.reader(ifile)
  data = list(reader)

ofile = open('matriculas_grado_1516.rdf', 'w')
ofile.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"+
"<rdf:RDF\n"+
"\txmlns:rdf=\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\"\n"+
"\txmlns:rdfs=\"http://www.w3.org/2000/01/rdf-schema#\"\n"+
"\txmlns:xsd=\"http://www.w3.org/2001/XMLSchema#\"\n"+
"\txmlns:owl=\"http://www.w3.org/2002/07/owl#\"\n"+
"\txmlns:vivo=\"http://vivoweb.org/ontology/core#\"\n"+
"\txmlns:ugr=\"http://cabas.ugr.es/ontology/ugr#\">\n\n")
ofile.close()

with open('matriculas_grado_1516.rdf', 'a') as ofile:
        for lines in data:
            if id > 0:
                ofile.write("<rdf:Description rdf:about=\"http://cabas.ugr.es/resources/MatriculasGrado1516#"+str(id)+"\">\n"+
                "\t<rdfs:label>"+lines[1]+"</rdfs:label>\n"+
                "\t<ugr:RamaConocimiento>"+lines[0]+"</ugr:RamaConocimiento>\n"+
                "\t<ugr:Titulación>"+lines[1]+"</ugr:Titulación>\n"+
                "\t<ugr:hombres>"+lines[2]+"</ugr:hombres>\n"+
                "\t<ugr:mujeres>"+lines[3]+"</ugr:mujeres>\n"+
                "\t<vivo:AcademicTerm>2015/2016</vivo:AcademicTerm>\n"+
                "</rdf:Description>\n\n")
            id += 1

ofile = open('matriculas_grado_1516.rdf', 'a')
ofile.write("</rdf:RDF>")
ofile.close()
