@echo off
chcp 65001 >nul 2>&1
cd /d "C:\root\.openclaw\workspaces\mercadolibre"
set PYTHONIOENCODING=utf-8
python daily_report_0429.py 2>&1