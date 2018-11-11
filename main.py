import rdflib.graph as g
from rake_nltk import Rake
from textblob import TextBlob

graph = g.Graph()
graph.parse('./92771.ttl', format='ttl')
#print(graph.serialize(format='pretty-xml'))
wantsTalk = True;

qres = graph.query(
    """SELECT ?person
WHERE
{  
  ?person dbo:ReligiousBuilding :nave .
}""")
 
# for row in qres:
#     print(row[0])      
help = input("How can I help you?\n")
type(help)
r = Rake() # Uses stopwords for english from NLTK, and all punctuation characters.
r.extract_keywords_from_text(help)
print(r.get_ranked_phrases()) # To get keyword phrases ranked highest to lowest.

while wantsTalk:
    help = input("Do you have anymore questions?\n")
    
    type(help)
    testimonial = TextBlob(help)
    if testimonial.sentiment.polarity < 0:
        wantsTalk = False
        print("Alright have a nice day!") # To get keyword phrases ranked highest to lowest.

    r = Rake() # Uses stopwords for english from NLTK, and all punctuation characters.
    r.extract_keywords_from_text(help)
    #print(r.get_ranked_phrases()) # To get keyword phrases ranked highest to lowest.

