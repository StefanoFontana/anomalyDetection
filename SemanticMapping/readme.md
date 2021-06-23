# Semantic Mapping
Esempio di mapping semantico di alcuni dati secondo l'ontologia [SSN](https://www.w3.org/TR/vocab-ssn/).

## Dati di partenza
I dati di partenza sono raccolti in 2 file CSV diversi.
- *sensors.csv* contiene una lista di sensori, ognuno dei quali possiete un id univoco e una label di descrizione
- *observations.csv* contiene una lista di osservazioni (valori registrati) dei sensori. Ogni riga contiene l'id dell'osservazione, l'id del sensore che ha eseguito l'osservazione, un timestamp e il valore dell'osservazione.

## Creazione del file RML
Per creare il file RML è stato utilizzato il linguaggio [YARRRML](https://rml.io/yarrrml/) che permette di definire la struttura semantica dei dati in un formato facilmente leggibile.
Per eseguire la conversione da YARRRML a RML è stato utilizzato un editor online chiamato [Matey](https://rml.io/yarrrml/matey/).
- *yarrrml_schema.yaml* Schema di partenza che descrive la semantica dei dati.
- *mapping.rml.ttl* Risultato della conversione in file RML.

## Crezione triple
Per creare le triple RDF partendo dallo schema RML, è stata utilizzata ina libreria chiamata [rmlmapper](https://github.com/RMLio/rmlmapper-java) tramite un container Docker.
Il file *result.txt* contiene il risultato della conversione del file *mapping.rml.ttl*