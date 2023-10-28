from flask import Flask, render_template, send_from_directory
from flask_uploads import UploadSet, IMAGES, configure_uploads
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField
import os

SECRET_KEY = os.urandom(32)

app = Flask(__name__)
app.config["SECRET_KEY"] = "asvfdb"
app.config["UPLOADED_PHOTOS_DEST"] = 'uploads'


photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

class UploadForm(FlaskForm):
    photo = FileField(
        validators=[
            FileAllowed(photos, "Only images allowed"),
            FileRequired("File field should not be empty"),
        ]
    )
    submit=SubmitField("Upload")

@app.route("/", methods=['GET', 'POST'])
def upload_image():
    form = UploadForm()
    if form.validate_on_submit():
        filename = photos.save(form.photo.data)
    return render_template("index.html", form=form)

if __name__ == "__main__":
    app.run()