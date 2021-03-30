#! /bin/bash
python3 -m pytest -s -v -m "sanity and regression" --html=./Reports/report.html /Users/nicolasulmete/pytest-tutorial/testCases/ --browser chrome
