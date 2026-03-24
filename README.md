# Emberlamp Bot

Automation bot for managing emberlamp organization repositories.

## Overview

This bot provides automated tasks for the emberlamp organization:
- Sync repository configuration from `repos.json`
- Execute commands across all repos
- Monitor and report repository status

## Components

### GitHub Actions Workflow
Located in `.github/workflows/sync.yml`
- Manual trigger via workflow_dispatch
- Syncs repos from config repo
- Compares config vs actual GitHub repos

### Python Bot Script
`bot.py` - Standalone automation script

## Usage

### Python Script
```bash
python bot.py sync      # Sync and compare repos
python bot.py list      # List all repos
python bot.py update "command"  # Run command in all repos
```

### GitHub Actions
1. Go to https://github.com/emberlamp/bot/actions
2. Click "Run workflow"
3. Select action: sync, list, or update-all

## Setup

1. Create a Personal Access Token with `repo` scope
2. Add as GitHub secret `GH_TOKEN`
3. Or use `gh auth login` for CLI access

## Environment Variables

- `GH_TOKEN` - GitHub Personal Access Token

## Example Workflow

```yaml
name: Daily Sync
on:
  schedule:
    - cron: '0 0 * * *'  # Daily at midnight
  workflow_dispatch:

jobs:
  sync:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run sync
        run: python bot.py sync
```