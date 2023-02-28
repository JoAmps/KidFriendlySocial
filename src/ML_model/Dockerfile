FROM huggingface/transformers-pytorch-gpu:latest
FROM python:3.8

COPY ./ /app
WORKDIR /app

RUN pip install --no-cache-dir --requirement /app/requirements.txt
EXPOSE 3000
CMD ["python", "app.py"]