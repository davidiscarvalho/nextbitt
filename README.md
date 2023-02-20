# nextbitt


# virtual environment
# --------------------------------create virtual environment
python -m venv .v
# --------------------------------activate virtual environment
.v/Scripts/activate

# requirements
# --------------------------------freeze requirements
pip freeze > requirements.txt
# --------------------------------install requirements
pip install -r requirements.txt -v