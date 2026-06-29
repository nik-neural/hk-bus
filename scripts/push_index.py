#!/usr/bin/env python3
"""Push index.html to GitHub via Contents API."""
import base64
import json
import subprocess
import sys
import urllib.request

REPO = "nik-neural/hk-bus"
FILE_PATH = "index.html"
COMMIT_MSG = "ui: 重排頂部 — 天氣左、標題中、時間右"
LOCAL_FILE = "/Users/niksum/Documents/GitHub/hk-bus/index.html"


def get_token():
    proc = subprocess.run(
        ["git", "credential", "fill"],
        input=b"protocol=https\nhost=github.com\n",
        capture_output=True,
        cwd="/Users/niksum/Documents/GitHub/hk-bus",
    )
    for line in proc.stdout.decode().splitlines():
        if line.startswith("password="):
            return line.split("=", 1)[1]
    raise RuntimeError("Could not obtain GitHub token from git credential")


def api_request(url, token, data=None, method=None):
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "hk-bus-push-script",
    }
    body = None
    if data is not None:
        headers["Content-Type"] = "application/json"
        body = json.dumps(data).encode()
    req = urllib.request.Request(url, data=body, headers=headers, method=method or ("POST" if data else "GET"))
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode())


def main():
    with open(LOCAL_FILE, "rb") as f:
        content = f.read()
    if len(content) < 1000:
        print("ERROR: file too small, refusing to push placeholder", file=sys.stderr)
        sys.exit(1)

    token = get_token()
    sha_url = f"https://api.github.com/repos/{REPO}/contents/{FILE_PATH}?ref=main"
    meta = api_request(sha_url, token)
    sha = meta.get("sha")
    if not sha:
        print("ERROR: could not get current SHA:", meta, file=sys.stderr)
        sys.exit(1)

    payload = {
        "message": COMMIT_MSG,
        "content": base64.b64encode(content).encode(),
        "sha": sha,
        "branch": "main",
    }
    put_url = f"https://api.github.com/repos/{REPO}/contents/{FILE_PATH}"
    result = api_request(put_url, token, payload, method="PUT")
    commit_sha = result.get("commit", {}).get("sha")
    if not commit_sha:
        print("ERROR: push failed:", json.dumps(result, indent=2), file=sys.stderr)
        sys.exit(1)
    print(commit_sha)


if __name__ == "__main__":
    main()
