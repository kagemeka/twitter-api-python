FROM public.ecr.aws/lambda/python:3.8

COPY env/py/requirements.txt .
RUN pip install -r requirements.txt

# COPY __main__.py .
COPY src/__main__.py .
COPY src/lib /opt/python/lib

CMD ["__main__.lambda_handler"]
