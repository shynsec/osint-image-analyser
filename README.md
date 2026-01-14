# 🔍 OSINT Image Metadata Analyser

A containerized Python web application designed for digital investigators to extract, analyze, and visualize EXIF metadata from images.

## 🛠 Features
- **Technical Extraction:** Pulls Camera Make/Model, Software versions, and unique Image IDs.
- **GPS Visualization:** Automatically converts raw GPS coordinates and provides a direct Google Maps link.
- **Interactive Mapping:** Displays a pin on a built-in map using Streamlit.
- **Visual OSINT Fallback:** When metadata is stripped (e.g., from social media), the tool provides a checklist and links to external geolocation tools like Google Lens and Yandex.
- **Privacy Focused:** Runs locally via Docker; no data is sent to external servers.

## 🚀 Quick Start (Docker)

To run this tool without installing Python dependencies locally:

1. **Clone the repo:**
   \`\`\`bash
   git clone https://github.com/shynsec/osint-image-analyser.git
   cd osint-image-analyser
   \`\`\`

2. **Build & Run:**
   \`\`\`bash
   docker build -t osint-tool .
   docker run -d -p 8501:8501 --name my-analyser osint-tool
   \`\`\`

3. **Access:**
   Navigate to \`http://localhost:8501\` in your browser.

## 📸 Screenshots
*(Tip: Once you save this file, you can upload your screenshots to the repo and link them here!)*
![Main Dashboard](path/to/your/screenshot1.png)
![Map View](path/to/your/screenshot2.png)

## ⚖️ License
Distributed under the MIT License. See \`LICENSE\` for more information.
