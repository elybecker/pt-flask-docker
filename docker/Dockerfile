# ========== Fetch a Docker image ========== 
FROM pytorch/pytorch:1.0-cuda10.0-cudnn7-devel


# ========== Fetch Args ========== 
ARG USER_ID
ARG USER_NAME

USER root
WORKDIR /


# ========== Install system dependencies ========== 
RUN apt-get update && apt-get install -y tmux


# ========== Install Python dependencies ========== 
COPY requirements.txt /tmp/
RUN pip install pip -U && \
    pip install --requirement /tmp/requirements.txt


# ========== Add user ==========
RUN apt-get -y install sudo

RUN useradd --no-log-init --system --uid ${USER_ID} \
    --create-home --shell /bin/bash ${USER_NAME}

USER ${USER_NAME}

# ========== Start gunicorn ==========
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "api:app"]sub