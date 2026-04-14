from github import Github
from code_reviewer.config import GITHUB_TOKEN, SUPPORTED_EXTENSIONS, IGNORED_DIRS
from pathlib import Path #this helps in the format for the path
from dataclasses import dataclass

@dataclass
class RepoFile:
    path:str
    content:str
    language:str

class GitHubReader:
    def __init__(self):
        self._gh = Github (GITHUB_TOKEN)
    def read_git_repo(self, url: str):
        items = url.split("/")
        splitted_url = items[3] + "/" + items[4]
        repo = self._gh.get_repo(splitted_url)
        repo_content = repo.get_contents("")#gets everything in root folder
        readable_content = []
        while repo_content:
            item = repo_content.pop(0)#gets the first item
            if item.type == "dir":#checks if it is a folder
                repo_content.extend(repo.get_contents(item.path))#goes in folder(extend), repeats get content, gets file path
            else:
                if(Path(item.path).suffix in SUPPORTED_EXTENSIONS):#changes string to path, suffix takes the extension out
                    raw_content = item.decoded_content.decode("utf-8")
                    readable_content.append(RepoFile(item.path, raw_content, Path(item.path).suffix))
        return (readable_content)
    def read_local_repo(self, folder_path:str): 
        files = []
        for item in Path(folder_path).rglob("*"):# rglob means recursive glob - finds ALL files in all subfolders
            if item.is_file() and item.suffix in SUPPORTED_EXTENSIONS and not any(ignored in item.parts for ignored in IGNORED_DIRS):
                raw_content = item.read_text(encoding="utf-8")
                files.append(RepoFile(str(item), raw_content, item.suffix))
        return files


