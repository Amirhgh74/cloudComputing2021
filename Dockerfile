FROM python 
RUN apt-get update

RUN pip install --upgrade pip

ADD request_demo.py /
ADD metrics.py /
ADD t2_cluster.json /
ADD m4_cluster.json /
ADD ec2_m4.json /
ADD ec2_t2.json /

RUN pip install requests
RUN pip install boto3
RUN pip install python-dateutil
RUN pip install datetime
RUN pip install numpy
RUN pip install pandas
RUN pip install matplotlib
RUN pip install PyQt5
ADD run.sh /
RUN chmod +x run.sh
CMD ["./run.sh"]
