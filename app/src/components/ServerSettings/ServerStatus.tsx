import { Loader2, XCircle } from 'lucide-react';
import { Badge } from '@/components/ui/badge';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { MODEL_DISPLAY_NAMES } from '@/lib/constants/modelAliases';
import { useServerHealth } from '@/lib/hooks/useServer';
import { useServerStore } from '@/stores/serverStore';
import { ModelProgress } from './ModelProgress';

export function ServerStatus() {
  const { data: health, isLoading, error } = useServerHealth();
  const serverUrl = useServerStore((state) => state.serverUrl);

  return (
    <Card>
      <CardHeader>
        <CardTitle>Server Status</CardTitle>
      </CardHeader>
      <CardContent className="space-y-4">
        <div>
          <div className="text-sm text-muted-foreground mb-1">Server URL</div>
          <div className="font-mono text-sm">{serverUrl}</div>
        </div>

        {/* Model download progress */}
        <div className="space-y-2">
          <ModelProgress modelName="qwen-tts-1.7B" displayName={MODEL_DISPLAY_NAMES['qwen-tts-1.7B']} />
          <ModelProgress modelName="qwen-tts-0.6B" displayName={MODEL_DISPLAY_NAMES['qwen-tts-0.6B']} />
          <ModelProgress modelName="whisper-base" displayName={MODEL_DISPLAY_NAMES['whisper-base']} />
          <ModelProgress modelName="whisper-small" displayName={MODEL_DISPLAY_NAMES['whisper-small']} />
          <ModelProgress modelName="whisper-medium" displayName={MODEL_DISPLAY_NAMES['whisper-medium']} />
          <ModelProgress modelName="whisper-large" displayName={MODEL_DISPLAY_NAMES['whisper-large']} />
        </div>

        {isLoading ? (
          <div className="flex items-center gap-2">
            <Loader2 className="h-4 w-4 animate-spin" />
            <span className="text-sm">Checking connection...</span>
          </div>
        ) : error ? (
          <div className="flex items-center gap-2">
            <XCircle className="h-4 w-4 text-destructive" />
            <span className="text-sm text-destructive">Connection failed: {error.message}</span>
          </div>
        ) : health ? (
          <div className="space-y-2">
            <div className="flex items-center gap-2">
              <span className="text-sm">Connected</span>
            </div>
            <div className="flex flex-wrap gap-2">
              <Badge
                variant={health.model_loaded || health.model_downloaded ? 'default' : 'secondary'}
              >
                {health.model_loaded || health.model_downloaded ? 'Model Ready' : 'No Model'}
              </Badge>
              <Badge variant={health.gpu_available ? 'default' : 'secondary'}>
                GPU: {health.gpu_available ? 'Available' : 'Not Available'}
              </Badge>
              {health.vram_used_mb && (
                <Badge variant="outline">VRAM: {health.vram_used_mb.toFixed(0)} MB</Badge>
              )}
            </div>
          </div>
        ) : null}
      </CardContent>
    </Card>
  );
}
