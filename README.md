# Emberlamp Auto Bot

Automation bot for managing emberlamp organization repositories.

## Overview

This bot provides automated tasks for the emberlamp organization through GitHub Actions workflows that run automatically or on-demand.

## Features

### GitHub Actions Workflows

#### 1. Auto-Bot Workflow (.github/workflows/auto-bot.yml)

Automatically runs based on:

- **Schedule**: Daily at midnight (`0 0 * * *`)
- **Repository Dispatch**: When config repo is updated
- **Manual Trigger**: Workflow dispatch with action selection

#### Actions Available

| Action | Description |
|--------|-------------|
| `sync` | Compare config vs GitHub repos |
| `update` | Update all repos automatically |
| `backup` | Create backup of all repos |
| `report` | Generate daily report |

## Usage

### Automatic (Scheduled)

The workflow runs automatically every day at midnight.

### Manual Trigger

1. Go to https://github.com/emberlamp/bot/actions
2. Click "Run workflow"
3. Select action: sync, update, backup, or report

### Trigger from Config Changes

Update `repos.json` in config repo → triggers auto-update!

## Workflows

### Daily Sync
- Runs at midnight every day
- Compares config repos vs actual GitHub repos
- Reports any discrepancies

### Update All Repos
- Clones all repos
- Makes specified changes
- Commits and pushes to all repos

### Backup
- Creates mirror clones of all repos
- Archives as .tar.gz
- Uploads as artifact

### Report
- Generates daily statistics
- Lists public vs private repos
- Maintains history

## Setup

No additional setup needed! The workflows use GitHub's built-in token.

## How It Works

```
Config Repo (repos.json)
       ↓
  Repository Dispatch
       ↓
  Auto-Bot Workflow
       ↓
  Updates All Repos
       ↓
  Commits & Pushes
```

## Repositories Managed

See [emberlamp/config/repos.json](https://github.com/emberlamp/config/blob/main/repos.json)

Total: 12 repositories