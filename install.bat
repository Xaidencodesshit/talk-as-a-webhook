@echo off
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python first.
    exit /b
)

echo Installing requests library...
pip install requests

pip show requests >nul 2>&1
if %errorlevel% equ 0 (
    echo Requests library has been successfully installed.
) else (
    echo Failed to install Requests library.
)

pause
