FROM python:3.11.9-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python", "bot.py"]