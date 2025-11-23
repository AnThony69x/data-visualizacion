"""
Módulo de visualizaciones de Spotify
Contiene todos los gráficos del sistema

Autores: Anthony (@AnThony69x), Emilio (@EmilioSle)
Universidad: ULEAM - Visualización de Datos
"""

import importlib

# Importar usando importlib para módulos que empiezan con números
mod_01 = importlib.import_module('.01_personalizacion_avanzada', package='src.visualizations')
mod_02 = importlib.import_module('.02_mapa_calor', package='src.visualizations')
mod_03 = importlib.import_module('.03_histogramas', package='src.visualizations')
mod_04 = importlib.import_module('.04_boxplots', package='src.visualizations')
mod_05 = importlib.import_module('.05_kde_densidad', package='src.visualizations')
mod_06 = importlib.import_module('.06_pareto', package='src.visualizations')
mod_07 = importlib.import_module('.07_radar', package='src.visualizations')
mod_08 = importlib.import_module('.08_cascada', package='src.visualizations')
mod_09 = importlib.import_module('.09_enjambre', package='src.visualizations')
mod_10 = importlib.import_module('.10_sankey', package='src.visualizations')

# Exponer las funciones
personalization_advanced = mod_01.personalization_advanced
heatmap = mod_02.heatmap
histograms = mod_03.histograms
boxplots = mod_04.boxplots
kde_plots = mod_05.kde_plots
pareto_chart = mod_06.pareto_chart
radar_chart = mod_07.radar_chart
waterfall_chart = mod_08.waterfall_chart
swarm_plot = mod_09.swarm_plot
sankey_diagram = mod_10.sankey_diagram

__all__ = [
    'personalization_advanced',
    'heatmap',
    'histograms',
    'boxplots',
    'kde_plots',
    'pareto_chart',
    'radar_chart',
    'waterfall_chart',
    'swarm_plot',
    'sankey_diagram'
]
