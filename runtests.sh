#! /bin/bash
pytest -s -v -m "sanity and regression" --html=./Reports/report.html testCases/ --browser chrome

