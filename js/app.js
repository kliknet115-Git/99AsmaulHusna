/**
 * ASMAUL HUSNA PWA - MAIN APPLICATION CONTROLLER
 * Mobile-First Progressive Web App Optimized for iPhone / iOS Safari
 */

// Application State
const AppState = {
  currentScreen: 'home',
  previousScreen: 'list',
  currentId: 1,
  activeRange: 'all',
  searchQuery: '',
  favorites: [],
  lastReadId: null,
  theme: 'light',
  tasbihCount: 0,
  tasbihTarget: 33
};

// Storage Helpers
function getStoredJson(key, fallback) {
  try {
    const val = localStorage.getItem(key);
    return val ? JSON.parse(val) : fallback;
  } catch (e) {
    return fallback;
  }
}

function setStoredJson(key, value) {
  try {
    localStorage.setItem(key, JSON.stringify(value));
  } catch (e) {
    console.warn('Storage error:', e);
  }
}

// Initialize Application
document.addEventListener('DOMContentLoaded', () => {
  // Load saved state
  AppState.favorites = getStoredJson('asmaul-favorites', []);
  AppState.lastReadId = Number(localStorage.getItem('asmaul-last-read')) || null;
  AppState.theme = localStorage.getItem('asmaul-theme') || 'light';
  
  applyTheme(AppState.theme);
  setupTouchSwipeGesture();
  setupEventListeners();

  // Check URL parameters (e.g. ?name=5 or ?screen=favorites)
  const urlParams = new URLSearchParams(window.location.search);
  const paramName = urlParams.get('name');
  const paramScreen = urlParams.get('screen');

  if (paramName && !isNaN(paramName)) {
    const id = parseInt(paramName, 10);
    if (id >= 1 && id <= 99) {
      openDetail(id, 'home');
      return;
    }
  }

  if (paramScreen && ['home', 'list', 'favorites', 'about'].includes(paramScreen)) {
    showScreen(paramScreen);
  } else {
    showScreen('home');
  }

  updateHomeMeta();
});

// Setup Global Event Listeners
function setupEventListeners() {
  // Global search input in list screen
  const listSearch = document.getElementById('listSearch');
  if (listSearch) {
    listSearch.addEventListener('input', (e) => {
      AppState.searchQuery = e.target.value.trim();
      renderList();
      toggleClearButton('clearListSearch', AppState.searchQuery.length > 0);
    });
  }

  // Home search input
  const homeSearch = document.getElementById('homeSearch');
  if (homeSearch) {
    homeSearch.addEventListener('input', (e) => {
      const q = e.target.value.trim();
      toggleClearButton('clearHomeSearch', q.length > 0);
    });
    homeSearch.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') {
        executeHomeSearch();
      }
    });
  }

  // Keyboard navigation for detail screen
  window.addEventListener('keydown', (e) => {
    if (AppState.currentScreen === 'detail') {
      if (e.key === 'ArrowLeft') {
        moveDetail(-1);
      } else if (e.key === 'ArrowRight') {
        moveDetail(1);
      } else if (e.key === 'Escape') {
        goBack();
      }
    }
  });
}

