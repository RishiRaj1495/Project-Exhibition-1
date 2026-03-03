<div align="center"> <h1>🚀 Electricity Bill Project 2.0 </h1>
  <br>
  <b>A modern Streamlit web app for electricity bill calculation, tracking, and management</b> </div><br/><h2>✨ <b>Key Features</b></h2><ul><li>⚡ <b>Real-time bill calculations</b></li><li>📱 <b>Fully responsive UI</b> (Desktop + Mobile)</li><li>🔧 <b>Customizable tariff rates</b></li><li>📊 <b>Bill breakdown & history</b></li><li>🚀 <b>One-click deployment</b> to Streamlit Cloud</li></ul><h2>🛠️ <b>Tech Stack</b></h2><table><thead><tr><th>Frontend</th><th>Backend</th><th>Tools</th></tr></thead><tbody><tr><td>Streamlit</td><td>Python</td><td>VS Code</td></tr><tr><td>HTML/CSS/JS</td><td>Pandas</td><td>GitHub</td></tr></tbody></table><h2>🚀 <b>Quick Start</b> *(Windows)*</h2><h3>📥 <b>Step 1: Navigate to Project</b></h3><pre><code>C:
cd C:\Users\RISHI\OneDrive\Documents\electricitybillproject2.0</code></pre><h3>▶️ <b>Step 2: Launch App</b></h3><pre><code>python -m streamlit run app.py</code></pre><h3>🌐 <b>Step 3: Open Browser</b></h3><pre><code>✅ App running at: http://localhost:8501</code></pre><div align="center"><img src="https://img.shields.io/badge/Ready%20in-30s-brightgreen"></div><h2>📦 <b>Installation</b></h2><h3><b>1. Dependencies</b> (Create <code>requirements.txt</code>)</h3><pre><code>streamlit&gt;=1.28.0
pandas&gt;=2.0.0
plotly&gt;=5.15.0
numpy&gt;=1.24.0</code></pre><h3><b>2. Install</b></h3><pre><code>pip install -r requirements.txt</code></pre><h2>📁 <b>Project Structure</b></h2><pre><code>electricitybillproject2.0/
├── app.py                 # 🎯 Main Streamlit App
├── requirements.txt       # 📦 Dependencies
├── pages/                 # 📄 Additional Pages
│   └── 1_📊_History.py
├── data/                  # 💾 Sample Data
│   └── tariffs.csv
├── utils/                 # ⚙️ Helper Functions
│   └── calculator.py
└── README.md             # 📖 This file!</code></pre><h2>💻 <b>How to Use</b></h2><ol><li><b>Launch</b> → <code>python -m streamlit run app.py</code></li><li><b>Input</b> → Units consumed, tariff slab</li><li><b>Calculate</b> → Instant bill breakdown</li><li><b>Export</b> → PDF/CSV reports</li></ol><h3><b>Sample Calculation</b></h3><table><thead><tr><th>Units</th><th>Slab Rate</th><th>Fixed Charges</th><th>Total</th></tr></thead><tbody><tr><td>0-100</td><td>₹6.50</td><td>₹100</td><td>₹750</td></tr><tr><td>101-300</td><td>₹7.50</td><td>₹150</td><td>₹1,950</td></tr><tr><td>300+</td><td>₹8.50</td><td>₹200</td><td>₹3,250</td></tr></tbody></table><h2>☁️ <b>Deployment Guide</b></h2><h3><b>Streamlit Cloud</b> *(Free & Easy)*</h3><pre><code>1️⃣ Push to GitHub
2️⃣ Visit share.streamlit.io
3️⃣ Connect repo → Deploy ✅</code></pre><h2>🔧 <b>Development Commands</b></h2><pre><code># Development
streamlit run app.py --server.port 8501 --server.headless false

# Production
streamlit run app.py --server.headless true --server.port 80</code></pre><h2>🐛 <b>Troubleshooting</b></h2><table><thead><tr><th>Issue</th><th>Solution</th></tr></thead><tbody><tr><td><code>streamlit: command not found</code></td><td><code>pip install streamlit</code></td></tr><tr><td><code>Port 8501 busy</code></td><td><code>--server.port 8502</code></td></tr><tr><td><code>Module not found</code></td><td><code>pip install -r requirements.txt</code></td></tr></tbody></table><h2>👥 <b>Drafted by:</b></h2><div align="center"><ol><li><b>Rishi Raj</b> (24BCE10149) - Project Lead & Frontend</li><li><b>Abhilash Singh</b> (24BCE10706) - Backend Logic</li><li><b>Arnab Kumar</b> (24BCE11017) - UI/UX Design</li><li><b>Brotodeep Pal</b> (24BC10477) - Testing & Deployment</li></ol><table><tr><td>🏫 Computer Science Engineering</td></tr></table><a href="https://github.com/RishiRaj1495"><img src="https://img.shields.io/badge/GitHub-Follow%20Us-181717?style=for-the-badge&logo=github&logoColor=white"></a></div><hr/><div align="center">**Built with ❤️ by Team Electricity Bill**<br/>⭐ <b>Star this repo if it helps you!</b><br/><img src="https://img.shields.io/badge/Setup%20Time-30s-brightgreen"><img src="https://img.shields.io/badge/Deployment-Free-blue"></div>
