
```
first install all packages mentioned in requirements.txt
run "scraping_and_count.py" file or run "python scraping_and_count.py" in terminal.
```

![img.png](img.png)

```
API:-->
        POST: http://127.0.0.1:5000/
        request_body:
            {
                "url": "https://anatta.io/",
                "words": [
                    "Sustainable",
                    "Growth",
                    "Anatta"
                ]
            }
        
        response:
            {
                "body": {
                    "url": "https://anatta.io/",
                    "words": [
                        "Sustainable",
                        "Growth",
                        "Anatta"
                    ]
                },
                "response": {
                    "Anatta": 10,
                    "Growth": 3,
                    "Sustainable": 7
                },
                "type": "success"
            }
```