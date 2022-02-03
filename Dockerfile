# pull official base image
FROM python:3.8.1-slim-buster

# create directory for the app user
RUN mkdir -p /home/app

# create the app user
RUN addgroup --system blog && adduser --system blog --ingroup blog

# create the appropriate directories
ENV APP_HOME=/home/app/blog
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# copy project
COPY . $APP_HOME


# install dependencies
RUN apt-get update && apt-get upgrade -y && apt-get install -y --no-install-recommends netcat
RUN apt-get install -y --no-install-recommends \
    build-essential \
    default-libmysqlclient-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip
RUN pip install -r requirements.txt




# chown all the files to the app user
RUN chown -R hoc:hoc $APP_HOME
RUN chmod +x $APP_HOME

# change to the app user
USER blog

EXPOSE 5000
# run entrypoint.prod.sh
ENTRYPOINT ["sh","/home/app/blog/run.sh"]