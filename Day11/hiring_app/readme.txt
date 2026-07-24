To create the virtual environment

python -m venv venv

To activate the virtual environment

venv\Scripts\activate

To run the requirements.txt

pip install -r requirements.txt

to check the pip
pip list

To run the applicatioon
uvicorn app.main:app --reload

uvicorn

Starts the server



main -> Python File
--reload -> Automatically restarts the server whenever you save changes

URL - check the swagger
http://127.0.0.1:8000/docs