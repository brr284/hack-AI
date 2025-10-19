@echo off
if "%1"=="open" (
    python "%~dp0hackai_app.py"
) else (
    echo Kullanim: hackai open
)
