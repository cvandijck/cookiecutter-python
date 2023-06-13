@ECHO off
ECHO.
ECHO Create environment
CALL conda create --name {{cookiecutter.package_name}}_env python=3.8 -y
ECHO.
IF %ERRORLEVEL% NEQ 0 EXIT /b %ERRORLEVEL%

ECHO Activate environment
CALL conda activate {{cookiecutter.package_name}}_env
ECHO.
IF %ERRORLEVEL% NEQ 0 EXIT /b %ERRORLEVEL%

PAUSE