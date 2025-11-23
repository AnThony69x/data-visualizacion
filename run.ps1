# ═══════════════════════════════════════════════════════════
# 🎵 SPOTIFY DATA VISUALIZER - LAUNCHER
# ═══════════════════════════════════════════════════════════

Write-Host ""
Write-Host "╔═══════════════════════════════════════════════════════════╗" -ForegroundColor Green
Write-Host "║     🎵 INICIANDO SPOTIFY DATA VISUALIZER                 ║" -ForegroundColor Green
Write-Host "╚═══════════════════════════════════════════════════════════╝" -ForegroundColor Green
Write-Host ""

# Verificar si existe el entorno virtual
if (-Not (Test-Path "venv\Scripts\Activate.ps1")) {
    Write-Host "❌ Error: No se encontró el entorno virtual" -ForegroundColor Red
    Write-Host "📌 Ejecuta primero: python -m venv venv" -ForegroundColor Yellow
    Write-Host ""
    Read-Host "Presiona Enter para salir"
    exit 1
}

Write-Host "⏳ Activando entorno virtual..." -ForegroundColor Cyan
Write-Host ""

# Activar entorno virtual
& .\venv\Scripts\Activate.ps1

Write-Host "✅ Entorno virtual activado" -ForegroundColor Green
Write-Host ""
Write-Host "🚀 Ejecutando programa..." -ForegroundColor Cyan
Write-Host ""
Write-Host "═══════════════════════════════════════════════════════════" -ForegroundColor Yellow
Write-Host ""

# Ejecutar main.py
python main.py

Write-Host ""
Write-Host "═══════════════════════════════════════════════════════════" -ForegroundColor Yellow
Write-Host ""
Write-Host "✅ Programa finalizado" -ForegroundColor Green
Write-Host ""

# Desactivar entorno virtual
deactivate

Read-Host "Presiona Enter para salir"