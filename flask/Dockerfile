FROM python
RUN pip install Flask
RUN pip install psycopg2-binary
COPY index.py /root/
COPY templates /root/templates
WORKDIR /root
EXPOSE 5000
CMD ["python", "index.py"]