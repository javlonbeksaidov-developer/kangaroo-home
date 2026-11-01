/* Kangaroo Home — login / register logic */
(() => {
  'use strict';

  const form = document.getElementById('authForm');
  if (!form) return;

  const mode = form.dataset.mode; // "login" | "register"
  const scene = document.getElementById('scene');
  const meter = document.getElementById('meter');
  const meterText = document.getElementById('meterText');
  const toastEl = document.getElementById('toast');
  const formError = document.getElementById('formError');
  const formNote = document.getElementById('formNote');
  const btn = form.querySelector('.btn');

  const TOTAL = 6;                  // windows in the house
  const ORDER = [0, 3, 1, 4, 2, 5]; // lighting order
  const USERS_KEY = 'kh_users';
  const SESSION_KEY = 'kh_session';
  const LAST_KEY = 'kh_last_user';

  /* ---------- Scene (SVG) ---------- */
  function skySVG() {
    let seed = 7;
    const rnd = () => (seed = (seed * 16807) % 2147483647) / 2147483647;
    let stars = '';
    for (let i = 0; i < 60; i++) {
      stars += `<circle class="star${i % 5 === 0 ? ' tw' : ''}" cx="${(rnd() * 1440).toFixed(0)}" cy="${(rnd() * 600).toFixed(0)}" r="${(rnd() * 1.4 + 0.5).toFixed(1)}" style="animation-delay:${(rnd() * 4).toFixed(1)}s"/>`;
    }
    const gum = (x, y, s) => `<g transform="translate(${x} ${y}) scale(${s})" fill="#123A2C"><rect x="-3" y="-60" width="6" height="62"/><ellipse cx="0" cy="-66" rx="34" ry="21"/><ellipse cx="20" cy="-80" rx="22" ry="13"/><ellipse cx="-22" cy="-76" rx="20" ry="12"/></g>`;
    return `
<svg class="sky" viewBox="0 0 1440 900" preserveAspectRatio="xMidYMax slice" xmlns="http://www.w3.org/2000/svg">
  <defs><radialGradient id="moonGlow"><stop offset="0" stop-color="#F2FBE9"/><stop offset=".5" stop-color="#DDF2D4"/><stop offset="1" stop-color="#DDF2D4" stop-opacity="0"/></radialGradient></defs>
  ${stars}
  <circle cx="1090" cy="300" r="90" fill="url(#moonGlow)" opacity=".26"/>
  <circle cx="1090" cy="300" r="34" fill="#EAF8E0"/>
  <path d="M0 760 Q300 690 620 745 T1240 735 T1440 750 V900 H0Z" fill="#0F3226"/>
  ${gum(250, 748, 1.15)}${gum(640, 770, .8)}${gum(1010, 760, 1)}${gum(1330, 770, .7)}
</svg>`;
  }

  function houseSVG() {
    let wins = '';
    for (let i = 0; i < TOTAL; i++) {
      const x = i % 2 ? 344 : 264;
      const y = 210 + Math.floor(i / 2) * 80;
      wins += `<g class="win" data-i="${i}"><rect class="pane" x="${x}" y="${y}" width="56" height="60" rx="4"/><path class="bars" d="M${x + 28} ${y}v60M${x} ${y + 30}h56"/></g>`;
    }
    return `
<svg viewBox="196 96 268 410" xmlns="http://www.w3.org/2000/svg">
  <rect x="392" y="110" width="22" height="56" fill="#0E3026"/>
  <circle class="smoke" cx="403" cy="102" r="9"/>
  <circle class="smoke s2" cx="403" cy="102" r="9"/>
  <circle class="smoke s3" cx="403" cy="102" r="9"/>
  <rect x="220" y="180" width="220" height="326" fill="#14412F"/>
  <path d="M202 184 330 102 458 184z" fill="#1E5A45"/>
  <rect x="220" y="180" width="220" height="6" fill="#0F3A2B"/>
  ${wins}
  <rect class="door-glow" x="308" y="440" width="44" height="66" rx="3"/>
  <g class="door"><rect x="308" y="440" width="44" height="66" rx="3"/><circle cx="344" cy="476" r="2.6"/></g>
  <rect x="298" y="500" width="64" height="6" fill="#1F5A44"/>
</svg>`;
  }

  function rooSVG() {
    return `
<svg viewBox="0 0 220 300" xmlns="http://www.w3.org/2000/svg">
  <path d="M74 212C42 224 18 252 4 294 34 282 66 264 98 248Z" fill="#245F44"/>
  <ellipse cx="94" cy="216" rx="34" ry="42" transform="rotate(22 94 216)" fill="#2E7D5A"/>
  <path d="M82 244 116 262 122 284 180 289 180 299 104 299 94 282 66 252Z" fill="#276E4E"/>
  <ellipse cx="102" cy="168" rx="44" ry="74" transform="rotate(-12 102 168)" fill="#2E7D5A"/>
  <ellipse cx="130" cy="102" rx="20" ry="40" transform="rotate(14 130 102)" fill="#2E7D5A"/>
  <ellipse cx="128" cy="40" rx="6" ry="22" transform="rotate(-12 128 40)" fill="#2E7D5A"/>
  <ellipse cx="143" cy="41" rx="6" ry="20" transform="rotate(12 143 41)" fill="#276E4E"/>
  <ellipse cx="128" cy="42" rx="2.6" ry="14" transform="rotate(-12 128 42)" fill="#9FE3B0"/>
  <ellipse cx="141" cy="62" rx="21" ry="15" transform="rotate(20 141 62)" fill="#2E7D5A"/>
  <ellipse cx="162" cy="73" rx="19" ry="9" transform="rotate(25 162 73)" fill="#2E7D5A"/>
  <circle cx="179" cy="80" r="4.2" fill="#0B261D"/>
  <circle cx="149" cy="59" r="3" fill="#0B261D"/><circle cx="150" cy="58" r="1" fill="#fff"/>
  <ellipse cx="152" cy="130" rx="6" ry="19" transform="rotate(-52 152 130)" fill="#276E4E"/>
  <ellipse cx="124" cy="176" rx="22" ry="38" transform="rotate(-12 124 176)" fill="#8FD9AA"/>
  <circle cx="126" cy="158" r="12" fill="#2E7D5A"/>
  <ellipse cx="121" cy="147" rx="3.4" ry="8" transform="rotate(-18 121 147)" fill="#2E7D5A"/>
  <ellipse cx="131" cy="147" rx="3.4" ry="8" transform="rotate(14 131 147)" fill="#276E4E"/>
  <circle cx="130" cy="157" r="2" fill="#0B261D"/>
  <path d="M102 168Q126 160 148 172L146 196Q126 214 108 200Z" fill="#6CC28D"/>
  <path d="M104 168Q126 160 148 172" stroke="#245F44" stroke-width="2.5" fill="none" stroke-linecap="round"/>
</svg>`;
  }

  scene.innerHTML = `${skySVG()}<div class="house">${houseSVG()}</div><div class="roo" id="roo">${rooSVG()}</div><div class="ground"></div>`;
  const wins = [...scene.querySelectorAll('.win')];
  const roo = document.getElementById('roo');

  window.addEventListener('pointermove', (e) => {
    scene.style.setProperty('--mx', ((e.clientX / window.innerWidth - 0.5) * 2).toFixed(3));
  });

  function hop() {
    roo.classList.remove('hop');
    void roo.offsetWidth;
    roo.classList.add('hop');
  }

  /* ---------- Validation ---------- */
  const EMPTY = "To'ldiring";
  const nameRule = (v) => !v ? EMPTY : /^[\p{L}'’ʻ`\- ]{2,40}$/u.test(v) ? '' : "Kamida 2 ta harf";

  const registerRules = {
    first_name: nameRule,
    last_name: nameRule, // ixtiyoriy: bo'sh bo'lsa tekshirilmaydi
    username: (v) => !v ? EMPTY : /^[a-zA-Z0-9_]{3,20}$/.test(v) ? '' : "3–20: lotin harf, raqam, _",
    email: (v) => !v ? EMPTY : /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v) ? '' : "Email noto'g'ri",
    password: (v) => !v ? EMPTY
      : v.length < 8 ? "Kamida 8 ta belgi"
      : !/[A-Za-z]/.test(v) || !/\d/.test(v) ? "Harf va raqam kerak" : '',
    password_confirm: (v) => !v ? EMPTY : v !== form.elements.password.value ? "Parollar mos emas" : ''
  };
  const loginRules = {
    username: (v) => v ? '' : EMPTY,
    password: (v) => v ? '' : EMPTY
  };
  const RULES = mode === 'login' ? loginRules : registerRules;

  let ready = false; // set after the first update (no hop for prefilled values)

  const fields = [...form.querySelectorAll('.field')].map((el, i, all) => {
    const per = TOTAL / all.length;
    return {
      el,
      name: el.dataset.field,
      optional: el.hasAttribute('data-optional'),
      input: el.querySelector('input'),
      msg: el.querySelector('.msg'),
      touched: false,
      valid: false,
      ok: false,
      error: '',
      windows: ORDER.slice(Math.floor(i * per), Math.floor((i + 1) * per))
    };
  });

  const getVal = (f) => f.name.startsWith('password') ? f.input.value : f.input.value.trim();

  function render(f) {
    const show = f.touched && !f.valid;
    f.el.classList.toggle('is-invalid', show);
    f.el.classList.toggle('is-valid', f.ok);
    f.msg.textContent = show ? f.error : '';
    f.input.setAttribute('aria-invalid', show ? 'true' : 'false');
  }

  function update() {
    let shouldHop = false;
    fields.forEach((f) => {
      const v = getVal(f);
      f.error = f.optional && !v ? '' : RULES[f.name](v);
      f.valid = !f.error;
      const wasOk = f.ok;
      f.ok = f.valid && v !== '';
      if (f.ok && !wasOk) shouldHop = true;
      render(f);
    });
    if (shouldHop && ready) hop();

    const lit = new Set();
    fields.forEach((f) => f.ok && f.windows.forEach((w) => lit.add(w)));
    wins.forEach((w) => w.classList.toggle('on', lit.has(+w.dataset.i)));

    const all = fields.every((f) => f.valid);
    scene.classList.toggle('lit', lit.size > 0);
    scene.classList.toggle('ready', all);
    form.classList.toggle('ready', all);
    btn.classList.toggle('ready', all);
    meter.classList.toggle('on', lit.size > 0);
    meterText.textContent = all ? 'Eshik ochiq — davom eting' : `${lit.size} / ${TOTAL} deraza yondi`;
  }

  /* ---------- Field events ---------- */
  fields.forEach((f) => {
    f.input.addEventListener('input', () => {
      formError.hidden = true;
      update();
    });
    f.input.addEventListener('blur', () => {
      f.touched = true;
      update();
      f.windows.forEach((w) => wins[w].classList.remove('target'));
    });
    f.input.addEventListener('focus', () => {
      f.windows.forEach((w) => wins[w].classList.add('target'));
    });
  });

  // show / hide password
  form.querySelectorAll('.toggle').forEach((t) => {
    t.addEventListener('click', () => {
      const input = t.parentElement.querySelector('input');
      const show = input.type === 'password';
      input.type = show ? 'text' : 'password';
      t.setAttribute('aria-pressed', show);
    });
  });

  // password strength (register)
  const strengthEl = form.querySelector('.strength');
  if (strengthEl) {
    const labels = ['', 'Zaif', "O'rtacha", 'Yaxshi', 'Kuchli'];
    const pw = form.elements.password;
    pw.addEventListener('input', () => {
      const v = pw.value;
      let s = 0;
      if (v.length >= 8) s++;
      if (/[a-z]/.test(v) && /[A-Z]/.test(v)) s++;
      if (/\d/.test(v)) s++;
      if (/[^A-Za-z0-9]/.test(v) || v.length >= 12) s++;
      const level = v ? Math.max(1, s) : 0;
      strengthEl.dataset.level = level;
      strengthEl.querySelector('span').textContent = labels[level];
    });
  }

  /* ---------- Helpers ---------- */
  let toastTimer;
  function toast(text) {
    toastEl.textContent = text;
    toastEl.classList.add('show');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => toastEl.classList.remove('show'), 3000);
  }
  function shake() {
    form.classList.remove('shake');
    void form.offsetWidth;
    form.classList.add('shake');
  }
  const fail = (message, field) => {
    btn.classList.remove('loading');
    btn.disabled = false;
    shake();
    if (field) {
      const f = fields.find((x) => x.name === field);
      f.el.classList.add('is-invalid');
      f.el.classList.remove('is-valid');
      f.msg.textContent = message;
      f.input.focus();
    } else {
      formError.textContent = message;
      formError.hidden = false;
    }
  };
  function success(text, url) {
    wins.forEach((w) => w.classList.add('on'));
    scene.classList.add('lit', 'ready', 'open');
    meterText.textContent = 'Eshik ochildi';
    hop();
    toast(text);
    setTimeout(() => { location.href = url; }, 1900);
  }
  async function hash(s) {
    try {
      const buf = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(s));
      return [...new Uint8Array(buf)].map((b) => b.toString(16).padStart(2, '0')).join('');
    } catch {
      return btoa(unescape(encodeURIComponent(s)));
    }
  }
  const readUsers = () => { try { return JSON.parse(localStorage.getItem(USERS_KEY)) || []; } catch { return []; } };

  /* ---------- Auth (DEMO: localStorage) ----------
     Backend tayyor bo'lganda faqat shu ikki funksiyani fetch() bilan
     almashtiring, masalan:
       const res = await fetch('/api/auth/register/', {
         method: 'POST',
         headers: { 'Content-Type': 'application/json' },
         body: JSON.stringify(data)
       });
  ------------------------------------------------ */
  async function register(data) {
    const users = readUsers();
    if (users.some((u) => u.username.toLowerCase() === data.username.toLowerCase())) {
      return fail("Bu nom band", 'username');
    }
    if (users.some((u) => u.email.toLowerCase() === data.email.toLowerCase())) {
      return fail("Bu email band", 'email');
    }
    users.push({
      first_name: data.first_name,
      last_name: data.last_name || '',
      username: data.username,
      email: data.email,
      password: await hash(data.password)
    });
    localStorage.setItem(USERS_KEY, JSON.stringify(users));
    localStorage.setItem(LAST_KEY, data.username);
    success(`Xush kelibsiz, ${data.first_name}! Hisobingiz yaratildi.`, 'login.html?registered=1');
  }

  async function login(data) {
    const user = readUsers().find((u) => u.username.toLowerCase() === data.username.toLowerCase());
    if (!user || user.password !== await hash(data.password)) {
      return fail("Foydalanuvchi nomi yoki parol noto'g'ri");
    }
    localStorage.setItem(SESSION_KEY, user.username);
    success(`Qaytganingiz bilan, ${user.first_name}!`, 'index.html');
  }

  /* ---------- Submit ---------- */
  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    fields.forEach((f) => { f.touched = true; });
    update();
    const bad = fields.find((f) => !f.valid);
    if (bad) { shake(); bad.input.focus(); return; }

    const data = Object.fromEntries(fields.map((f) => [f.name, getVal(f)]));
    btn.classList.add('loading');
    btn.disabled = true;
    await new Promise((r) => setTimeout(r, 700));
    try {
      await (mode === 'register' ? register(data) : login(data));
    } catch {
      fail("Xatolik yuz berdi. Qayta urinib ko'ring.");
    }
  });

  /* ---------- Init ---------- */
  if (mode === 'login' && new URLSearchParams(location.search).get('registered')) {
    formNote.hidden = false;
    const last = localStorage.getItem(LAST_KEY);
    if (last) form.elements.username.value = last;
  }
  update();
  ready = true;
  if (mode === 'login' && form.elements.username.value) form.elements.password.focus();
})();