> ⚠️ **Note:** Before exploring this repository, I highly recommend checking out the project [**A Machine Learning Based Crop Recommendation System**](https://github.com/anant13sharma/A-Machine-Learning-Based-Crop-Recommendation-System), where I’ve thoroughly explained how I trained and evaluated various models including **Logistic Regression**, **Naive Bayes**, **Decision Tree**, **Random Forest**, and a **Neural Network (MLPClassifier)**. It will give you a much better understanding of the approach and methodology used here.


#  Crop Recommendation System by Anant Sharma

A machine learning-based web application that predicts the most suitable crop to cultivate based on soil nutrients and environmental conditions like temperature, pH, and rainfall.

![ezgif com-animated-gif-maker-3](https://github.com/user-attachments/assets/e99713f8-e277-47cb-8be4-c47af27a402c)

---
## Dataset

The dataset used in this project was compiled by the **Indian Council of Agricultural Research (ICAR)** and made publicly available by the **Indian Chamber of Food and Agriculture (ICFA)**. It includes soil nutrient ratios (N, P, K, C, S, Mg, Fe, Mn), pH levels, temperature, humidity, and rainfall data across 69,718 samples covering 22 crops.

- **Source:** Indian Chamber of Food and Agriculture (ICFA)  
- **Accessed from:** [Figshare - Crop Recommendation Dataset](https://figshare.com/articles/dataset/Crop_Recommendation_dataset/26308696)

---

##  Features

-  Predicts the best crop to grow based on 12 inputs
-  Beautiful responsive UI built with Bootstrap & Vanta.js live background
-  Neural Network model trained on 69,000+ samples
-  Model accuracy: ~99.4%
-  Normalized and encoded data using Scikit-learn
-  Model, encoder, and scaler saved as `.pkl` files for deployment

---

##  Tech Stack

| Frontend      | Backend         | ML Model         | Tools          |
|---------------|------------------|------------------|----------------|
| HTML, CSS, Bootstrap 5, FontAwesome, Vanta.js | Flask, Jinja2        | MLPClassifier (Scikit-learn) | Python, Pandas, NumPy, Scikit-learn, joblib |

---

##  Model Inputs

| Feature          | Unit        |
|------------------|-------------|
| Nitrogen (N)     | mg/kg       |
| Phosphorus (P)   | mg/kg       |
| Potassium (K)    | mg/kg       |
| Temperature      | °C          |
| Humidity         | %           |
| pH               | -           |
| Rainfall         | mm          |
| Carbon (C)       | %           |
| Sulfur (S)       | mg/kg       |
| Magnesium (Mg)   | mg/kg       |
| Iron (Fe)        | mg/kg       |
| Manganese (Mn)   | mg/kg       |

---

## 📁 Folder Structure

```
Crop-Recommendation/
│
├── app.py                      # Flask backend
├── requirements.txt            # Project dependencies
├── Procfile                    # For Railway deployment
│
├── Model/
│   ├── crop_recommendation_model.pkl
│   ├── label_encoder.pkl
│   └── scaler.pkl
│
├── templates/
│   └── index.html              # UI form + results
│
├── static/                     # (Optional CSS, images)
```

---

## ⚙️ How to Run Locally

1. **Clone the repo**
   ```bash
   git clone https://github.com/anant13sharma/crop-recommendation-app.git
   cd crop-recommendation-app
   ```

2. **Create virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**
   ```bash
   python app.py
   ```

5. **Open in browser**
   ```
   http://127.0.0.1:5000
   ```

---

##  Live Demo

> 🔗 [Hosted on Railway](https://your-deployed-link-if-any.railway.app)

---

##  About Me

👨‍💻 **Anant Sharma**  
📸 [Instagram](https://www.instagram.com/therealanantsharma)  
💼 [LinkedIn](https://www.linkedin.com/in/anant13sharma/)  
💻 [GitHub](https://github.com/anant13sharma)

---

##  License

MIT License. Use it freely, improve it, and grow more crops 

---

> *“Grow smart. Code smarter.” — Anant Sharma*
