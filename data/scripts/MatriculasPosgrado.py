#!/usr/bin/python3

import csv
import os
import errno

files = [("1011", "2010/2011"), ("1112", "2011/2012"), ("1213", "2012/2013"), ("1314", "2013/2014"), ("1415", "2014/2015"), ("1516", "2015/2016")]

for x in files:
    id = 0

    with open("../csv/MatriculasPosgrado" + x[0] + ".csv", "r") as ifile:
      reader = csv.reader(ifile)
      data = list(reader)

    if not os.path.exists("../semantic/resources/Matriculas/Posgrado/"):
        try:
            os.makedirs("../semantic/resources/Matriculas/Posgrado/")
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise

    ofile = open("../semantic/resources/Matriculas/Posgrado/MatriculasPosgrado" + x[0] + ".rdf", "w")
    ofile.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n\n" +
        "<!DOCTYPE rdf:RDF [\n" +
        "\t<!ENTITY rdf \"http://www.w3.org/1999/02/22-rdf-syntax-ns#\" >\n" +
        "\t<!ENTITY rdfs \"http://www.w3.org/2000/01/rdf-schema#\" >\n" +
        "\t<!ENTITY xsd \"http://www.w3.org/2001/XMLSchema#\" >\n" +
        "\t<!ENTITY owl \"http://www.w3.org/2002/07/owl#\" >\n" +
        "\t<!ENTITY ugr \"http://cabas.ugr.es/ontology/ugr#\" >\n" +
        "]>\n\n" +
        "<rdf:RDF\n" +
        "\txmlns=\"http://cabas.ugr.es/resources/\"\n" +
        "\txmlns:rdf=\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\"\n" +
        "\txmlns:rdfs=\"http://www.w3.org/2000/01/rdf-schema#\"\n" +
        "\txmlns:xsd=\"http://www.w3.org/2001/XMLSchema#\"\n" +
        "\txmlns:owl=\"http://www.w3.org/2002/07/owl#\"\n" +
        "\txmlns:ugr=\"http://cabas.ugr.es/ontology/ugr#\">\n\n")
    ofile.close()

    with open("../semantic/resources/Matriculas/Posgrado/MatriculasPosgrado" + x[0] + ".rdf", "a") as ofile:
            for lines in data:
                if id > 0:
                    ofile.write("<rdf:Description rdf:about=\"" + x[0] + "#" + str(id) + "\">\n" +
                        "\t<rdf:type rdf:resource=\"#MatriculasPosgrado\" />\n" +
                        "\t<ugr:titulacion>" + lines[0] + "</ugr:titulacion>\n" +
                        "\t<ugr:hombres rdf:datatype=\"&xsd;nonNegativeInteger\">" + lines[1] + "</ugr:hombres>\n" +
                        "\t<ugr:mujeres rdf:datatype=\"&xsd;nonNegativeInteger\">" + lines[2] + "</ugr:mujeres>\n" +
                        "\t<ugr:curso>" + x[1] + "</ugr:curso>\n" +
                        "</rdf:Description>\n\n")
                id += 1

    ofile = open("../semantic/resources/Matriculas/Posgrado/MatriculasPosgrado" + x[0] + ".rdf", "a")
    ofile.write("</rdf:RDF>")
    ofile.close()
