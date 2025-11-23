"""
🎨 CONFIGURACIÓN DE COLORES
===========================
Paletas de colores profesionales para todas las visualizaciones
"""

# Colores principales de Spotify
SPOTIFY = {
    'primary': '#1DB954',      # Verde Spotify
    'secondary': '#1ED760',    # Verde claro
    'dark': '#191414',         # Negro Spotify
    'gray': '#535353',         # Gris
    'white': '#FFFFFF'
}

# Paleta categórica (8 colores distintos)
CATEGORICAL = [
    '#1DB954',  # Verde Spotify
    '#FF6B6B',  # Rojo coral
    '#4ECDC4',  # Turquesa
    '#FFD93D',  # Amarillo
    '#6BCB77',  # Verde menta
    '#A8E6CF',  # Verde agua
    '#FF8B94',  # Rosa salmón
    '#FFD3B6',  # Melocotón
]

# Paletas para mapas de calor
SEQUENTIAL = 'Greens'
DIVERGENT = 'RdYlGn'

# Colores para contenido explícito
EXPLICIT = {
    True: '#FF6B6B',   # Rojo para explícito
    False: '#1DB954'   # Verde para no explícito
}

# Gradientes personalizados
GRADIENT_GREEN = ['#E8F5E9', '#81C784', '#388E3C', '#1B5E20']
GRADIENT_PURPLE = ['#F3E5F5', '#BA68C8', '#7B1FA2', '#4A148C']
GRADIENT_SUNSET = ['#FFF59D', '#FFCA28', '#FF7043', '#E91E63']

def get_palette(name='categorical', n_colors=None):
    """
    Obtiene una paleta de colores
    
    Args:
        name: Nombre de la paleta
        n_colors: Número de colores (None = todos)
    
    Returns:
        Lista de colores en formato hex
    """
    palettes = {
        'spotify': list(SPOTIFY.values()),
        'categorical': CATEGORICAL,
        'gradient_green': GRADIENT_GREEN,
        'gradient_purple': GRADIENT_PURPLE,
        'gradient_sunset': GRADIENT_SUNSET
    }
    
    palette = palettes.get(name, CATEGORICAL)
    return palette[:n_colors] if n_colors else palette