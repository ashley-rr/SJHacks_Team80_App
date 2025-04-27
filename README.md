# Connect ♥️ Care

A bilingual (English and Spanish) mobilized web app that centralizes food, shelter, and healthcare resources for the City of San Jose — accessible anytime, anywhere.
*	**Backend API** serving real-time English and Spanish resource datasets
* **Category filtering** to quickly find food, shelter, or medical services
* **Mobile-friendly design** for accessibility on the go
*	**Faster access:** Users can instantly find available resources without navigating through external links

Connect Care increases access to essential services for underserved, multilingual communities across San José.

---
## 🛠️ Tech Stack
* **Frontend:** Javascript, Typescript, CSS, React.js, Next.js
* **Backend:** Python, Flask
* **Database:** Static JSON files (English + Spanish resource datasets)

---
## ⚙️ Setup Instructions
#### 1. Frontend (Next.js)
```
cd frontend
npm install
npm run dev
```
Visit http://localhost:3000 to see the web app.

#### 2. Backend (Flask API)
```
cd backend
python3 -m venv venv
source venv/bin/activate
pip install flask
python app.py
```
The backend will run on http://127.0.0.1:5000.

---
## 🌐 API Endpoints
| Route  | Method | Description |
| ------------- | ------------- | ------------- |
| /resources  | GET  | Returns all resources (default in English) |
| /resources?lang=es | GET  | Returns all resources in Spanish |
| /resources?category=food | GET | Filters resources by category |
| /health | GET | Simple health check to confirm backend is running |

**Example:**
```http://127.0.0.1:5000/resources?lang=es&category=shelter```

---
## 🏙️ About the Data 
This project used information from: 
* [City of San José: Homelessness Resources](https://www.sanjoseca.gov/your-government/departments-offices/housing/homelessness-response/homeless-families-individuals)
* [Second Harvest of Silicon Valley](https://www.shfb.org/get-food/?filter_mode=distribution/)
* [Interim Housing Communities](https://experience.arcgis.com/experience/f523b39c39c74af48890bcf0672e2457)
* [Valley Homeless Healthcare Program](https://scvmc.scvh.org/hospitals-clinics/valley-homeless-health-care-program-vhhp/about-us)

Instead of requiring users to visit **multiple external websites**, Connect Care brings everything together — offering **real-time**, **filtered**, and **bilingual** resource access.

---
## 👩‍💻 Meet the Team

| Name  | Role | Focus |
| ------------- | ------------- | ------------- |
| Ashley Roman  | [@ashley-rr](https://github.com/ashley-rr) | Frontend Developer  | Web design, UI/UX, React, Next.js |
| Julia Husainzada | [@juliahusainzada](https://github.com/juliahusainzada) | Backend Developer, Data Researcher  | Flask API, Database Management, Resource collection, Spanish translations |
| Meera Bhaskarbhai Vyas | [@meeraa-vyas](https://www.linkedin.com/in/meeraa-vyas/) | Designer | Visual design, Figma | User experience |

---
## 📚 Additional Notes
- Built during SJHacks 2025 🛠️
- Focused on real-world community impact 🌎
- Powered by teamwork, technology, and heart 🫶

