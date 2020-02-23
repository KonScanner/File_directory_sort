@echo off
rem Check each file in the folder placed
for %%a in (".\*") do (
rem Check if file has an extension (excluding script)
if "%%~xa" NEQ "" if "%%~dpxa" NEQ "%~dpx0" (
rem Check if extension folder exists, if not it creates one
if not exist "%%~xa" mkdir "%%~xa"
rem Moves file in the directory
move "%%a" "%%~dpa%%~xa\"
))