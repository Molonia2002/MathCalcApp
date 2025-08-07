import os
from mathcalcapp import create_app  # ✅ correct import path

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))