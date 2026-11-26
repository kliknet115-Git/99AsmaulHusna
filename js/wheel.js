/**
 * ASMAUL HUSNA 99 RADIAL READER (RODA 99 SEGMEN)
 * Mathematical SVG Generator & Interactive Auto-Playback Engine
 * Mobile-First Optimized for iPhone Safari PWA
 */

const WheelController = (() => {
  // State
  const state = {
    data: [],
    currentId: 1,
    isPlaying: false,
    duration: 2, // seconds per name (1, 2, 3, 5)
    loop: false, // repeat after 99
    soundEnabled: true,
    timer: null,
    progressInterval: null,
    stepStartTime: 0,
    isInitialized: false,
    audioCtx: null
  };

  // Audio Chime using Web Audio API (gentle, peaceful sine chime)
  function playSoftChime() {
    if (!state.soundEnabled) return;
    try {
      if (!state.audioCtx) {
        const AudioContext = window.AudioContext || window.webkitAudioContext;
        if (!AudioContext) return;
        state.audioCtx = new AudioContext();
      }
      if (state.audioCtx.state === 'suspended') {
        state.audioCtx.resume();
      }
      const osc = state.audioCtx.createOscillator();
      const gain = state.audioCtx.createGain();
      osc.type = 'sine';
      // Harmonic pleasant frequencies (528Hz Solfeggio / calm)
      osc.frequency.setValueAtTime(528, state.audioCtx.currentTime);
      gain.gain.setValueAtTime(0.04, state.audioCtx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.0001, state.audioCtx.currentTime + 0.5);
      osc.connect(gain);
      gain.connect(state.audioCtx.destination);
      osc.start();
      osc.stop(state.audioCtx.currentTime + 0.52);
    } catch (e) {
      // Audio context might be restricted before user gesture
    }
  }

  // Math utility: Polar to Cartesian coordinates
  function polarToCartesian(cx, cy, r, angleDeg) {
    const rad = (angleDeg * Math.PI) / 180.0;
    return {
      x: cx + r * Math.cos(rad),
      y: cy + r * Math.sin(rad)
    };
  }

  // Initialize Controller
  async function init() {
    if (state.isInitialized) return;

    // Load data from data/asmaul-husna.json or fallback to window.ASMAUL_HUSNA
    try {
      const res = await fetch('./data/asmaul-husna.json');
      if (res.ok) {
        state.data = await res.json();
      } else {
        throw new Error('Fallback to data.js');
      }
    } catch (e) {
      if (typeof ASMAUL_HUSNA !== 'undefined' && Array.isArray(ASMAUL_HUSNA)) {
        state.data = ASMAUL_HUSNA.map(item => ({
          number: item.number,
          slug: item.slug || '',
          arabic: item.arabic,
          transliteration: item.transliteration || item.latin || '',
          meaning: item.meaning,
          description: item.description || '',
          references: item.reference ? [item.reference] : (item.references || []),
          verification_status: 'verified'
        }));
      }
    }

    if (!state.data || state.data.length === 0) {
      console.error('Data Asmaul Husna tidak ditemukan');
      return;
    }

    // Load saved preferences
    const savedDuration = localStorage.getItem('asmaul-wheel-duration');
    if (savedDuration) {
      const parsed = parseInt(savedDuration, 10);
      if ([1, 2, 3, 5].includes(parsed)) {
        state.duration = parsed;
      } else {
        state.duration = 2;
      }
    }

    const savedLoop = localStorage.getItem('asmaul-wheel-loop');
    if (savedLoop !== null) state.loop = savedLoop === 'true';

    const savedSound = localStorage.getItem('asmaul-wheel-sound');
    if (savedSound !== null) state.soundEnabled = savedSound === 'true';

    const lastRead = Number(localStorage.getItem('asmaul-last-read')) || 1;
    state.currentId = lastRead >= 1 && lastRead <= 99 ? lastRead : 1;

    renderSVGWheel();
    setupDOMEventListeners();
    updateUI(state.currentId, false);
    updateControlsUI();

    state.isInitialized = true;
  }

  // Generate SVG with 99 mathematical annular wedges and radial numbers
  function renderSVGWheel() {
    const svgEl = document.getElementById('wheelSvg');
    if (!svgEl) return;

    const total = 99;
    const cx = 250;
    const cy = 250;
    const rOut = 242;
    const rIn = 168;
    const rText = 205;
    const step = 360.0 / total;

    let svgInner = `
      <defs>
        <!-- Gradients & Drop Shadows -->
        <linearGradient id="activeWedgeGrad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#3b82f6" />
          <stop offset="100%" stop-color="#1d4ed8" />
        </linearGradient>
        <radialGradient id="ringBgGrad" cx="50%" cy="50%" r="50%">
          <stop offset="65%" stop-color="#ffffff" />
          <stop offset="100%" stop-color="#f0f5fc" />
        </radialGradient>
        <filter id="activeShadow" x="-20%" y="-20%" width="140%" height="140%">
          <feDropShadow dx="0" dy="2" stdDeviation="3.5" flood-color="#1d4ed8" flood-opacity="0.45" />
        </filter>
      </defs>

      <!-- Background guide rings -->
      <circle cx="${cx}" cy="${cy}" r="${rOut}" class="wheel-guide-outer" />
      <circle cx="${cx}" cy="${cy}" r="${rIn}" class="wheel-guide-inner" />
      <g id="wheelSegmentsGroup" role="listbox" aria-label="99 Segmen Asmaul Husna">
    `;

    for (let i = 1; i <= total; i++) {
      // Starting from 12 o'clock (-90 deg), going clockwise
      const a1 = -90.0 + (i - 1) * step;
      const a2 = -90.0 + i * step;
      const aMid = (a1 + a2) / 2.0;

      const p1 = polarToCartesian(cx, cy, rOut, a1);
      const p2 = polarToCartesian(cx, cy, rOut, a2);
      const p3 = polarToCartesian(cx, cy, rIn, a2);
      const p4 = polarToCartesian(cx, cy, rIn, a1);

      // Annular wedge path: outer arc -> line to inner -> inner arc back -> close
      const d = `M ${p1.x.toFixed(2)} ${p1.y.toFixed(2)} A ${rOut} ${rOut} 0 0 1 ${p2.x.toFixed(2)} ${p2.y.toFixed(2)} L ${p3.x.toFixed(2)} ${p3.y.toFixed(2)} A ${rIn} ${rIn} 0 0 0 ${p4.x.toFixed(2)} ${p4.y.toFixed(2)} Z`;

      // Text position & rotation
      const tPos = polarToCartesian(cx, cy, rText, aMid);
      let rot = aMid + 90.0;
      // Invert lower numbers so they remain readable right-side up
      if (aMid > 0 && aMid < 180) {
        rot += 180.0;
      }

      svgInner += `
        <g class="wheel-segment-group" id="wheelGroup-${i}" data-id="${i}" role="option" aria-label="Nomor ${i}" tabindex="0">
          <path id="wheelSeg-${i}" class="wheel-segment" d="${d}" />
          <text id="wheelText-${i}" class="wheel-segment-text" x="${tPos.x.toFixed(2)}" y="${tPos.y.toFixed(2)}"
            transform="rotate(${rot.toFixed(2)}, ${tPos.x.toFixed(2)}, ${tPos.y.toFixed(2)})">${i}</text>
        </g>
      `;
    }

    svgInner += `</g>`;
    svgEl.innerHTML = svgInner;

    // Attach click & keydown handlers to each segment
    for (let i = 1; i <= total; i++) {
      const g = document.getElementById(`wheelGroup-${i}`);
      if (g) {
        g.addEventListener('click', (e) => {
          e.stopPropagation();
          selectName(i, true);
        });
        g.addEventListener('keydown', (e) => {
          if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            selectName(i, true);
          }
        });
      }
    }
  }

  // Setup DOM Event Listeners
  function setupDOMEventListeners() {
    // Scrubber input slider
    const scrubber = document.getElementById('wheelScrubber');
    if (scrubber) {
      scrubber.addEventListener('input', (e) => {
        const val = parseInt(e.target.value, 10);
        if (val >= 1 && val <= 99) {
          selectName(val, true);
        }
      });
    }

    // Keyboard navigation when wheel / home screen is active
    window.addEventListener('keydown', (e) => {
      if (AppState.currentScreen === 'home' || AppState.currentScreen === 'wheel') {
        if (e.key === 'ArrowLeft') {
          prev();
        } else if (e.key === 'ArrowRight') {
          next();
        } else if (e.key === ' ' && e.target.tagName !== 'BUTTON' && e.target.tagName !== 'INPUT') {
          e.preventDefault();
          togglePlay();
        }
      }
    });
  }

  // Select name by ID (1–99)
  function selectName(id, manual = false) {
    if (id < 1) id = 1;
    if (id > 99) id = 99;

    const previousId = state.currentId;
    state.currentId = id;

    // Update highlight on SVG segments
    if (previousId && previousId !== id) {
      const prevSeg = document.getElementById(`wheelSeg-${previousId}`);
      const prevText = document.getElementById(`wheelText-${previousId}`);
      const prevGroup = document.getElementById(`wheelGroup-${previousId}`);
      if (prevSeg) prevSeg.classList.remove('active');
      if (prevText) prevText.classList.remove('active');
      if (prevGroup) prevGroup.setAttribute('aria-selected', 'false');
    }

    const curSeg = document.getElementById(`wheelSeg-${id}`);
    const curText = document.getElementById(`wheelText-${id}`);
    const curGroup = document.getElementById(`wheelGroup-${id}`);
    if (curSeg) curSeg.classList.add('active');
    if (curText) curText.classList.add('active');
    if (curGroup) {
      curGroup.setAttribute('aria-selected', 'true');
    }

    // Update central panel and UI
    updateUI(id, manual);

    // Save as last read
    localStorage.setItem('asmaul-last-read', String(id));
    AppState.lastReadId = id;
    if (typeof updateHomeMeta === 'function') updateHomeMeta();

    // Play subtle chime on change
    playSoftChime();

    // If manual change happened while auto-playing, reset current step timer gracefully
    if (manual && state.isPlaying) {
      resetStepTimer();
    }
  }

  // Update center panel and controls UI
  function updateUI(id, isManual) {
    if (!state.data || state.data.length < id) return;
    const item = state.data[id - 1];

    // Center card elements
    const centerNumber = document.getElementById('wheelCenterNumber');
    const centerArabic = document.getElementById('wheelCenterArabic');
    const centerLatin = document.getElementById('wheelCenterLatin');
    const centerMeaning = document.getElementById('wheelCenterMeaning');
    const favBtn = document.getElementById('wheelFavBtn');

    if (centerNumber) centerNumber.textContent = `${item.number} / 99`;
    if (centerArabic) {
      centerArabic.textContent = item.arabic;
      centerArabic.classList.toggle('is-compact', item.number === 85);
    }
    if (centerLatin) centerLatin.textContent = item.transliteration;
    if (centerMeaning) centerMeaning.textContent = item.meaning;

    // Update favorite button state
    if (favBtn) {
      const isFav = AppState.favorites.includes(item.number);
      favBtn.classList.toggle('active', isFav);
      favBtn.innerHTML = isFav
        ? `<svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" stroke="currentColor" stroke-width="1.5"><path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1.1-1.1a5.5 5.5 0 0 0-7.8 7.8l1.1 1.1L12 21l7.8-7.5 1.1-1.1a5.5 5.5 0 0 0-.1-7.8Z"/></svg>`
        : `<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1.1-1.1a5.5 5.5 0 0 0-7.8 7.8l1.1 1.1L12 21l7.8-7.5 1.1-1.1a5.5 5.5 0 0 0-.1-7.8Z"/></svg>`;
    }

    // Update scrubber slider & progress text
    const scrubber = document.getElementById('wheelScrubber');
    if (scrubber) scrubber.value = id;

    const progressLabel = document.getElementById('wheelProgressLabel');
    if (progressLabel) {
      progressLabel.textContent = `Nama ke-${id} dari 99`;
    }

    // Update Prev / Next button states
    const btnPrev = document.getElementById('wheelBtnPrev');
    const btnNext = document.getElementById('wheelBtnNext');
    if (btnPrev) btnPrev.disabled = id === 1;
    if (btnNext) btnNext.disabled = id === 99;
  }

  // Update controls and settings indicators
  function updateControlsUI() {
    // Play/Pause button
    const playBtn = document.getElementById('wheelPlayBtn');
    if (playBtn) {
      playBtn.classList.toggle('is-playing', state.isPlaying);
      playBtn.setAttribute('aria-label', state.isPlaying ? 'Jeda Bacaan' : 'Mulai Baca Otomatis');
      playBtn.innerHTML = state.isPlaying
        ? `<svg width="26" height="26" viewBox="0 0 24 24" fill="currentColor"><rect x="6" y="4" width="4" height="16" rx="1.5"/><rect x="14" y="4" width="4" height="16" rx="1.5"/></svg>`
        : `<svg width="26" height="26" viewBox="0 0 24 24" fill="currentColor"><path d="M7 4.5v15a1 1 0 0 0 1.54.84l11.5-7.5a1 1 0 0 0 0-1.68l-11.5-7.5A1 1 0 0 0 7 4.5Z"/></svg>`;
    }

    // Sound toggle button
    const soundBtn = document.getElementById('wheelSoundBtn');
    if (soundBtn) {
      soundBtn.classList.toggle('active', state.soundEnabled);
      soundBtn.innerHTML = state.soundEnabled
        ? `<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14"/></svg>`
        : `<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><line x1="23" y1="9" x2="17" y2="15"/><line x1="17" y1="9" x2="23" y2="15"/></svg>`;
    }

    // Duration chips
    document.querySelectorAll('.speed-pill').forEach((pill) => {
      const sec = parseInt(pill.dataset.sec, 10);
      pill.classList.toggle('active', sec === state.duration);
    });

    // Loop chip
    const loopBtn = document.getElementById('wheelLoopBtn');
    if (loopBtn) {
      loopBtn.classList.toggle('active', state.loop);
      loopBtn.textContent = state.loop ? 'Ulangi: Aktif (1–99)' : 'Ulangi: Sekali';
    }
  }

  // Playback Engine: Starts auto reading
  function play() {
    if (state.isPlaying) return;

    // If at end (99) and loop is false, start from 1
    if (state.currentId >= 99 && !state.loop) {
      selectName(1, true);
    }

    state.isPlaying = true;
    updateControlsUI();
    resetStepTimer();
    showToast('Mode Baca Otomatis dimulai');
  }

  // Playback Engine: Pauses auto reading
  function pause() {
    if (!state.isPlaying) return;
    state.isPlaying = false;
    clearTimers();
    updateControlsUI();
    resetProgressVisual();
  }

  // Toggle Play / Pause
  function togglePlay() {
    if (state.isPlaying) {
      pause();
    } else {
      play();
    }
  }

  // Previous Name
  function prev() {
    if (state.currentId > 1) {
      selectName(state.currentId - 1, true);
    }
  }

  // Next Name
  function next() {
    if (state.currentId < 99) {
      selectName(state.currentId + 1, true);
    } else if (state.loop) {
      selectName(1, true);
    }
  }

  // Restart to #1
  function restart() {
    selectName(1, true);
    if (state.isPlaying) {
      resetStepTimer();
    }
    showToast('Kembali ke nama ke-1');
  }

  // Auto 1–99 (Starts from 1 and plays)
  function autoAll() {
    selectName(1, true);
    if (!state.isPlaying) {
      play();
    } else {
      resetStepTimer();
    }
    showToast('Memulai Auto Baca 1–99');
  }

  // Reset current step timer using recursive setTimeout (never cumulative setInterval)
  function resetStepTimer() {
    clearTimers();
    state.stepStartTime = Date.now();

    const durationMs = state.duration * 1000;

    // Visual progress fill animation
    const progressBar = document.getElementById('wheelStepProgress');
    if (progressBar) {
      progressBar.style.transition = 'none';
      progressBar.style.width = '0%';
      // Force reflow
      void progressBar.offsetWidth;
      progressBar.style.transition = `width ${state.duration}s linear`;
      progressBar.style.width = '100%';
    }

    // Main step timeout
    state.timer = setTimeout(() => {
      onStepComplete();
    }, durationMs);
  }

  // Step complete handler
  function onStepComplete() {
    if (!state.isPlaying) return;

    if (state.currentId < 99) {
      selectName(state.currentId + 1, false);
      resetStepTimer();
    } else {
      // Reached 99
      if (state.loop) {
        selectName(1, false);
        resetStepTimer();
      } else {
        pause();
        showToast('Selesai membaca 99 Asmaul Husna. Alhamdulillah!');
      }
    }
  }

  // Clear all running timers
  function clearTimers() {
    if (state.timer) {
      clearTimeout(state.timer);
      state.timer = null;
    }
    if (state.progressInterval) {
      clearInterval(state.progressInterval);
      state.progressInterval = null;
    }
  }

  // Reset visual progress bar
  function resetProgressVisual() {
    const progressBar = document.getElementById('wheelStepProgress');
    if (progressBar) {
      progressBar.style.transition = 'none';
      progressBar.style.width = '0%';
    }
  }

  // Set duration per name (1, 2, 3, 5 seconds)
  function setDuration(sec) {
    sec = parseInt(sec, 10);
    if (![1, 2, 3, 5].includes(sec)) return;
    state.duration = sec;
    localStorage.setItem('asmaul-wheel-duration', String(sec));
    updateControlsUI();
    if (state.isPlaying) {
      resetStepTimer();
    }
    showToast(`Durasi baca: ${sec} detik per nama`);
  }

  // Toggle Loop mode
  function toggleLoop() {
    state.loop = !state.loop;
    localStorage.setItem('asmaul-wheel-loop', String(state.loop));
    updateControlsUI();
    showToast(state.loop ? 'Pengulangan 1–99 diaktifkan' : 'Berhenti di nama ke-99');
  }

  // Toggle Sound chime
  function toggleSound() {
    state.soundEnabled = !state.soundEnabled;
    localStorage.setItem('asmaul-wheel-sound', String(state.soundEnabled));
    updateControlsUI();
    if (state.soundEnabled) playSoftChime();
    showToast(state.soundEnabled ? 'Suara lonceng aktif' : 'Suara lonceng dimatikan');
  }

  // Toggle Favorite for currently selected name
  function toggleFavorite() {
    if (typeof window.toggleFavoriteId === 'function') {
      window.toggleFavoriteId(state.currentId);
    } else if (typeof window.toggleFavorite === 'function') {
      const prevId = AppState.currentId;
      AppState.currentId = state.currentId;
      window.toggleFavorite();
      AppState.currentId = prevId;
    }
    updateUI(state.currentId, false);
  }

  // Open Full Detail screen for currently selected name
  function openDetail() {
    pause(); // pause reading when navigating away
    if (typeof window.openDetail === 'function') {
      window.openDetail(state.currentId, 'home');
    }
  }

  // Lifecycle hook: called when navigating away from wheel screen
  function onLeaveScreen() {
    pause();
  }

  // Lifecycle hook: called when entering wheel screen
  function onEnterScreen() {
    if (!state.isInitialized) {
      init();
    } else {
      // Sync with last read if available
      const lastRead = Number(localStorage.getItem('asmaul-last-read')) || state.currentId;
      if (lastRead >= 1 && lastRead <= 99 && lastRead !== state.currentId) {
        selectName(lastRead, false);
      }
    }
  }

  // Public API
  return {
    init,
    selectName,
    play,
    pause,
    togglePlay,
    prev,
    next,
    restart,
    autoAll,
    setDuration,
    toggleLoop,
    toggleSound,
    toggleFavorite,
    openDetail,
    onLeaveScreen,
    onEnterScreen,
    getState: () => ({ ...state })
  };
})();

// Attach to window for HTML event handlers
window.WheelController = WheelController;
