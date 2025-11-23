"""
🔤 UTILIDADES PARA MANEJO DE TEXTO
==================================
Funciones para formatear texto en gráficos
"""

def truncate_text(text, max_length=25):
    """
    Trunca texto largo
    
    Args:
        text: Texto a truncar
        max_length: Longitud máxima
    
    Returns:
        Texto truncado con '...' si es necesario
    """
    if len(str(text)) > max_length:
        return str(text)[:max_length-3] + '...'
    return str(text)


def wrap_text(text, max_width=20):
    """
    Divide texto en múltiples líneas
    
    Args:
        text: Texto a dividir
        max_width: Ancho máximo por línea
    
    Returns:
        Texto con saltos de línea
    """
    words = str(text).split()
    lines = []
    current_line = []
    current_length = 0
    
    for word in words:
        if current_length + len(word) + 1 <= max_width:
            current_line.append(word)
            current_length += len(word) + 1
        else:
            if current_line:
                lines.append(' '.join(current_line))
            current_line = [word]
            current_length = len(word)
    
    if current_line:
        lines.append(' '.join(current_line))
    
    return '\n'.join(lines)


def clean_label(text):
    """
    Limpia etiquetas para visualización
    
    Args:
        text: Texto a limpiar
    
    Returns:
        Texto limpio y formateado
    """
    # Reemplazar caracteres problemáticos
    replacements = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U',
        'ñ': 'n', 'Ñ': 'N',
        '&': 'y', '$': 'S'
    }
    
    text = str(text)
    for old, new in replacements.items():
        text = text.replace(old, new)
    
    return text.strip()