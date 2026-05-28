# Database reset and migrations

From the repository root:

```bash
docker compose down -v --remove-orphans
docker compose up -d --build
docker compose exec api uv run alembic upgrade head
docker compose exec db psql -U app -d app -c "\\dt public.*"
```

The `users` table (and `alembic_version`) should appear in `public`.
