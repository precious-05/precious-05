<!DOCTYPE html>
<html>
<head>
<title>Alina Liaquat · AI & ML</title>
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }

body {
    background: #0a0618;
    font-family: 'Inter', -apple-system, sans-serif;
    display: flex;
    justify-content: center;
    padding: 2rem 1rem;
    color: #e8e0f5;
    line-height: 1.6;
    min-height: 100vh;
}

.container {
    max-width: 1200px;
    width: 100%;
    background: radial-gradient(ellipse at 50% 0%, #1a0f2e 0%, #0a0618 70%);
    border-radius: 3rem;
    padding: 2rem 2rem 1.5rem;
    box-shadow: 0 30px 60px -20px #000000, 
                0 0 0 1px rgba(157, 78, 221, 0.2),
                inset 0 0 100px rgba(157, 78, 221, 0.03);
    border: 1px solid rgba(157, 78, 221, 0.15);
    position: relative;
    overflow: hidden;
}

/* Animated gradient overlay */
.container::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle at 30% 20%, rgba(157, 78, 221, 0.05), transparent 50%),
                radial-gradient(circle at 70% 80%, rgba(60, 12, 108, 0.08), transparent 50%);
    animation: shimmer 15s ease-in-out infinite alternate;
    pointer-events: none;
    z-index: 0;
}

@keyframes shimmer {
    0% { transform: translate(0, 0) rotate(0deg); }
    100% { transform: translate(2%, 2%) rotate(3deg); }
}

/* ---- header wave ---- */
.capsule-header {
    width: 100%;
    margin-bottom: 1.8rem;
    border-radius: 2rem;
    overflow: hidden;
    position: relative;
    z-index: 1;
    box-shadow: 0 15px 40px -15px #9D4EDD44, 0 0 60px #3C096C22;
    transition: transform 0.3s ease;
}

.capsule-header:hover {
    transform: scale(1.01);
}

.capsule-header img {
    display: block;
    width: 100%;
    height: auto;
    object-fit: cover;
}

/* badges row - glassmorphism */
.badge-strip {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;
    gap: 0.6rem 1rem;
    margin: 1.2rem 0 1.8rem;
    position: relative;
    z-index: 1;
}

.badge-strip a, .badge-strip .badge {
    text-decoration: none;
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    background: rgba(30, 20, 50, 0.6);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    padding: 0.5rem 1.3rem;
    border-radius: 50px;
    font-weight: 600;
    font-size: 0.78rem;
    letter-spacing: 0.3px;
    border: 1px solid rgba(157, 78, 221, 0.2);
    color: #d4c8f0;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
}

