#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Wrapper to run daily_report_0429.py with UTF-8 encoding"""
import sys, os
sys.stdout.reconfigure(encoding='utf-8')
os.chdir(r"C:\root\.openclaw\workspaces\mercadolibre")
exec(open(r"C:\root\.openclaw\workspaces\mercadolibre\daily_report_0429.py", encoding="utf-8").read())