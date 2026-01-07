document.addEventListener('DOMContentLoaded', () => {
    initializeThemeSwitcher();
    initializeBackButton();
    initializeFontSizeSwitcher();
    applyAppearance();
});

function initializeBackButton() {
    const backBtns = document.querySelectorAll('.back-button');
    backBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            // If the button is inside a form or has specific behavior, respect it.
            // Otherwise, default to history back.
            if (!btn.getAttribute('type') && !btn.getAttribute('onclick')) {
                e.preventDefault();
                window.history.back();
            }
        });
    });
}

function initializeThemeSwitcher() {
    const currentTheme = localStorage.getItem('privalk_color_theme') || 'green-black';
    
    // Highlight the active theme button
    document.querySelectorAll('.theme-option').forEach(opt => {
        if (opt.getAttribute('data-value') === currentTheme) {
            opt.classList.add('active');
            // Scroll active theme into view
            setTimeout(() => {
                const container = document.querySelector('.theme-grid');
                if (container) {
                    const scrollLeft = opt.offsetLeft - (container.offsetWidth / 2) + (opt.offsetWidth / 2);
                    container.scrollTo({ left: scrollLeft, behavior: 'smooth' });
                }
            }, 100);
        } else {
            opt.classList.remove('active');
        }
    });
}

function toggleEdit(field) {
    const input = document.getElementById('field-' + field);
    const editBtn = document.getElementById('btn-edit-' + field);
    const saveBtn = document.getElementById('btn-save-' + field);
    
    if (input.hasAttribute('readonly')) {
        input.removeAttribute('readonly');
        input.focus();
        editBtn.style.display = 'none';
        saveBtn.style.display = 'flex';
    }
}

async function saveField(field) {
    const input = document.getElementById('field-' + field);
    const editBtn = document.getElementById('btn-edit-' + field);
    const saveBtn = document.getElementById('btn-save-' + field);
    const val = input.value;
    
    try {
        const res = await fetch(`/update/${field}?${field}=${encodeURIComponent(val)}`);
        const data = await res.json();
        
        if (data.status === 'success') {
            showToast('Updated successfully', false);
            input.setAttribute('readonly', true);
            editBtn.style.display = 'flex';
            saveBtn.style.display = 'none';
        } else {
            showToast(data.message || 'Error updating', true);
        }
    } catch (e) {
        showToast('Network error', true);
    }
}

function initializeFontSizeSwitcher() {
    const buttons = document.querySelectorAll('#font-size-toggle .theme-toggle-btn');
    buttons.forEach(btn => {
        btn.addEventListener('click', () => {
            setFontSize(btn.dataset.size);
        });
    });
}

function toggleAmoled(isChecked) {
    localStorage.setItem('privalk_amoled', isChecked);
    applyAppearance();
}

function setWallpaper(url) {
    localStorage.setItem('privalk_wallpaper', url);
    applyAppearance();
}

function setBubbleStyle(style) {
    localStorage.setItem('privalk_bubble', style);
    applyAppearance();
}

function setFontSize(size) {
    localStorage.setItem('privalk_fontsize', size);
    applyAppearance();
}

function applyAppearance() {
    const root = document.documentElement;
    const body = document.body;
    
    // 1. AMOLED (Only applies if not light mode)
    const isAmoled = localStorage.getItem('privalk_amoled') === 'true';
    const isLight = body.classList.contains('light-mode');
    
    if (isAmoled && !isLight) {
        root.style.setProperty('--bg-body', '#000000');
        root.style.setProperty('--bg-sidebar', '#000000');
        root.style.setProperty('--bg-chat', '#000000');
        root.style.setProperty('--border', 'rgba(255,255,255,0.15)');
    } else if (!isLight) {
        root.style.removeProperty('--bg-body');
        root.style.removeProperty('--bg-sidebar');
        root.style.removeProperty('--bg-chat');
        root.style.removeProperty('--border');
    }

    // 2. Wallpaper
    const wallpaper = localStorage.getItem('privalk_wallpaper');
    if (wallpaper) root.style.setProperty('--chat-bg-image', `url('${wallpaper}')`);
    else root.style.setProperty('--chat-bg-image', 'none');

    // 3. Bubble Style
    const bubble = localStorage.getItem('privalk_bubble') || 'modern';
    let radius = '16px';
    if (bubble === 'rounded') radius = '25px';
    if (bubble === 'classic') radius = '4px';
    root.style.setProperty('--bubble-radius', radius);
    
    // Update Bubble Toggle UI
    document.querySelectorAll('#bubble-style-toggle .theme-toggle-btn').forEach(btn => {
        if(btn.dataset.bubble === bubble) btn.classList.add('active');
        else btn.classList.remove('active');
    });

    // 4. Font Size
    const size = localStorage.getItem('privalk_fontsize') || 'medium';
    let fontSize = '0.9rem';
    if (size === 'small') fontSize = '0.8rem';
    if (size === 'large') fontSize = '1.05rem';
    root.style.setProperty('--msg-font-size', fontSize);
    
    // Update Font Toggle UI
    document.querySelectorAll('#font-size-toggle .theme-toggle-btn').forEach(btn => {
        if(btn.dataset.size === size) btn.classList.add('active');
        else btn.classList.remove('active');
    });
    
    // Update Inputs
    const amoledInput = document.querySelector('#amoled-toggle input');
    if(amoledInput) amoledInput.checked = isAmoled;
}

function applyTheme(themeKey) {
    document.documentElement.setAttribute('data-theme', themeKey);
    localStorage.setItem('privalk_color_theme', themeKey);
    
    // Haptic feedback for mobile feel
    if (navigator.vibrate) navigator.vibrate(10);
    
    document.querySelectorAll('.theme-option').forEach(opt => {
        if (opt.getAttribute('data-value') === themeKey) {
            opt.classList.add('active');
            const container = document.querySelector('.theme-grid');
            if (container) {
                const scrollLeft = opt.offsetLeft - (container.offsetWidth / 2) + (opt.offsetWidth / 2);
                container.scrollTo({ left: scrollLeft, behavior: 'smooth' });
            }
        } else {
            opt.classList.remove('active');
        }
    });
}