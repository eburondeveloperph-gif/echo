#!/usr/bin/env python3
"""
Enhance Dutch lexicon using Multilingual LibriSpeech dataset.
This script downloads Dutch speech data and extracts common words to improve pronunciation.
"""

import sys
import os
from pathlib import Path

# Add the backend directory to the path
sys.path.append(str(Path(__file__).parent.parent))

from utils.dataset_processor import DatasetProcessor


def main():
    """Main function to enhance Dutch lexicon."""
    print("🇳🇱 Enhancing Dutch Lexicon with Multilingual LibriSpeech")
    print("=" * 60)
    
    processor = DatasetProcessor()
    
    # Enhance standard Dutch lexicon
    print("\n📚 Processing standard Dutch (nl)...")
    success_nl = processor.enhance_lexicon_from_dataset('dutch', 'nl.txt')
    
    if success_nl:
        print("✅ Standard Dutch lexicon enhanced successfully!")
    else:
        print("❌ Failed to enhance standard Dutch lexicon")
    
    # Enhance Flemish Dutch lexicon
    print("\n📚 Processing Flemish Dutch (nl_be)...")
    success_nl_be = processor.enhance_lexicon_from_dataset('dutch', 'nl_be.txt')
    
    if success_nl_be:
        print("✅ Flemish Dutch lexicon enhanced successfully!")
    else:
        print("❌ Failed to enhance Flemish Dutch lexicon")
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 Enhancement Summary:")
    print(f"Standard Dutch (nl): {'✅ Success' if success_nl else '❌ Failed'}")
    print(f"Flemish Dutch (nl_be): {'✅ Success' if success_nl_be else '❌ Failed'}")
    
    if success_nl or success_nl_be:
        print("\n🎉 Dutch lexicon enhancement completed!")
        print("💡 The enhanced lexicons now include more words from real Dutch speech data.")
        print("🔄 Restart the Eburon Echo server to load the updated lexicons.")
    else:
        print("\n⚠️  Lexicon enhancement failed. Check the error messages above.")
    
    print("\n📖 Next steps:")
    print("1. Review the enhanced lexicon files in data/lexicons/")
    print("2. Add proper IPA pronunciations for the new words")
    print("3. Test Dutch voice generation with the enhanced lexicon")
    print("4. Consider processing other languages using the same approach")


if __name__ == "__main__":
    main()
