print("HOLA MUNDO")

from rdflib import Graph()

g = Graph()

PATH_TO_DATA = "92771.ttl"

g.parse(PATH_TO_DATA)

for i in g.objects(): print(i)

