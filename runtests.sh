#! /bin/bash
python3 -m pytest -s -v -m "sanity and regression" --html=./Reports/report.html testCases/ --browser chrome
