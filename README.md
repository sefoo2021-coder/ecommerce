# Ecommerce Updates Aggregator

Python 3.11 application that collects e-commerce and marketing updates, verifies them using an LLM, and publishes to WordPress.

## Installation

```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux
pip install -r requirements.txt
```

## Configuration

Copy `.env.example` to `.env` and fill values:

```
OPENAI_API_KEY=...
WORDPRESS_BASE_URL=https://YOUR-SITE.com
WORDPRESS_USERNAME=YOUR_USER
WORDPRESS_APP_PASSWORD=YOUR_APP_PASSWORD
TIMEZONE=Africa/Cairo
MAX_ITEMS_PER_RUN=200
DRY_RUN=true
```

## Database

```bash
python app/db/migrate.py
```

## Run Once

```bash
python manage.py run-once --limit 100
```

## Dashboard

```bash
streamlit run app/ui/dashboard.py
```

## Scheduler

```bash
python scheduler.py
```

## Config Files

- `app/config/feeds.yaml`
- `app/config/people.yaml`
- `app/config/topics.yaml`

## Tests

```bash
pytest
```

