import streamlit as st

st.set_page_config(
    page_title="Endüstriyel Üretimde Yapay Zeka Destekli Yalın Üretim Yaklaşımı",
    page_icon="🏭",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@300;400;500;600;700&family=Exo+2:wght@300;400;600;800&display=swap');

* { margin: 0; padding: 0; box-sizing: border-box; }

/* Mevcut .stApp kısmını bununla değiştir */
html, body, .stApp {
    background: 
        linear-gradient(rgba(6, 13, 26, 0.88), rgba(6, 13, 26, 0.92)), 
        url("https://www.yildizentegre.com/uploads/news/04--05-2026/e0400698-fb0a-4c79-9d89-c53dec4b16d8.jpg"); 
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    font-family: 'Exo 2', sans-serif;
}

/* Mevcut .stApp::before (grid) kısmını bununla değiştir */
.stApp::before {
    content: '';
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    background-image:
        linear-gradient(rgba(0,180,255,0.07) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0,180,255,0.07) 1px, transparent 1px);
    background-size: 50px 50px;
    animation: gridMove 20s linear infinite;
    pointer-events: none;
    z-index: 0;
}

/* Kartların altına (module-card içine) şu satırı ekle ki resim üzerinde cam gibi dursunlar */
.module-card {
    backdrop-filter: blur(10px);
    /* diğer mevcut özelliklerin kalsın... */
}

@keyframes gridMove {
    0% { transform: translateY(0); }
    100% { transform: translateY(50px); }
}

/* Glowing orbs */
.stApp::after {
    content: '';
    position: fixed;
    width: 600px; height: 600px;
    background: radial-gradient(circle, rgba(0,120,255,0.08) 0%, transparent 70%);
    top: -200px; left: -200px;
    pointer-events: none;
    z-index: 0;
    animation: float 8s ease-in-out infinite;
}

@keyframes float {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(30px); }
}

/* Hero Section */
.hero {
    position: relative;
    text-align: center;
    padding: 60px 20px 40px;
    z-index: 1;
}

.hero-badge {
    display: inline-block;
    background: linear-gradient(135deg, rgba(0,180,255,0.15), rgba(0,80,255,0.1));
    border: 1px solid rgba(0,180,255,0.3);
    color: #00b4ff;
    font-family: 'Rajdhani', sans-serif;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 3px;
    text-transform: uppercase;
    padding: 6px 20px;
    border-radius: 20px;
    margin-bottom: 24px;
    animation: pulse 2s ease-in-out infinite;
}

@keyframes pulse {
    0%, 100% { box-shadow: 0 0 0 0 rgba(0,180,255,0.3); }
    50% { box-shadow: 0 0 0 8px rgba(0,180,255,0); }
}

.hero-title {
    font-family: 'Rajdhani', sans-serif;
    font-size: clamp(36px, 6vw, 72px);
    font-weight: 700;
    line-height: 1.1;
    margin-bottom: 8px;
    background: linear-gradient(135deg, #ffffff 0%, #a0d4ff 50%, #00b4ff 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    text-shadow: none;
}

.hero-subtitle {
    font-family: 'Rajdhani', sans-serif;
    font-size: clamp(16px, 2.5vw, 22px);
    font-weight: 300;
    color: rgba(160,212,255,0.7);
    letter-spacing: 4px;
    text-transform: uppercase;
    margin-bottom: 16px;
}

.hero-desc {
    font-size: 15px;
    color: rgba(255,255,255,0.45);
    max-width: 600px;
    margin: 0 auto 40px;
    line-height: 1.8;
    font-weight: 300;
}

/* Divider */
.divider {
    display: flex;
    align-items: center;
    gap: 16px;
    margin: 0 auto 50px;
    max-width: 400px;
}

.divider-line {
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(0,180,255,0.4), transparent);
}

.divider-dot {
    width: 6px; height: 6px;
    border-radius: 50%;
    background: #00b4ff;
    box-shadow: 0 0 10px #00b4ff;
}

/* Cards Section */
.cards-container {
    position: relative;
    z-index: 1;
    padding: 0 20px 60px;
}

.section-label {
    font-family: 'Rajdhani', sans-serif;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: rgba(0,180,255,0.5);
    text-align: center;
    margin-bottom: 40px;
}

/* Module Cards */
.module-card {
    position: relative;
    background: linear-gradient(135deg, rgba(255,255,255,0.04) 0%, rgba(255,255,255,0.01) 100%);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 20px;
    padding: 36px 28px;
    cursor: pointer;
    transition: all 0.4s cubic-bezier(0.23, 1, 0.32, 1);
    overflow: hidden;
    height: 100%;
    min-height: 300px;
    display: flex;
    flex-direction: column;
}

.module-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0;
    right: 0; height: 1px;
    background: linear-gradient(90deg, transparent, var(--accent), transparent);
    opacity: 0;
    transition: opacity 0.4s;
}

