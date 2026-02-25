const QWEN_ALIAS = 'Echo';
const WHISPER_ALIAS = 'Orbit';

export const MODEL_DISPLAY_NAMES: Record<string, string> = {
  'qwen-tts-1.7B': `${QWEN_ALIAS} 1.7B`,
  'qwen-tts-0.6B': `${QWEN_ALIAS} 0.6B`,
  'whisper-base': `${WHISPER_ALIAS} Base`,
  'whisper-small': `${WHISPER_ALIAS} Small`,
  'whisper-medium': `${WHISPER_ALIAS} Medium`,
  'whisper-large': `${WHISPER_ALIAS} Large`,
};

export const TTS_MODEL_ALIAS = QWEN_ALIAS;
export const STT_MODEL_ALIAS = WHISPER_ALIAS;

export function getAliasedModelDisplayName(
  modelName: string,
  fallbackDisplayName?: string,
): string {
  const explicitAlias = MODEL_DISPLAY_NAMES[modelName];
  if (explicitAlias) {
    return explicitAlias;
  }

  if (!fallbackDisplayName) {
    return modelName;
  }

  return fallbackDisplayName
    .replace(/Qwen3?-TTS/gi, QWEN_ALIAS)
    .replace(/Qwen\s*TTS/gi, QWEN_ALIAS)
    .replace(/\bQwen\b/gi, QWEN_ALIAS)
    .replace(/\bWhisper\b/gi, WHISPER_ALIAS);
}
