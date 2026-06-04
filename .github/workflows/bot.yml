name: Daily Bot

on:
  workflow_dispatch:

jobs:
  run:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v5

      - uses: actions/setup-python@v6
        with:
          python-version: '3.12'

      - name: Install packages
        run: pip install tweepy

      - name: Run Bot
        run: python bot.py
