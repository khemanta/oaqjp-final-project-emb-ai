
# 🧠 Emotion Detection Web App using IBM Watson NLP

This project is a part of the [IBM AI Engineering Professional Certificate](https://www.coursera.org/professional-certificates/ai-engineer) on Coursera. It demonstrates how to build and deploy an **AI-based web application** using Flask that detects emotions from text using **IBM Watson Embeddable AI Libraries**.

---

## 📌 Project Overview

This web app analyzes user-provided textual input and detects the **dominant emotion** expressed in it. The emotions include:

- 😠 Anger
- 🤢 Disgust
- 😨 Fear
- 😊 Joy
- 😢 Sadness

It makes use of IBM Watson's `EmotionPredict` model to perform real-time inference via HTTP POST request.

---

## 🛠️ Technologies Used

- Python 3.10+
- Flask
- HTML + JS (Bootstrap)
- IBM Watson NLP (embedded API)
- PyLint (for static code analysis)
- unittest (for testing)

---

## 🗂️ Project Structure

```
final_project/
├── EmotionDetection/                  # Python package for emotion detection
│   ├── __init__.py
│   └── emotion_detection.py
├── static/
│   └── mywebscript.js                 # JS logic for frontend interaction
├── templates/
│   └── index.html                     # UI template for web app
├── test_emotion_detection.py         # Unit tests
├── server.py                         # Flask backend
├── requirements.txt                  # (optional) Python dependencies
└── screenshots/                      # Saved screenshots for submission
```

---

## 🚀 Setup Instructions

### 1. Clone this repository

```bash
git clone https://github.com/khemanta/oaqjp-final-project-emb-ai.git
cd oaqjp-final-project-emb-ai
```

### 2. Install dependencies

```bash
pip install flask requests pylint
```

> ⚠️ The Watson NLP library is accessed via API. No installation needed.

---

## ▶️ Run the Web App

```bash
python3 server.py
```

Then open the app in your browser:

```
http://localhost:5000
```

> If using IBM Cloud IDE or Theia, use the proxy URL provided in the terminal output.

---

## ✅ Run Unit Tests

```bash
python3 -m unittest test_emotion_detection.py
```

---

## 🔎 Static Code Analysis (Optional)

Ensure PEP8 compliance using:

```bash
pylint server.py
```

Aim for a **10/10** score.

---

## 🖼️ Screenshots (for Coursera submission)

| Task | Screenshot |
|------|------------|
| Task 1 | `1_folder_structure.png` |
| Task 2a | `2a_emotion_detection.png` |
| Task 2b | `2b_application_creation.png` |
| Task 3a | `3a_output_formatting.png` |
| Task 3b | `3b_formatted_output_test.png` |
| Task 4a | `4a_packaging.png` |
| Task 4b | `4b_packaging_test.png` |
| Task 5a | `5a_unit_testing.png` |
| Task 5b | `5b_unit_testing_result.png` |
| Task 6a | `6a_server.png` |
| Task 6b | `6b_deployment_test.png` |
| Task 7a | `7a_error_handling_function.png` |
| Task 7b | `7b_error_handling_server.png` |
| Task 7c | `7c_error_handling_interface.png` |
| Task 8a | `8a_server_modified.png` |
| Task 8b | `8b_static_code_analysis.png` |

---

## 👤 Author

**Hemant, K.**  
Email: kumar.hemant.iitg@gmail.com  
GitHub: [@khemanta](https://github.com/khemanta)

---

## 🏁 License

This project is released under the [MIT License](LICENSE).
