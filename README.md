# FastAPI Media Project

A simple **FastAPI-based backend project** with basic API setup and environment-based configuration, designed to be extended with media handling features (e.g., ImageKit integration).

---

## 📦 Project Structure

```text
.
├── app/
│   └── app.py          # FastAPI application instance
├── main.py             # Uvicorn entry point
├── pyproject.toml      # Project configuration & dependencies
├── .env.example        # Example environment variables
├── .python-version     # Python version requirement
└── README.md           # Project documentation
```

---

## 🚀 Features

* FastAPI backend setup
* Uvicorn server configuration
* Environment variable support using `python-dotenv`
* Ready for ImageKit media integration
* Python 3.12 compatible

---

## 🛠 Requirements

* **Python**: 3.12+
* **pip** or **uv / poetry** (any modern Python package manager)

---

## 📥 Installation

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-url>
cd fashapi-media-project
```

### 2️⃣ Create Virtual Environment

```bash
python3.12 -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

> If using `pyproject.toml`:

```bash
pip install .
```

---

## ⚙️ Environment Variables

Create a `.env` file from the example:

```bash
cp .env.example .env
```

Update with your ImageKit credentials:

```env
IMAGEKIT_PRIVATE_KEY=your_imagekit_private_key_here
IMAGEKIT_PUBLIC_KEY=your_imagekit_public_key_here
IMAGEKIT_URL=https://ik.imagekit.io/your_imagekit_id
```

---

## ▶️ Running the Application

Start the development server:

```bash
python main.py
```

The API will be available at:

```
http://localhost:8080
```

---

## 🔗 API Endpoints

### Hello World

```http
GET /hello
```

**Response**:

```json
{
  "msg": "Hello"
}
```

---

## 📚 Tech Stack

* **FastAPI** – Web framework
* **Uvicorn** – ASGI server
* **ImageKit** – Media storage & delivery (planned/optional)
* **python-dotenv** – Environment management
* **SQLite / SQLAlchemy** – Ready for DB integration

---

## 🧩 Future Improvements

* Image upload APIs using ImageKit
* Authentication (FastAPI Users)
* Database models & migrations
* Media metadata storage
* Production-ready settings

---

## 🧑‍💻 Author

**Jamal**
FastAPI & Backend Developer

---

## 📄 License

This project is open-source and available under the **MIT License**.

---

✨ Happy Coding with FastAPI!
