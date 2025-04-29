
# 🚀 Roloi: Smartwatch for Martian Colonists  

**Mission:** Enable sustainable human habitation on Mars by combating dust storms and health risks.  

**Features:**  
- 🌪️ 6-days forecasts (NASA InSight API)  
- ❤️ Astronaut vital monitoring  
- 🔋 Storm alerts to protect equipment  

**Description**: All the data is being consumed from NASA's InSight Mars Weather API. However, the information provided by this API is not synchronized with real-time stats because the rover, unfortunately, stopped working due to the dust storms.

---

## 🛠️ One-Click Setup  

### 1. Create & Activate Virtual Environment  
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Django Server
```bash
python manage.py runserver
```
