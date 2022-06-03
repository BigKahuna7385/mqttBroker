# mqttBroker
Hallo Arne,
Dies ist unser mqttBroker Projekt. Es enthält primär einen mqttBroker und einen mqtt Test Klienten. Folgende MQTT Funktionalitäten werden unterstützt:
- SUBSCRIBE
- PUBLISH
- UNSUBSCRIBE <br>

Dies stellt einen reduzierten Funktionsumfang des gesamten MQTT-Protokolls dar, da die restlichen Keywords den Projektumfang gesprengt hätten.
Wir haben das Protokoll mithilfe TCP-Sockets umgesetzt. Der Broker läuft dabei im ASYNC Modus und lässt die Sockets vom Betriebssystem über FileDescriptor verwalten.
Der Client läuft wiederum im blockierenden Modus um Threading in Python zu vermeiden, da Interpreterlock usw.
Starten kann man unseren Broker mit:
```
python RunBroker.py
```
und den Client Test kann man starten mit:
```
python RunClient.py
```
Der Broker hört auf beide gängigen MQTT-Ports: 1883, 8883 auf Verbindungen. Die Clients subscriben jeweils auf den gleichen Topic / Channel,
nutzen dabei aber unterschiedliche Broker Ports um beide Varianten zu prüfen. Anschließend setzt Client A ein publish mit "Dies ist ein Test" ab und Client B
wartet auf dessen Empfang. Danach Antwortet Client B mit einem Publish "Dies ist eine Test Antwort" und Client A wartet auf diese Nachricht. Haben beide Cleints
die entsprechenden Nachrichten gesendet und die Antworten empfangen, werden beide Client Sockets geschlossen und der Broker entfernt aus der bekannten
Userliste.

Wir haben Unit Tests geschrieben im tests Ordner, die können über eine gängige IDE (getestet in Pycharm) ausgeführt werden. Der gesamte Code ist
mit den neuen Python 3 TypeHints versehen um dir das Lesen und die Bewertung zu vereinfachen. Zum Entwickeln wurde Python 3.9 / 3.10 verwendetet.
Es werden **keine** externen Bibliotheken benötigt, alles was verwendet wird sollte Teil deiner standard Installation und teil der Python standard Bibliothek sein.
