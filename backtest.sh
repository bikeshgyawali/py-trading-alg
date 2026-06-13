#!/bin/bash

cd "$(dirname "$0")"

if [ ! -d ".venv" ] && [ ! -d "venv" ]; then
    python3 -m venv .venv
    source .venv/bin/activate
else
    source .venv/bin/activate
fi

python main.py