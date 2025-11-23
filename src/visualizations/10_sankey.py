"""
🌊 GRÁFICO 10: DIAGRAMA DE SANKEY (FLUJO)
=========================================

📋 DESCRIPCIÓN:
Diagrama de flujo interactivo que muestra el movimiento de datos entre categorías.
Visualiza transiciones y relaciones entre diferentes estados.

🎯 OBJETIVO:
Visualizar flujos y transiciones complejas:
- Mostrar cómo los datos fluyen entre categorías
- Identificar rutas principales
- Visualizar proporciones de cada flujo
- Análisis de procesos y transiciones

📊 DATOS QUE VISUALIZA:
Flujo de 3 niveles:
1. Tipo de Álbum (album, single, compilation)
2. Contenido (Explícito / No Explícito)
3. Popularidad (Baja, Media, Alta)

🎨 ELEMENTOS VISUALES:
- Nodos (categorías)
- Enlaces (flujos entre nodos)
- Ancho proporcional al volumen
- Colores por categoría
- Interactivo (HTML)

💡 CUÁNDO USAR:
- Visualizar procesos complejos
- Análisis de flujos de usuarios
- Transiciones entre estados
- Análisis de conversiones

⚠️ NOTA:
Este gráfico genera un archivo HTML interactivo además del PNG.

Autores: Anthony (@AnThony69x), Emilio (@EmilioSle)
Universidad: ULEAM - Visualización de Datos
Fecha: 2025-11-23
"""

import plotly.graph_objects as go
import pandas as pd
from ..config.settings import INTERACTIVE_DIR, IMAGES_DIR
from ..utils.logger import Logger

logger = Logger()

def sankey_diagram(data):
    """
    Genera diagrama de Sankey interactivo
    
    Args:
        data: DataFrame con datos de Spotify
    """
    logger.info("Generando: Diagrama de Sankey (Flujo de datos)")
    
    try:
        # Crear categorías de popularidad
        data_copy = data.copy()
        data_copy['pop_category'] = pd.cut(
            data_copy['track_popularity'],
            bins=[0, 30, 60, 100],
            labels=['Baja', 'Media', 'Alta']
        )
        
        # Preparar datos: Tipo de Álbum -> Explícito -> Popularidad
        sankey_data = (data_copy
                      .groupby(['album_type', 'explicit', 'pop_category'])
                      .size()
                      .reset_index(name='count'))
        
        # Filtrar flujos pequeños (menos de 10 canciones)
        sankey_data = sankey_data[sankey_data['count'] > 10]
        
        if len(sankey_data) == 0:
            logger.warning("No hay suficientes datos para el diagrama de Sankey")
            return
        
        # Crear mapeo de nodos
        all_nodes = (
            list(sankey_data['album_type'].unique()) +
            ['Explícito', 'No Explícito'] +
            list(sankey_data['pop_category'].unique())
        )
        
        node_dict = {node: idx for idx, node in enumerate(all_nodes)}
        
        # Crear enlaces (source, target, value)
        sources = []
        targets = []
        values = []
        colors = []
        
        for _, row in sankey_data.iterrows():
            # Álbum tipo -> Explícito/No Explícito
            sources.append(node_dict[row['album_type']])
            explicit_label = 'Explícito' if row['explicit'] else 'No Explícito'
            targets.append(node_dict[explicit_label])
            values.append(row['count'])
            colors.append('rgba(29, 185, 84, 0.4)')  # Verde transparente
            
            # Explícito -> Popularidad
            sources.append(node_dict[explicit_label])
            targets.append(node_dict[row['pop_category']])
            values.append(row['count'])
            
            # Color según explícito
            if row['explicit']:
                colors.append('rgba(255, 107, 107, 0.4)')  # Rojo transparente
            else:
                colors.append('rgba(30, 215, 96, 0.4)')    # Verde claro transparente
        
        # Crear gráfico Sankey
        fig = go.Figure(data=[go.Sankey(
            node=dict(
                pad=15,
                thickness=20,
                line=dict(color="black", width=0.5),
                label=all_nodes,
                color=[
                    '#1DB954', '#1ED760', '#535353',  # Tipos de álbum
                    '#FF6B6B', '#1DB954',              # Explícito/No Explícito
                    '#FFD93D', '#6BCB77', '#1ED760'   # Popularidad
                ][:len(all_nodes)]
            ),
            link=dict(
                source=sources,
                target=targets,
                value=values,
                color=colors
            )
        )])
        
        fig.update_layout(
            title_text="🌊 Diagrama de Sankey - Flujo de Canciones<br>Tipo de Álbum → Contenido → Popularidad",
            title_font_size=18,
            font_size=12,
            height=600,
            width=1200
        )
        
        # Guardar HTML interactivo
        html_path = INTERACTIVE_DIR / '10_sankey.html'
        fig.write_html(html_path)
        logger.success(f"Guardado: {html_path.name} (interactivo)")
        
        # Intentar guardar PNG también
        try:
            png_path = IMAGES_DIR / '10_sankey.png'
            fig.write_image(png_path, width=1200, height=600, scale=2)
            logger.success(f"Guardado: {png_path.name}")
        except Exception as e:
            logger.warning(f"No se pudo guardar PNG (instala kaleido): {e}")
        
        # Mostrar en navegador
        fig.show()
        
        logger.info("💡 Abre el archivo HTML en tu navegador para interactividad completa")
        
    except Exception as e:
        logger.error(f"Error al generar Sankey: {e}")
        raise