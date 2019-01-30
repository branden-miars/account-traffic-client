# Testing

Repo contains Docker and Make files for setup. Tests can be run using:

```
make test
```

# Use

The Dockerfile ensures the necessary libraries are present and can be started with:

```
make run
```

Once in the container, the script can be called with:

```
python main.py -a <account>
```

You can provide a custom API URL as well in case you're testing locally:

```
python main.py -a test -u http://0.0.0.0:8080/traffic/api/v1/
```

