@echo off

echo Installing Python 3.13...
winget install Python.Python.3.13

echo Creating virtual environment... 
py -3.13 -m venv .vir

echo Activating virtual environment...
call .vir\Scripts\activate

echo environment setup complete. You can now install your project dependencies using pip.
