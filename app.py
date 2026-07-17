import os
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
DATABASE_URL = os.environ.get("DATABASE_URL")
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-secret-key")
db = SQLAlchemy(app)
with app.app_context():
    db.create_all()
class Complaint(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    priority = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(20), default='Open')
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

def __repr__(self):
        return f"{self.sno} - {self.category}"
def categorize_complaint(description):
    description = description.lower()
    
    keywords = {
        'Pothole': ['pothole', 'road', 'sadak', 'gaddha', 'crater'],
        'Electricity': ['bijli', 'light', 'electricity', 'power', 'wire'],
        'Water': ['paani', 'water', 'pipe', 'drainage', 'sewage'],
        'Garbage': ['kachra', 'garbage', 'waste', 'dustbin', 'smell'],
        'Street Light': ['streetlight', 'lamp', 'dark', 'andhera'],
    }
    
    for category, words in keywords.items():
        for word in words:
            if word in description:
                return category
    
    return 'Other'
def get_priority(description):
    description = description.lower()
    
    high_keywords = ['urgent', 'emergency', 'accident', 'danger', 
                     'khatra', 'jaldi', 'serious', 'dead', 'injury']
    
    medium_keywords = ['problem', 'issue', 'broken', 'repair', 
                       'fix', 'kharab', 'toot', 'band']
    
    for word in high_keywords:
        if word in description:
            return 'High'
    
    for word in medium_keywords:
        if word in description:
            return 'Medium'
    
    return 'Low'
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        location = request.form['location']
        description = request.form['description']
        
        category = categorize_complaint(description)
        priority = get_priority(description)
        
        complaint = Complaint(
            name=name,
            location=location,
            description=description,
            category=category,
            priority=priority
        )
        db.session.add(complaint)
        db.session.commit()
        return redirect('/')
    
    filter_status = request.args.get('status')
    filter_category = request.args.get('category')
    
    query = Complaint.query
    
    if filter_status:
        query = query.filter_by(status=filter_status)
    if filter_category:
        query = query.filter_by(category=filter_category)
    
    complaints = query.all()
    
    return render_template('index.html', complaints=complaints)

@app.route('/update/<int:sno>')
def update_status(sno):
    complaint = Complaint.query.filter_by(sno=sno).first()
    
    if complaint.status == 'Open':
        complaint.status = 'In Progress'
    elif complaint.status == 'In Progress':
        complaint.status = 'Resolved'
    else:
        complaint.status = 'Open'
    
    db.session.commit()
    return redirect('/')

@app.route('/dashboard')
def dashboard():
    total = Complaint.query.count()
    open_count = Complaint.query.filter_by(status='Open').count()
    progress_count = Complaint.query.filter_by(status='In Progress').count()
    resolved_count = Complaint.query.filter_by(status='Resolved').count()
    
    high_priority = Complaint.query.filter_by(priority='High').count()
    
    categories = db.session.query(Complaint.category, db.func.count(Complaint.category)).group_by(Complaint.category).all()
    
    return render_template('dashboard.html', 
                          total=total, 
                          open_count=open_count,
                          progress_count=progress_count,
                          resolved_count=resolved_count,
                          high_priority=high_priority,
                          categories=categories)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
