@echo off
echo Population Forecasting - GitHub Upload Tool
echo =========================================
echo.

echo This script will help you upload your project to GitHub.
echo Make sure you have:
echo 1. Installed Git
echo 2. Created a GitHub account
echo 3. Created a new repository on GitHub
echo.
set /p repo_url=Please enter your GitHub repository URL: 

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
git remote add origin %repo_url%
echo.

echo Pushing to GitHub...
git push -u origin master
echo.

echo If you see any errors about 'main' vs 'master', try this command:
echo git push -u origin main
echo.

echo Done! Your project should now be on GitHub.
echo =========================================
pause 