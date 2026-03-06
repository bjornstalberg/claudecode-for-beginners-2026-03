[gh-conf-ssh-keys]: https://docs.github.com/en/authentication/connecting-to-github-with-ssh
[gh-troubleshoot-ssh-keys-conf]: https://docs.github.com/authentication/troubleshooting-ssh
[claude-pricing]: https://claude.com/pricing
[claude-install]: https://claude.com/product/claude-code

![AI Coding Labb](resources/heading-image.png)

# Pre-requisites

- GitHub account, a free account works.
- VS Code with the following extensions:
  - [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) — core language support, debugger, test runner
  - [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) — fast IntelliSense and type information
  - [Pyright](https://marketplace.visualstudio.com/items?itemName=ms-pyright.pyright) — static type checker
  - [Ruff](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff) — linter and formatter
  - [REST Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) — send HTTP requests and inspect responses directly from VS Code
- Your preferred terminal emulator (optional, only needed if running locally)
- Claude Subscription, a _Free_ plan works. You can get one at [Claude Pricing][claude-pricing]

> **Note (local setup only):** If you plan to clone the repository using SSH, make sure to configure your [SSH Keys][gh-conf-ssh-keys] beforehand. Refer to the [troubleshooting guide][gh-troubleshoot-ssh-keys-conf] if you run into issues.

# Exercises and Setup

We'll go over two different exercises where we'll work together with Claude Code to perform programming tasks; the exercises can be carried out locally on your machine or in _GitHub Codespaces_.

## Fork the Repository

You'll work on your own fork of this repository. To get started, locate the fork button at the top of the repository page, next to _Watch_ and _Star_.

![gh-code-toolbar](resources/gh-repo-toolbar.png)

1. Click the Fork button.
2. Make sure your user is selected in the _Owner_ drop-down.
3. Provide a name for the repository or leave as-is.

You may now browse to the new repository under your account.

## Clone or Open the Repository

### Option 1 - Start Codespaces

Once you are on the front page of your forked repository:

1. Click the _Code_ green button which will open up a palette.
2. Select _Codespaces_ and then click on the green button _Create Codespace on main_. 

![gh-repo-code](resources/gh-codespaces.png)

This will open a new tab where your codespace will be bootstrapped — wait for it to finish, and you should then see an editor with the file tree on the left side.

### Option 2 - Clone the Repository

Once you are on the front page of your forked repository:

1. Click on the _Code_ green button which will open a palette.
2. While on the _Local_ tab, _Clone_ using SSH; you may alternatively use the GitHub CLI if you already have set it up.

## Installing Claude Code

Navigate to [Install Claude Code][claude-install] and select the option that suits your platform and workstation configuration.

Once installed, run the following to confirm everything is working:

```bash
claude --version
```

### GitHub Codespaces

Once your codespace is up and running, install the Claude Code extension:

1. Open the Extensions sidebar (_Ctrl+Shift+X_).
2. Search for **Claude Code**.
3. Click **Install**.

# Authenticating

Start Claude Code by:

- *VS Code or Codespaces*: if the tab isn't visible yet, hit _Ctrl+Shift+P_ to show the command palette, then Claude > Open in New Tab.
- *Terminal emulator*: first make sure you are in the directory where you've cloned the repository, then run the command *claude*.

Select the option to authenticate with a Claude subscription and use your account to sign in.

# Claude Configuration

# Sandboxing

# Exercises

## E1 - Refactor the Asset Management Application

This is a Web API application written in Python and that uses Fast API, it supports a ficticious system used to manage hardware assets in an organisateion. The code is found under `asset_managemente_app`. We are going to refactor this application to add a couple of new features and improvements assisted with Claude Code.

Refactoring tasks:
1. Add a new endpoin which allows adding one or more tags to an asset.
2. Ability to activate or deactivate an asset, remind Claude that it inactive assets should not be listed by default; for audit purposes we should now when the asset was deactivated and by who
3. Ability to decomission an asset, this is a permanent action and we should include when the asset was decomissioned and by who
3. Show the details of an asset by its ID, inactive and decomissioned assets can be looked up.

## E2 - Create an Application from Scratch

To complement the assets management system, we need a new Web API where assets can report all sort of security events caught by a local agent running on certain devices. The description and requirements have been documented under `threat_management_app/README.md`

Things to do:
- You may change the description or requirements as you wish, for example use a different programming language / stack, functional and security requirements, etc.
- Instruct Claude to read the description and requirements in`threat_management_app/README.md` and implement the web api as well as testing it
- Review its work and make any adjustments you may think necessary via direct prompts to claude and follow ups.

