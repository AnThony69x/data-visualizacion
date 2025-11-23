"""
🛠️ FUNCIONES AUXILIARES
=======================
Utilidades y helpers para el proyecto
"""
import pandas as pd
import numpy as np

def format_number(num, decimals=2):
    """
    Formatea números con separador de miles
    
    Args:
        num: Número a formatear
        decimals: Cantidad de decimales
    
    Returns:
        String formateado
    """
    if pd.isna(num):
        return "N/A"
    
    if isinstance(num, (int, float)):
        if decimals == 0:
            return f"{int(num):,}"
        return f"{num:,.{decimals}f}"
    
    return str(num)


def calculate_percentage(part, total):
    """
    Calcula porcentaje
    
    Args:
        part: Parte del total
        total: Total
    
    Returns:
        Porcentaje (0-100)
    """
    if total == 0:
        return 0
    return (part / total) * 100


def get_top_n(data, column, n=10, ascending=False):
    """
    Obtiene los top N valores de una columna
    
    Args:
        data: DataFrame
        column: Columna a analizar
        n: Cantidad de elementos
        ascending: Orden ascendente/descendente
    
    Returns:
        DataFrame filtrado
    """
    return data.nlargest(n, column) if not ascending else data.nsmallest(n, column)


def filter_outliers(data, column, n_std=3):
    """
    Filtra outliers usando desviación estándar
    
    Args:
        data: DataFrame
        column: Columna a filtrar
        n_std: Número de desviaciones estándar
    
    Returns:
        DataFrame sin outliers
    """
    mean = data[column].mean()
    std = data[column].std()
    
    lower_bound = mean - (n_std * std)
    upper_bound = mean + (n_std * std)
    
    return data[(data[column] >= lower_bound) & (data[column] <= upper_bound)]


def create_category_bins(data, column, bins=3, labels=None):
    """
    Crea categorías desde una columna numérica
    
    Args:
        data: DataFrame
        column: Columna a categorizar
        bins: Número de bins o lista de bordes
        labels: Etiquetas para las categorías
    
    Returns:
        Serie con categorías
    """
    if labels is None:
        labels = [f"Cat_{i+1}" for i in range(bins if isinstance(bins, int) else len(bins)-1)]
    
    return pd.cut(data[column], bins=bins, labels=labels)


def safe_divide(numerator, denominator, default=0):
    """
    División segura que evita división por cero
    
    Args:
        numerator: Numerador
        denominator: Denominador
        default: Valor por defecto si denominador es 0
    
    Returns:
        Resultado de la división o default
    """
    if denominator == 0:
        return default
    return numerator / denominator


def search_songs(data, query):
    """
    Busca canciones por nombre
    
    Args:
        data: DataFrame con datos de Spotify
        query: Texto a buscar en el nombre de la canción
    
    Returns:
        DataFrame con resultados ordenados por popularidad
    
    Ejemplo:
        >>> results = search_songs(data, "love")
        >>> print(results.head())
    """
    import pandas as pd
    
    if not query or query.strip() == "":
        return pd.DataFrame()
    
    # Buscar en track_name (case insensitive)
    results = data[
        data['track_name'].str.contains(query, case=False, na=False)
    ]
    
    # Seleccionar columnas relevantes
    results = results[[
        'track_name', 
        'artist_name', 
        'track_popularity', 
        'album_name', 
        'track_duration_min',
        'explicit'
    ]].copy()
    
    # Ordenar por popularidad descendente
    results = results.sort_values('track_popularity', ascending=False)
    
    # Eliminar duplicados
    results = results.drop_duplicates(subset=['track_name', 'artist_name'])
    
    return results


def compare_artists(data, artist1, artist2):
    """
    Compara dos artistas en múltiples métricas
    
    Args:
        data: DataFrame con datos de Spotify
        artist1: Nombre del primer artista
        artist2: Nombre del segundo artista
    
    Returns:
        DataFrame con comparación o None si no se encuentran
    
    Ejemplo:
        >>> comparison = compare_artists(data, "Drake", "The Weeknd")
        >>> print(comparison)
    """
    import pandas as pd
    
    # Buscar artistas (case insensitive)
    data1 = data[data['artist_name'].str.lower() == artist1.lower()]
    data2 = data[data['artist_name'].str.lower() == artist2.lower()]
    
    # Verificar si existen
    if len(data1) == 0 or len(data2) == 0:
        return None
    
    # Calcular métricas
    comparison = pd.DataFrame({
        'Métrica': [
            '🎵 Total de canciones',
            '⭐ Popularidad promedio',
            '🏆 Popularidad máxima',
            '👥 Seguidores',
            '⏱️  Duración promedio (min)',
            '💿 Álbumes únicos',
            '🔞 Canciones explícitas',
            '📊 % Contenido explícito',
            '🎼 Géneros principales'
        ],
        artist1: [
            len(data1),
            f"{data1['track_popularity'].mean():.1f}",
            f"{data1['track_popularity'].max():.0f}",
            f"{data1['artist_followers'].iloc[0]:,}",
            f"{data1['track_duration_min'].mean():.2f}",
            data1['album_name'].nunique(),
            data1['explicit'].sum(),
            f"{(data1['explicit'].sum() / len(data1) * 100):.1f}%",
            data1['artist_genres'].iloc[0][:50] if 'artist_genres' in data1.columns else 'N/A'
        ],
        artist2: [
            len(data2),
            f"{data2['track_popularity'].mean():.1f}",
            f"{data2['track_popularity'].max():.0f}",
            f"{data2['artist_followers'].iloc[0]:,}",
            f"{data2['track_duration_min'].mean():.2f}",
            data2['album_name'].nunique(),
            data2['explicit'].sum(),
            f"{(data2['explicit'].sum() / len(data2) * 100):.1f}%",
            data2['artist_genres'].iloc[0][:50] if 'artist_genres' in data2.columns else 'N/A'
        ]
    })
    
    return comparison