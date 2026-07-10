FROM python:3.13
WORKDIR /usr/local/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src ./src
EXPOSE 8080

COPY .env ./

# CMD ["python", "src/app.py"]
CMD ["python", "-m", "src.app"]