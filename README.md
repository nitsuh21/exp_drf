# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

# Install required packages
pip install -r requirements.txt


# Create migrations for models
python manage.py makemigrations

# Apply migrations to the database
python manage.py migrate

# Swagger Documentation
http://127.0.0.1:8000/swagger/
