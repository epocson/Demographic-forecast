@echo off
echo Population Forecasting - GitHub Upload Tool
echo =========================================
echo.

echo This script will upload your project to https://github.com/epocson/Demographic-forecast.git
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
git remote add origin https://github.com/epocson/Demographic-forecast.git
echo.

echo Pushing to GitHub...
git push -u origin main
echo.

echo If you see any errors about 'main' vs 'master', try this command:
echo git push -u origin master
echo.

echo Done! Your project should now be on GitHub.
echo Visit: https://github.com/epocson/Demographic-forecast
echo =========================================
pause 