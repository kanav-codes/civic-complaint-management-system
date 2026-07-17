import os
from datetime import datetime

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash,
    abort,
)

from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import (
    generate_password_hash,
    check_password_hash,
)

# ==========================================
# Flask Configuration
# ==========================================

app = Flask(__name__)

DATABASE_URL = os.environ.get("DATABASE_URL")

if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace(
        "postgres://",
        "postgresql://",
        1,
    )

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = os.environ.get(
    "SECRET_KEY",
    "change-this-secret"
)

db = SQLAlchemy(app)

# ==========================================
# Admin Credentials
# ==========================================

ADMIN_USERNAME = "shinku"

# Password:
# MalabarHills@212

ADMIN_PASSWORD_HASH = generate_password_hash(
    "MalabarHills@212"
)

# ==========================================
# Database Model
# ==========================================

class Complaint(db.Model):

    __tablename__ = "complaint"

    sno = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )

    location = db.Column(
        db.String(200),
        nullable=False
    )

    category = db.Column(
        db.String(50),
        nullable=False
    )

    description = db.Column(
        db.String(1000),
        nullable=False
    )

    priority = db.Column(
        db.String(20),
        nullable=False
    )

    status = db.Column(
        db.String(20),
        default="Open"
    )

    date_created = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def __repr__(self):

        return f"{self.sno} - {self.category}"

# ==========================================
# Create Database Tables
# ==========================================

with app.app_context():
    db.create_all()

# ==========================================
# Helper Functions
# ==========================================

def admin_logged_in():

    return session.get("admin") is True


def categorize_complaint(description):

    description = description.lower()

    keywords = {

        "Pothole": [
            "pothole",
            "road",
            "sadak",
            "gaddha",
            "crater",
        ],

        "Electricity": [
            "bijli",
            "light",
            "electricity",
            "wire",
            "power",
        ],

        "Water": [
            "water",
            "paani",
            "pipe",
            "leak",
            "drainage",
            "sewage",
        ],

        "Garbage": [
            "garbage",
            "kachra",
            "dustbin",
            "waste",
            "smell",
        ],

        "Street Light": [
            "streetlight",
            "lamp",
            "dark",
            "andhera",
        ],

    }

    for category, words in keywords.items():

        for word in words:

            if word in description:

                return category

    return "Other"


def get_priority(description):

    description = description.lower()

    high = [

        "urgent",
        "danger",
        "accident",
        "injury",
        "fire",
        "dead",
        "emergency",
        "serious",
        "khatra",
    ]

    medium = [

        "repair",
        "broken",
        "issue",
        "problem",
        "fix",
        "kharab",
        "band",
        "toot",
    ]

    for word in high:

        if word in description:

            return "High"

    for word in medium:

        if word in description:

            return "Medium"

    return "Low"
# ==========================================
# Admin Authentication Routes
# ==========================================

@app.route("/admin-login", methods=["GET", "POST"])
def admin_login():

    if admin_logged_in():
        return redirect(url_for("dashboard"))

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        if (
            username == ADMIN_USERNAME
            and check_password_hash(
                ADMIN_PASSWORD_HASH,
                password,
            )
        ):

            session["admin"] = True

            flash(
                "Login Successful!",
                "success"
            )

            return redirect(
                url_for("dashboard")
            )

        flash(
            "Invalid Username or Password",
            "danger"
        )

    return render_template(
        "admin_login.html"
    )


@app.route("/logout")
def logout():

    session.clear()

    flash(
        "Logged out successfully.",
        "success"
    )

    return redirect(
        url_for("index")
    )


# ==========================================
# Home Page
# ==========================================

@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":

        name = request.form.get("name")
        location = request.form.get("location")
        description = request.form.get("description")

        category = categorize_complaint(
            description
        )

        priority = get_priority(
            description
        )

        complaint = Complaint(

            name=name,

            location=location,

            description=description,

            category=category,

            priority=priority,

            status="Open",
        )

        db.session.add(
            complaint
        )

        db.session.commit()

        flash(
            "Complaint submitted successfully.",
            "success"
        )

        return redirect(
            url_for("index")
        )

    filter_status = request.args.get(
        "status"
    )

    filter_category = request.args.get(
        "category"
    )

    query = Complaint.query

    if filter_status:

        query = query.filter_by(
            status=filter_status
        )

    if filter_category:

        query = query.filter_by(
            category=filter_category
        )

    complaints = query.order_by(
        Complaint.date_created.desc()
    ).all()

    return render_template(

        "index.html",

        complaints=complaints,

        admin=admin_logged_in()

    )
# ==========================================
# Update Complaint Status (Admin Only)
# ==========================================

@app.route("/update/<int:sno>")
def update_status(sno):

    if not admin_logged_in():
        abort(403)

    complaint = Complaint.query.get_or_404(sno)

    # Lock resolved complaints
    if complaint.status == "Resolved":

        flash(
            "This complaint has already been resolved.",
            "warning"
        )

        return redirect(
            url_for("dashboard")
        )

    if complaint.status == "Open":

        complaint.status = "In Progress"

    elif complaint.status == "In Progress":

        complaint.status = "Resolved"

    db.session.commit()

    flash(
        "Complaint status updated successfully.",
        "success"
    )

    return redirect(
        url_for("dashboard")
    )


# ==========================================
# Admin Dashboard
# ==========================================

@app.route("/dashboard")
def dashboard():

    if not admin_logged_in():
        abort(403)

    total = Complaint.query.count()

    open_count = Complaint.query.filter_by(
        status="Open"
    ).count()

    progress_count = Complaint.query.filter_by(
        status="In Progress"
    ).count()

    resolved_count = Complaint.query.filter_by(
        status="Resolved"
    ).count()

    high_priority = Complaint.query.filter_by(
        priority="High"
    ).count()

    medium_priority = Complaint.query.filter_by(
        priority="Medium"
    ).count()

    low_priority = Complaint.query.filter_by(
        priority="Low"
    ).count()

    categories = (

        db.session.query(

            Complaint.category,

            db.func.count(
                Complaint.category
            )

        )

        .group_by(
            Complaint.category
        )

        .all()

    )

    complaints = Complaint.query.order_by(
        Complaint.date_created.desc()
    ).all()

    return render_template(

        "dashboard.html",

        complaints=complaints,

        total=total,

        open_count=open_count,

        progress_count=progress_count,

        resolved_count=resolved_count,

        high_priority=high_priority,

        medium_priority=medium_priority,

        low_priority=low_priority,

        categories=categories,

        admin=True,

    )


# ==========================================
# Error Handlers
# ==========================================

@app.errorhandler(403)
def forbidden(error):

    return render_template(
        "403.html"
    ), 403


@app.errorhandler(404)
def page_not_found(error):

    return render_template(
        "404.html"
    ), 404


# ==========================================
# Run App
# ==========================================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True,
    )