#!/usr/bin/env python3
"""Publish the ATP 2015 sample to the Hugging Face Hub as a dataset.

This is Ben's account step. Run it after logging in:

    pip install "huggingface_hub>=0.24"
    huggingface-cli login          # paste a WRITE token from
                                   # https://huggingface.co/settings/tokens
    python upload_to_hf.py

It creates (if needed) the dataset repo and uploads every file in this folder
(the README dataset card, LICENSE, and the data/ CSV + Parquet).

Override the target with env vars, e.g.:
    HF_REPO_ID=livetennisapi/atp-2015-results python upload_to_hf.py
"""
import os
import sys

from huggingface_hub import HfApi

REPO_ID = os.environ.get("HF_REPO_ID", "livetennisapi/atp-2015-results")
HERE = os.path.dirname(os.path.abspath(__file__))

# Only upload the dataset artifacts, not the build tooling / venv.
ALLOW = ["README.md", "LICENSE", "data/*"]
IGNORE = [
    ".venv/*", "*.pyc", "__pycache__/*", "upload_to_hf.py",
    "build_parquet.py", "extract.sql", ".git/*",
]


def main() -> int:
    api = HfApi()
    try:
        who = api.whoami()
    except Exception as exc:  # noqa: BLE001
        print("Not logged in. Run `huggingface-cli login` first.", file=sys.stderr)
        print(f"({exc})", file=sys.stderr)
        return 1

    print(f"Logged in as: {who.get('name')}")
    print(f"Target dataset repo: {REPO_ID}")

    api.create_repo(repo_id=REPO_ID, repo_type="dataset", exist_ok=True)
    print("Repo ready. Uploading folder...")

    commit = api.upload_folder(
        repo_id=REPO_ID,
        repo_type="dataset",
        folder_path=HERE,
        allow_patterns=ALLOW,
        ignore_patterns=IGNORE,
        commit_message="Add ATP 2015 tour-level singles results (CC-BY-4.0 sample)",
    )
    print("Done.")
    print(f"Commit: {getattr(commit, 'commit_url', commit)}")
    print(f"View:   https://huggingface.co/datasets/{REPO_ID}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
