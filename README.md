# 🚀 GitHub Repository Automation Tool

![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Ollama](https://img.shields.io/badge/Ollama-AI%20Powered-green?style=for-the-badge)

## 📋 Overview

This automation tool simplifies the process of creating GitHub repositories and pushing your local projects to GitHub. It leverages local LLM capabilities through Ollama to generate intelligent project names and descriptions, saving you time and effort.

## ✨ Features

- 🤖 **AI-Generated Content**: Uses Ollama's local LLM to generate project names and descriptions
- 🔄 **Automatic Repository Creation**: Creates GitHub repositories with appropriate visibility settings
- 📦 **Git Initialization**: Handles git init, commits, and pushes automatically
- 🌐 **Browser Integration**: Option to open the newly created repository in your web browser
- 🔔 **Notification**: will sound when you need input from the user and after the upload is complete
- 🚫 **Ignore File**: will ignore files that are not needed


## 🛠️ Prerequisites

- Python 3.10+
- Git installed and configured
- GitHub account with personal access token
- Ollama installed with at least one model (I recommend you to install mistral or openchat only because I also use it too)

## 🔧 Installation

1. Clone this repository or download the script
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Make sure Ollama is running with your desired model

## ⚙️ Configuration

Before running the script, update the following variables in the code:

```python
GITHUB_USERNAME = "your-github-username"
GITHUB_TOKEN = "your-github-personal-access-token"
PROJECT_PATH = "/path/to/your/project"
OLLAMA_MODEL = "openchat:latest"  # or any other Ollama model you have installed
```

## 🚀 Usage

1. Navigate to your project directory
2. Run the script:
   ```
   main.py
   ```
3. Follow the prompts to enter project information
4. The script will create a repository and push your project

## 🔮 Planned Features

- 📝 **README Template Generation**: AI-powered creation of complete README files based on project content
- 🛣️ **Effective path**: Insert the path through the terminal
- 🕹️ **Manual Input**: You will be able to choose to use Chatbot or not to create a name and description
- 🔄 **Repeat execution**: if the program experiences malfunction, you can choose to repeat the program or manual input
- 🔒 **Enhanced Security**: Better token management and secure authentication

## 🤝 Contributing

Contributions are welcome! Feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgements

- [Ollama](https://ollama.com/) for providing local LLM capabilities
- [GitHub API](https://docs.github.com/en/rest) for repository management