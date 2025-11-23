"""
📝 SISTEMA DE LOGGING CON COLORES
=================================
Logger personalizado con timestamps y colores para mejor legibilidad
"""
from datetime import datetime
from colorama import Fore, Style, init

# Inicializar colorama para Windows
init(autoreset=True)

class Logger:
    """Sistema de logging con colores y timestamps"""
    
    @staticmethod
    def _timestamp():
        """Retorna timestamp actual formateado"""
        return datetime.now().strftime("%H:%M:%S")
    
    def info(self, message):
        """Log de información (azul)"""
        print(f"{Fore.CYAN}ℹ️  [{self._timestamp()}] {message}{Style.RESET_ALL}")
    
    def success(self, message):
        """Log de éxito (verde)"""
        print(f"{Fore.GREEN}✅ [{self._timestamp()}] {message}{Style.RESET_ALL}")
    
    def warning(self, message):
        """Log de advertencia (amarillo)"""
        print(f"{Fore.YELLOW}⚠️  [{self._timestamp()}] {message}{Style.RESET_ALL}")
    
    def error(self, message):
        """Log de error (rojo)"""
        print(f"{Fore.RED}❌ [{self._timestamp()}] {message}{Style.RESET_ALL}")
    
    def header(self, message):
        """Log de encabezado (magenta)"""
        print(f"\n{Fore.MAGENTA}{'='*60}")
        print(f"{message}")
        print(f"{'='*60}{Style.RESET_ALL}\n")