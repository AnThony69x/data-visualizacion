"""
🎵 SISTEMA DE VISUALIZACIÓN DE DATOS DE SPOTIFY
===============================================
Programa principal con menú interactivo mejorado

Autores: Anthony (@AnThony69xd), Emilio (@EmilioSle)
Fecha: 2025-11-23
Universidad: ULEAM - Visualización de Datos
"""

import sys
import os
from pathlib import Path
from colorama import Fore, Back, Style, init

# Importar módulos del proyecto
from src.config.settings import MESSAGES, CLEAN_DATA_FILE
from src.data.loader import DataLoader
from src.data.cleaner import DataCleaner
from src.utils.logger import Logger

# Importar funciones de visualización
from src.visualizations import (
    personalization_advanced,
    heatmap,
    histograms,
    boxplots,
    kde_plots,
    pareto_chart,
    radar_chart,
    waterfall_chart,
    swarm_plot,
    sankey_diagram
)

# Inicializar colorama
init(autoreset=True)

logger = Logger()

class SpotifyVisualizerApp:
    """Aplicación principal de visualización de datos"""
    
    def __init__(self):
        self.data_loader = DataLoader()
        self.data = None
        self.running = True
    
    def clear_screen(self):
        """Limpia la pantalla de la consola"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_header(self):
        """Imprime el encabezado principal con diseño mejorado"""
        self.clear_screen()
        
        # Banner ASCII
        print(f"{Fore.GREEN}")
        print("""
    ███████╗██████╗  ██████╗ ████████╗██╗███████╗██╗   ██╗
    ██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝██║██╔════╝╚██╗ ██╔╝
    ███████╗██████╔╝██║   ██║   ██║   ██║█████╗   ╚████╔╝ 
    ╚════██║██╔═══╝ ██║   ██║   ██║   ██║██╔══╝    ╚██╔╝  
    ███████║██║     ╚██████╔╝   ██║   ██║██║        ██║   
    ╚══════╝╚═╝      ╚═════╝    ╚═╝   ╚═╝╚═╝        ╚═╝   
    """)
        print(f"{Style.RESET_ALL}")
        print(f"{Back.GREEN}{Fore.BLACK}{'═'*70}{Style.RESET_ALL}")
        print(f"{Back.GREEN}{Fore.BLACK}{'  📊 DATA VISUALIZER - ANÁLISIS AVANZADO  ':^70}{Style.RESET_ALL}")
        print(f"{Back.GREEN}{Fore.BLACK}{'═'*70}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'  Universidad ULEAM - 2025  ':^70}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}{'  Anthony (@AnThony69x) & Emilio (@EmilioSle)  ':^70}{Style.RESET_ALL}")
        print(f"{Back.GREEN}{Fore.BLACK}{'═'*70}{Style.RESET_ALL}\n")
    
    def initialize(self):
        """Inicializa la aplicación y carga datos"""
        self.print_header()
        
        try:
            # Verificar si existen datos limpios
            if CLEAN_DATA_FILE.exists():
                logger.info("Cargando datos procesados...")
                self.data = self.data_loader.load_clean_data()
            else:
                logger.warning("Datos limpios no encontrados. Procesando datos crudos...")
                raw_data = self.data_loader.load_raw_data()
                
                logger.info("Limpiando datos...")
                cleaner = DataCleaner(raw_data)
                self.data = cleaner.clean()
                cleaner.save()
            
            # Mostrar resumen de datos
            summary = self.data_loader.get_data_summary()
            self._show_summary(summary)
            
            input(f"\n{Fore.CYAN}📌 Presiona Enter para continuar al menú principal...{Style.RESET_ALL}")
            
        except Exception as e:
            logger.error(f"Error al inicializar: {e}")
            logger.error("Verifica que el archivo 'spotify_data.csv' esté en 'data/raw/'")
            sys.exit(1)
    
    def _show_summary(self, summary):
        """Muestra resumen de datos cargados con diseño mejorado"""
        logger.success("✅ Sistema inicializado correctamente\n")
        
        print(f"{Fore.YELLOW}{'─'*70}{Style.RESET_ALL}")
        print(f"{Back.BLUE}{Fore.WHITE}{'  📊 RESUMEN DE DATOS CARGADOS  ':^70}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}{'─'*70}{Style.RESET_ALL}")
        
        print(f"{Fore.GREEN}  🎵 Total de canciones:      {Fore.WHITE}{summary['total_tracks']:,}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}  🎤 Artistas únicos:         {Fore.WHITE}{summary['unique_artists']:,}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}  💿 Álbumes únicos:          {Fore.WHITE}{summary['unique_albums']:,}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}  🔞 Canciones explícitas:    {Fore.WHITE}{summary['explicit_count']:,}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}  ⭐ Popularidad promedio:    {Fore.WHITE}{summary['avg_popularity']:.1f}{Style.RESET_ALL}")
        
        if summary['date_range'][0]:
            print(f"{Fore.GREEN}  📅 Rango de años:           {Fore.WHITE}{int(summary['date_range'][0])} - {int(summary['date_range'][1])}{Style.RESET_ALL}")
        
        print(f"{Fore.YELLOW}{'─'*70}{Style.RESET_ALL}")
    
    def show_menu(self):
        """Muestra el menú principal con diseño mejorado"""
        self.print_header()
        
        print(f"{Back.CYAN}{Fore.BLACK}{'  🎨 MENÚ DE VISUALIZACIONES  ':^70}{Style.RESET_ALL}\n")
        
        # GRÁFICOS BÁSICOS
        print(f"{Back.BLUE}{Fore.WHITE}  📊 GRÁFICOS BÁSICOS  {Style.RESET_ALL}")
        print(f"{Fore.CYAN}  1️⃣  {Fore.WHITE}Personalización Avanzada {Fore.YELLOW}(Barras con estilo){Style.RESET_ALL}")
        print(f"{Fore.CYAN}  2️⃣  {Fore.WHITE}Mapa de Calor {Fore.YELLOW}(Correlaciones){Style.RESET_ALL}")
        
        # DISTRIBUCIONES
        print(f"\n{Back.MAGENTA}{Fore.WHITE}  📈 DISTRIBUCIONES  {Style.RESET_ALL}")
        print(f"{Fore.CYAN}  3️⃣  {Fore.WHITE}Histogramas y Densidad{Style.RESET_ALL}")
        print(f"{Fore.CYAN}  4️⃣  {Fore.WHITE}Diagramas de Caja y Bigotes {Fore.YELLOW}(Boxplots){Style.RESET_ALL}")
        print(f"{Fore.CYAN}  5️⃣  {Fore.WHITE}Gráficos de Densidad KDE{Style.RESET_ALL}")
        
        # GRÁFICOS AVANZADOS
        print(f"\n{Back.RED}{Fore.WHITE}  🎯 GRÁFICOS AVANZADOS  {Style.RESET_ALL}")
        print(f"{Fore.CYAN}  6️⃣  {Fore.WHITE}Gráfico de Pareto {Fore.YELLOW}(Principio 80/20){Style.RESET_ALL}")
        print(f"{Fore.CYAN}  7️⃣  {Fore.WHITE}Gráfico de Radar {Fore.YELLOW}(Comparación multidimensional){Style.RESET_ALL}")
        print(f"{Fore.CYAN}  8️⃣  {Fore.WHITE}Gráfico de Cascada {Fore.YELLOW}(Waterfall){Style.RESET_ALL}")
        print(f"{Fore.CYAN}  9️⃣  {Fore.WHITE}Gráfico de Enjambre {Fore.YELLOW}(Swarmplot){Style.RESET_ALL}")
        
        # GRÁFICOS DE FLUJO
        print(f"\n{Back.CYAN}{Fore.BLACK}  🌊 GRÁFICOS DE FLUJO  {Style.RESET_ALL}")
        print(f"{Fore.CYAN}  🔟 {Fore.WHITE}Diagrama de Sankey {Fore.YELLOW}(Flujo de datos - HTML Interactivo){Style.RESET_ALL}")
        
        # OPCIONES ESPECIALES
        print(f"\n{Back.YELLOW}{Fore.BLACK}  ✨ OPCIONES ESPECIALES  {Style.RESET_ALL}")
        print(f"{Fore.GREEN}  11. 🎨 Generar TODOS los gráficos{Style.RESET_ALL}")
        print(f"{Fore.GREEN}  12. 📊 Ver resumen de datos{Style.RESET_ALL}")
        print(f"{Fore.RED}   0. 🚪 Salir del sistema{Style.RESET_ALL}")
        
        print(f"\n{Fore.YELLOW}{'═'*70}{Style.RESET_ALL}")
    
    def handle_choice(self, choice):
        """Maneja la selección del usuario"""
        
        # Mapeo de opciones a funciones
        actions = {
            '1': lambda: personalization_advanced(self.data),
            '2': lambda: heatmap(self.data),
            '3': lambda: histograms(self.data),
            '4': lambda: boxplots(self.data),
            '5': lambda: kde_plots(self.data),
            '6': lambda: pareto_chart(self.data),
            '7': lambda: radar_chart(self.data),
            '8': lambda: waterfall_chart(self.data),
            '9': lambda: swarm_plot(self.data),
            '10': lambda: sankey_diagram(self.data),
            '11': self.generate_all,
            '12': self._show_data_summary,
            '0': self.exit_app
        }
        
        action = actions.get(choice)
        
        if action:
            try:
                if choice not in ['0', '12']:
                    self.print_header()
                    logger.info(MESSAGES['generating'])
                
                action()
                
                if choice not in ['0', '11', '12']:
                    logger.success(MESSAGES['success'])
                    input(f"\n{Fore.CYAN}📌 Presiona Enter para volver al menú...{Style.RESET_ALL}")
                    
            except Exception as e:
                logger.error(f"{MESSAGES['error']}: {e}")
                import traceback
                print(f"\n{Fore.RED}{'='*70}")
                print(f"{'DETALLES DEL ERROR':^70}")
                print(f"{'='*70}{Style.RESET_ALL}")
                traceback.print_exc()
                print(f"{Fore.RED}{'='*70}{Style.RESET_ALL}")
                input(f"\n{Fore.CYAN}📌 Presiona Enter para continuar...{Style.RESET_ALL}")
        else:
            logger.warning(f"{Fore.YELLOW}⚠️  Opción inválida. Por favor, intenta de nuevo.{Style.RESET_ALL}")
            input(f"\n{Fore.CYAN}📌 Presiona Enter para continuar...{Style.RESET_ALL}")
    
    def generate_all(self):
        """Genera todos los gráficos con diseño mejorado"""
        self.print_header()
        
        print(f"{Back.GREEN}{Fore.BLACK}{'  🎨 GENERANDO TODAS LAS VISUALIZACIONES  ':^70}{Style.RESET_ALL}\n")
        
        all_functions = [
            ("1. Personalización Avanzada", lambda: personalization_advanced(self.data)),
            ("2. Mapa de Calor", lambda: heatmap(self.data)),
            ("3. Histogramas", lambda: histograms(self.data)),
            ("4. Boxplots", lambda: boxplots(self.data)),
            ("5. KDE Densidad", lambda: kde_plots(self.data)),
            ("6. Pareto", lambda: pareto_chart(self.data)),
            ("7. Radar", lambda: radar_chart(self.data)),
            ("8. Cascada", lambda: waterfall_chart(self.data)),
            ("9. Enjambre", lambda: swarm_plot(self.data)),
            ("10. Sankey", lambda: sankey_diagram(self.data)),
        ]
        
        total = len(all_functions)
        exitosos = 0
        fallidos = 0
        
        for i, (name, func) in enumerate(all_functions, 1):
            try:
                # Barra de progreso visual
                progress = int((i / total) * 50)
                bar = f"{Fore.GREEN}{'█' * progress}{Fore.WHITE}{'░' * (50 - progress)}{Style.RESET_ALL}"
                print(f"\r{Fore.CYAN}[{i}/{total}] {bar} {name}...{Style.RESET_ALL}", end='')
                
                func()
                exitosos += 1
                print(f" {Fore.GREEN}✅{Style.RESET_ALL}")
            except Exception as e:
                logger.error(f"Error en {name}: {e}")
                fallidos += 1
                print(f" {Fore.RED}❌{Style.RESET_ALL}")
        
        print(f"\n\n{Fore.YELLOW}{'='*70}{Style.RESET_ALL}")
        print(f"{Back.BLUE}{Fore.WHITE}{'  📊 RESUMEN DE GENERACIÓN  ':^70}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}{'='*70}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}  ✅ Exitosos: {Fore.WHITE}{exitosos}/{total}{Style.RESET_ALL}")
        print(f"{Fore.RED}  ❌ Fallidos:  {Fore.WHITE}{fallidos}/{total}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}{'='*70}{Style.RESET_ALL}")
        
        if exitosos == total:
            print(f"\n{Fore.GREEN}🎉 ¡Todos los gráficos generados exitosamente!{Style.RESET_ALL}")
        else:
            print(f"\n{Fore.YELLOW}⚠️  Se generaron {exitosos} de {total} gráficos{Style.RESET_ALL}")
        
        print(f"\n{Fore.CYAN}📁 Los gráficos están guardados en:{Style.RESET_ALL}")
        print(f"{Fore.WHITE}   • PNG:  {Fore.GREEN}output/images/{Style.RESET_ALL}")
        print(f"{Fore.WHITE}   • HTML: {Fore.GREEN}output/interactive/{Style.RESET_ALL}")
        
        input(f"\n{Fore.CYAN}📌 Presiona Enter para volver al menú...{Style.RESET_ALL}")
    
    def _show_data_summary(self):
        """Muestra resumen detallado de datos"""
        self.print_header()
        
        summary = self.data_loader.get_data_summary()
        self._show_summary(summary)
        
        # Información adicional
        print(f"\n{Back.MAGENTA}{Fore.WHITE}  📈 ESTADÍSTICAS ADICIONALES  {Style.RESET_ALL}")
        print(f"{Fore.CYAN}  • Duración promedio: {Fore.WHITE}{self.data['track_duration_min'].mean():.2f} min{Style.RESET_ALL}")
        print(f"{Fore.CYAN}  • Duración máxima:   {Fore.WHITE}{self.data['track_duration_min'].max():.2f} min{Style.RESET_ALL}")
        print(f"{Fore.CYAN}  • Duración mínima:   {Fore.WHITE}{self.data['track_duration_min'].min():.2f} min{Style.RESET_ALL}")
        print(f"{Fore.CYAN}  • Seguidores promedio: {Fore.WHITE}{self.data['artist_followers'].mean():,.0f}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}  • Seguidores máximos:  {Fore.WHITE}{self.data['artist_followers'].max():,.0f}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}  • Tracks por álbum:    {Fore.WHITE}{self.data['album_total_tracks'].mean():.1f}{Style.RESET_ALL}")
        
        # Top 5 artistas
        print(f"\n{Back.YELLOW}{Fore.BLACK}  🏆 TOP 5 ARTISTAS MÁS POPULARES  {Style.RESET_ALL}")
        top_5 = (self.data
                .groupby('artist_name')['artist_popularity']
                .max()
                .nlargest(5)
                .reset_index())
        
        for i, (_, row) in enumerate(top_5.iterrows(), 1):
            medal = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else "🏅"
            print(f"{Fore.YELLOW}  {medal} {i}. {Fore.WHITE}{row['artist_name']}: {Fore.GREEN}{row['artist_popularity']:.0f}{Style.RESET_ALL}")
        
        print(f"\n{Fore.YELLOW}{'─'*70}{Style.RESET_ALL}")
        input(f"\n{Fore.CYAN}📌 Presiona Enter para volver al menú...{Style.RESET_ALL}")
    
    def exit_app(self):
        """Sale de la aplicación con diseño mejorado"""
        self.print_header()
        
        print(f"{Back.RED}{Fore.WHITE}{'  👋 CERRANDO SISTEMA  ':^70}{Style.RESET_ALL}\n")
        print(f"{Fore.CYAN}Gracias por usar el Sistema de Visualización de Datos de Spotify{Style.RESET_ALL}")
        print(f"\n{Fore.YELLOW}👥 Desarrollado por:{Style.RESET_ALL}")
        print(f"{Fore.GREEN}   • Anthony (@AnThony69x){Style.RESET_ALL}")
        print(f"{Fore.GREEN}   • Emilio (@EmilioSle){Style.RESET_ALL}")
        print(f"\n{Fore.CYAN}🎓 Universidad: ULEAM - Visualización de Datos{Style.RESET_ALL}")
        print(f"{Fore.CYAN}📅 Fecha: 2025-11-23{Style.RESET_ALL}\n")
        print(f"{Fore.YELLOW}{'═'*70}{Style.RESET_ALL}\n")
        
        self.running = False
    
    def run(self):
        """Ejecuta el loop principal de la aplicación"""
        self.initialize()
        
        while self.running:
            self.show_menu()
            choice = input(f"\n{Fore.GREEN}👉 Selecciona una opción: {Style.RESET_ALL}").strip()
            self.handle_choice(choice)


def main():
    """Función principal"""
    try:
        app = SpotifyVisualizerApp()
        app.run()
    except KeyboardInterrupt:
        print(f"\n\n{Fore.RED}⚠️  Programa interrumpido por el usuario{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}👋 ¡Hasta luego!{Style.RESET_ALL}\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Fore.RED}❌ Error fatal: {e}{Style.RESET_ALL}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()