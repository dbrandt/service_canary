FROM python:3.5-slim

COPY bindist /dist

EXPOSE 80

# Install python deps from binary builds.
RUN pip install --index-url /dist /dist/*whl 
    
WORKDIR /

CMD ["/usr/local/bin/gunicorn", "-w4", "-unobody", "-gnogroup", "-b0.0.0.0:80", "service_canary.web:app"]
