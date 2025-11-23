@echo off
title Spotify Data Visualizer - Setup & Run
color 0A

echo ╔═══════════════════════════════════════════════════════════╗
echo ║     🎵 SPOTIFY DATA VISUALIZER - SETUP                   ║
echo ╚═══════════════════════════════════════════════════════════╝
echo.

REM Verificar si Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Error: Python no está instalado
    echo 📌 Descarga Python desde: https://www.python.org/
    pause
    exit /b 1
)

echo ✅ Python detectado
echo.

REM Verificar si existe el entorno virtual
if not exist "venv\" (
    echo 📦 Creando entorno virtual...
    python -m venv venv
    echo ✅ Entorno virtual creado
) else (
    echo ✅ Entorno virtual ya existe
)
echo.

REM Activar entorno virtual
echo ⏳ Activando entorno virtual...
call venv\Scripts\activate.bat
echo ✅ Entorno activado
echo.

REM Verificar si están instaladas las dependencias
pip show pandas >nul 2>&1
if errorlevel 1 (
    echo 📦 Instalando dependencias...
    echo    Esto puede tomar unos minutos...
    echo.
    pip install -r requirements.txt
    echo.
    echo ✅ Dependencias instaladas
) else (
    echo ✅ Dependencias ya instaladas
)
echo.

REM Verificar estructura de carpetas
if not exist "data\raw\" mkdir "data\raw"
if not exist "data\processed\" mkdir "data\processed"
if not exist "output\images\" mkdir "output\images"
if not exist "output\interactive\" mkdir "output\interactive"

echo ✅ Estructura de carpetas verificada
echo.

REM Verificar archivo CSV
if not exist "data\raw\spotify_data.csv" (
    echo ⚠️  ADVERTENCIA: No se encontró spotify_data.csv
    echo    Coloca tu archivo CSV en: data\raw\spotify_data.csv
    echo.
    set /p continue="¿Continuar de todas formas? (S/N): "
    if /i not "%continue%"=="S" exit /b 0
)

echo.
echo ═══════════════════════════════════════════════════════════
echo.
echo 🚀 EJECUTANDO PROGRAMA...
echo.
echo ═══════════════════════════════════════════════════════════
echo.

REM Ejecutar programa
python main.py

echo.
echo ═══════════════════════════════════════════════════════════
echo.
echo ✅ Programa finalizado
echo.
pause