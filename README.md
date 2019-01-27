# Testing

Run tests from project directory

```
python -m unittest discover ./
```

# Use

```
python main.py -a <account>
```

You can provide a custom API URL as well in case you're testing locally:

```
python main.py -a test -u http://0.0.0.0:8080/traffic/api/v1/
```
