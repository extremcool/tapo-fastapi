Ein simpler FastAPI Microservice, der den RTSP Stream von TP-Link Tapo Kameras abgreift

Die FastAPI wird durch einen Bearer Token geschützt, deshalb bitte nur in isolierten Netzwerken oder hinter einem SSL/TLS-verschlüsselten Reverse Proxy betreiben.

### Projekt klonen
```bash
git clone https://github.com/extremcool/tapo-fastapi.git
```

### Virtuelle Umgebung erstellen:
```bash
python -m venv venv
source venv/bin/activate
```

### Abhängigkeiten installieren
```bash
pip install -r requirements.txt
```
### Konfiguration

Es wird ein Tapo Kamerakonto benötigt: https://www.tapo.com/de/faq/76/

Beispiel .env mit folgendem Befehl erstelen

```bash
cp .env.example .env
```

### Starten

```bash
python service.py
```
Alle weiteren Informationen zur Nutzung sind in der FastAPI Oberfläche sichtbar

http://API_HOST:API_PORT/docs
