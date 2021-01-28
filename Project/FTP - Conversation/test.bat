echo off
title Testing FTP Script
cls
:1
py FTP.py
timeout 3 >nul
GOTO 1