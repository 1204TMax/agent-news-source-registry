# agent-news-source-registry

Agent-first registry for news/intelligence sources.

## What this is
- Structured, machine-readable source registry for AI agents
- Designed for filtering, ranking, verification, and monitoring workflows
- Current seed set: **158** sources

## Layout
- `data/sources.jsonl` canonical dataset (one source per line)
- `schemas/source.schema.json` strict schema
- `tags/taxonomy.yaml` tag definitions
- `prompts/source-selection.md` source selection guide for agents
- `policies/source-trust-policy.md` trust and conflict-resolution policy
- `scripts/validate.py` schema + quality checks
- `scripts/build.py` regenerate exports
- `exports/` human-readable views

## Quickstart
```bash
python3 scripts/validate.py
python3 scripts/build.py
```

## Agent usage
1. Load `data/sources.jsonl`
2. Filter by `coverage_topics`, `type`, `task_tags`
3. Rank with `reliability_score` + `signal_to_noise`
4. For contested claims, require cross-source confirmation across different `type`
