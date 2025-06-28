📄 Resume Skills Extractor & Job Finder 🚀

An AI-powered tool to extract skills from resumes and find relevant job opportunities in just a few clicks!

✨ Features

✅ Upload Resume Image – Extract skills from an image-based resume using OCR.
✅ Intelligent Skill Extraction – Uses advanced text processing to detect skills.
✅ AI-Powered Job Search – Fetches relevant job listings based on extracted skills.
✅ Clickable Job Links – Open job postings directly from the app.
✅ User-Friendly Interface – Clean and modern UI for seamless interaction.
✅ Reset & Refresh – Easily clear extracted data and start fresh.
Ai

🛠 Technologies Used

🔹 Python – Core programming language.
🔹 OpenCV – Image processing and enhancement.
🔹 Tesseract OCR – Optical character recognition for text extraction.
🔹 Tkinter & ttkbootstrap – GUI design and user experience.
🔹 Requests – Fetching job listings via API.
🔹 PIL (Pillow) – Image handling and processing.
🔹 Regular Expressions (Regex) – Smart text extraction.
🔹 SerpAPI – Job search API integration.

🚀 Installation & Setup

📌 Prerequisites

Before running this project, ensure that you have the following:
✅ Python 3.x installed.
✅ Tesseract-OCR installed (Download from Tesseract GitHub).
✅ Required Python libraries installed.

🔧 Install Required Dependencies

Run the following command to install all necessary libraries:

pip install opencv-python pytesseract ttkbootstrap requests pillow

⚙ Configure Tesseract

Set the correct path to Tesseract OCR in the script:

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

Modify this path based on your system setup.

🎯 How to Use

1️⃣ Run the Python script:

python script.py

2️⃣ Upload Resume Image – Click "Select Resume" and choose an image.
3️⃣ Extract Skills – The extracted skills will be displayed automatically.
4️⃣ Find Jobs – Click "Find Jobs" to fetch job opportunities.
5️⃣ Explore Listings – Click on "Click Here" to view job details online.
6️⃣ Reset Data – Click "Clear" to start fresh.

⚙ Configuration

🔹 Replace SERPAPI_KEY in the script with your actual SerpAPI key:

SERPAPI_KEY = "Your-SerpAPI-Key"

Get an API key from SerpAPI.

🛠 Troubleshooting & FAQs

❓ Tesseract OCR is not working?
✔ Ensure the correct path is set in the script.
✔ Confirm Tesseract is installed and added to system PATH.

❓ Job listings are not appearing?
✔ Check your internet connection.
✔ Verify that your SERPAPI_KEY is valid and not expired.
✔ Ensure your API request limit has not been exceeded.

