Ein simpler FastAPI Microservice, der den RTSP Stream von TP-Link Tapo Kameras abgreift

### Virtuelle Umgebung erstellen:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
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
