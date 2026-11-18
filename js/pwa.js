// PWA Registration & Service Worker Activation

(function () {
  // 1. Register Service Worker
  if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
      navigator.serviceWorker
        .register('./sw.js')
        .then((registration) => {
          console.log('[PWA] Service Worker terdaftar dengan scope:', registration.scope);
        })
        .catch((error) => {
          console.error('[PWA] Pendaftaran Service Worker gagal:', error);
        });
    });
  }

  // 2. Standard PWA install prompt handler (Chrome / Android)
  let deferredPrompt;
  window.addEventListener('beforeinstallprompt', (e) => {
    e.preventDefault();
    deferredPrompt = e;
  });
})();