.module-card:hover {
    transform: translateY(-8px);
    border-color: var(--accent);
    box-shadow:
        0 20px 60px rgba(0,0,0,0.5),
        0 0 40px var(--glow);
    background: linear-gradient(135deg, rgba(255,255,255,0.07) 0%, rgba(255,255,255,0.02) 100%);
}

.module-card:hover::before { opacity: 1; }

/* Card accent backgrounds */
.card-1 { --accent: rgba(0,180,255,0.5); --glow: rgba(0,180,255,0.1); }
.card-2 { --accent: rgba(255,100,80,0.5); --glow: rgba(255,100,80,0.1); }
.card-3 { --accent: rgba(100,220,120,0.5); --glow: rgba(100,220,120,0.1); }
.card-4 { --accent: rgba(200,100,255,0.5); --glow: rgba(200,100,255,0.1); }

.card-number {
    font-family: 'Rajdhani', sans-serif;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 3px;
    color: var(--accent-solid, rgba(0,180,255,0.5));
    margin-bottom: 20px;
    text-transform: uppercase;
}

.card-icon-wrap {
    width: 64px; height: 64px;
    border-radius: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 28px;
    margin-bottom: 24px;
    position: relative;
}

.card-1 .card-icon-wrap { background: rgba(0,180,255,0.1); border: 1px solid rgba(0,180,255,0.2); }
.card-2 .card-icon-wrap { background: rgba(255,100,80,0.1); border: 1px solid rgba(255,100,80,0.2); }
.card-3 .card-icon-wrap { background: rgba(100,220,120,0.1); border: 1px solid rgba(100,220,120,0.2); }
.card-4 .card-icon-wrap { background: rgba(200,100,255,0.1); border: 1px solid rgba(200,100,255,0.2); }

.card-title {
    font-family: 'Rajdhani', sans-serif;
    font-size: 22px;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 10px;
    line-height: 1.2;
}

.card-desc {
    font-size: 13px;
    color: rgba(255,255,255,0.4);
    line-height: 1.7;
    flex: 1;
    font-weight: 300;
}

.card-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    margin: 20px 0;
}

.tag {
    font-size: 10px;
    font-family: 'Rajdhani', sans-serif;
    font-weight: 600;
    letter-spacing: 1px;
    text-transform: uppercase;
    padding: 4px 10px;
    border-radius: 6px;
}

.card-1 .tag { background: rgba(0,180,255,0.1); color: rgba(0,180,255,0.8); border: 1px solid rgba(0,180,255,0.2); }
.card-2 .tag { background: rgba(255,100,80,0.1); color: rgba(255,100,80,0.8); border: 1px solid rgba(255,100,80,0.2); }
.card-3 .tag { background: rgba(100,220,120,0.1); color: rgba(100,220,120,0.8); border: 1px solid rgba(100,220,120,0.2); }
.card-4 .tag { background: rgba(200,100,255,0.1); color: rgba(200,100,255,0.8); border: 1px solid rgba(200,100,255,0.2); }

.card-arrow {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    font-family: 'Rajdhani', sans-serif;
    font-size: 13px;
    font-weight: 600;
    letter-spacing: 1px;
    text-transform: uppercase;
    color: rgba(255,255,255,0.3);
    transition: all 0.3s;
    margin-top: 20px;
}

.module-card:hover .card-arrow {
    color: rgba(255,255,255,0.8);
    gap: 12px;
}

/* Stats bar */
.stats-bar {
    position: relative;
    z-index: 1;
    display: flex;
    justify-content: center;
    gap: 60px;
    padding: 30px;
    margin: 0 20px 50px;
    background: linear-gradient(135deg, rgba(255,255,255,0.03) 0%, rgba(255,255,255,0.01) 100%);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 16px;
    flex-wrap: wrap;
}

.stat-item { text-align: center; }

.stat-value {
    font-family: 'Rajdhani', sans-serif;
    font-size: 32px;
    font-weight: 700;
    background: linear-gradient(135deg, #ffffff, #00b4ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1;
    margin-bottom: 6px;
}

.stat-label {
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: rgba(255,255,255,0.3);
    font-family: 'Rajdhani', sans-serif;
}

/* Footer */
.footer {
    position: relative;
    z-index: 1;
    text-align: center;
    padding: 30px;
    border-top: 1px solid rgba(255,255,255,0.05);
}

.footer-text {
    font-size: 12px;
    color: rgba(255,255,255,0.2);
    font-family: 'Rajdhani', sans-serif;
    letter-spacing: 2px;
}

/* Streamlit overrides */
.stButton > button {
    width: 100%;
    background: transparent !important;
    border: none !important;
    padding: 0 !important;
    height: auto !important;
}

div[data-testid="column"] { padding: 8px !important; }

.stMarkdown { position: relative; z-index: 1; }

/* Hide streamlit elements */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }
</style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero">
    <div class="hero-badge">◆ Bitirme Projesi 2026 ◆</div>
    <div class="hero-title">ENDÜSTRİYEL ÜRETİMDE YAPAY ZEKA DESTEKLİ YALIN ÜRETİM YAKLAŞIMI</div>
    <div class="hero-title" style="margin-top: -12px;">AI SİSTEMİ</div>
    <div class="hero-subtitle">Yapay Zeka Destekli Akıllı Fabrika</div>
    <div class="hero-desc">
        Dört farklı makine öğrenmesi modülüyle üretim süreçlerinizi optimize edin.
        Gerçek zamanlı tahmin, sınıflandırma ve analiz.
    </div>
