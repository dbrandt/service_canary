FROM python:3.5-slim

COPY bindist /dist

EXPOSE 5000

# Install python deps from binary builds.
RUN pip install --index-url /dist /dist/*whl 
    
WORKDIR /

CMD ["/usr/local/bin/gunicorn", "-w4", "-unobody", "-gnogroup", "-b0.0.0.0:5000", "service_canary.web:app"]
