<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Alina Liaquat · AI & ML</title>
    <!-- Font Awesome for icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <!-- Google Font (Inter) -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,300;14..32,400;14..32,600;14..32,700;14..32,800&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            background-color: #0d0b1a; /* deep dark base */
            font-family: 'Inter', sans-serif;
            display: flex;
            justify-content: center;
            padding: 2rem 1rem;
            color: #eae6f0;
            line-height: 1.5;
        }

        .container {
            max-width: 1200px;
            width: 100%;
            background: rgba(18, 15, 30, 0.7);
            backdrop-filter: blur(2px);
            border-radius: 2.5rem;
            padding: 2rem 2rem 1.5rem;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.8), 0 0 0 1px rgba(157, 78, 221, 0.15);
            border: 1px solid rgba(157, 78, 221, 0.2);
        }

        /* ---- header wave (capsule) ---- */
        .capsule-header {
            width: 100%;
            margin-bottom: 1.5rem;
            border-radius: 2rem;
            overflow: hidden;
            box-shadow: 0 10px 30px -10px #14002166;
        }
        .capsule-header img {
            display: block;
            width: 100%;
            height: auto;
            object-fit: cover;
        }

        /* badges row */
        .badge-strip {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            align-items: center;
            gap: 0.75rem 1rem;
            margin: 1.2rem 0 1.8rem;
        }

        .badge-strip a, .badge-strip .badge {
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            background: rgba(30, 25, 50, 0.7);
            backdrop-filter: blur(4px);
            padding: 0.4rem 1rem;
            border-radius: 40px;
            font-weight: 600;
            font-size: 0.8rem;
            letter-spacing: 0.3px;
            border: 1px solid rgba(157, 78, 221, 0.25);
            color: #ddd8f0;
            transition: all 0.2s;
        }
        .badge-strip a:hover {
            background: #3C096C;
            border-color: #9D4EDD;
            color: white;
            transform: scale(1.02);
            box-shadow: 0 0 15px #9D4EDD55;
        }
        .badge-strip i {
            font-size: 1rem;
            color: #b48ad9;
        }

        /* avatar + about */
        .intro-section {
            display: flex;
            flex-direction: row;
            flex-wrap: wrap;
            align-items: center;
            justify-content: center;
            gap: 2rem 3rem;
            margin: 2rem 0 2.5rem;
        }

        .avatar {
            flex-shrink: 0;
            background: radial-gradient(circle at 30% 30%, #2e1a47, #140021);
            padding: 0.4rem;
            border-radius: 50%;
            box-shadow: 0 0 40px #9D4EDD33, 0 0 80px #3C096C22;
            border: 2px solid #9D4EDD88;
        }
        .avatar img {
            display: block;
            width: 200px;
            height: 200px;
            object-fit: cover;
            border-radius: 50%;
            background: #1f1430;
        }

        .about-text {
            max-width: 600px;
            background: rgba(20, 10, 35, 0.5);
            backdrop-filter: blur(4px);
            padding: 1.8rem 2.2rem;
            border-radius: 2.5rem;
            border-left: 4px solid #9D4EDD;
            border-right: 4px solid #3C096C;
            box-shadow: 0 8px 20px -8px #00000080;
        }
        .about-text h2 {
            font-weight: 700;
            font-size: 1.7rem;
            background: linear-gradient(135deg, #d9b3ff, #b47aea);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 0.5rem;
        }
        .about-text p {
            color: #cfc8e6;
            font-weight: 300;
            font-size: 1rem;
        }

        /* tech stack pills */
        .tech-pills {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 0.6rem 1rem;
            margin: 1.5rem 0 2rem;
        }
        .tech-pills span {
            background: #1d1630;
            padding: 0.3rem 1.1rem;
            border-radius: 40px;
            font-size: 0.8rem;
            font-weight: 500;
            color: #cbb7f0;
            border: 1px solid #4d2b70;
            box-shadow: 0 0 8px #3C096C33;
            letter-spacing: 0.2px;
        }

        /* projects grid */
        .section-title {
            font-size: 1.9rem;
            font-weight: 700;
            margin: 2.2rem 0 1.2rem;
            background: linear-gradient(135deg, #c9adff, #a06cdb);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            display: inline-block;
            border-bottom: 3px solid #6b3f9e;
            padding-bottom: 0.3rem;
        }

        .projects-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 1.8rem;
            margin: 1.5rem 0 2rem;
        }

        .project-card {
            background: #151029;
            padding: 1.5rem 1.6rem;
            border-radius: 2rem;
            border: 1px solid #3f2a5a;
            box-shadow: 0 6px 18px #00000055;
            transition: all 0.25s ease;
            backdrop-filter: blur(2px);
        }
        .project-card:hover {
            transform: translateY(-6px);
            border-color: #9D4EDD;
            box-shadow: 0 15px 30px -10px #3C096C99, 0 0 0 1px #9D4EDD55;
            background: #1c1433;
        }
        .project-card h3 {
            font-weight: 700;
            font-size: 1.4rem;
            margin-bottom: 0.3rem;
            color: #dcc9ff;
        }
        .project-card .sub {
            font-weight: 600;
            font-size: 0.9rem;
            color: #b290da;
            margin-bottom: 0.75rem;
            display: block;
        }
        .project-card p {
            font-size: 0.95rem;
            color: #cbc2e0;
            margin-bottom: 1rem;
            font-weight: 300;
        }
        .project-stack {
            display: flex;
            flex-wrap: wrap;
            gap: 0.4rem 0.6rem;
            margin-top: 0.6rem;
        }
        .project-stack span {
            background: #261e3b;
            padding: 0.15rem 0.9rem;
            border-radius: 30px;
            font-size: 0.7rem;
            font-weight: 600;
            color: #b69fdb;
            border: 1px solid #4a2e6b;
        }

        /* More builds (table style) */
        .more-builds {
            background: #100c20;
            border-radius: 2rem;
            padding: 1.2rem 1.8rem;
            margin: 1.8rem 0;
            border: 1px solid #34264a;
        }
        .build-row {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
            align-items: center;
            padding: 0.7rem 0;
            border-bottom: 1px solid #2f1f47;
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
            background: #1f1732;
            padding: 0.1rem 0.8rem;
            border-radius: 30px;
            font-size: 0.7rem;
            font-weight: 500;
            color: #b595e6;
            border: 1px solid #412f59;
            font-style: normal;
        }

        /* toolbox */
        .toolbox {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            align-items: center;
            gap: 1.5rem 2.2rem;
            background: #130e22;
            padding: 1.5rem 0.5rem;
            border-radius: 3rem;
            margin: 2rem 0 1.5rem;
            border: 1px solid #382a50;
        }
        .toolbox img {
            height: 44px;
            width: auto;
            filter: drop-shadow(0 0 6px #763fa8);
            transition: 0.2s;
        }
        .toolbox img:hover {
            transform: scale(1.12);
            filter: drop-shadow(0 0 14px #b47aea);
        }

        /* code snippet */
        .code-block {
            background: #0f0b1c;
            padding: 1.2rem 1.8rem;
            border-radius: 2rem;
            border-left: 6px solid #9D4EDD;
            margin: 1.5rem 0 2rem;
            font-family: 'Inter', monospace;
            font-size: 0.9rem;
            color: #cbbcf0;
            box-shadow: inset 0 0 30px #00000066;
        }
        .code-block span.keyword { color: #b48ad9; font-weight: 600; }
        .code-block span.string { color: #a7d0b0; }
        .code-block span.comment { color: #6d5f83; font-style: italic; }

        /* contribution */
        .contribution {
            margin: 2rem 0 1.5rem;
            border-radius: 2rem;
            overflow: hidden;
            box-shadow: 0 0 40px #1f0e2e;
        }
        .contribution img {
            display: block;
            width: 100%;
            height: auto;
            background: #0d091a;
        }

        /* building badges */
        .building-badges {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 0.8rem 1.2rem;
            margin: 1.8rem 0;
        }
        .building-badges span {
            background: #1d1433;
            padding: 0.4rem 1.5rem;
            border-radius: 40px;
            font-weight: 600;
            font-size: 0.85rem;
            border: 1px solid #6a3f94;
            color: #d6c2fc;
            backdrop-filter: blur(2px);
        }
        .building-badges i {
            margin-right: 0.4rem;
            color: #b185e6;
        }

        .footer-wave {
            margin-top: 2rem;
            width: 100%;
            border-radius: 2rem;
            overflow: hidden;
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
            .about-text { padding: 1.2rem; }
            .avatar img { width: 140px; height: 140px; }
            .build-row { flex-direction: column; align-items: flex-start; gap: 0.3rem; }
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
        <a href="https://www.linkedin.com/in/alina-liaquat-779347325/" target="_blank"><i class="fab fa-linkedin-in"></i> LinkedIn</a>
        <span class="badge"><i class="fas fa-eye"></i> 1.2k views</span>
        <span class="badge"><i class="fas fa-brain"></i> AI + ML</span>
        <span class="badge"><i class="fas fa-robot"></i> Deep Learning</span>
        <span class="badge"><i class="fas fa-language"></i> NLP</span>
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
    <h2 class="section-title"><i class="fas fa-code" style="margin-right: 10px; color: #9D4EDD;"></i> Featured Projects</h2>
    <div class="projects-grid">
        <!-- card 1 -->
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
        <div style="font-weight: 700; font-size: 1.2rem; margin-bottom: 0.5rem; color: #c7b0f0;"><i class="fas fa-cubes" style="margin-right: 10px;"></i>More Builds</div>
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
        <img src="https://cdn.simpleicons.org/fastapi/009688" height="44" alt="FastAPI" />
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
        <span><i class="fas fa-seedling"></i> AI for Agriculture</span>
        <span><i class="fas fa-heartbeat"></i> Health AI</span>
        <span><i class="fas fa-chart-line"></i> ML Pipelines</span>
        <span><i class="fab fa-android"></i> Android ML</span>
    </div>

    <!-- model lab animation -->
    <div style="text-align: center; margin: 1rem 0 1.5rem;">
        <img src="./assets/model-lab-animation.svg" width="85%" alt="model lab animation" style="border-radius: 2rem; background: #0b0718; padding: 0.3rem;" />
    </div>

    <!-- FOOTER wave -->
    <div class="footer-wave">
        <img src="https://capsule-render.vercel.app/api?type=waving&height=120&section=footer&color=0:9D4EDD,50:3C096C,100:140021" alt="footer wave" />
    </div>

</div>
</body>
</html>