.badge-strip a:hover {
    background: linear-gradient(135deg, #3C096C, #9D4EDD);
    border-color: #9D4EDD;
    color: white;
    transform: translateY(-2px) scale(1.03);
    box-shadow: 0 8px 30px #9D4EDD55, 0 0 40px #9D4EDD33;
}

.badge-strip .badge {
    cursor: default;
}

/* intro section */
.intro-section {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    align-items: center;
    justify-content: center;
    gap: 2.5rem 4rem;
    margin: 2rem 0 2.5rem;
    position: relative;
    z-index: 1;
}

.avatar {
    flex-shrink: 0;
    position: relative;
    padding: 4px;
    border-radius: 50%;
    background: conic-gradient(from 0deg, #9D4EDD, #3C096C, #140021, #9D4EDD);
    animation: rotateBorder 6s linear infinite;
    box-shadow: 0 0 60px #9D4EDD44, 0 0 120px #3C096C33;
}

@keyframes rotateBorder {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

.avatar img {
    display: block;
    width: 200px;
    height: 200px;
    object-fit: cover;
    border-radius: 50%;
    background: #0a0618;
    border: 3px solid #0a0618;
}

.about-text {
    max-width: 600px;
    background: rgba(20, 10, 35, 0.6);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    padding: 2rem 2.5rem;
    border-radius: 2.5rem;
    border: 1px solid rgba(157, 78, 221, 0.15);
    box-shadow: 0 20px 50px -15px #000000, inset 0 1px 0 rgba(157, 78, 221, 0.1);
    transition: all 0.3s ease;
}

.about-text:hover {
    border-color: rgba(157, 78, 221, 0.3);
    box-shadow: 0 25px 60px -15px #000000, 0 0 40px #9D4EDD11;
}

.about-text h2 {
    font-weight: 700;
    font-size: 1.9rem;
    background: linear-gradient(135deg, #d9b3ff, #b47aea, #9D4EDD);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 0.6rem;
}

.about-text p {
    color: #cfc8e6;
    font-weight: 300;
    font-size: 1rem;
    -webkit-text-fill-color: #cfc8e6;
}

/* tech pills - neon */
.tech-pills {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 0.5rem 0.9rem;
    margin: 1.5rem 0 2rem;
    position: relative;
    z-index: 1;
}

.tech-pills span {
    background: rgba(25, 15, 45, 0.7);
    backdrop-filter: blur(8px);
    padding: 0.35rem 1.2rem;
    border-radius: 50px;
    font-size: 0.78rem;
    font-weight: 500;
    color: #cbb7f0;
    border: 1px solid rgba(157, 78, 221, 0.2);
    box-shadow: 0 0 15px #3C096C22;
    transition: all 0.3s ease;
    letter-spacing: 0.2px;
}

.tech-pills span:hover {
    transform: translateY(-2px);
    border-color: #9D4EDD;
    box-shadow: 0 0 30px #9D4EDD44, inset 0 0 20px #9D4EDD11;
    background: rgba(60, 12, 108, 0.4);
}

/* section title with glow */
.section-title {
    font-size: 2rem;
    font-weight: 700;
    margin: 2.5rem 0 1.5rem;
    background: linear-gradient(135deg, #d9b3ff, #9D4EDD, #6b3f9e);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    display: inline-block;
    padding-bottom: 0.3rem;
    border-bottom: 3px solid #9D4EDD;
    text-shadow: 0 0 40px #9D4EDD33;
    position: relative;
    z-index: 1;
}

/* projects grid - glassmorphism cards */
.projects-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin: 1.8rem 0 2rem;
    position: relative;
    z-index: 1;
}

.project-card {
    background: rgba(18, 10, 35, 0.6);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    padding: 1.8rem 1.8rem;
    border-radius: 2rem;
    border: 1px solid rgba(157, 78, 221, 0.1);
    box-shadow: 0 8px 30px -10px #000000, inset 0 1px 0 rgba(157, 78, 221, 0.05);
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

.project-card:hover {
    transform: translateY(-8px) scale(1.01);
    border-color: rgba(157, 78, 221, 0.4);
    box-shadow: 0 20px 50px -15px #000000, 0 0 50px #9D4EDD22, inset 0 0 30px #9D4EDD08;
    background: rgba(25, 15, 45, 0.7);
}

.project-card h3 {
    font-weight: 700;
    font-size: 1.5rem;
    margin-bottom: 0.2rem;
    color: #dcc9ff;
}

.project-card .sub {
    font-weight: 600;
    font-size: 0.85rem;
    color: #b290da;
    margin-bottom: 0.8rem;
    display: block;
}

.project-card p {
    font-size: 0.95rem;
    color: #cbc2e0;
    margin-bottom: 1.2rem;
    font-weight: 300;
    line-height: 1.6;
}

.project-stack {
    display: flex;
    flex-wrap: wrap;
    gap: 0.4rem 0.6rem;
    margin-top: 0.6rem;
}

.project-stack span {
    background: rgba(60, 12, 108, 0.3);
    padding: 0.2rem 1rem;
    border-radius: 30px;
    font-size: 0.7rem;
    font-weight: 600;
    color: #b69fdb;
    border: 1px solid rgba(157, 78, 221, 0.15);
    transition: all 0.3s ease;
}

.project-stack span:hover {
    background: rgba(157, 78, 221, 0.2);
    border-color: #9D4EDD;
    color: #dcc9ff;
}

/* More builds */
.more-builds {
    background: rgba(15, 8, 28, 0.6);
    backdrop-filter: blur(8px);
    border-radius: 2rem;
    padding: 1.5rem 2rem;
    margin: 1.8rem 0;
    border: 1px solid rgba(157, 78, 221, 0.1);
    box-shadow: 0 10px 40px -15px #000000;
    position: relative;
    z-index: 1;
}

.more-builds > div:first-child {
    font-weight: 700;
    font-size: 1.3rem;
    margin-bottom: 0.8rem;
    color: #c7b0f0;
}

.build-row {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    align-items: center;
    padding: 0.8rem 0;
    border-bottom: 1px solid rgba(157, 78, 221, 0.08);
    gap: 0.5rem;
}

.build-row:last-child {
    border-bottom: none;
}

.build-row strong {
    color: #d7c4fc;
    font-weight: 600;
    min-width: 180px;
}

.build-row span {
    color: #b8a6d9;
    font-weight: 300;
    font-size: 0.95rem;
    flex: 1;
    padding: 0 0.5rem;
}

.build-stack {
    display: flex;
    flex-wrap: wrap;
    gap: 0.3rem 0.7rem;
}

.build-stack i {
    background: rgba(30, 18, 50, 0.5);
    padding: 0.15rem 0.9rem;
    border-radius: 30px;
    font-size: 0.7rem;
    font-weight: 500;
    color: #b595e6;
    border: 1px solid rgba(157, 78, 221, 0.1);
    font-style: normal;
    transition: all 0.3s ease;
}

.build-stack i:hover {
    background: rgba(60, 12, 108, 0.3);
    border-color: #9D4EDD;
}

/* toolbox - glass */
.toolbox {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;
    gap: 1.8rem 2.5rem;
    background: rgba(15, 8, 28, 0.5);
    backdrop-filter: blur(12px);
    padding: 1.8rem 1rem;
    border-radius: 4rem;
    margin: 2rem 0 1.8rem;
    border: 1px solid rgba(157, 78, 221, 0.08);
    box-shadow: 0 10px 40px -15px #000000;
    position: relative;
    z-index: 1;
}

.toolbox img {
    height: 46px;
    width: auto;
    filter: drop-shadow(0 0 10px #9D4EDD33);
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.toolbox img:hover {
    transform: scale(1.15) translateY(-3px);
    filter: drop-shadow(0 0 25px #9D4EDD66);
}

/* code block - neon glow */
.code-block {
    background: rgba(10, 5, 25, 0.8);
    backdrop-filter: blur(8px);
    padding: 1.5rem 2rem;
    border-radius: 2rem;
    border-left: 6px solid #9D4EDD;
    margin: 1.8rem 0 2rem;
    font-family: 'Inter', 'SF Mono', monospace;
    font-size: 0.9rem;
    color: #cbbcf0;
    box-shadow: 0 10px 40px -15px #000000, inset 0 0 50px #9D4EDD08;
    position: relative;
    z-index: 1;
    border: 1px solid rgba(157, 78, 221, 0.1);
}

.code-block span.keyword { color: #b48ad9; font-weight: 700; }
.code-block span.string { color: #7fc9a8; }
.code-block span.comment { color: #6d5f83; font-style: italic; }

/* contribution */
.contribution {
    margin: 2rem 0 1.8rem;
    border-radius: 2rem;
    overflow: hidden;
    box-shadow: 0 0 60px #1f0e2e44;
    position: relative;
    z-index: 1;
    border: 1px solid rgba(157, 78, 221, 0.05);
}

.contribution img {
    display: block;
    width: 100%;
    height: auto;
    background: #0a0618;
}

/* building badges - neon pills */
.building-badges {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 0.8rem 1.2rem;
    margin: 1.8rem 0;
    position: relative;
    z-index: 1;
}

.building-badges span {
    background: rgba(20, 10, 40, 0.7);
    backdrop-filter: blur(8px);
    padding: 0.5rem 1.8rem;
    border-radius: 50px;
    font-weight: 600;
    font-size: 0.85rem;
    border: 1px solid rgba(157, 78, 221, 0.15);
    color: #d6c2fc;
    transition: all 0.3s ease;
    box-shadow: 0 4px 20px rgba(0,0,0,0.2);
}

.building-badges span:hover {
    transform: translateY(-2px);
    border-color: #9D4EDD;
    box-shadow: 0 8px 30px #9D4EDD33;
    background: rgba(60, 12, 108, 0.3);
}

/* model lab animation */
.model-lab {
    text-align: center;
    margin: 1.5rem 0 2rem;
    position: relative;
    z-index: 1;
}

.model-lab img {
    width: 85%;
    border-radius: 2rem;
    background: rgba(10, 5, 25, 0.6);
    padding: 0.5rem;
    border: 1px solid rgba(157, 78, 221, 0.05);
    box-shadow: 0 10px 40px -15px #000000;
    transition: all 0.3s ease;
}

.model-lab img:hover {
    border-color: rgba(157, 78, 221, 0.2);
    box-shadow: 0 10px 50px -15px #000000, 0 0 60px #9D4EDD11;
}

/* FOOTER wave */
.footer-wave {
    margin-top: 2.5rem;
    width: 100%;
    border-radius: 2rem;
    overflow: hidden;
    position: relative;
    z-index: 1;
    box-shadow: 0 -10px 40px -15px #9D4EDD44;
}

.footer-wave img {
    display: block;
    width: 100%;
    height: auto;
}

/* responsive */
@media (max-width: 700px) {
    .container { padding: 1rem; }
    .intro-section { flex-direction: column; text-align: center; }
    .about-text { padding: 1.5rem; }
    .avatar img { width: 150px; height: 150px; }
    .build-row { flex-direction: column; align-items: flex-start; gap: 0.4rem; }
    .section-title { font-size: 1.6rem; }
    .projects-grid { grid-template-columns: 1fr; }
}
</style>
</head>
<body>

<div class="container">

<!-- HEADER wave -->
<div class="capsule-header">
    <img src="https://capsule-render.vercel.app/api?type=waving&height=220&color=0:140021,50:3C096C,100:9D4EDD&text=Alina%20Liaquat&fontColor=ffffff&fontSize=52&fontAlignY=38&desc=AI%20%7C%20Machine%20Learning%20%7C%20Deep%20Learning%20%7C%20NLP&descSize=17&descAlignY=58" alt="header capsule" />
</div>

<!-- Badge strip -->
<div class="badge-strip">
    <a href="https://www.linkedin.com/in/alina-liaquat-779347325/" target="_blank">🔗 LinkedIn</a>
    <span class="badge">👁️ 1.2k views</span>
    <span class="badge">🧠 AI + ML</span>
    <span class="badge">🤖 Deep Learning</span>
    <span class="badge">🗣️ NLP</span>
</div>

<!-- intro: avatar + about -->
<div class="intro-section">
    <div class="avatar">
        <img src="./assets/girl.gif" alt="Alina avatar" />
    </div>
    <div class="about-text">
        <h2>👩🏻‍💻 Alina Liaquat</h2>
        <p>Computer Science undergraduate building practical AI, machine learning, and data-driven applications. I turn real-world problems into working systems: crop disease detection, forest fire risk, clinical safety, health prediction, and interactive ML products.</p>
    </div>
</div>

<!-- tech pills -->
<div class="tech-pills">
    <span>Python</span><span>Java</span><span>C++</span><span>C</span>
    <span>TensorFlow</span><span>PyTorch</span><span>NLP</span>
    <span>scikit-learn</span><span>FastAPI</span><span>Streamlit</span>
    <span>Android</span><span>PostgreSQL</span><span>MongoDB</span><span>Git</span>
</div>

<!-- Projects -->
<h2 class="section-title">✦ Featured Projects</h2>
<div class="projects-grid">
    <div class="project-card">
        <h3>Bazgar AI</h3>
        <span class="sub">Apple Disease Detection · Smart Farming</span>
        <p>Full-stack AI for Balochi farmers: real-time leaf disease diagnostics, localized treatment, Balochi voice guidance, and UCB1 reinforcement crop assistant.</p>
        <div class="project-stack"><span>Python</span><span>FastAPI</span><span>TensorFlow Lite</span><span>JavaScript</span></div>
    </div>
    <div class="project-card">
        <h3>EcoSafe AI</h3>
        <span class="sub">Forest Fire Detection & Risk Analysis</span>
        <p>Offline-first Android with dynamic risk mapping, CameraX capture, TensorFlow Lite fire classification, and FastAPI backend.</p>
        <div class="project-stack"><span>Java</span><span>Android Studio</span><span>Google Maps</span><span>SQLite</span></div>
    </div>
    <div class="project-card">
        <h3>ThyroAssess AI</h3>
        <span class="sub">Thyroid Cancer Risk Assessment</span>
        <p>ML web app trained on 200K+ records, EDA, Logistic Regression, FastAPI + MongoDB, Vercel deployment.</p>
        <div class="project-stack"><span>scikit-learn</span><span>FastAPI</span><span>MongoDB</span><span>Vercel</span></div>
    </div>
    <div class="project-card">
        <h3>MediNomix</h3>
        <span class="sub">Medication Error Prevention</span>
        <p>Clinical DB for LASA medication errors: phonetic similarity, OpenFDA ETL, Streamlit, Neon PostgreSQL.</p>
        <div class="project-stack"><span>Streamlit</span><span>PostgreSQL</span><span>OpenFDA</span><span>ETL</span></div>
    </div>
    <div class="project-card">
        <h3>Prosperous Farmer</h3>
        <span class="sub">Agriculture Data Web App</span>
        <p>Bilingual Urdu-English dashboard for crop tracking, CRUD, CSV exports, interactive yield analytics.</p>
        <div class="project-stack"><span>Streamlit</span><span>Pandas</span><span>Plotly</span><span>Neon</span></div>
    </div>
    <div class="project-card">
        <h3>Dakati Game</h3>
        <span class="sub">Dacoit-Themed Social Deduction</span>
        <p>Cross-platform game with Kivy GUI, trigonometry-based circular layout, voting logic, Android packaging.</p>
        <div class="project-stack"><span>Python</span><span>Kivy</span><span>Buildozer</span><span>Game Logic</span></div>
    </div>
</div>

<!-- More builds -->
<div class="more-builds">
    <div>📦 More Builds</div>
    <div class="build-row">
        <strong>US Natural Resources Revenue EDA</strong>
        <span>Cleaned, transformed, explored monthly revenue; visual dashboards.</span>
        <div class="build-stack"><i>NumPy</i><i>Pandas</i><i>Seaborn</i><i>Matplotlib</i></div>
    </div>
    <div class="build-row">
        <strong>Arduino Voice & Bluetooth Robot Car</strong>
        <span>Voice & Bluetooth controlled robot with real‑time response.</span>
        <div class="build-stack"><i>Arduino</i><i>C</i><i>Bluetooth</i><i>Voice Recognition</i></div>
    </div>
</div>

<!-- Toolbox -->
<div class="toolbox">
    <img src="https://www.vectorlogo.zone/logos/python/python-icon.svg" alt="Python" />
    <img src="https://www.vectorlogo.zone/logos/tensorflow/tensorflow-icon.svg" alt="TensorFlow" />
    <img src="https://cdn.simpleicons.org/fastapi/009688" height="46" alt="FastAPI" />
    <img src="https://www.vectorlogo.zone/logos/java/java-icon.svg" alt="Java" />
    <img src="https://www.vectorlogo.zone/logos/android/android-icon.svg" alt="Android" />
    <img src="https://www.vectorlogo.zone/logos/postgresql/postgresql-icon.svg" alt="PostgreSQL" />
    <img src="https://www.vectorlogo.zone/logos/mongodb/mongodb-icon.svg" alt="MongoDB" />
    <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="Git" />
    <img src="https://www.vectorlogo.zone/logos/vercel/vercel-icon.svg" alt="Vercel" />
</div>

<!-- code snippet -->
<div class="code-block">
    <span class="keyword">class</span> AlinaLiaquat:<br>
    &nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">focus</span> = [<span class="string">"Machine Learning"</span>, <span class="string">"Deep Learning"</span>, <span class="string">"NLP"</span>, <span class="string">"AI Applications"</span>, <span class="string">"Full-Stack Projects"</span>]<br>
    &nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">current_stack</span> = [<span class="string">"Python"</span>, <span class="string">"FastAPI"</span>, <span class="string">"TensorFlow Lite"</span>, <span class="string">"Scikit-learn"</span>, <span class="string">"Streamlit"</span>]<br>
    &nbsp;&nbsp;&nbsp;&nbsp;<span class="keyword">build_style</span> = <span class="string">"turn models, data, and interfaces into useful real-world systems"</span>
</div>

<!-- contribution grid (neon) -->
<div class="contribution">
    <img src="./assets/neon-contribution-grid.svg" alt="contribution grid" />
</div>

<!-- building around -->
<div class="building-badges">
    <span>🌱 AI for Agriculture</span>
    <span>❤️ Health AI</span>
    <span>📈 ML Pipelines</span>
    <span>📱 Android ML</span>
</div>

<!-- model lab animation -->
<div class="model-lab">
    <img src="./assets/model-lab-animation.svg" alt="model lab animation" />
</div>

<!-- FOOTER wave -->
<div class="footer-wave">
    <img src="https://capsule-render.vercel.app/api?type=waving&height=120&section=footer&color=0:9D4EDD,50:3C096C,100:140021" alt="footer wave" />
</div>

</div>
</body>
</html>
