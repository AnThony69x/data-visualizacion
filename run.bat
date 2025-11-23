@echo off
echo ╔═══════════════════════════════════════════════════════════╗
echo ║     🎵 INICIANDO SPOTIFY DATA VISUALIZER                 ║
echo ╚═══════════════════════════════════════════════════════════╝
echo.
echo ⏳ Activando entorno virtual...
echo.

REM Verificar si existe el entorno virtual
if not exist "venv\Scripts\activate.bat" (
    echo ❌ Error: No se encontró el entorno virtual
    echo 📌 Ejecuta primero: python -m venv venv
    pause
    exit /b 1
)

REM Activar entorno virtual y ejecutar main.py
call venv\Scripts\activate.bat

echo ✅ Entorno virtual activado
echo.
echo 🚀 Ejecutando programa...
echo.
echo ═══════════════════════════════════════════════════════════
echo.

python main.py

echo.
echo ═══════════════════════════════════════════════════════════
echo.
echo ✅ Programa finalizado
echo.
pause