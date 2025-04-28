import os

def Ignore_Content(Path):
    GitIgnore_Path = os.path.join(Path, ".gitignore")

    if not os.path.exists(GitIgnore_Path):
        IGNORE_FILE = input("No .gitignore file found. Do you want to create one? (y/n): ").lower()
        if IGNORE_FILE == "y":
            gitignore_content = """
            # Python
            __pycache__/
            *.py[cod]
            *.pyo
            env/
            venv/
            build/
            develop-eggs/
            .eggs/
            *.egg-info/
            dist/
        
            # Node.js
            node_modules/
            npm-debug.log
            yarn-error.log
            .pnpm-debug.log
        
            # Java
            *.class
            *.jar
            *.war
            *.ear
        
            # VSCode
            .vscode/
                """.strip()

            with open(os.path.join(Path, ".gitignore"), "w") as f:
                f.write(gitignore_content)
            print(".gitignore file created successfully!")