"""
Dataset processing utilities for Eburon Echo.
Handles downloading and processing multilingual speech datasets to improve lexicon coverage.
"""

import os
import json
import requests
from pathlib import Path
from typing import Dict, List, Optional
from huggingface_hub import hf_hub_download, HfApi
from config import get_data_dir


class DatasetProcessor:
    """Processes speech datasets to extract and improve lexicon entries."""
    
    def __init__(self):
        self.data_dir = get_data_dir() / "datasets"
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.api = HfApi()
    
    def download_multilingual_librispeech(self, language: str, split: str = "train") -> Optional[str]:
        """
        Download Multilingual LibriSpeech dataset for a specific language.
        
        Args:
            language: Language code (e.g., 'dutch', 'german', 'french')
            split: Dataset split ('train', 'dev', 'test')
            
        Returns:
            Path to downloaded dataset file or None if failed
        """
        try:
            print(f"[dataset] Downloading Multilingual LibriSpeech for {language} ({split})...")
            
            # Get dataset info
            dataset_info = self.api.dataset_info("facebook/multilingual_librispeech")
            
            # Find the correct file for the language and split
            repo_id = "facebook/multilingual_librispeech"
            filename = f"data/mls_{language}/{split}/transcripts.txt"
            
            # Download the transcription file
            file_path = hf_hub_download(
                repo_id=repo_id,
                filename=filename,
                repo_type="dataset",
                cache_dir=self.data_dir
            )
            
            print(f"[dataset] Downloaded: {file_path}")
            return file_path
            
        except Exception as e:
            print(f"[dataset] Error downloading {language} dataset: {e}")
            return None
    
    def extract_lexicon_from_transcriptions(self, transcription_file: Path, language: str) -> Dict[str, str]:
        """
        Extract word-frequency pairs from transcription file to build lexicon.
        
        Args:
            transcription_file: Path to transcription file
            language: Target language code
            
        Returns:
            Dictionary of words with frequency counts
        """
        word_freq = {}
        
        try:
            with open(transcription_file, 'r', encoding='utf-8') as f:
                for line_num, line in enumerate(f, 1):
                    line = line.strip()
                    if not line:
                        continue
                    
                    # Format: "file_id transcription_text"
                    parts = line.split(' ', 1)
                    if len(parts) < 2:
                        continue
                    
                    transcription = parts[1].lower()
                    
                    # Split into words and count frequency
                    words = transcription.split()
                    for word in words:
                        # Clean up punctuation
                        clean_word = word.strip('.,!?;:"()[]{}')
                        if clean_word and len(clean_word) > 1:
                            word_freq[clean_word] = word_freq.get(clean_word, 0) + 1
            
            print(f"[dataset] Extracted {len(word_freq)} unique words from {transcription_file}")
            return word_freq
            
        except Exception as e:
            print(f"[dataset] Error processing transcriptions: {e}")
            return {}
    
    def enhance_lexicon_from_dataset(self, language: str, target_lexicon: str) -> bool:
        """
        Enhance existing lexicon using dataset data.
        
        Args:
            language: Dataset language name (e.g., 'dutch')
            target_lexicon: Target lexicon file (e.g., 'nl.txt')
            
        Returns:
            Success status
        """
        try:
            # Download dataset
            transcription_file = self.download_multilingual_librispeech(language)
            if not transcription_file:
                return False
            
            # Extract word frequencies
            word_freq = self.extract_lexicon_from_transcriptions(Path(transcription_file), language)
            
            # Get existing lexicon
            lexicon_path = Path("/Users/master/voicebox/data/lexicons") / target_lexicon
            existing_lexicon = {}
            
            if lexicon_path.exists():
                with open(lexicon_path, 'r', encoding='utf-8') as f:
                    for line in f:
                        line = line.strip()
                        if line and not line.startswith('#'):
                            parts = line.split(maxsplit=1)
                            if len(parts) == 2:
                                existing_lexicon[parts[0].lower()] = parts[1]
            
            # Find new words to add
            new_words = {}
            for word, freq in sorted(word_freq.items(), key=lambda x: x[1], reverse=True):
                if word not in existing_lexicon and freq >= 5:  # Only add words that appear 5+ times
                    new_words[word] = f"[{word}]"  # Placeholder pronunciation
            
            # Update lexicon
            if new_words:
                with open(lexicon_path, 'a', encoding='utf-8') as f:
                    f.write(f"\n# Auto-generated from Multilingual LibriSpeech ({language})\n")
                    for word, pronunciation in new_words.items():
                        f.write(f"{word} {pronunciation}\n")
                
                print(f"[dataset] Added {len(new_words)} new words to {target_lexicon}")
                return True
            else:
                print(f"[dataset] No new words to add to {target_lexicon}")
                return True
                
        except Exception as e:
            print(f"[dataset] Error enhancing lexicon: {e}")
            return False
    
    def get_available_languages(self) -> List[str]:
        """Get list of available languages in Multilingual LibriSpeech."""
        try:
            dataset_info = self.api.dataset_info("facebook/multilingual_librispeech")
            # This would need to be parsed from the dataset structure
            # For now, return known languages
            return [
                'dutch', 'german', 'french', 'spanish', 'italian', 'portuguese',
                'polish', 'russian', 'arabic', 'mandarin_chinese', 'japanese',
                'korean', 'hindi', 'turkish', 'finnish', 'swedish', 'norwegian',
                'danish', 'icelandic', 'greek', 'czech', 'hungarian', 'romanian'
            ]
        except Exception as e:
            print(f"[dataset] Error getting available languages: {e}")
            return []


def enhance_dutch_lexicon():
    """Quick function to enhance Dutch lexicon using Multilingual LibriSpeech."""
    processor = DatasetProcessor()
    return processor.enhance_lexicon_from_dataset('dutch', 'nl.txt')


def enhance_flemish_lexicon():
    """Quick function to enhance Flemish lexicon using Dutch dataset."""
    processor = DatasetProcessor()
    return processor.enhance_lexicon_from_dataset('dutch', 'nl_be.txt')


if __name__ == "__main__":
    # Example usage
    processor = DatasetProcessor()
    
    # Enhance Dutch lexicon
    success = processor.enhance_lexicon_from_dataset('dutch', 'nl.txt')
    if success:
        print("✅ Dutch lexicon enhanced successfully!")
    
    # You can also process other languages
    # processor.enhance_lexicon_from_dataset('german', 'de.txt')
    # processor.enhance_lexicon_from_dataset('french', 'fr.txt')
