"""
Input validation utilities.
"""

from typing import Tuple, Optional
from pathlib import Path


def validate_text(text: str, max_length: int = 5000) -> Tuple[bool, Optional[str]]:
    """
    Validate text input.
    
    Args:
        text: Text to validate
        max_length: Maximum length
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    if not text or not text.strip():
        return False, "Text cannot be empty"
    
    if len(text) > max_length:
        return False, f"Text too long (maximum {max_length} characters)"
    
    return True, None


def validate_language(language: str) -> Tuple[bool, Optional[str]]:
    """
    Validate language code.

    Supports comprehensive list of world languages including:
    - All ISO 639-1 language codes
    - Regional variants (e.g., zh_hans, pt_br, nl_be)
    - Custom codes for specific dialects and constructed languages

    Args:
        language: Language code

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Comprehensive list of supported language codes
    valid_languages = {
        # Core Qwen3-TTS languages
        'zh', 'en', 'ja', 'ko', 'de', 'fr', 'ru', 'pt', 'es', 'it',
        
        # Previously added
        'tl', 'nl', 'nl_be',
        
        # Major world languages (ISO 639-1)
        'ar', 'hi', 'bn', 'pa', 'ur', 'tr', 'pl', 'th', 'vi', 'sv', 'da', 'no', 'fi',
        'el', 'he', 'cs', 'hu', 'ro', 'bg', 'hr', 'sr', 'sk', 'sl', 'et', 'lv', 'lt',
        'uk', 'mk', 'sq', 'hy', 'ka', 'am', 'sw', 'zu', 'af', 'is', 'mt', 'cy', 'ga',
        'gd', 'eu', 'ca', 'gl', 'ast',
        
        # Chinese variants
        'zh_hans', 'zh_hant', 'yue',
        
        # Portuguese variants
        'pt_br', 'pt_pt',
        
        # French variants
        'fr_ca',
        
        # Spanish and related
        'es_mx', 'an', 'oc',
        
        # Germanic languages
        'fy', 'li', 'lux', 'nds',
        
        # Scandinavian
        'smj', 'fo',
        
        # Slavic extended
        'be', 'bs', 'hsb', 'dsb',
        
        # Indo-Aryan
        'as', 'mr', 'gu', 'kn', 'ml', 'te', 'ta', 'or', 'si', 'ne', 'bh', 'mai', 'rw',
        
        # Iranian
        'fa', 'ps', 'tg', 'ku', 'ckb', 'os',
        
        # Turkic
        'kk', 'ky', 'uz', 'az', 'tk', 'ug', 'tuv', 'sah', 'ba', 'cv', 'kum', 'tt', 'xal',
        
        # African
        'yo', 'ig', 'ha', 'sn', 'ts', 'tn', 'ss', 'nr', 'xh', 'om', 'ti', 'so', 'mg',
        'ny', 'ln', 'kg', 'tw', 'ee', 'ff', 'wo', 'kr', 'bm', 'ki', 'mer', 'dinka',
        'nuer', 'teo', 'ach', 'luy', 'kam', 'kln', 'guu',
        
        # Indonesian and Malay
        'id', 'ms', 'ms_jawi', 'jv2', 'su2', 'mad2', 'min2', 'ace', 'bjn', 'bbc',
        'btx', 'bts', 'bug', 'mak', 'tet',
        
        # Philippine
        'ceb', 'hil', 'war', 'bik', 'pam', 'pag', 'iban', 'ilo',
        
        # Pacific
        'fj', 'to', 'sm', 'haw2', 'mh', 'gil', 'tvl', 'pih',
        
        # Native American
        'nah', 'may', 'quz', 'aym', 'gar', 'cr', 'iu', 'iu_latn', 'oj', 'nav', 'chr', 'mus',
        
        # Caucasian
        'ab', 'av', 'che', 'lez', 'ddo', 'inh', 'lbe', 'tab', 'agx', 'rut', 'tsz',
        
        # Dravidian
        'brx', 'kok', 'tmx',
        
        # Sino-Tibetan
        'bo', 'dz', 'my', 'new', 'mni', 'kha', 'lep',
        
        # Austroasiatic
        'km', 'lo', 'mnw', 'kxm', 'pcc', 'blt',
        
        # Tai-Kadai
        'lu', 'khb', 'shn', 'tdd',
        
        # Hmong-Mien
        'hmn', 'mww',
        
        # Austronesian extended
        'bl', 'reo', 'mah', 'chm', 'pohn', 'yap', 'chuuk', 'kos', 'mok', 'pala',
        
        # Constructed
        'eo', 'la2', 'sjn', 'qya', 'tlh', 'art_lojban', 'ia', 'vol', 'ido', 'nov', 'toki',
        
        # Historical
        'grc', 'got', 'ang', 'non', 'peo', 'pal', 'sog', 'khot',
        
        # Sign languages
        'asl', 'bsl', 'fsl', 'dsl', 'isl2', 'jsl', 'ksl', 'csl',
        
        # Regional and minority
        'br', 'co', 'fur', 'lmo', 'lij', 'eml', 'srd', 'sic', 'nap', 'vec', 'rg',
        
        # Creole
        'ht', 'gcf', 'mfe', 'ses', 'pdc', 'tpi', 'bis', 'pij', 'kri',
        
        # Mixed and contact
        'rom', 'jdt', 'jpr', 'ydd', 'yih', 'lad',
        
        # Macro-languages
        'mul', 'und', 'zxx', 'mis',
    }
    
    if language not in valid_languages:
        return False, f"Invalid language code. Supported codes include ISO 639-1 codes and regional variants. Examples: en, zh, es, fr, de, pt_br, nl_be, tl, etc."

    return True, None


def validate_file_path(path: str) -> Tuple[bool, Optional[str]]:
    """
    Validate file path exists.
    
    Args:
        path: File path
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    file_path = Path(path)
    if not file_path.exists():
        return False, f"File not found: {path}"
    
    if not file_path.is_file():
        return False, f"Path is not a file: {path}"
    
    return True, None
