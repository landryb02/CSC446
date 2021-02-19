echo off
title Testing FTP Script
cls
:1
py FTP1.py
timeout 1 >nul
GOTO 1