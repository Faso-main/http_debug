# HTTP Data JSON Parser

A simple Python script that:
- Reads JSON data from `src/httpdata.json` (CP1251 encoded)
- Fixes decimal separators (replaces commas with dots)
- Attempts to parse the JSON and display the first item

Handles:
- Keyboard interrupts
- JSON decode errors with context display

Usage: `python script.py`