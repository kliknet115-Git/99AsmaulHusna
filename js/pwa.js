// PWA Registration & iOS Safari "Add to Home Screen" Detection

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

  // 2. Detect iOS Safari and Standalone Mode
  const isIOS =
    /iPad|iPhone|iPod/.test(navigator.userAgent) ||
    (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1);

  const isStandalone =
    window.navigator.standalone === true ||
    window.matchMedia('(display-mode: standalone)').matches;

  // Global helper for showing iOS Install Guide Modal
  window.showIOSInstallPrompt = function () {
    const modal = document.getElementById('iosInstallModal');
    if (modal) {
      modal.classList.add('show');
    }
  };

  window.closeIOSInstallPrompt = function (neverShowAgain = false) {
    const modal = document.getElementById('iosInstallModal');
    if (modal) {
      modal.classList.remove('show');
    }
    if (neverShowAgain) {
      localStorage.setItem('pwa-ios-prompt-dismissed', 'true');
    }
  };

  // Capture standard PWA install prompt (Chrome / Android)
  let deferredPrompt;
  window.addEventListener('beforeinstallprompt', (e) => {
    e.preventDefault();
    deferredPrompt = e;
    const btnInstall = document.getElementById('btnInstallApp');
    if (btnInstall) {
      btnInstall.style.display = 'inline-flex';
      btnInstall.addEventListener('click', async () => {
        if (deferredPrompt) {
          deferredPrompt.prompt();
          const { outcome } = await deferredPrompt.userChoice;
          console.log('[PWA] User response:', outcome);
          deferredPrompt = null;
          btnInstall.style.display = 'none';
        }
      });
    }
  });
})();
