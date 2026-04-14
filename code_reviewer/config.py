from dotenv import load_dotenv
import os

load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
SUPPORTED_EXTENSIONS = {".py", ".js", ".ts", ".java", ".c", ".cpp", ".h", ".jsx",".vue",".cs",".php"}
IGNORED_DIRS = {"node_modules", ".git", "__pycache__", "venv"}