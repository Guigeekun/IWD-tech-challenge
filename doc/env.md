# Env vars

You can see or add more env vars in [.env](../.env), don't forget to update [.env.example](../.env.example)

```python
import os
from dotenv import load_dotenv

load_dotenv()  # allow usage of os.getenv('thing from .env')

csv_path = os.getenv('CSV_PATH')
```
