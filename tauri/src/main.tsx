import React from 'react';
import ReactDOM from 'react-dom/client';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
// import { ReactQueryDevtools } from '@tanstack/react-query-devtools';
import App from '@app/App';
// Import CSS from app directory using explicit alias so Tailwind can scan shared source files
import '@app/index.css';
import { PlatformProvider } from '@app/platform/PlatformContext';
import { tauriPlatform } from '@tauri/platform';

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
      <PlatformProvider platform={tauriPlatform}>
        <App />
        {/* <ReactQueryDevtools initialIsOpen={false} /> */}
      </PlatformProvider>
    </QueryClientProvider>
  </React.StrictMode>,
);
