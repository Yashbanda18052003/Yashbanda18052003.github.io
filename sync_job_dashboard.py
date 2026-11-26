import os
import subprocess
import json
import pandas as pd
from datetime import datetime

base_dir = os.path.dirname(os.path.abspath(__file__))
excel_path = r"C:\Users\YASH\Downloads\Yash_Daily_15_Job_Applications.xlsx"

print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Starting EOD Job Hunting Dashboard Sync...")

if not os.path.exists(excel_path):
    print(f"Excel file not found at {excel_path}")
    exit(1)

# Run build script
script_path = r"C:\Users\YASH\.gemini\antigravity\scratch\build_tracker_html.py"
res = subprocess.run(["python", script_path], capture_output=True, text=True)
print(res.stdout)
if res.stderr:
    print("Build Warnings/Errors:", res.stderr)

# Git commit and push
os.chdir(base_dir)
subprocess.run(["git", "add", "."], check=True)
commit_msg = f"EOD Sync: Job Hunting Dashboard updated ({datetime.now().strftime('%d-%b-%Y %I:%M %p')})"
res_commit = subprocess.run(["git", "commit", "-m", commit_msg], capture_output=True, text=True)
print(res_commit.stdout)

print("Pushing to GitHub Pages...")
res_push = subprocess.run(["git", "push", "origin", "main"], capture_output=True, text=True)
print(res_push.stdout)
if res_push.stderr:
    print(res_push.stderr)

print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] LIVE SYNC COMPLETE! Dashboard is live on GitHub Pages.")
