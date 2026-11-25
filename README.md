# demo-app

Maza Flask lietotne DevOps praksei (Docker, Helm, GitHub Actions).

## Endpointi

- `/` — JSON ar ziņu, vidi (`APP_ENV`) un versiju (`APP_VERSION`)
- `/health` — `{"status": "ok"}`, izmanto Kubernetes probes

## Palaist lokāli

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
curl localhost:8080/health
```

## Testi

```bash
pytest
```
# test
