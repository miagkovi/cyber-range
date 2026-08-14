FROM python:3.11-slim

WORKDIR /app

# Install dependencies directly without
# caching to reduce image size
RUN pip install --no-cache-dir flask

COPY app.py init_db.py ./

RUN python init_db.py

EXPOSE 5000

CMD ["python", "app.py"]