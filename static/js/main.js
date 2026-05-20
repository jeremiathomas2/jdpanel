// ─── NAVIGATION ───
const pageNames = {
  'dashboard':'Dashboard','websites':'Websites','domains':'Domains',
  'subdomains':'Subdomains','parked':'Parked Domains','redirects':'Redirects',
  'filemanager':'File Manager','databases':'Databases','db-users':'DB Users',
  'phpmyadmin':'phpMyAdmin','email':'Email Hosting','webmail':'Webmail',
  'forwarders':'Email Forwarders','autoresponders':'Auto Responders',
  'spam':'Spam Filters','dkim':'DKIM / SPF','dns':'DNS Zones',
  'dns-records':'DNS Records','dns-propagation':'Propagation Check',
  'ssl':'SSL Certificates','ssl-install':'Auto Install SSL','ssl-custom':'Custom SSL',
  'ftp':'FTP Accounts','ftp-logs':'FTP Logs','security':'Security Center',
  'fail2ban':'Fail2Ban','malware':'Malware Scanner','ip-block':'IP Blocking',
  'modsecurity':'ModSecurity','backups':'Backup Manager','backup-schedule':'Schedules',
  'backup-restore':'Restore Backups','backup-remote':'Remote Storage',
  'packages':'Hosting Packages','resellers':'Reseller Accounts','users':'Hosting Users',
  'billing':'Invoices','subscriptions':'Subscriptions','payments':'Payment Gateway',
  'api':'API & Webhooks','notifications':'Notifications','settings-page':'Panel Settings',
  'server-info':'Server Info','services':'Service Control','cron':'Cron Jobs',
  'logs':'System Logs','packages-update':'Package Updates','resources':'Resource Monitor',
  'network':'Network Traffic','processes':'Process Viewer'
};

const explicitPages = ['dashboard','websites','databases','email','dns','ssl','security','backups','filemanager','ftp','api','settings-page'];

function navigate(page, el) {
  // Update breadcrumb
  const breadcrumb = document.getElementById('breadcrumbCurrent');
  if (breadcrumb) breadcrumb.textContent = pageNames[page] || page;
  
  // Hide all pages
  document.querySelectorAll('.page-view').forEach(p => p.classList.remove('active'));
  
  // Show target or generic
  const target = document.getElementById('page-' + page);
  if (target) {
    target.classList.add('active');
  } else {
    const genTitle = document.getElementById('genericTitle');
    const genSubtitle = document.getElementById('genericSubtitle');
    const genPage = document.getElementById('page-generic');
    
    if (genTitle) genTitle.textContent = pageNames[page] || page;
    if (genSubtitle) genSubtitle.textContent = 'Module: ' + (pageNames[page] || page);
    if (genPage) genPage.classList.add('active');
  }
  
  // Update active nav links
  document.querySelectorAll('.nav-link, .sub-link').forEach(l => l.classList.remove('active'));
  if (el) el.classList.add('active');
  
  // Close mobile
  closeMobileSidebar();
  // Close dropdowns
  closeDropdowns();
}

function toggleMenu(id) {
  const item = document.getElementById(id);
  if (!item) return;
  const isOpen = item.classList.contains('open');
  document.querySelectorAll('.nav-item.open').forEach(i => { if(i.id !== id) i.classList.remove('open'); });
  item.classList.toggle('open', !isOpen);
  // Mark link active on parent
  const link = item.querySelector('.nav-link');
  if (link) link.classList.toggle('active', !isOpen);
}

// ─── SIDEBAR TOGGLE ───
let sidebarCollapsed = false;
function toggleSidebar() {
  const sidebar = document.getElementById('sidebar');
  const wrapper = document.getElementById('main-wrapper');
  if (window.innerWidth <= 768) {
    sidebar.classList.toggle('mobile-open');
    const overlay = document.getElementById('mobile-overlay');
    if (overlay) overlay.classList.toggle('show', sidebar.classList.contains('mobile-open'));
  } else {
    sidebarCollapsed = !sidebarCollapsed;
    sidebar.classList.toggle('collapsed', sidebarCollapsed);
    wrapper.classList.toggle('collapsed', sidebarCollapsed);
    const compactToggle = document.getElementById('toggleCompact');
    if (compactToggle) compactToggle.classList.toggle('on', sidebarCollapsed);
  }
}

function closeMobileSidebar() {
  const sidebar = document.getElementById('sidebar');
  const overlay = document.getElementById('mobile-overlay');
  if (sidebar) sidebar.classList.remove('mobile-open');
  if (overlay) overlay.classList.remove('show');
}

// ─── SETTINGS PANEL ───
function openSettings() {
  const panel = document.getElementById('settings-panel');
  const overlay = document.getElementById('settingsOverlay');
  if (panel) panel.classList.add('open');
  if (overlay) overlay.classList.add('show');
  closeDropdowns();
}
function closeSettings() {
  const panel = document.getElementById('settings-panel');
  const overlay = document.getElementById('settingsOverlay');
  if (panel) panel.classList.remove('open');
  if (overlay) overlay.classList.remove('show');
}

