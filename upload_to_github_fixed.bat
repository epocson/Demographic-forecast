@echo off
echo Population Forecasting - GitHub Upload Tool (Improved Version)
echo =========================================
echo.

echo This script will upload your project to https://github.com/epocson/Demographic-forecast.git
echo.

REM Check if Git identity is configured
git config --get user.name > nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Git user identity not configured.
    echo Please run set_git_identity.bat first.
    echo.
    pause
    exit /b 1
)

echo Using Git identity: 
FOR /F "tokens=*" %%G IN ('git config --get user.name') DO echo Name:  %%G
FOR /F "tokens=*" %%G IN ('git config --get user.email') DO echo Email: %%G
echo.

echo Initializing local Git repository...
git init
echo.

echo Adding all files to Git...
git add .
echo.

echo Committing changes...
git commit -m "Initial commit: Population forecasting project"
echo.

echo Setting up remote repository...
git remote remove origin 2>nul
git remote add origin https://github.com/epocson/Demographic-forecast.git
echo.

echo NOTE: When prompted for password, use your Personal Access Token instead.
echo If you don't have a token, create one at: https://github.com/settings/tokens
echo.

echo Creating and checking out master branch...
git checkout -b master 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo Branch already exists, switching to master...
    git checkout master
)
echo.

echo Pushing to GitHub using master branch...
git push -u origin master
echo.

echo Done! Your project should now be on GitHub.
echo Visit: https://github.com/epocson/Demographic-forecast
echo =========================================
pause 