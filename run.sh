if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $DATABASE_HOST $DATABASE_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi
# gunicorn --bind 0.0.0.0:5000 manage:app

# python testdata.py

# python compare_apis.py
python server.py
exec "$@"