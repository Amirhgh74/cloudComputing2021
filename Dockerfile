FROM python 
ADD request.py /
RUN pip install requests
CMD ["python", "./request.py"]