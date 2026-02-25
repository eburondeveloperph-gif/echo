#!/usr/bin/env python3
"""
Enhance multiple lexicons using Multilingual LibriSpeech dataset.
This script processes all available languages to improve pronunciation coverage.
"""

import sys
import os
from pathlib import Path

# Add the backend directory to the path
sys.path.append(str(Path(__file__).parent.parent))

from utils.dataset_processor import DatasetProcessor


def main():
    """Main function to enhance all available lexicons."""
    print("🌍 Enhancing Multiple Lexicons with Multilingual LibriSpeech")
    print("=" * 60)
    
    processor = DatasetProcessor()
    
    # Available languages in Multilingual LibriSpeech
    available_languages = {
        'dutch': ['nl.txt', 'nl_be.txt'],  # Standard Dutch and Flemish
        'french': ['fr.txt', 'fr_ca.txt'],  # French and Canadian French
        'german': ['de.txt'],               # German
        'italian': ['it.txt'],              # Italian
        'polish': ['pl.txt'],               # Polish
        'portuguese': ['pt.txt', 'pt_br.txt', 'pt_pt.txt'],  # Portuguese variants
        'spanish': ['es.txt', 'es_mx.txt'],  # Spanish and Mexican Spanish
    }
    
    results = {}
    
    for language, lexicon_files in available_languages.items():
        print(f"\n📚 Processing {language.capitalize()}...")
        
        lang_results = []
        for lexicon_file in lexicon_files:
            print(f"  📝 Enhancing {lexicon_file}...")
            success = processor.enhance_lexicon_from_dataset(language, lexicon_file)
            lang_results.append((lexicon_file, success))
            
            if success:
                print(f"    ✅ {lexicon_file} enhanced successfully!")
            else:
                print(f"    ❌ {lexicon_file} enhancement failed")
        
        results[language] = lang_results
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 Enhancement Summary:")
    
    total_success = 0
    total_failed = 0
    
    for language, lang_results in results.items():
        print(f"\n{language.capitalize()}:")
        for lexicon_file, success in lang_results:
            status = "✅ Success" if success else "❌ Failed"
            print(f"  {lexicon_file}: {status}")
            if success:
                total_success += 1
            else:
                total_failed += 1
    
    print(f"\n🎯 Overall Results:")
    print(f"✅ Successful: {total_success}")
    print(f"❌ Failed: {total_failed}")
    print(f"📈 Success Rate: {total_success/(total_success+total_failed)*100:.1f}%")
    
    if total_success > 0:
        print(f"\n🎉 Lexicon enhancement completed for {total_success} languages!")
        print("💡 The enhanced lexicons now include more words from real speech data.")
        print("🔄 Restart the Eburon Echo server to load the updated lexicons.")
    
    print("\n📖 Next steps:")
    print("1. Review the enhanced lexicon files in data/lexicons/")
    print("2. Add proper IPA pronunciations for the new words")
    print("3. Test voice generation with the enhanced lexicons")
    print("4. Consider processing additional datasets for further improvements")
    
    # Show statistics
    print(f"\n📈 Dataset Statistics:")
    print(f"🌍 Languages processed: {len(available_languages)}")
    print(f"📝 Lexicon files enhanced: {total_success + total_failed}")
    print(f"🗂️  Total lexicon files available: {sum(len(files) for files in available_languages.values())}")


if __name__ == "__main__":
    main()
