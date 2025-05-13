@echo off
echo Setting up Git user identity
echo ===========================
echo.

set /p user_name=Enter your name (e.g., John Doe): 
set /p user_email=Enter your email address (e.g., your.email@example.com): 

echo.
echo Setting Git global user name and email...
git config --global user.name "%user_name%"
git config --global user.email "%user_email%"

echo.
echo Git identity configured:
git config --global user.name
git config --global user.email

echo.
echo Now you can run the upload script again.
echo.
pause 