// Screen Navigation
function showScreen(screenId) {
  if (screenId === 'detail') return;

  AppState.currentScreen = screenId;

  // Update screens visibility
  document.querySelectorAll('.screen').forEach((el) => {
    el.classList.toggle('active', el.id === screenId);
  });

  // Update bottom nav button states
  document.querySelectorAll('.nav-btn').forEach((btn) => {
    btn.classList.toggle('active', btn.dataset.screen === screenId);
  });

  if (screenId === 'list') {
    renderList();
  } else if (screenId === 'favorites') {
    renderFavorites();
  }

  updateHomeMeta();
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Open Detail View for Asmaul Husna #id
function openDetail(id, from = AppState.currentScreen) {
  if (id < 1 || id > 99) return;

  AppState.previousScreen = from === 'detail' ? AppState.previousScreen : from;
  AppState.currentId = id;
  AppState.lastReadId = id;
  localStorage.setItem('asmaul-last-read', String(id));

  // Reset mini-tasbih for this name
  AppState.tasbihCount = 0;
  updateTasbihUI();

  const item = ASMAUL_HUSNA[id - 1];

  // Update screens
  AppState.currentScreen = 'detail';
  document.querySelectorAll('.screen').forEach((el) => {
    el.classList.toggle('active', el.id === 'detail');
  });

  // Keep current nav highlight reflecting origin
  document.querySelectorAll('.nav-btn').forEach((btn) => {
    btn.classList.toggle('active', btn.dataset.screen === AppState.previousScreen);
  });

  // Back button label
  const backLabel =
    AppState.previousScreen === 'favorites'
      ? 'Favorit'
      : AppState.previousScreen === 'home'
      ? 'Beranda'
      : 'Daftar';
  document.getElementById('detailBackLabel').textContent = backLabel;

  // Populate data
  document.getElementById('detailNumber').textContent = item.number;
  document.getElementById('detailArabic').textContent = item.arabic;
  document.getElementById('detailLatin').textContent = item.latin;
  document.getElementById('detailMeaning').textContent = item.meaning;
  document.getElementById('detailDescription').textContent = item.description;

  const refEl = document.getElementById('detailReference');
  if (item.reference) {
    refEl.innerHTML = `“${escapeHTML(item.arabic)}”<br><strong>${escapeHTML(item.reference)}</strong>`;
  } else {
    refEl.textContent = 'Referensi Al-Qur’an / Hadits';
  }

  // Prev / Next button states
  document.getElementById('prevName').disabled = id === 1;
  document.getElementById('nextName').disabled = id === 99;

  updateFavoriteButtons();
  updateHomeMeta();
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Go Back from Detail Screen
function goBack() {
  if (AppState.previousScreen === 'favorites') {
    showScreen('favorites');
  } else if (AppState.previousScreen === 'home') {
    showScreen('home');
  } else {
    showScreen('list');
  }
}

// Next / Previous Navigation in Detail View
function moveDetail(step) {
  const nextId = AppState.currentId + step;
  if (nextId >= 1 && nextId <= 99) {
    // Add slide transition effect
    const detailCard = document.querySelector('.detail-card');
    if (detailCard) {
      detailCard.style.opacity = '0.5';
      detailCard.style.transform = step > 0 ? 'translateX(10px)' : 'translateX(-10px)';
      setTimeout(() => {
        openDetail(nextId, 'detail');
        detailCard.style.opacity = '1';
        detailCard.style.transform = 'translateX(0)';
      }, 100);
    } else {
      openDetail(nextId, 'detail');
    }
  }
}

// Touch Gestures: Swipe Left for Next, Swipe Right for Previous
function setupTouchSwipeGesture() {
  let touchStartX = 0;
  let touchStartY = 0;
  let touchEndX = 0;
  let touchEndY = 0;

  const detailScreen = document.getElementById('detail');
  if (!detailScreen) return;

  detailScreen.addEventListener(
    'touchstart',
    (e) => {
      touchStartX = e.changedTouches[0].screenX;
      touchStartY = e.changedTouches[0].screenY;
    },
    { passive: true }
  );

  detailScreen.addEventListener(
    'touchend',
    (e) => {
      touchEndX = e.changedTouches[0].screenX;
      touchEndY = e.changedTouches[0].screenY;
      handleSwipe();
    },
    { passive: true }
  );

  function handleSwipe() {
    const deltaX = touchEndX - touchStartX;
    const deltaY = touchEndY - touchStartY;

    // Only recognize horizontal swipe if X distance > 50 and dominant over Y
    if (Math.abs(deltaX) > 60 && Math.abs(deltaX) > Math.abs(deltaY) * 1.5) {
      if (deltaX < 0) {
        // Swiped Left -> Next name
        moveDetail(1);
      } else {
        // Swiped Right -> Previous name
        moveDetail(-1);
      }
    }
  }
}

// Filter Range in List
function setRange(range, btn) {
  AppState.activeRange = range;
  document.querySelectorAll('.filter-chip').forEach((el) => {
    el.classList.toggle('active', el === btn);
  });
  renderList();
}

// Matches query
function matchesQuery(item, query) {
  if (!query) return true;
  const q = query.toLowerCase();
  return (
    String(item.number).includes(q) ||
    item.latin.toLowerCase().includes(q) ||
    item.arabic.toLowerCase().includes(q) ||
    item.meaning.toLowerCase().includes(q) ||
    item.description.toLowerCase().includes(q)
  );
}

// Render 99 Asmaul Husna List
function renderList() {
  const container = document.getElementById('nameList');
  if (!container) return;

  const q = AppState.searchQuery;
  const filtered = ASMAUL_HUSNA.filter((item) => {
    let rangeOk = true;
    if (AppState.activeRange === '1') rangeOk = item.number <= 33;
    else if (AppState.activeRange === '2') rangeOk = item.number >= 34 && item.number <= 66;
    else if (AppState.activeRange === '3') rangeOk = item.number >= 67 && item.number <= 99;

    return rangeOk && matchesQuery(item, q);
  });

  const listMeta = document.getElementById('listMeta');
  if (listMeta) {
    listMeta.textContent = `${filtered.length} dari 99 nama ditampilkan`;
  }

  if (filtered.length === 0) {
    container.innerHTML = `
      <div class="empty-state">
        <div class="empty-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="11" cy="11" r="7"/><path d="m20 20-4-4"/>
          </svg>
        </div>
        <h3>Nama tidak ditemukan</h3>
        <p>Coba kata kunci pencarian lain seperti arti, transliterasi Latin, atau nomor.</p>
      </div>`;
    return;
  }

  container.innerHTML = filtered.map(generateCardHTML).join('');
}

// Render Card HTML
function generateCardHTML(item) {
  const isFav = AppState.favorites.includes(item.number);
  const isLong = item.arabic.length > 15;

  let arabicDisplay = escapeHTML(item.arabic);
  if (item.number === 85) {
    arabicDisplay = 'ذُو الْجَلَالِ<br>وَالْإِكْرَامِ';
  } else if (item.number === 84) {
    arabicDisplay = 'مَالِكُ الْـمُلْكِ';
  }

  return `
    <button class="name-card ${isLong ? 'is-long' : ''}" onclick="openDetail(${item.number})" aria-label="Nama ${item.number}: ${item.latin}">
      <span class="number-badge">${item.number}</span>
      <span class="card-arabic ${isLong ? 'is-long' : ''}" lang="ar" dir="rtl">${arabicDisplay}</span>
      <div class="card-info">
        <span class="card-latin">
          ${escapeHTML(item.latin)}
          ${isFav ? '<span class="fav-heart-icon">♥</span>' : ''}
        </span>
        <span class="card-meaning">${escapeHTML(item.meaning)}</span>
      </div>
      <svg class="card-arrow" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <path d="m9 18 6-6-6-6" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
    </button>
  `;
}

// Render Favorites List
function renderFavorites() {
  const container = document.getElementById('favoriteList');
  if (!container) return;

  const favItems = ASMAUL_HUSNA.filter((item) => AppState.favorites.includes(item.number));

  if (favItems.length === 0) {
    container.innerHTML = `
      <div class="empty-state">
        <div class="empty-icon" style="color:#e11d48;background:#ffe4e6;">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1.1-1.1a5.5 5.5 0 0 0-7.8 7.8l1.1 1.1L12 21l7.8-7.5 1.1-1.1a5.5 5.5 0 0 0-.1-7.8Z"/>
          </svg>
        </div>
        <h3>Belum ada nama favorit</h3>
        <p>Buka detail nama Asmaul Husna lalu ketuk ikon hati untuk menambahkannya ke koleksi pribadi Anda.</p>
        <button class="primary-action" style="max-width:200px;margin:18px auto 0;" onclick="showScreen('list')">
          Jelajahi 99 Nama
        </button>
      </div>`;
    return;
  }

  container.innerHTML = favItems.map(generateCardHTML).join('');
}

// Favorite Management
function toggleFavorite() {
  const id = AppState.currentId;
  const idx = AppState.favorites.indexOf(id);

  if (idx > -1) {
    AppState.favorites.splice(idx, 1);
    showToast('Dihapus dari favorit');
  } else {
    AppState.favorites.push(id);
    showToast('Ditambahkan ke favorit ♥');
    triggerHaptic();
  }

  setStoredJson('asmaul-favorites', AppState.favorites);
  updateFavoriteButtons();
  updateHomeMeta();

  if (AppState.currentScreen === 'favorites') {
    renderFavorites();
  }
}

function updateFavoriteButtons() {
  const isFav = AppState.favorites.includes(AppState.currentId);
  const topBtn = document.getElementById('detailFavoriteTop');
  const bottomBtn = document.getElementById('detailFavoriteButton');

  if (topBtn) {
    topBtn.style.color = isFav ? '#e11d48' : 'var(--navy)';
    topBtn.setAttribute('aria-label', isFav ? 'Hapus favorit' : 'Tambah favorit');
  }

  if (bottomBtn) {
    bottomBtn.classList.toggle('is-favorite', isFav);
  }
}

// Mini Tasbih / Dzikir Feature in Detail View
function incrementTasbih() {
  AppState.tasbihCount++;
  triggerHaptic();

  // If reached target, celebrate with toast & vibration pattern
  if (AppState.tasbihCount === AppState.tasbihTarget) {
    showToast(`Alhamdulillah, tercapai ${AppState.tasbihTarget}x! 🎉`);
    if ('vibrate' in navigator) {
      navigator.vibrate([40, 60, 40]);
    }
  }

  updateTasbihUI();
}

function resetTasbih() {
  AppState.tasbihCount = 0;
  updateTasbihUI();
  showToast('Hitungan dzikir direset');
}

function changeTasbihTarget(val) {
  AppState.tasbihTarget = parseInt(val, 10);
  AppState.tasbihCount = 0;
  updateTasbihUI();
}

function updateTasbihUI() {
  const countEl = document.getElementById('tasbihCount');
  if (countEl) {
    countEl.textContent = AppState.tasbihCount;
  }
}

// Home Quick Search
function executeHomeSearch() {
  const input = document.getElementById('homeSearch');
  if (!input) return;
  const query = input.value.trim();
  if (query) {
    AppState.searchQuery = query;
    const listInput = document.getElementById('listSearch');
    if (listInput) listInput.value = query;
    showScreen('list');
    renderList();
  }
}

function clearSearch(inputId, btnId) {
  const input = document.getElementById(inputId);
  if (input) {
    input.value = '';
    AppState.searchQuery = '';
    renderList();
  }
  toggleClearButton(btnId, false);
}

function toggleClearButton(btnId, show) {
  const btn = document.getElementById(btnId);
  if (btn) {
    btn.classList.toggle('show', show);
  }
}

function openLastRead() {
  if (AppState.lastReadId) {
    openDetail(AppState.lastReadId, 'home');
  } else {
    showToast('Belum ada riwayat membaca. Membuka nama pertama.');
    openDetail(1, 'home');
  }
}

function updateHomeMeta() {
  const favCountEl = document.getElementById('homeFavCount');
  if (favCountEl) {
    favCountEl.textContent = `${AppState.favorites.length} nama tersimpan`;
  }

  const lastReadEl = document.getElementById('lastReadText');
  if (lastReadEl) {
    if (AppState.lastReadId && ASMAUL_HUSNA[AppState.lastReadId - 1]) {
      const item = ASMAUL_HUSNA[AppState.lastReadId - 1];
      lastReadEl.textContent = `${item.number}. ${item.latin}`;
    } else {
      lastReadEl.textContent = 'Mulai membaca';
    }
  }
}

// Audio Pronunciation & Melodic Chime
function playPronunciation() {
  triggerHaptic();
  const currentItem = ASMAUL_HUSNA[AppState.currentId - 1];
  if (!currentItem) return;

  // Try Web Speech Synthesis first
  if ('speechSynthesis' in window) {
    window.speechSynthesis.cancel(); // Stop any pending utterance

    const utterance = new SpeechSynthesisUtterance(currentItem.arabic);
    utterance.lang = 'ar-SA';
    utterance.rate = 0.85; // Slightly slower, respectful recitation pace

    // Try finding Arabic voice
    const voices = window.speechSynthesis.getVoices();
    const arabicVoice = voices.find((v) => v.lang.startsWith('ar') || v.name.includes('Arabic'));
    if (arabicVoice) {
      utterance.voice = arabicVoice;
    }

    utterance.onstart = () => {
      showToast(`Mendengarkan: ${currentItem.latin}`);
    };

    utterance.onerror = () => {
      playHarmonicChime();
    };

    window.speechSynthesis.speak(utterance);
  } else {
    playHarmonicChime();
    showToast(`Pelafalan: ${currentItem.latin}`);
  }
}

// Gentle Web Audio API Harmonic Chime Fallback
function playHarmonicChime() {
  try {
    const AudioContext = window.AudioContext || window.webkitAudioContext;
    if (!AudioContext) return;

    const ctx = new AudioContext();
    const osc = ctx.createOscillator();
    const gain = ctx.createGain();

    osc.type = 'sine';
    osc.frequency.setValueAtTime(528, ctx.currentTime); // 528 Hz soothing Solfeggio frequency
    osc.frequency.exponentialRampToValueAtTime(660, ctx.currentTime + 0.3);

    gain.gain.setValueAtTime(0.2, ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.8);

    osc.connect(gain);
    gain.connect(ctx.destination);

    osc.start();
    osc.stop(ctx.currentTime + 0.8);
  } catch (e) {
    // Audio context restricted or muted
  }
}

// Native Share API
async function shareCurrent() {
  const item = ASMAUL_HUSNA[AppState.currentId - 1];
  if (!item) return;

  const shareData = {
    title: `Asmaul Husna: ${item.latin}`,
    text: `✨ Asmaul Husna #${item.number}\n\n${item.arabic}\n${item.latin}\nArtinya: "${item.meaning}"\n\n${item.description}\n\nDalil: ${item.reference}\n\nDibagikan melalui Web App Asmaul Husna`,
    url: window.location.href.split('?')[0] + `?name=${item.number}`
  };

  try {
    if (navigator.share) {
      await navigator.share(shareData);
    } else {
      await navigator.clipboard.writeText(shareData.text);
      showToast('Teks nama Allah berhasil disalin!');
    }
  } catch (err) {
    if (err.name !== 'AbortError') {
      try {
        await navigator.clipboard.writeText(shareData.text);
        showToast('Teks nama Allah disalin ke clipboard');
      } catch {
        showToast('Fitur bagikan tidak didukung peramban ini');
      }
    }
  }
}

// Theme Toggle (Light / Dark)
function toggleTheme() {
  const nextTheme = AppState.theme === 'light' ? 'dark' : 'light';
  applyTheme(nextTheme);
  showToast(`Tema ${nextTheme === 'dark' ? 'Gelap' : 'Terang'} aktif`);
}

function applyTheme(theme) {
  AppState.theme = theme;
  localStorage.setItem('asmaul-theme', theme);
  document.documentElement.setAttribute('data-theme', theme);

  // Update theme meta color for Safari address bar
  const themeMeta = document.getElementById('metaThemeColor');
  if (themeMeta) {
    themeMeta.content = theme === 'dark' ? '#09111c' : '#17365d';
  }

  // Update toggle button icon
  const themeIcon = document.getElementById('themeToggleIcon');
  if (themeIcon) {
    themeIcon.innerHTML =
      theme === 'dark'
        ? '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="4"/><path d="M12 2v2m0 16v2M4.93 4.93l1.41 1.41m11.32 11.32 1.41 1.41M2 12h2m16 0h2M6.34 17.66l-1.41 1.41m14.14-14.14-1.41 1.41"/></svg>'
        : '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>';
  }
}

// Haptic Vibration helper
function triggerHaptic() {
  if ('vibrate' in navigator) {
    navigator.vibrate(15);
  }
}

// Toast notification
let toastTimer;
function showToast(message) {
  const toast = document.getElementById('toast');
  if (!toast) return;

  toast.textContent = message;
  toast.classList.add('show');

  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => {
    toast.classList.remove('show');
  }, 2200);
}

// HTML Escaping Utility
function escapeHTML(str) {
  return String(str).replace(/[&<>"']/g, (c) => ({
    '&': '&amp;',
    '<': '&lt;',
    '>': '&gt;',
    '"': '&quot;',
    "'": '&#39;'
  }[c]));
}
