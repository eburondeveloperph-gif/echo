import React from 'react';
import ReactDOM from 'react-dom/client';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import App from '@app/App';
import '@app/index.css';
import { PlatformProvider } from '@app/platform/PlatformContext';
import { webPlatform } from '@web/platform';

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      staleTime: 1000 * 60 * 5, // 5 minutes
      gcTime: 1000 * 60 * 10, // 10 minutes
      retry: 1,
      refetchOnWindowFocus: false,
    },
  },
});

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <QueryClientProvider client={queryClient}>
      <PlatformProvider platform={webPlatform}>
        <App />
      </PlatformProvider>
    </QueryClientProvider>
  </React.StrictMode>,
);
