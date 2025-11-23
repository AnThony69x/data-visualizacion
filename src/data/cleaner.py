"""
🧹 LIMPIADOR DE DATOS
====================
Limpia y preprocesa datos de Spotify
"""
import pandas as pd
from ..config.settings import CLEAN_DATA_FILE
from ..utils.logger import Logger

logger = Logger()

class DataCleaner:
    """Clase para limpiar datos de Spotify"""
    
    def __init__(self, data):
        """
        Inicializa el limpiador con datos
        
        Args:
            data: DataFrame con datos crudos
        """
        self.data = data.copy()
        self.original_count = len(data)
    
    def clean(self):
        """
        Ejecuta todo el proceso de limpieza
        
        Returns:
            DataFrame limpio
        """
        logger.header("LIMPIEZA DE DATOS")
        logger.info("Iniciando proceso de limpieza...")
        
        self._remove_duplicates()
        self._handle_missing_values()
        self._clean_text_fields()
        self._convert_types()
        self._validate_numeric_fields()
        self._sort_data()
        
        removed = self.original_count - len(self.data)
        logger.success(f"Limpieza completada: {len(self.data):,} registros válidos ({removed:,} eliminados)")
        
        return self.data
    
    def _remove_duplicates(self):
        """Elimina registros duplicados por track_id"""
        before = len(self.data)
        
        if 'track_id' in self.data.columns:
            self.data = self.data.drop_duplicates(subset=['track_id'], keep='first')
            removed = before - len(self.data)
            if removed > 0:
                logger.info(f"  • Duplicados eliminados: {removed:,}")
        else:
            logger.warning("  • Columna 'track_id' no encontrada, omitiendo eliminación de duplicados")
    
    def _handle_missing_values(self):
        """Maneja valores faltantes en columnas críticas"""
        before = len(self.data)
        
        critical_columns = ['track_id', 'track_name', 'artist_name']
        existing_columns = [col for col in critical_columns if col in self.data.columns]
        
        if existing_columns:
            self.data = self.data.dropna(subset=existing_columns)
            removed = before - len(self.data)
            if removed > 0:
                logger.info(f"  • Valores faltantes eliminados: {removed:,}")
        else:
            logger.warning("  • No se encontraron columnas críticas para validar")
    
    def _clean_text_fields(self):
        """Limpia espacios en blanco de campos de texto"""
        text_fields = ['track_name', 'artist_name', 'album_name']
        cleaned = 0
        
        for field in text_fields:
            if field in self.data.columns:
                self.data[field] = self.data[field].astype(str).str.strip()
                cleaned += 1
        
        if cleaned > 0:
            logger.info(f"  • Campos de texto limpiados: {cleaned}")
    
    def _convert_types(self):
        """Convierte tipos de datos apropiadamente"""
        conversions = 0
        
        # Convertir explicit a booleano
        if 'explicit' in self.data.columns:
            self.data['explicit'] = self.data['explicit'].map({
                'TRUE': True, 'FALSE': False, 
                True: True, False: False,
                1: True, 0: False,
                '1': True, '0': False
            })
            conversions += 1
        
        # Convertir fechas
        if 'album_release_date' in self.data.columns:
            self.data['album_release_date'] = pd.to_datetime(
                self.data['album_release_date'], 
                errors='coerce'
            )
            self.data['year'] = self.data['album_release_date'].dt.year
            conversions += 1
        
        if conversions > 0:
            logger.info(f"  • Tipos de datos convertidos: {conversions}")
    
    def _validate_numeric_fields(self):
        """Valida y corrige campos numéricos"""
        before = len(self.data)
        
        # Validar duración (entre 0 y 30 minutos)
        if 'track_duration_min' in self.data.columns:
            self.data = self.data[
                (self.data['track_duration_min'] > 0) & 
                (self.data['track_duration_min'] < 30)
            ]
        
        # Validar popularidad (0-100)
        if 'track_popularity' in self.data.columns:
            self.data['track_popularity'] = self.data['track_popularity'].clip(0, 100)
        
        if 'artist_popularity' in self.data.columns:
            self.data['artist_popularity'] = self.data['artist_popularity'].clip(0, 100)
        
        # Validar seguidores (no negativos)
        if 'artist_followers' in self.data.columns:
            self.data = self.data[self.data['artist_followers'] >= 0]
        
        removed = before - len(self.data)
        if removed > 0:
            logger.info(f"  • Valores numéricos inválidos corregidos/eliminados: {removed:,}")
    
    def _sort_data(self):
        """Ordena datos por popularidad descendente"""
        if 'track_popularity' in self.data.columns:
            self.data = self.data.sort_values('track_popularity', ascending=False)
            self.data = self.data.reset_index(drop=True)
            logger.info(f"  • Datos ordenados por popularidad")
    
    def save(self, filepath=None):
        """
        Guarda datos limpios en CSV
        
        Args:
            filepath: Ruta donde guardar (usa default si es None)
        """
        filepath = filepath or CLEAN_DATA_FILE
        
        try:
            self.data.to_csv(filepath, index=False, encoding='utf-8-sig')
            logger.success(f"Datos guardados en: {filepath.name}")
        except Exception as e:
            logger.error(f"Error al guardar datos: {e}")
            raise