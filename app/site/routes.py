from flask import Blueprint, render_template

site = Blueprint('site', __name__, template_folder='site_templates')

@site.route('/')
def home():
    return render_template('index.html')

@site.route('/car')
def car():
    return render_template('car.html')

@site.route('/service')
def service():
    return render_template('service.html')

@site.route('/profile')
def profile():
    return render_template('profile.html')