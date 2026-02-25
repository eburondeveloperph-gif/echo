# Comprehensive Language Support in Eburon Echo

This document describes the extensive language support in Eburon Echo, now supporting **200+ languages and variants** from around the world.

## Supported Languages Overview

Eburon Echo now supports an unprecedented range of languages, organized into several categories:

### Core Qwen3-TTS Native Languages (Highest Quality)
These languages have native support in the base Qwen3-TTS model and typically provide the highest quality synthesis:

- **Chinese** (zh) - Native support
- **English** (en) - Native support  
- **Japanese** (ja) - Native support
- **Korean** (ko) - Native support
- **German** (de) - Native support
- **French** (fr) - Native support
- **Russian** (ru) - Native support
- **Portuguese** (pt) - Native support
- **Spanish** (es) - Native support
- **Italian** (it) - Native support

### Enhanced Languages with Lexicon Support
These languages include comprehensive pronunciation dictionaries for improved accuracy:

- **Tagalog (Filipino)** (tl) - Complete lexicon with cultural expressions
- **Dutch (Netherlands)** (nl) - Standard Dutch pronunciation guide
- **Dutch (Flemish - Belgium)** (nl_be) - Belgian Dutch with regional variations
- **Arabic** (ar) - Modern Standard Arabic with common expressions
- **Hindi** (hi) - Devanagari script with IPA pronunciations
- **Swahili** (sw) - Comprehensive East African language support
- **Japanese** (ja) - Enhanced with proper pronunciation guides
- **Korean** (ko) - Hangul script with detailed phonetics

### Major World Languages
Additional widely spoken languages with ISO 639-1 support:

#### European Languages
- **Germanic**: Swedish (sv), Danish (da), Norwegian (no), Icelandic (is), Afrikaans (af)
- **Slavic**: Polish (pl), Czech (cs), Hungarian (hu), Romanian (ro), Bulgarian (bg), Croatian (hr), Serbian (sr), Slovak (sk), Slovenian (sl), Estonian (et), Latvian (lv), Lithuanian (lt), Ukrainian (uk), Macedonian (mk), Belarusian (be), Bosnian (bs)
- **Other**: Albanian (sq), Armenian (hy), Georgian (ka), Greek (el), Hebrew (he), Maltese (mt), Irish (ga), Scottish Gaelic (gd), Welsh (cy), Basque (eu), Catalan (ca), Galician (gl), Breton (br), Corsican (co), Friulian (fur)

#### Asian Languages
- **Indo-Aryan**: Bengali (bn), Punjabi (pa), Urdu (ur), Assamese (as), Marathi (mr), Gujarati (gu), Kannada (kn), Malayalam (ml), Telugu (te), Tamil (ta), Odia (or), Sinhala (si), Nepali (ne), Bhojpuri (bh), Maithili (mai), Kinyarwanda (rw)
- **Iranian**: Persian/Farsi (fa), Pashto (ps), Tajik (tg), Kurdish (Kurmanji) (ku), Kurdish (Sorani) (ckb), Ossetian (os)
- **Turkic**: Turkish (tr), Azerbaijani (az), Uzbek (uz), Kazakh (kk), Kyrgyz (ky), Turkmen (tk), Uyghur (ug), Tuvan (tuv), Yakut (sah), Bashkir (ba), Chuvash (cv), Tatar (tt), Kalmyk (xal)
- **Southeast Asian**: Vietnamese (vi), Thai (th), Indonesian (id), Malay (ms), Lao (lo), Khmer (km), Burmese (my)

#### African Languages
- **Niger-Congo**: Yoruba (yo), Igbo (ig), Hausa (ha), Shona (sn), Tsonga (ts), Tswana (tn), Swati (ss), Ndebele (nr), Xhosa (xh), Oromo (om), Tigrinya (ti), Somali (so), Malagasy (mg), Chichewa (ny), Lingala (ln), Kikongo (kg), Twi (tw), Ewe (ee), Fulani (ff), Wolof (wo), Kanuri (kr), Bambara (bm), Kikuyu (ki)
- **Other**: Amharic (am), Zulu (zu)

#### Pacific Languages
- Fijian (fj), Tongan (to), Samoan (sm), Hawaiian (haw2), Marshallese (mh), Gilbertese (gil), Tuvaluan (tvl)

#### Indigenous American Languages
- **North American**: Navajo (nav), Cherokee (chr), Ojibwe (oj), Cree (cr), Inuktitut (iu), Nahuatl (nah)
- **Central/South American**: Quechua (quz), Aymara (aym), Yucatec Maya (may), Guarani (gn)

### Regional Variants and Dialects
- **Chinese**: Simplified (zh_hans), Traditional (zh_hant), Cantonese (yue)
- **Portuguese**: Brazil (pt_br), Portugal (pt_pt)
- **French**: Canada (fr_ca)
- **Spanish**: Mexico (es_mx)
- **Dutch**: Netherlands (nl), Flemish Belgium (nl_be)
- **Inuktitut**: Syllabics (iu), Latin script (iu_latn)

### Constructed and Historical Languages
- **Constructed**: Esperanto (eo), Klingon (tlh), Lojban (art_lojban), Interlingua (ia), Volapük (vol), Ido (ido), Novial (nov), Toki Pona (toki), Sindarin (sjn), Quenya (qya)
- **Historical**: Ancient Greek (grc), Latin (la2), Gothic (got), Old English (ang), Old Norse (non), Old Persian (peo), Pahlavi (pal), Sogdian (sog)

