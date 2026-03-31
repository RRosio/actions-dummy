#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.8"
# dependencies = [
#     "httpx",
# ]
# ///
"""
GitHub Issues Triage Scraper - UV Script
Fetches untriaged issues from Jupyter repositories and generates markdown meeting notes.

Usage: uv run gen_triage_issues.py

Based on: https://github.com/danyeaw/jupyter-triage-tool (triage.py)
Original author: Dan Yeaw
See original repository for license terms.
"""

import httpx
import argparse
import asyncio
from typing import Dict, List

class GitHubTriageScraper:
    def __init__(self):
        self.headers = {
            'Accept': 'application/vnd.github.v3+json',
            'User-Agent': 'Jupyter-Triage-Scraper/1.0'
        }
        
        # Repository configurations
        self.repositories = {
            'JupyterLab': 'jupyterlab/jupyterlab',
            'Notebook': 'jupyter/notebook', 
            'JupyterLab-Desktop': 'jupyterlab/jupyterlab-desktop',
            'NBClassic': 'jupyter/nbclassic'
        }

    async def get_issues_for_repo(self, client: httpx.AsyncClient, repo_full_name: str) -> List[Dict]:
        """Get issues with 'status:Needs Triage' label for a repository."""
        url = f"https://api.github.com/repos/{repo_full_name}/issues"
        
        params = {
            'state': 'open',
            'labels': 'status:Needs Triage',
            'sort': 'created',
            'direction': 'asc',
            'per_page': 100
        }
        
        all_issues = []
        page = 1
        
        while True:
            params['page'] = page
            
            try:
                response = await client.get(url, params=params)
                response.raise_for_status()
                
                issues = response.json()
                
                if not issues:
                    break
                
                # Filter out pull requests
                issues = [issue for issue in issues if 'pull_request' not in issue]
                
                for issue in issues:
                    all_issues.append({
                        'number': issue['number'],
                        'title': issue['title'],
                        'url': issue['html_url'],
                        'created_at': issue['created_at']
                    })
                
                if len(issues) < params['per_page']:
                    break
                
                page += 1
                
            except Exception as e:
                print(f"Error fetching issues for {repo_full_name}: {e}")
                break
        
        return sorted(all_issues, key=lambda x: x['number'])

    async def get_all_issues(self, verbose: bool = False) -> Dict[str, List[Dict]]:
        """Get issues from all repositories asynchronously."""
        async with httpx.AsyncClient(headers=self.headers, timeout=30.0) as client:
            tasks = []
            
            for repo_name, repo_full_name in self.repositories.items():
                if verbose:
                    print(f"Fetching issues for {repo_name} ({repo_full_name})...")
                task = self.get_issues_for_repo(client, repo_full_name)
                tasks.append((repo_name, task))
            
            results = {}
            for repo_name, task in tasks:
                issues = await task
                results[repo_name] = issues
                if verbose:
                    print(f"Found {len(issues)} issues in {repo_name}")
        
        return results

    def generate_meeting_template(self, issues_data: Dict[str, List[Dict]]) -> str:
        """Generate meeting template only."""
        lines = []
        
        for repo_name, issues in issues_data.items():
            issue_count = len(issues)
            
            if issue_count == 0:
                lines.append(f"Before the meeting, 0 issues in {repo_name} needed triage. After the meeting, none remain.")
            else:
                lines.append(f"Before the meeting, {issue_count} issues in {repo_name} needed triage. After the meeting, [UPDATE] remain.")
                
                for issue in issues:
                    lines.append(f"* {issue['url']} ()")
            
            # Add newline between repository sections
            lines.append("")
        
        return "\n".join(lines).rstrip()  # Remove trailing newline

async def main():
    """Main function."""
    parser = argparse.ArgumentParser(description="A script that generates list of triage issues for markdown notes.")
    parser.add_argument('--verbose', action='store_true', help="Verbose text output.")
    args = parser.parse_args()

    scraper = GitHubTriageScraper()

    if args.verbose:
        print("Fetching issues from all repositories...")

    issues_data = await scraper.get_all_issues(args.verbose)

    # Generate meeting template
    meeting_template = scraper.generate_meeting_template(issues_data)
    print(meeting_template)
    print()

    # Summary
    if args.verbose:
        total = sum(len(issues) for issues in issues_data.values())
        print(f"Total: {total} issues")
        for repo_name, issues in issues_data.items():
            print(f"  {repo_name}: {len(issues)}")

if __name__ == "__main__":
    asyncio.run(main())
