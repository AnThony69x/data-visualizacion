"""
📊 CLASE BASE PARA GRÁFICOS
===========================
Clase abstracta de la que heredan todos los gráficos
"""
import matplotlib.pyplot as plt
import seaborn as sns
from abc import ABC, abstractmethod
from ..config.colors import CATEGORICAL
from ..config.settings import IMAGES_DIR, FIGURE_SIZE, FIGURE_DPI, SAVE_DPI
from ..utils.logger import Logger

logger = Logger()

class BasePlot(ABC):
    """Clase base abstracta para todos los gráficos"""
    
    def __init__(self, data, title="", filename="plot", figsize=None):
        """
        Inicializa el gráfico base
        
        Args:
            data: DataFrame con los datos
            title: Título del gráfico
            filename: Nombre del archivo de salida (sin extensión)
            figsize: Tamaño personalizado (ancho, alto) o None para usar default
        """
        self.data = data
        self.title = title
        self.filename = filename
        self.figsize = figsize or FIGURE_SIZE
        self.fig = None
        self.axes = None
        
        # Configurar estilo
        self._setup_style()
    
    def _setup_style(self):
        """Configura el estilo visual de matplotlib y seaborn"""
        sns.set_style("whitegrid")
        sns.set_context("notebook", font_scale=1.0)
        sns.set_palette(CATEGORICAL)
        
        # Aplicar configuración de tamaño
        plt.rcParams['figure.figsize'] = self.figsize
        plt.rcParams['figure.dpi'] = FIGURE_DPI
    
    @abstractmethod
    def create(self):
        """
        Método abstracto para crear el gráfico
        
        DEBE implementarse en todas las subclases
        """
        pass
    
    def customize(self):
        """
        Personaliza el gráfico después de crearlo
        
        Puede sobrescribirse en subclases para personalización adicional
        """
        if self.fig and self.title:
            self.fig.suptitle(self.title, fontsize=14, fontweight='bold', y=0.98)
    
    def fix_labels(self, ax, axis='x', rotation=45, ha='right'):
        """
        Arregla etiquetas distorsionadas
        
        Args:
            ax: Axes de matplotlib
            axis: 'x' o 'y'
            rotation: Ángulo de rotación
            ha: Alineación horizontal
        """
        if axis == 'x':
            ax.tick_params(axis='x', labelrotation=rotation)
            plt.setp(ax.get_xticklabels(), rotation=rotation, ha=ha)
        else:
            plt.setp(ax.get_yticklabels(), ha=ha)
    
    def maximize_window(self):
        """
        Ajusta la ventana al tamaño de la pantalla (sin maximizar completamente)
        """
        try:
            manager = plt.get_current_fig_manager()
            
            # Intentar diferentes backends
            if hasattr(manager, 'window'):
                # TkAgg backend
                try:
                    # Obtener tamaño de pantalla
                    screen_width = manager.window.winfo_screenwidth()
                    screen_height = manager.window.winfo_screenheight()
                    
                    # Usar 90% del tamaño de pantalla
                    width = int(screen_width * 0.9)
                    height = int(screen_height * 0.85)
                    
                    # Posicionar en el centro
                    x = (screen_width - width) // 2
                    y = (screen_height - height) // 2
                    
                    manager.window.geometry(f'{width}x{height}+{x}+{y}')
                except:
                    pass
            
            elif hasattr(manager, 'resize'):
                # Qt backend
                manager.resize(1200, 700)
                
        except Exception as e:
            logger.warning(f"No se pudo ajustar ventana: {e}")
    
    def save(self, filepath=None):
        """
        Guarda el gráfico en archivo PNG de alta resolución
        
        Args:
            filepath: Ruta completa o None para usar default
        """
        if filepath is None:
            filepath = IMAGES_DIR / f"{self.filename}.png"
        
        try:
            # Guardar con alta resolución (300 DPI)
            self.fig.savefig(
                filepath, 
                dpi=SAVE_DPI,              # ← Alta resolución para archivo
                bbox_inches='tight',
                pad_inches=0.3,
                facecolor='white',
                edgecolor='none'
            )
            logger.success(f"Guardado: {filepath.name}")
        except Exception as e:
            logger.error(f"Error al guardar gráfico: {e}")
    
    def show(self):
        """Muestra el gráfico en pantalla con tamaño ajustado"""
        try:
            # Ajustar ventana antes de mostrar
            self.maximize_window()
            
            # Mostrar
            plt.show()
            
        except Exception as e:
            logger.error(f"Error al mostrar gráfico: {e}")
    
    def generate(self, show=True, save=True):
        """
        Genera el gráfico completo (crear + personalizar + guardar + mostrar)
        
        Args:
            show: Si mostrar el gráfico en pantalla
            save: Si guardar el gráfico en archivo
        """
        logger.info(f"Generando: {self.title}")
        
        try:
            self.create()
            self.customize()
            
            # Ajustar layout
            if self.fig:
                self.fig.tight_layout()
            
            if save:
                self.save()
            
            if show:
                self.show()
            
        except Exception as e:
            logger.error(f"Error al generar gráfico: {e}")
            raise
        finally:
            plt.close('all')  