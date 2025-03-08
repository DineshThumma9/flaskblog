import json
from flaskblog import current_app, db
from flaskblog.models import User, Post

# List of posts
posts_data = [
    {"title": "My Updated Pooost", "content": "My first updated post!\n\nThis is exciting!", "user_id": 1},
    {"title": "A Second Ponst", "content": "This is a post from a different user...", "user_id": 2},
    {"title": "Top 5 Programming Languages", "content": "Te melius apeirian postulant cum, labitur admodum cu eos! ...", "user_id": 1},
    {"title": "Sublime Text Tips and Tricks", "content": "Ea vix dico modus voluptatibus, mel iudico suavitate iracundia eu...", "user_id": 1},
    # Add more posts as needed
]

# Insert posts into the database
with current_app.current_app_context():
    try:
        db.session.bulk_insert_mcurrent_appings(Post, posts_data)
        db.session.commit()
        print("Posts added successfully!")
    except Exception as e:
        db.session.rollback()
        print(f"Error: {e}")
