@echo off
setlocal
cd /d "%~dp0"
where py >nul 2>&1
if errorlevel 1 (
    python selfassessment.py %*
) else (
    py -3 selfassessment.py %*
)
set "rc=%errorlevel%"
if not "%rc%"=="0" pause
exit /b %rc%
