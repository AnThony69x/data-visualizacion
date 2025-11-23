"""
📥 CARGADOR DE DATOS
===================
Carga y valida datos desde archivos CSV
"""
import pandas as pd
from pathlib import Path
from ..config.settings import RAW_DATA_FILE, CLEAN_DATA_FILE
from ..utils.logger import Logger

logger = Logger()

class DataLoader:
    """Clase para cargar datos de Spotify"""
    
    def __init__(self):
        self.raw_data = None
        self.clean_data = None
    
    def load_raw_data(self, filepath=None):
        """
        Carga datos crudos desde CSV
        
        Args:
            filepath: Ruta del archivo (usa default si es None)
        
        Returns:
            DataFrame con los datos cargados
        """
        filepath = filepath or RAW_DATA_FILE
        
        try:
            logger.info(f"Cargando datos desde: {filepath.name}")
            
            # Intentar diferentes encodings
            for encoding in ['utf-8', 'latin-1', 'cp1252']:
                try:
                    self.raw_data = pd.read_csv(
                        filepath, 
                        encoding=encoding,
                        encoding_errors='ignore'
                    )
                    logger.success(f"Datos cargados: {len(self.raw_data):,} registros")
                    return self.raw_data
                except UnicodeDecodeError:
                    continue
            
            raise ValueError("No se pudo leer el archivo con ningún encoding")
            
        except FileNotFoundError:
            logger.error(f"Archivo no encontrado: {filepath}")
            logger.info(f"Coloca tu archivo en: data/raw/spotify_data.csv")
            raise
        except Exception as e:
            logger.error(f"Error al cargar datos: {e}")
            raise
    
    def load_clean_data(self, filepath=None):
        """
        Carga datos limpios desde CSV
        
        Args:
            filepath: Ruta del archivo (usa default si es None)
        
        Returns:
            DataFrame con los datos limpios
        """
        filepath = filepath or CLEAN_DATA_FILE
        
        try:
            if not Path(filepath).exists():
                logger.warning("Archivo limpio no encontrado. Usando datos crudos.")
                return self.load_raw_data()
            
            logger.info(f"Cargando datos limpios...")
            self.clean_data = pd.read_csv(
                filepath, 
                encoding='utf-8',
                encoding_errors='ignore'
            )
            
            # Convertir fechas
            if 'album_release_date' in self.clean_data.columns:
                self.clean_data['album_release_date'] = pd.to_datetime(
                    self.clean_data['album_release_date'], 
                    errors='coerce'
                )
                self.clean_data['year'] = self.clean_data['album_release_date'].dt.year
            
            logger.success(f"Datos limpios cargados: {len(self.clean_data):,} registros")
            return self.clean_data
            
        except Exception as e:
            logger.error(f"Error al cargar datos limpios: {e}")
            raise
    
    def get_data_summary(self):
        """
        Obtiene resumen estadístico de los datos
        
        Returns:
            Diccionario con estadísticas
        """
        if self.clean_data is None:
            self.load_clean_data()
        
        df = self.clean_data
        
        summary = {
            'total_tracks': len(df),
            'unique_artists': df['artist_name'].nunique() if 'artist_name' in df.columns else 0,
            'unique_albums': df['album_name'].nunique() if 'album_name' in df.columns else 0,
            'explicit_count': df['explicit'].sum() if 'explicit' in df.columns else 0,
            'avg_popularity': df['track_popularity'].mean() if 'track_popularity' in df.columns else 0,
            'date_range': (
                df['year'].min() if 'year' in df.columns else None,
                df['year'].max() if 'year' in df.columns else None
            )
        }
        
        return summary