### Special Categories
- **Sign Languages**: American (asl), British (bsl), French (fsl), German (dsl), International (isl2), Japanese (jsl), Korean (ksl), Chinese (csl)
- **Creole Languages**: Haitian (ht), Mauritian (mfe), Seychellois (ses), Tok Pisin (tpi), Bislama (bis), Nigerian Pidgin (pij), Krio (kri)
- **Mixed Languages**: Romani (rom), Ladino (lad), Yiddish (ydd/yih)
- **Macro-languages**: Multiple (mul), Undetermined (und), No content (zxx), Uncoded (mis)

## Lexicon System

The enhanced lexicon system provides pronunciation guidance for improved accuracy across supported languages.

### How It Works
1. **Automatic Detection**: The system automatically loads available lexicon files
2. **Pronunciation Enhancement**: Text is enhanced with phonetic guidance before TTS generation
3. **Fallback Support**: If no lexicon entry exists, the model uses built-in pronunciation
4. **Regional Variants**: Support for dialect-specific pronunciations

### Available Lexicon Files
Currently includes comprehensive lexicons for:
- **Arabic** (ar.txt) - Modern Standard Arabic with IPA
- **Hindi** (hi.txt) - Devanagari script with detailed phonetics  
- **Swahili** (sw.txt) - East African Bantu language
- **Japanese** (ja.txt) - Enhanced with proper pronunciation
- **Korean** (ko.txt) - Hangul with Revised Romanization
- **Tagalog** (tl.txt) - Filipino with cultural expressions
- **Dutch** (nl.txt) - Standard Dutch pronunciation
- **Flemish** (nl_be.txt) - Belgian Dutch variants

### Lexicon Format
```
# Comments start with #
word phonetic_pronunciation
مرحباː marˈħa.baː
नमस्ते nə.məs.teː
jambo d͡ʒam.bo
こんにちは kon.ni.ti.wa
```

## Implementation Details

### Frontend Changes
- **Language Constants**: Updated with 200+ language codes and display names
- **UI Components**: Dropdown menus now support extensive language selection
- **TypeScript**: Proper typing for all language codes
- **Search**: Enhanced filtering for large language lists

### Backend Changes
- **Validation**: Comprehensive language code validation
- **API Support**: All endpoints accept the full range of language codes
- **Lexicon Integration**: Automatic enhancement system for pronunciation
- **TTS Backends**: Both PyTorch and MLX backends support lexicon enhancement

### Database Schema
- **Profiles**: Language field supports all ISO 639-1 and custom codes
- **Generations**: Full language tracking for history and analytics
- **Transcriptions**: Multi-language transcription support

## Usage Examples

### Create an Arabic Voice Profile
```bash
curl -X POST http://localhost:8000/profiles \
  -H "Content-Type: application/json" \
  -d '{"name": "صوت عربي", "language": "ar"}'
```

### Generate Hindi Speech
```bash
curl -X POST http://localhost:8000/generate \
  -H "Content-Type: application/json" \
  -d '{
    "profile_id": "uuid",
    "text": "नमस्ते दुनिया!",
    "language": "hi"
  }'
```

### Swahili Transcription
```bash
curl -X POST http://localhost:8000/transcribe \
  -F "file=@audio.wav" \
  -F "language=sw"
```

## Quality Tiers

### Tier 1: Native Qwen3-TTS Support
**Expected Quality**: Excellent
- Chinese, English, Japanese, Korean, German, French, Russian, Portuguese, Spanish, Italian
- Direct model support with optimal pronunciation

### Tier 2: Enhanced with Lexicon
**Expected Quality**: Good to Very Good
- Arabic, Hindi, Swahili, Japanese, Korean, Tagalog, Dutch, Flemish
- Lexicon-enhanced pronunciation with comprehensive coverage

### Tier 3: Basic Support
**Expected Quality**: Fair to Good
- Other major world languages with ISO 639-1 codes
- Model-dependent pronunciation quality

### Tier 4: Experimental Support
**Expected Quality**: Variable
- Regional variants, historical languages, constructed languages
- Quality depends on base model capabilities and training data

## Adding New Languages

To add additional languages:

1. **Frontend**: Add to `app/src/lib/constants/languages.ts`
2. **Backend**: Update validation in `backend/utils/validation.py`
3. **Lexicon**: Create `{language_code}.txt` in `data/lexicons/`
4. **Testing**: Verify profile creation and generation work correctly

## Future Enhancements

- **Automatic Lexicon Generation**: ML-based pronunciation extraction
- **Context-Aware Pronunciation**: Disambiguation of homographs
- **User Custom Lexicons**: Personal pronunciation dictionaries
- **Dialect Detection**: Automatic regional variant identification
- **Quality Assessment**: Automatic pronunciation quality scoring
- **Real-Time Learning**: User feedback integration for improvement

## Language Statistics

- **Total Languages**: 200+
- **Native Support**: 10 languages
- **Lexicon-Enhanced**: 8 languages (growing)
- **Regional Variants**: 15+ variants
- **Writing Systems**: 20+ scripts supported
- **Language Families**: All major families represented

This comprehensive language support makes Eburon Echo one of the most multilingual TTS systems available, enabling voice synthesis and cloning for hundreds of millions of speakers worldwide.
