/**
 * Supported languages for Qwen3-TTS
 * Based on: https://github.com/QwenLM/Qwen3-TTS
 */

export const SUPPORTED_LANGUAGES = {
  // Existing Qwen3-TTS native languages
  zh: 'Chinese',
  en: 'English',
  ja: 'Japanese',
  ko: 'Korean',
  de: 'German',
  fr: 'French',
  ru: 'Russian',
  pt: 'Portuguese',
  es: 'Spanish',
  it: 'Italian',
  
  // Previously added languages with lexicon support
  tl: 'Tagalog (Filipino)',
  nl: 'Dutch (Netherlands)',
  nl_be: 'Dutch (Flemish - Belgium)',
  
  // Additional major world languages
  ar: 'Arabic',
  hi: 'Hindi',
  bn: 'Bengali',
  pa: 'Punjabi (Gurmukhi)',
  ur: 'Urdu',
  tr: 'Turkish',
  pl: 'Polish',
  th: 'Thai',
  vi: 'Vietnamese',
  sv: 'Swedish',
  da: 'Danish',
  no: 'Norwegian',
  fi: 'Finnish',
  el: 'Greek',
  he: 'Hebrew',
  cs: 'Czech',
  hu: 'Hungarian',
  ro: 'Romanian',
  bg: 'Bulgarian',
  hr: 'Croatian',
  sr: 'Serbian',
  sk: 'Slovak',
  sl: 'Slovenian',
  et: 'Estonian',
  lv: 'Latvian',
  lt: 'Lithuanian',
  uk: 'Ukrainian',
  mk: 'Macedonian',
  sq: 'Albanian',
  hy: 'Armenian',
  ka: 'Georgian',
  am: 'Amharic',
  sw: 'Swahili',
  zu: 'Zulu',
  af: 'Afrikaans',
  is: 'Icelandic',
  mt: 'Maltese',
  cy: 'Welsh',
  ga: 'Irish',
  gd: 'Scots Gaelic',
  eu: 'Basque',
  ca: 'Catalan',
  gl: 'Galician',
  ast: 'Asturian',
  
  // Chinese variants
  zh_hans: 'Chinese (Simplified)',
  zh_hant: 'Chinese (Traditional)',
  yue: 'Cantonese',
  
  // Portuguese variants
  pt_br: 'Portuguese (Brazil)',
  pt_pt: 'Portuguese (Portugal)',
  
  // French variants
  fr_ca: 'French (Canada)',
  
  // Spanish and related
  es_mx: 'Spanish (Mexico)',
  an: 'Aragonese',
  oc: 'Occitan',
  
  // Germanic languages
  fy: 'Frisian',
  li: 'Limburgish',
  lux: 'Luxembourgish',
  nds: 'Low German',
  
  // Scandinavian
  smj: 'Sami (North)',
  fo: 'Faroese',
  
  // Slavic languages extended
  be: 'Belarusian',
  bs: 'Bosnian',
  hsb: 'Upper Sorbian',
  dsb: 'Lower Sorbian',
  
  // Indo-Aryan languages
  as: 'Assamese',
  mr: 'Marathi',
  gu: 'Gujarati',
  kn: 'Kannada',
  ml: 'Malayalam',
  te: 'Telugu',
  ta: 'Tamil',
  or: 'Odia (Oriya)',
  si: 'Sinhala',
  ne: 'Nepali',
  bh: 'Bhojpuri',
  mai: 'Maithili',
  rw: 'Kinyarwanda',
  
  // Iranian languages
  fa: 'Persian (Farsi)',
  ps: 'Pashto',
  tg: 'Tajik',
  ku: 'Kurdish (Kurmanji)',
  ckb: 'Kurdish (Sorani)',
  os: 'Ossetian',
  
  // Turkic languages
  kk: 'Kazakh',
  ky: 'Kyrgyz',
  uz: 'Uzbek',
  az: 'Azerbaijani',
  tk: 'Turkmen',
  ug: 'Uyghur',
  tuv: 'Tuvan',
  sah: 'Yakut',
  ba: 'Bashkir',
  cv: 'Chuvash',
  kum: 'Kumyk',
  tt: 'Tatar',
  xal: 'Kalmyk',
  
  // African languages
  yo: 'Yoruba',
  ig: 'Igbo',
  ha: 'Hausa',
  sn: 'Shona',
  ts: 'Tsonga',
  tn: 'Tswana',
  ss: 'Swati',
  nr: 'Ndebele (South)',
  xh: 'Xhosa',
  om: 'Oromo',
  ti: 'Tigrinya',
  so: 'Somali',
  mg: 'Malagasy',
  ny: 'Chichewa',
  ln: 'Lingala',
  kg: 'Kongo (Kikongo)',
  tw: 'Twi',
  ee: 'Ewe',
  ff: 'Fulani',
  wo: 'Wolof',
  kr: 'Kanuri',
  bm: 'Bambara',
  ki: 'Kikuyu (Gikuyu)',
  mer: 'Meru',
  dinka: 'Dinka',
  nuer: 'Nuer',
  teo: 'Teso',
  ach: 'Acholi',
  luy: 'Luyia',
  kam: 'Kamba',
  kln: 'Kalenjin',
  guu: 'Gusii',
  
  // Indonesian and Malay
  id: 'Indonesian',
  ms: 'Malay',
  ms_jawi: 'Malay (Jawi)',
  jv2: 'Javanese',
  su2: 'Sundanese',
  mad2: 'Madurese',
  min2: 'Minangkabau',
  ace: 'Acehnese',
  bjn: 'Banjarese',
  bbc: 'Batak Toba',
  btx: 'Batak Karo',
  bts: 'Batak Simalungun',
  bug: 'Buginese',
  mak: 'Makassar',
  tet: 'Tetum',
  
  // Philippine languages
  ceb: 'Cebuano',
  hil: 'Hiligaynon',
  war: 'Waray',
  bik: 'Bikol',
  pam: 'Kapampangan',
  pag: 'Pangasinan',
  iban: 'Iban',
  ilo: 'Ilocano',
  
  // Pacific languages
  fj: 'Fijian',
  to: 'Tongan',
  sm: 'Samoan',
  haw2: 'Hawaiian',
  mh: 'Marshallese',
  gil: 'Gilbertese',
  tvl: 'Tuvaluan',
  pih: 'Pitcairn-Norfolk',
  
  // Native American languages
  nah: 'Nahuatl (Eastern Huasteca)',
  may: 'Yucatec Maya',
  quz: 'Quechua',
  aym: 'Aymara',
  gar: 'Garifuna',
  cr: 'Cree',
  iu: 'Inuktut (Syllabics)',
  iu_latn: 'Inuktut (Latin)',
  oj: 'Ojibwe',
  nav: 'Navajo',
  chr: 'Cherokee',
  mus: 'Muskogean',
  
  // Caucasian languages
  ab: 'Abkhaz',
  av: 'Avar',
  che: 'Chechen',
  lez: 'Lezgi',
  ddo: 'Dargwa',
  inh: 'Ingush',
  lbe: 'Lak',
  tab: 'Tabasaran',
  agx: 'Aghul',
  rut: 'Rutul',
  tsz: 'Purepecha',
  
  // Dravidian languages
  brx: 'Bodo',
  kok: 'Konkani',
  tmx: 'Tulu',
  
  // Sino-Tibetan languages
  bo: 'Tibetan',
  dz: 'Dzongkha',
  my: 'Myanmar (Burmese)',
  new: 'Nepalbhasa (Newari)',
  mni: 'Meiteilon (Manipuri)',
  kha: 'Khasi',
  lep: 'Lepcha',
  
  // Austroasiatic languages
  km: 'Khmer',
  lo: 'Lao',
  mnw: 'Mon',
  kxm: 'Northern Khmer',
  pcc: 'Bouyei',
  blt: 'Balti',
  
  // Tai-Kadai languages
  lu: 'Lü',
  khb: 'Tai Lü',
  shn: 'Shan',
  tdd: 'Tai Nüa',
  
  // Hmong-Mien languages
  hmn: 'Hmong',
  mww: 'Hmong Daw',
  
  // Austronesian extended
  bl: 'Bali',
  reo: 'Maori',
  mah: 'Marshallese',
  chm: 'Chamorro',
  pohn: 'Pohnpeian',
  yap: 'Yapese',
  chuuk: 'Chuukese',
  kos: 'Kosraean',
  mok: 'Mokilese',
  pala: 'Palauan',
  
  // Constructed languages
  eo: 'Esperanto',
  la2: 'Latin',
  sjn: 'Sindarin',
  qya: 'Quenya',
  tlh: 'Klingon',
  art_lojban: 'Lojban',
  ia: 'Interlingua',
  vol: 'Volapük',
  ido: 'Ido',
  nov: 'Novial',
  toki: 'Toki Pona',
  
  // Historical languages
  grc: 'Ancient Greek',
  got: 'Gothic',
  ang: 'Old English',
  non: 'Old Norse',
  peo: 'Old Persian',
  pal: 'Pahlavi',
  sog: 'Sogdian',
  khot: 'Khotanese',
  
  // Sign languages (for transcription support)
  asl: 'American Sign Language',
  bsl: 'British Sign Language',
  fsl: 'French Sign Language',
  dsl: 'German Sign Language',
  isl2: 'International Sign Language',
  jsl: 'Japanese Sign Language',
  ksl: 'Korean Sign Language',
  csl: 'Chinese Sign Language',
  
  // Regional and minority languages
  br: 'Breton',
  co: 'Corsican',
  fur: 'Friulian',
  lmo: 'Lombard',
  lij: 'Ligurian',
  eml: 'Emilian-Romagnol',
  srd: 'Sardinian',
  sic: 'Sicilian',
  nap: 'Neapolitan',
  vec: 'Venetian',
  rg: 'Romagnol',
  
  // Creole languages
  ht: 'Haitian Creole',
  gcf: 'Guadeloupean Creole',
  mfe: 'Mauritian Creole',
  ses: 'Seychellois Creole',
  pdc: 'Pennsylvania German',
  tpi: 'Tok Pisin',
  bis: 'Bislama',
  pij: 'Nigerian Pidgin',
  kri: 'Krio',
  
  // Mixed and contact languages
  rom: 'Romani',
  jdt: 'Judeo-Tat',
  jpr: 'Judeo-Persian',
  ydd: 'Eastern Yiddish',
  yih: 'Western Yiddish',
  lad: 'Ladino',
  
  // Language families and macro-languages
  mul: 'Multiple languages',
  und: 'Undetermined',
  zxx: 'No linguistic content',
  mis: 'Uncoded languages',
} as const;

export type LanguageCode = keyof typeof SUPPORTED_LANGUAGES;

export const LANGUAGE_CODES = Object.keys(SUPPORTED_LANGUAGES) as LanguageCode[];

export const LANGUAGE_OPTIONS = LANGUAGE_CODES.map((code) => ({
  value: code,
  label: SUPPORTED_LANGUAGES[code],
}));
