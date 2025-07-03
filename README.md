# Banking FQA Chatbot with RASA

A RASA-powered chatbot for answering banking FAQs, deployable via CLI for development and Docker for QA/Production. Includes a web chat widget for website integration.

## Features

- RASA NLU & Core for intent classification and dialogue
- Custom actions for extensibility
- CLI support for local development/testing
- Docker Compose configs for QA and Production environments
- Simple web chat widget for website embedding

## Development (CLI)

1. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

2. Train RASA model:
   ```bash
   rasa train
   ```

3. Run RASA server (in one terminal):
   ```bash
   rasa run --enable-api --cors "*"
   ```

4. Run custom actions server (in another terminal):
   ```bash
   rasa run actions
   ```

5. Test in CLI:
   ```bash
   rasa shell
   ```

## QA/Production (Docker)

### QA

```bash
docker-compose -f docker-compose.qa.yml up --build
```

### Production

```bash
docker-compose -f docker-compose.prod.yml up --build
```

## Web Chat Widget

Open `webchat/index.html` and point `socketUrl` to your deployed RASA URL.

---

For more customization and production hardening, refer to [RASA docs](https://rasa.com/docs/).