</div>

<div class="divider">
    <div class="divider-line"></div>
    <div class="divider-dot"></div>
    <div class="divider-line"></div>
</div>
""", unsafe_allow_html=True)

# Stats Bar
st.markdown("""
<div class="stats-bar">
    <div class="stat-item">
        <div class="stat-value">4</div>
        <div class="stat-label">AI Modülü</div>
    </div>
    <div class="stat-item">
        <div class="stat-value">%90</div>
        <div class="stat-label">Doğruluk</div>
    </div>
    <div class="stat-item">
        <div class="stat-value">RT</div>
        <div class="stat-label">Gerçek Zamanlı</div>
    </div>
    <div class="stat-item">
        <div class="stat-value">ML</div>
        <div class="stat-label">Makine Öğrenmesi</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Module label
st.markdown("""
<div class="section-label">— AI Modülleri — Bir modül seçin —</div>
""", unsafe_allow_html=True)

# Module Cards
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="module-card card-1">
        <div class="card-number">Modül 01</div>
        <div class="card-icon-wrap">🤖</div>
        <div class="card-title">Duruş Sınıflandırma & Süre Tahmini</div>
        <div class="card-desc">
            Makine duruşlarını otomatik sınıflandır, duruş sürelerini tahmin et. Kayıpları minimize et, OEE'yi artır.
        </div>
        <div class="card-tags">
            <span class="tag">Sınıflandırma</span>
            <span class="tag">Tahmin</span>
            <span class="tag">OEE</span>
        </div>
        <div class="card-arrow">Modüle Git →</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Modül 1 →", key="btn1", help="Duruş Sınıflandırma"):
        st.switch_page("pages/1_Durus_Siniflandirma.py")

with col2:
    st.markdown("""
    <div class="module-card card-2">
        <div class="card-number">Modül 02</div>
        <div class="card-icon-wrap">🔥</div>
        <div class="card-title">Fire Tahmini</div>
        <div class="card-desc">
            Üretim sürecinde oluşabilecek fire miktarını önceden tahmin et. Hammadde israfını azalt, maliyetleri düşür.
        </div>
        <div class="card-tags">
            <span class="tag">Regresyon</span>
            <span class="tag">Fire</span>
            <span class="tag">Maliyet</span>
        </div>
        <div class="card-arrow">Modüle Git →</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Modül 2 →", key="btn2", help="Fire Tahmini"):
        st.switch_page("pages/2_Fire_Tahmini.py")

with col3:
    st.markdown("""
    <div class="module-card card-3">
        <div class="card-number">Modül 03</div>
        <div class="card-icon-wrap">📈</div>
        <div class="card-title">Talep & Satış Tahmini</div>
        <div class="card-desc">
            Gelecekteki talep ve satış trendlerini yapay zeka ile tahmin et. Stok optimizasyonu ve planlama.
        </div>
        <div class="card-tags">
            <span class="tag">Zaman Serisi</span>
            <span class="tag">Satış</span>
            <span class="tag">Talep</span>
        </div>
        <div class="card-arrow">Modüle Git →</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Modül 3 →", key="btn3", help="Talep Tahmini"):
        st.switch_page("pages/3_Talep_Tahmini.py")

with col4:
    st.markdown("""
    <div class="module-card card-4">
        <div class="card-number">Modül 04</div>
        <div class="card-icon-wrap">⚙️</div>
        <div class="card-title">Üretim Süresi Tahmini</div>
        <div class="card-desc">
            Sipariş bazlı üretim sürelerini tahmin et. Kapasite planlaması yap, teslimat tarihlerini optimize et.
        </div>
        <div class="card-tags">
            <span class="tag">Kapasite</span>
            <span class="tag">Planlama</span>
            <span class="tag">Süre</span>
        </div>
        <div class="card-arrow">Modüle Git →</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Modül 4 →", key="btn4", help="Üretim Süresi"):
        st.switch_page("pages/4_Uretim_Suresi.py")

st.markdown("""
<div class="footer">
    <div class="footer-text">MDF Üretim AI Sistemi · Bitirme Projesi 2026 · Yapay Zeka Tabanlı Akıllı Üretim</div>
</div>
""", unsafe_allow_html=True) 
