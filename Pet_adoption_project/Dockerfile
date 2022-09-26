# Use python image
FROM python:3.8-slim

EXPOSE 8080

# Copy all the files needed for the app to work
COPY models/ ./models
COPY streamlit/ ./streamlit

# Install all the necessary libraries
RUN pip install -r ./streamlit/requirements.txt
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

# Run the streamlit app!
ENTRYPOINT ["streamlit", "run", "streamlit/streamlit_app.py", "--server.port=8080", "--server.address=0.0.0.0"]