// ─── THEME PERSISTENCE ───
const SETTINGS_KEY = 'jdpanel_settings';
let settings = JSON.parse(localStorage.getItem(SETTINGS_KEY)) || {
  theme: 'dark',
  accent: '#3B82F6',
  accentHover: '#2563EB',
  sidebarBg: '#0f172a',
  headerBg: '#0f172a',
  footerBg: '#0f172a',
  sidebarWidth: '260',
  animSpeed: 'normal',
  compactSidebar: false,
  showFooter: true
};

function saveSettings() {
  localStorage.setItem(SETTINGS_KEY, JSON.stringify(settings));
}

function applySettings() {
  setTheme(settings.theme, false);
  setAccent(settings.accent, settings.accentHover, null, false);
  setSidebarBg(settings.sidebarBg, null, false);
  setHeaderBg(settings.headerBg, null, false);
  setFooterBg(settings.footerBg, null, false);
  setSidebarWidth(settings.sidebarWidth, false);
  setAnimSpeed(settings.animSpeed, null, false);
  
  if (settings.compactSidebar) {
    const sidebar = document.getElementById('sidebar');
    const wrapper = document.getElementById('main-wrapper');
    const toggle = document.getElementById('toggleCompact');
    if (sidebar) sidebar.classList.add('collapsed');
    if (wrapper) wrapper.classList.add('collapsed');
    if (toggle) toggle.classList.add('on');
    sidebarCollapsed = true;
  }
  
  const footer = document.getElementById('footer');
  const toggleFooter = document.getElementById('toggleFooter');
  if (footer) footer.style.display = settings.showFooter ? '' : 'none';
  if (toggleFooter) {
    if (settings.showFooter) toggleFooter.classList.add('on');
    else toggleFooter.classList.remove('on');
  }
}

// ─── THEME ───
function setTheme(theme, save = true) {
  if (save) {
    settings.theme = theme;
    saveSettings();
  }
  document.querySelectorAll('.theme-opt').forEach(o => o.classList.remove('active'));
  if(theme === 'light') {
    document.documentElement.setAttribute('data-theme','light');
    const opt = document.getElementById('themeLight');
    if (opt) opt.classList.add('active');
  } else if(theme === 'dark') {
    document.documentElement.setAttribute('data-theme','dark');
    const opt = document.getElementById('themeDark');
    if (opt) opt.classList.add('active');
  } else {
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    document.documentElement.setAttribute('data-theme', (save ? (prefersDark ? 'dark' : 'light') : theme));
    const opt = document.getElementById('themeAuto');
    if (opt) opt.classList.add('active');
  }
}

// ─── ACCENT COLOR ───
function setAccent(color, hover, el, save = true) {
  if (save) {
    settings.accent = color;
    settings.accentHover = hover;
    saveSettings();
  }
  document.documentElement.style.setProperty('--accent', color);
  document.documentElement.style.setProperty('--accent-hover', hover);
  document.documentElement.style.setProperty('--accent-light', hexToRgba(color, 0.12));
  document.querySelectorAll('#accentSwatches .swatch').forEach(s => s.classList.remove('active'));
  
  // Find and activate swatch if color matches
  if (!el) {
    el = document.querySelector(`#accentSwatches .swatch[data-color="${color}"]`);
  }
  
  if(el) el.classList.add('active');
  const custom = document.getElementById('accentCustom');
  const hex = document.getElementById('accentHex');
  if (custom) custom.value = color;
  if (hex) hex.value = color;
}
function setAccentCustom(val) {
  setAccent(val, val, null, true);
}
function setAccentHexInput(val) {
  if(/^#[0-9A-Fa-f]{6}$/.test(val)) {
    setAccent(val, val, null, true);
  }
}

// ─── SIDEBAR BG ───
function setSidebarBg(color, el, save = true) {
  if (save) {
    settings.sidebarBg = color;
    saveSettings();
  }
  document.documentElement.style.setProperty('--sidebar-bg', color);
  document.querySelectorAll('#sidebarSwatches .swatch').forEach(s => s.classList.remove('active'));
  
  if (!el) {
    el = document.querySelector(`#sidebarSwatches .swatch[data-color="${color}"]`);
  }

  if(el) el.classList.add('active');
  const custom = document.getElementById('sidebarCustom');
  const hex = document.getElementById('sidebarHex');
  if (custom) custom.value = color;
  if (hex) hex.value = color;
}
function setSidebarBgCustom(val) {
  setSidebarBg(val, null, true);
}

// ─── HEADER BG ───
function setHeaderBg(color, el, save = true) {
  if (save) {
    settings.headerBg = color;
    saveSettings();
  }
  document.documentElement.style.setProperty('--header-bg', color);
  document.querySelectorAll('#headerSwatches .swatch').forEach(s => s.classList.remove('active'));
  
  if (!el) {
    el = document.querySelector(`#headerSwatches .swatch[data-color="${color}"]`);
  }

  if(el) el.classList.add('active');
  const custom = document.getElementById('headerCustom');
  if (custom) custom.value = color;
}
function setHeaderBgCustom(val) {
  setHeaderBg(val, null, true);
}

