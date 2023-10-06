@echo off
REM This script was derived from PythonQwt project
REM ======================================================
REM Run coverage tests
REM ======================================================
REM Licensed under the terms of the MIT License
REM Copyright (c) 2020 Pierre Raybaut
REM (see PythonQwt LICENSE file for more details)
REM ======================================================
setlocal
call %~dp0utils GetScriptPath SCRIPTPATH
call %FUNC% GetModName MODNAME
call %FUNC% SetPythonPath
call %FUNC% UsePython

set COVERAGE_PROCESS_START=%SCRIPTPATH%\..\.coveragerc
pytest -v --cov --cov-report=html --unattended %MODNAME%
start .\htmlcov\index.html
call %FUNC% EndOfScript
