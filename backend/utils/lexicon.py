"""
Lexicon utilities for Eburon Echo.
Handles loading and managing language-specific pronunciation dictionaries.
"""

import os
from pathlib import Path
from typing import Dict, Optional
from ..config import get_data_dir


class LexiconManager:
    """Manages language-specific lexicons for improved pronunciation."""
    
    def __init__(self):
        self._lexicons: Dict[str, Dict[str, str]] = {}
        self._lexicon_dir = get_data_dir() / "lexicons"
        self._load_available_lexicons()
    
    def _load_available_lexicons(self):
        """Load all available lexicon files."""
        if not self._lexicon_dir.exists():
            return
        
        for lexicon_file in self._lexicon_dir.glob("*.txt"):
            language_code = lexicon_file.stem
            try:
                lexicon = self._load_lexicon_file(lexicon_file)
                if lexicon:
                    self._lexicons[language_code] = lexicon
                    print(f"[lexicon] Loaded {len(lexicon)} entries for {language_code}")
            except Exception as e:
                print(f"[lexicon] Error loading {lexicon_file}: {e}")
    
    def _load_lexicon_file(self, file_path: Path) -> Dict[str, str]:
        """Load a single lexicon file."""
        lexicon = {}
        with open(file_path, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                # Skip empty lines and comments
                if not line or line.startswith('#'):
                    continue
                
                # Format: word pronunciation
                parts = line.split(maxsplit=1)
                if len(parts) == 2:
                    word, pronunciation = parts
                    lexicon[word.lower()] = pronunciation
                else:
                    print(f"[lexicon] Invalid format in {file_path}:{line_num}: {line}")
        
        return lexicon
    
    def get_pronunciation(self, word: str, language: str) -> Optional[str]:
        """
        Get pronunciation for a word in a specific language.
        
        Args:
            word: The word to pronounce
            language: Language code (e.g., 'tl', 'nl', 'nl_be')
            
        Returns:
            Phonetic pronunciation string or None if not found
        """
        # Normalize word to lowercase
        word_lower = word.lower()
        
        # Try exact match first
        if language in self._lexicons:
            if word_lower in self._lexicons[language]:
                return self._lexicons[language][word_lower]
        
        # Try base language for variants (e.g., nl_be -> nl)
        if '_' in language:
            base_lang = language.split('_')[0]
            if base_lang in self._lexicons:
                if word_lower in self._lexicons[base_lang]:
                    return self._lexicons[base_lang][word_lower]
        
        return None
    
    def get_supported_languages(self) -> list[str]:
        """Get list of languages that have lexicons available."""
        return list(self._lexicons.keys())
    
    def reload_lexicons(self):
        """Reload all lexicon files (useful for development)."""
        self._lexicons.clear()
        self._load_available_lexicons()


# Global instance
_lexicon_manager = None


def get_lexicon_manager() -> LexiconManager:
    """Get the global lexicon manager instance."""
    global _lexicon_manager
    if _lexicon_manager is None:
        _lexicon_manager = LexiconManager()
    return _lexicon_manager


def enhance_text_with_lexicon(text: str, language: str) -> str:
    """
    Enhance text with pronunciation hints from lexicon.
    This can be used by TTS models to improve pronunciation.
    
    Args:
        text: Input text
        language: Language code
        
    Returns:
        Text with pronunciation enhancements (implementation depends on TTS model)
    """
    lexicon = get_lexicon_manager()
    
    # Split text into words and check for pronunciation entries
    words = text.split()
    enhanced_words = []
    
    for word in words:
        # Remove punctuation for lookup
        clean_word = word.strip('.,!?;:"()[]{}')
        punctuation = word[len(clean_word):] if len(clean_word) < len(word) else ''
        
        # Get pronunciation from lexicon
        pronunciation = lexicon.get_pronunciation(clean_word, language)
        
        if pronunciation:
            # Add pronunciation hint (format depends on TTS model requirements)
            enhanced_word = f"{clean_word}[{pronunciation}]{punctuation}"
        else:
            enhanced_word = word
        
        enhanced_words.append(enhanced_word)
    
    return ' '.join(enhanced_words)