// ─── FOOTER BG ───
function setFooterBg(color, el, save = true) {
  if (save) {
    settings.footerBg = color;
    saveSettings();
  }
  document.documentElement.style.setProperty('--footer-bg', color);
  document.querySelectorAll('#footerSwatches .swatch').forEach(s => s.classList.remove('active'));
  
  if (!el) {
    el = document.querySelector(`#footerSwatches .swatch[data-color="${color}"]`);
  }

  if(el) el.classList.add('active');
  const custom = document.getElementById('footerCustom');
  if (custom) custom.value = color;
}
function setFooterBgCustom(val) {
  setFooterBg(val, null, true);
}

// ─── SIDEBAR WIDTH ───
function setSidebarWidth(val, save = true) {
  if (save) {
    settings.sidebarWidth = val;
    saveSettings();
  }
  document.documentElement.style.setProperty('--sidebar-width', val + 'px');
  const valDisplay = document.getElementById('sidebarWidthVal');
  if (valDisplay) valDisplay.textContent = val + 'px';
  const slider = document.querySelector('input[type=range][oninput*="setSidebarWidth"]');
  if (slider) slider.value = val;
}

// ─── ANIMATION SPEED ───
function setAnimSpeed(speed, el, save = true) {
  if (save) {
    settings.animSpeed = speed;
    saveSettings();
  }
  document.querySelectorAll('.settings-section .theme-opt').forEach(o => { 
    if(o.textContent.toLowerCase().includes(speed)) o.classList.add('active');
    else if (o.textContent.match(/Fast|Normal|Slow|None/)) o.classList.remove('active');
  });
  
  document.body.classList.remove('anim-fast','anim-slow','anim-none');
  if(speed === 'fast') document.body.classList.add('anim-fast');
  else if(speed === 'slow') document.body.classList.add('anim-slow');
  else if(speed === 'none') document.body.classList.add('anim-none');
}

// ─── COMPACT SIDEBAR ───
function toggleCompactSidebar(el) {
  el.classList.toggle('on');
  const sidebar = document.getElementById('sidebar');
  const wrapper = document.getElementById('main-wrapper');
  sidebarCollapsed = el.classList.contains('on');
  sidebar.classList.toggle('collapsed', sidebarCollapsed);
  wrapper.classList.toggle('collapsed', sidebarCollapsed);
  
  settings.compactSidebar = sidebarCollapsed;
  saveSettings();
}

// ─── FOOTER VISIBILITY ───
function toggleFooterVis(el) {
  el.classList.toggle('on');
  const footer = document.getElementById('footer');
  const isVisible = el.classList.contains('on');
  if (footer) footer.style.display = isVisible ? '' : 'none';
  
  settings.showFooter = isVisible;
  saveSettings();
}

// ─── RESET ───
function resetSettings() {
  localStorage.removeItem(SETTINGS_KEY);
  location.reload();
}

// ─── DROPDOWNS ───
function toggleNotifs() {
  const d = document.getElementById('notifDropdown');
  const p = document.getElementById('profileDropdown');
  if (p) p.classList.remove('show');
  if (d) d.classList.toggle('show');
}
function toggleProfile() {
  const d = document.getElementById('profileDropdown');
  const n = document.getElementById('notifDropdown');
  if (n) n.classList.remove('show');
  if (d) d.classList.toggle('show');
}
function closeDropdowns() {
  const notif = document.getElementById('notifDropdown');
  const profile = document.getElementById('profileDropdown');
  if (notif) notif.classList.remove('show');
  if (profile) profile.classList.remove('show');
}
document.addEventListener('click', function(e) {
  if (!e.target.closest('.header-btn-wrap') && !e.target.closest('.notif-dropdown') && !e.target.closest('.profile-dropdown')) {
    closeDropdowns();
  }
});

// ─── UTILITY ───
function hexToRgba(hex, alpha) {
  const r = parseInt(hex.slice(1,3),16);
  const g = parseInt(hex.slice(3,5),16);
  const b = parseInt(hex.slice(5,7),16);
  return `rgba(${r},${g},${b},${alpha})`;
}

function rgbToHex(rgb) {
  if (!rgb) return '';
  if (rgb.startsWith('#')) return rgb.toLowerCase();
  const res = rgb.match(/\d+/g);
  if (!res || res.length < 3) return '';
  return "#" + ((1 << 24) + (parseInt(res[0]) << 16) + (parseInt(res[1]) << 8) + parseInt(res[2])).toString(16).slice(1).toLowerCase();
}

// Auto-open first submenu (server)
const serverNav = document.getElementById('nav-server');
if (serverNav) serverNav.classList.add('open');

// Apply saved settings
applySettings();

// Animate progress bars on load
window.addEventListener('load', () => {
  document.querySelectorAll('.resource-bar-fill, .progress-fill, .mini-fill').forEach(el => {
    const w = el.style.width;
    el.style.width = '0';
    setTimeout(() => { el.style.width = w; }, 200);
  });
});
