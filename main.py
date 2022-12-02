# from selenium.webdriver.common.by import By
# from selenium import webdriver
# import time
import os
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


# def google_images(image_link):
#     driver = webdriver.Chrome(executable_path="chromedriver.exe")
#     driver.maximize_window()
#     driver.get("https://images.google.com/")
#     driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[3]/div[3]/img').click()
#     driver.find_element(By.CSS_SELECTOR, '#ow6 > div.M8H8pb > c-wiz > div.ea0Lbe > div > div.gIYJUc > div.f6GA0 > c-wiz > div.PXT6cd > input').click()
#     driver.find_element(By.CSS_SELECTOR, '#ow6 > div.M8H8pb > c-wiz > div.ea0Lbe > div > div.gIYJUc > div.f6GA0 > c-wiz > div.PXT6cd > input').send_keys(image_link)
#     driver.find_element(By.CSS_SELECTOR, '#ow6 > div.M8H8pb > c-wiz > div.ea0Lbe > div > div.gIYJUc > div.f6GA0 > c-wiz > div.PXT6cd > div').click()


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file_():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            try:
                return file_path
                # k = google_images(file_path)
            except:
                return "Some Internal error occured"
    

if __name__ == '__main__':
   app.run(debug = True)