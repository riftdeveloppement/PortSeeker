@echo off
echo Installing required Python packages...

REM Check if Python is installed
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed. Please install Python first.
    pause
    exit /b
)

REM Install PyQt5
pip install PyQt5
IF %ERRORLEVEL% NEQ 0 (
    echo Failed to install PyQt5. Check your Python and pip installation.
    pause
    exit /b
)

REM Install additional dependencies (if any)
pip install ipaddress
IF %ERRORLEVEL% NEQ 0 (
    echo Failed to install additional dependencies.
    pause
    exit /b
)

echo All necessary packages have been installed.
pause
