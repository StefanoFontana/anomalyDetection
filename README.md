# Anomaly Detection

L'obiettivo di questa repository è quello di analizzare il metodo FLAGS nei suoi vari aspetti e tentare di produrre un metodo simile ma personalizzato per il dominio applicativo analizzato.

## Data-Driven
In questa cartella sono presenti le analisi sui metodi di Anomaly Detection basati su Machine Learning.
Sono stati presi in esame 3 algoritmi di ML:
- [Matrix Profile](https://matrixprofile.docs.matrixprofile.org/index.html) (recuperato dal metodo FLAGS)
- K-Means
- [Random Cut Forest](https://klabum.github.io/rrcf/)

L'analisi dei vari metodi è stata eseguita utilizzando 2 dataset diversi:
- NYC Taxi: Numero di passeggeri che i taxi di New York hanno trasportato in un periodo di qualche mese. I valori sono stati registrati ogni 30 minuti.
- Machine Temperature System Failure: Valore di temperatura di una macchina durante alcuni giorni. I valori sono stati registrati ogni 5 minuti.

Questi dataset sono stati recuperati da una repository GitHub chiamata [Numenta Anomaly Benchmark](https://github.com/numenta/NAB) che fornisce una libreria per eseguire un benchmark sugli algoritmi di Anomaly Detection.
Dei dataset si era a conoscenza dei timestamp in cui si verificavano le anomalie.