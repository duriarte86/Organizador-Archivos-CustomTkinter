@echo off

echo ===========================================
echo   ORGANIZADOR DE ARCHIVOS v2.1
echo   Generando ejecutable...
echo ===========================================
echo.

:: Eliminar carpeta build si existe
if exist build (
    echo Eliminando carpeta build...
    rmdir /s /q build
)

:: Eliminar carpeta dist si existe
if exist dist (
    echo Eliminando carpeta dist...
    rmdir /s /q dist
)

echo.
echo Compilando con PyInstaller...
echo.

pyinstaller main.spec

echo.
echo ===========================================
echo Compilacion finalizada.
echo ===========================================
echo.

:: Abrir carpeta dist
if exist "dist\Organizador de Archivos" (
    explorer "dist\Organizador de Archivos"
)

pause