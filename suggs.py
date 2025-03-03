import cv2
import pytesseract
import ttkbootstrap as ttk
import requests
import webbrowser
from tkinter import filedialog, Text, Label, messagebox, Scrollbar
import re
from PIL import Image, ImageTk


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
SERPAPI_KEY = "Enter Your API"
def extract_text(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    processed = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    return pytesseract.image_to_string(processed)
def extract_skills_section(text):
    match = re.search(r'(?i)(?:SKILLS|Technical Skills|Expertise)[\s:\n]+([\s\S]+?)(?=\n[A-Z]{2,}|\Z)', text)
    if match:
        skills = re.sub(r'\n+', ', ', match.group(1).strip())
        return skills
    return "❌ Skills section not found."

def fetch_jobs(skills):
    if not skills or "❌" in skills:
        messagebox.showwarning("Warning", "No skills extracted. Cannot fetch jobs.")
        return None

    skill_list = [s.strip() for s in skills.split(",") if s.strip()]
    skill_batches = [", ".join(skill_list[i:i+3]) for i in range(0, len(skill_list), 3)]

    all_jobs = []
    for query in skill_batches:
        url = "https://serpapi.com/search"
        params = {
            "engine": "google_jobs",
            "q": f"{query} jobs",
            "hl": "en",
            "api_key": SERPAPI_KEY
        }
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            jobs = response.json().get("jobs_results", [])
            all_jobs.extend(jobs)
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Failed to fetch jobs: {e}")

    return all_jobs if all_jobs else messagebox.showinfo("No Jobs Found", "No matching jobs found.")

def select_image():
    file_path = filedialog.askopenfilename(title="Select Resume Image", filetypes=[("Image Files", ".png;.jpg;.jpeg;.bmp")])
    if file_path:
        skills_text = extract_skills_section(extract_text(file_path))
        text_box.delete("1.0", ttk.END)
        text_box.insert(ttk.END, skills_text)

        try:
            img = Image.open(file_path)
            img.thumbnail((300, 300), Image.LANCZOS)
            img = ImageTk.PhotoImage(img)
            img_label.config(image=img)
            img_label.image = img
        except Exception as e:
            messagebox.showerror("Error", f"Error loading image: {e}")

def open_link(event, url):
    webbrowser.open_new(url)

def show_jobs():
    skills_text = text_box.get("1.0", ttk.END).strip()
    jobs = fetch_jobs(skills_text)
    if not jobs:
        return

    job_text_box.config(state=ttk.NORMAL)
    job_text_box.delete("1.0", ttk.END)

    for idx, job in enumerate(jobs):
        job_title = job['title']
        company_name = job['company_name']
        location = job.get('location', 'N/A')
        job_link = job.get("job_link") or job.get("apply_link") or f"https://www.google.com/search?q={job_title}+{company_name}+job"

        job_text_box.insert(ttk.END, f"📌 {job_title}\n")
        job_text_box.insert(ttk.END, f"🏢 {company_name}\n")
        job_text_box.insert(ttk.END, f"📍 {location}\n")

        start_index = job_text_box.index(ttk.END)
        job_text_box.insert(ttk.END, f"🔗 Click Here\n", f"link_{idx}")
        job_text_box.tag_config(f"link_{idx}", foreground="blue", underline=True)
        job_text_box.tag_bind(f"link_{idx}", "<Button-1>", lambda e, url=job_link: open_link(e, url))
        job_text_box.insert(ttk.END, "-" * 50 + "\n\n")

    job_text_box.config(state=ttk.DISABLED)

def clear_content():
    text_box.delete("1.0", ttk.END)
    job_text_box.config(state=ttk.NORMAL)
    job_text_box.delete("1.0", ttk.END)
    job_text_box.config(state=ttk.DISABLED)
    img_label.config(image='', text="📌 Image Preview")
    img_label.image = None

root = ttk.Window(themename="solar")
root.title("📄 Resume Skills Extractor & Job Finder 🏢")
root.geometry("750x900")

header_label = ttk.Label(root, text="Resume Skills Extractor & Job Finder", font=("Arial", 18, "bold"), bootstyle="primary")
header_label.pack(pady=15)

instructions_label = ttk.Label(root, text="1. Click 'Select Resume' to upload an image of your resume.\n2. Extracted skills will be displayed below.\n3. Click 'Find Jobs' to fetch relevant job listings.\n4. Click on 'Click Here' to open job links.\n5. Use 'Clear' to reset the application.", font=("Arial", 10), bootstyle="info", justify="left")
instructions_label.pack(pady=10)

button_frame = ttk.Frame(root)
button_frame.pack(pady=10)

btn_select = ttk.Button(button_frame, text="📂 Select Resume", command=select_image, bootstyle="primary")
btn_select.pack(side="left", padx=5)

btn_find_jobs = ttk.Button(button_frame, text="🔍 Find Jobs", command=show_jobs, bootstyle="success")
btn_find_jobs.pack(side="left", padx=5)

btn_clear = ttk.Button(button_frame, text="🗑 Clear", command=clear_content, bootstyle="danger")
btn_clear.pack(side="left", padx=5)

img_label = Label(root, text="📌 Image Preview", font=("Arial", 12), bg="gray", fg="white", width=40, height=12)
img_label.pack(pady=10)

text_box_label = ttk.Label(root, text="Extracted Skills", font=("Arial", 12, "bold"), bootstyle="success")
text_box_label.pack()
text_box = Text(root, height=5, width=70, wrap="word", font=("Arial", 10))
text_box.pack(pady=5)

job_box_label = ttk.Label(root, text="Matching Jobs", font=("Arial", 12, "bold"), bootstyle="info")
job_box_label.pack()

job_frame = ttk.Frame(root)
job_frame.pack(pady=5, fill='both', expand=True)

scrollbar = Scrollbar(job_frame)
scrollbar.pack(side="right", fill="y")

job_text_box = Text(job_frame, height=12, width=70, wrap="word", font=("Arial", 10), yscrollcommand=scrollbar.set, state=ttk.DISABLED)
job_text_box.pack(side="left", fill="both", expand=True)
scrollbar.config(command=job_text_box.yview)

print("Starting the application...")

root.mainloop()

print("Application closed.")
