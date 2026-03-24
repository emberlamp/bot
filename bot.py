#!/usr/bin/env python3
"""
Emberlamp Bot - Automation script for emberlamp organization
"""

import os
import json
import subprocess
from datetime import datetime

ORG = "emberlamp"
CONFIG_REPO = "emberlamp/config"
REPOS_JSON_URL = "https://raw.githubusercontent.com/emberlamp/config/main/repos.json"


class EmberlampBot:
    def __init__(self):
        self.token = os.environ.get("GH_TOKEN")
        if not self.token:
            print("⚠️  GH_TOKEN not set. Install gh CLI and run 'gh auth login'")

    def run(self, cmd):
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.stdout

    def get_repos_from_config(self):
        """Fetch repos list from config repo"""
        import urllib.request

        try:
            with urllib.request.urlopen(REPOS_JSON_URL) as response:
                data = json.loads(response.read())
                return data.get("repos", [])
        except Exception as e:
            print(f"Error fetching config: {e}")
            return []

    def get_github_repos(self):
        """Get all repos from GitHub"""
        output = self.run(f"gh api orgs/{ORG}/repos --jq '.[].name'")
        return output.strip().split("\n") if output else []

    def sync(self):
        """Sync repos from config to GitHub"""
        config_repos = self.get_repos_from_config()
        github_repos = self.get_github_repos()

        print(f"Config repos: {len(config_repos)}")
        print(f"GitHub repos: {len(github_repos)}")

        # Find missing repos
        missing = set(config_repos) - set(github_repos)
        if missing:
            print(f"⚠️  Repos in config but not on GitHub: {missing}")

        extra = set(github_repos) - set(config_repos)
        if extra:
            print(f"⚠️  Repos on GitHub but not in config: {extra}")

        print("✅ Sync complete!")

    def update_all(self, command):
        """Run a command in all repos"""
        repos = self.get_github_repos()
        for repo in repos:
            print(f"Running in {repo}...")
            self.run(f"gh repo clone {ORG}/{repo} /tmp/{repo} 2>/dev/null || true")
            if os.path.exists(f"/tmp/{repo}"):
                os.chdir(f"/tmp/{repo}")
                self.run(command)
                os.chdir("/")

    def list_repos(self):
        """List all repos"""
        repos = self.get_github_repos()
        for repo in repos:
            print(f"  - {repo}")


def main():
    import sys

    bot = EmberlampBot()

    if len(sys.argv) < 2:
        print("Usage: emberlamp-bot <command>")
        print("Commands: sync, list, update <command>")
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "sync":
        bot.sync()
    elif cmd == "list":
        bot.list_repos()
    elif cmd == "update":
        if len(sys.argv) < 3:
            print("Usage: emberlamp-bot update <command>")
            sys.exit(1)
        bot.update_all(sys.argv[2])
    else:
        print(f"Unknown command: {cmd}")


if __name__ == "__main__":
    main()
