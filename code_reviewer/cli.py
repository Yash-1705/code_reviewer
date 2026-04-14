import typer
from code_reviewer.github_integration.reader import GitHubReader

app = typer.Typer()

@app.command()
def analyse(target: str):
    reader = GitHubReader()
    if "https" in target:
        files = reader.read_git_repo(target)
        print(f"Found {len(files)} files")
    else:
        files = reader.read_local_repo(target)
        print(f"Found {len(files)} files")

if __name__ == "__main__":
    app()