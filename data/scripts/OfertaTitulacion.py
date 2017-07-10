#!/usr/bin/python3

import csv
import os
import errno

titulaciones = ["Doctorado", "Grado", "Master"]
files = [("1314", "2013/2014"), ("1415", "2014/2015"), ("1516", "2015/2016")]

for tipo in titulaciones:

    for x in files:
        id = 0

        with open("../csv/OfertaTitulacion" + tipo + x[0] + ".csv", "r") as ifile:
          reader = csv.reader(ifile)
          data = list(reader)

        if not os.path.exists("../semantic/resources/OfertaTitulacion/" + tipo + "/"):
            try:
                os.makedirs("../semantic/resources/OfertaTitulacion/" + tipo + "/")
            except OSError as exc:
                if exc.errno != errno.EEXIST:
                    raise

        ofile = open("../semantic/resources/OfertaTitulacion/" + tipo + "/OfertaTitulacion" + tipo + x[0] + ".rdf", "w")
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

        with open("../semantic/resources/OfertaTitulacion/" + tipo + "/OfertaTitulacion" + tipo + x[0] + ".rdf", "a") as ofile:
                for lines in data:
                    if id > 0:
                        ofile.write("<rdf:Description rdf:about=\"OfertaTitulacionDoctorado" + tipo + "/" + x[0] + "#" + str(id) + "\">\n" +
                        "\t<rdf:type rdf:resource=\"#OfertaTitulacion" + tipo + "\" />\n" +
                        "\t<ugr:ramaConocimiento>" + lines[0] + "</ugr:ramaConocimiento>\n" +
                        "\t<ugr:titulacion>" + lines[1] + "</ugr:titulacion>\n" +
                        "\t<ugr:campus>" + lines[2] + "</ugr:campus>\n" +
                        "\t<ugr:centro>" + lines[3] + "</ugr:centro>\n" +
                        "\t<ugr:curso>" + x[1] + "</ugr:curso>\n" +
                        "</rdf:Description>\n\n")
                    id += 1

        ofile = open("../semantic/resources/OfertaTitulacion/" + tipo + "/OfertaTitulacion" + tipo + x[0] + ".rdf", "a")
        ofile.write("</rdf:RDF>")
        ofile.close()
