#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r ./match_voice/requirements.txt

# Convert static asset files
python ./match_voice/manage.py collectstatic --no-input

# Apply any outstanding database migrations
python ./match_voice/manage.py migrate