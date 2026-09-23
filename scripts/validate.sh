#!/usr/bin/env bash
set -euo pipefail

repo_root=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
cd "$repo_root"

python3 tests/validate_repository.py

for script in .devcontainer/post-create.sh .devcontainer/post-start.sh scripts/lab scripts/validate.sh modules/SDN_Lab_5/node/entrypoint.sh; do
  bash -n "$script"
done
