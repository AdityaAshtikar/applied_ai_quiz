FROM python

RUN touch quiz_virtual.py

COPY quiz.py quiz_virtual.py

COPY quiz.json quiz.json

CMD ["python", "quiz_virtual.py"]

