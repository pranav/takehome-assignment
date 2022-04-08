FROM python:3
RUN  mkdir WORK_REPO
RUN  cd  WORK_REPO
WORKDIR  /WORK_REPO
ADD main.py .
CMD ["pip", "install", "-r", "requirements.txt"]
CMD ["python", "-u", "main.py"]
