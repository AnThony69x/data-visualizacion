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
        print(f"{Fore.GREEN}  13. 🔍 Buscar canciones{Style.RESET_ALL}")
        print(f"{Fore.GREEN}  14. 🎤 Comparar artistas{Style.RESET_ALL}")
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
            '13': self.search_songs_menu,
            '14': self.compare_artists_menu,
            '0': self.exit_app
        }
        
        action = actions.get(choice)
        
        if action:
            try:
                if choice not in ['0', '12']:
                    self.print_header()
                    logger.info(MESSAGES['generating'])
                
                action()
                
                if choice not in ['0', '11', '12', '13', '14']:
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
    
    def search_songs_menu(self):
        """Menú de búsqueda de canciones"""
        self.print_header()
        
        print(f"{Back.CYAN}{Fore.BLACK}{'  🔍 BÚSQUEDA DE CANCIONES  ':^70}{Style.RESET_ALL}\n")
        print(f"{Fore.YELLOW}Busca canciones por nombre (ej: love, happy, night){Style.RESET_ALL}\n")
        
        query = input(f"{Fore.GREEN}👉 Buscar canción: {Style.RESET_ALL}").strip()
        
        if not query:
            logger.warning("⚠️  Búsqueda vacía")
            input(f"\n{Fore.CYAN}📌 Presiona Enter para continuar...{Style.RESET_ALL}")
            return
        
        logger.info(f"Buscando '{query}'...")
        
        from src.utils.helpers import search_songs
        results = search_songs(self.data, query)
        
        if len(results) == 0:
            print(f"\n{Fore.RED}❌ No se encontraron resultados para '{query}'{Style.RESET_ALL}")
        else:
            print(f"\n{Fore.GREEN}✅ Se encontraron {len(results)} resultados:{Style.RESET_ALL}\n")
            print(f"{Fore.YELLOW}{'─'*70}{Style.RESET_ALL}")
            
            # Mostrar top 10 resultados
            for i, (_, row) in enumerate(results.head(10).iterrows(), 1):
                print(f"{Fore.CYAN}{i:2d}. {Fore.WHITE}{row['track_name'][:50]}")
                print(f"    {Fore.GREEN}🎤 Artista: {row['artist_name']}")
                print(f"    {Fore.MAGENTA}💿 Álbum: {row['album_name'][:40]}")
                
                # Popularidad con barra visual
                pop = int(row['track_popularity'])
                bar = '█' * (pop // 5)
                print(f"    {Fore.YELLOW}⭐ Popularidad: {pop:3d}/100 [{bar}]", end='')
                
                # Duración
                duration = row['track_duration_min']
                print(f" | {Fore.CYAN}⏱️  {duration:.2f} min", end='')
                
                # Explícito
                if row['explicit']:
                    print(f" | {Fore.RED}🔞 Explícito", end='')
                
                print()  # Nueva línea
                print(f"{Fore.YELLOW}{'─'*70}{Style.RESET_ALL}")
            
            if len(results) > 10:
                print(f"\n{Fore.YELLOW}💡 Mostrando 10 de {len(results)} resultados{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}   Refina tu búsqueda para resultados más específicos{Style.RESET_ALL}")
        
        input(f"\n{Fore.CYAN}📌 Presiona Enter para volver al menú...{Style.RESET_ALL}")
    
    def compare_artists_menu(self):
        """Menú de comparación de artistas"""
        self.print_header()
        
        print(f"{Back.MAGENTA}{Fore.WHITE}{'  🎤 COMPARADOR DE ARTISTAS  ':^70}{Style.RESET_ALL}\n")
        print(f"{Fore.YELLOW}Compara dos artistas en múltiples métricas{Style.RESET_ALL}\n")
        
        # Mostrar sugerencias de artistas populares
        top_artists = (self.data
                      .groupby('artist_name')['artist_popularity']
                      .first()
                      .nlargest(10)
                      .index.tolist())
        
        print(f"{Fore.CYAN}💡 Artistas disponibles (top 10):{Style.RESET_ALL}")
        for i, artist in enumerate(top_artists, 1):
            print(f"   {Fore.GREEN}{i:2d}. {artist}{Style.RESET_ALL}")
        print()
        print(f"{Fore.YELLOW}💡 Puedes escribir el número o el nombre completo del artista{Style.RESET_ALL}\n")
        
        # Solicitar artistas
        artist1_input = input(f"{Fore.GREEN}👉 Primer artista (número o nombre): {Style.RESET_ALL}").strip()
        artist2_input = input(f"{Fore.GREEN}👉 Segundo artista (número o nombre): {Style.RESET_ALL}").strip()
        
        if not artist1_input or not artist2_input:
            logger.warning("⚠️  Debes ingresar ambos artistas")
            input(f"\n{Fore.CYAN}📌 Presiona Enter para continuar...{Style.RESET_ALL}")
            return
        
        # Convertir números a nombres si es necesario
        try:
            num1 = int(artist1_input)
            if 1 <= num1 <= len(top_artists):
                artist1 = top_artists[num1 - 1]
            else:
                artist1 = artist1_input
        except ValueError:
            artist1 = artist1_input
        
        try:
            num2 = int(artist2_input)
            if 1 <= num2 <= len(top_artists):
                artist2 = top_artists[num2 - 1]
            else:
                artist2 = artist2_input
        except ValueError:
            artist2 = artist2_input
        
        logger.info(f"Comparando '{artist1}' vs '{artist2}'...")
        
        from src.utils.helpers import compare_artists
        comparison = compare_artists(self.data, artist1, artist2)
        
        if comparison is None:
            print(f"\n{Fore.RED}❌ Uno o ambos artistas no fueron encontrados{Style.RESET_ALL}")
            print(f"\n{Fore.YELLOW}💡 Verifica que escribiste correctamente los nombres{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}   (Mayúsculas y minúsculas no importan){Style.RESET_ALL}")
        else:
            self.clear_screen()
            print()
            print(f"{Fore.YELLOW}{'═'*70}{Style.RESET_ALL}")
            print(f"{Back.BLUE}{Fore.WHITE}{'  🎤 COMPARACIÓN DE ARTISTAS  ':^70}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}{'═'*70}{Style.RESET_ALL}")
            print()
            print(f"{Fore.GREEN}{'  ' + artist1:^35}{Style.RESET_ALL} {Fore.YELLOW}VS{Style.RESET_ALL} {Fore.MAGENTA}{artist2:^35}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}{'═'*70}{Style.RESET_ALL}")
            print()
            
            # Mostrar tabla formateada con colores
            for idx, row in comparison.iterrows():
                metric = row['Métrica']
                val1 = str(row[artist1])
                val2 = str(row[artist2])
                
                # Determinar ganador (si es numérico)
                try:
                    # Intentar comparar valores numéricos
                    num1 = float(val1.replace(',', '').replace('%', ''))
                    num2 = float(val2.replace(',', '').replace('%', ''))
                    
                    if num1 > num2:
                        color1 = Fore.GREEN
                        color2 = Fore.WHITE
                        winner = " 🏆"
                    elif num2 > num1:
                        color1 = Fore.WHITE
                        color2 = Fore.GREEN
                        winner = " 🏆"
                    else:
                        color1 = Fore.WHITE
                        color2 = Fore.WHITE
                        winner = ""
                except:
                    color1 = Fore.WHITE
                    color2 = Fore.WHITE
                    winner = ""
                
                print(f"{Fore.CYAN}{metric:35}{Style.RESET_ALL}", end='')
                print(f"{color1}{val1:>15}{Style.RESET_ALL}", end='')
                print(f"  {Fore.YELLOW}│{Style.RESET_ALL}  ", end='')
                print(f"{color2}{val2:<15}{winner}{Style.RESET_ALL}")
            
            print()
            print(f"{Fore.YELLOW}{'═'*70}{Style.RESET_ALL}")
            print()
            print(f"{Fore.GREEN}🏆 = Ganador en esa métrica{Style.RESET_ALL}")
            print()
        
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