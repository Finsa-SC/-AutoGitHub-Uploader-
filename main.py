import requests
import subprocess
import webbrowser
import os
from Make_Ignore import Ignore_Content
from Notification import Notify, Uploaded
from config import GITHUB_USERNAME, GITHUB_TOKEN, PROJECT_PATH, OLLAMA_MODEL

def Model(prompt):
    url = "http://localhost:11434/api/generate"
    headers = {
        "content-type": "application/json"
    }
    data = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(url, headers=headers, json=data, timeout=60)
        response.raise_for_status()
        return response.json()["response"]
    except Exception as e:
        print(f"Error: ", e)
        return None

def create_repo(Name, Description, Status):
    url = "https://api.github.com/user/repos"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}"
    }
    data = {
        "name": Name,
        "description": Description,
        "private": Status
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        print(f"Repository '{Name}' Created Successfully!!")
        return response.json()["html_url"]
    else:
        print(f"Error: While create the Repository {response.json()}")
        exit()

def init_and_push(url, name):
    os.chdir(PROJECT_PATH)

    subprocess.run(["git", "init"])
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", f"Initial commit: {name}"])
    subprocess.run(["git", "branch", "-M", "main"])

    if not GITHUB_USERNAME or not GITHUB_TOKEN:
        print("Error: Username or Token not set")
        exit(1)

    auth_url = url.replace("https://", f"https://{GITHUB_USERNAME}:{GITHUB_TOKEN}@")
    subprocess.run(["git", "remote", "remove", "origin"], stderr=subprocess.DEVNULL)
    subprocess.run(["git", "remote", "add", "origin", auth_url])
    subprocess.run(["git", "push", "-u", "origin", "main"])


def main():
    folder_name = os.path.basename(os.path.normpath(PROJECT_PATH))
    print(f"📂 Detected Project Folder: {folder_name}")


    Ignore_Content(PROJECT_PATH)

    Notify()
    project_description_detail = input("📝 Describe your project briefly: ")

    prompt = f"give me the name of the project and a description of the short project just make the {project_description_detail}, for description, do not exceed 350 words, make under 350 words"
    response = Model(prompt)

    if response:
        lines = response.strip().split("\n")
        project_name = ""
        project_description = ""
        for line in lines:
            if "Project Name:" in line:
                project_name = line.split(":", 1)[1].strip()
            elif "Description:" in line:
                project_description = line.split(":", 1)[1].strip()

        if not project_name or not project_description:
            print("Parsing Failed: Fallback to manual input.")
            Notify()
            project_name = input("📦 Enter project name manually: ")
            Notify()
            project_description = input("📝 Enter project description manually: ")

    else:
        print("Model Ollama unreachable. Fallback to manual input.")
        Notify()
        project_name = input("📦 Enter project name manually: ")
        Notify()
        project_description = input("📝 Enter project description manually: ")


    print(f"\n📦 Project Name: {project_name}")
    print(f"📝 Description: {project_description}")

    Notify()
    visibility = input("Do you want to make a private repository? (y/n): ").lower()
    private = True if visibility == "y" else False

    repository_url = create_repo(project_name, project_description, private)
    init_and_push(repository_url, project_name)

    Uploaded()
    open_web = input("Do you want to open your new repository? (y/n) : ")
    if open_web == "y":
        webbrowser.open(repository_url)

if __name__ == "__main__":
    main()