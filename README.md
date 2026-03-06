[gh-conf-ssh-keys]: https://docs.github.com/en/authentication/connecting-to-github-with-ssh
[gh-troubleshoot-ssh-keys-conf]: https://docs.github.com/authentication/troubleshooting-ssh
[claude-pricing]: https://claude.com/pricing
[claude-install]: https://claude.com/product/claude-code
[cc-settings]: https://docs.anthropic.com/en/docs/claude-code/settings
[cc-memory]: https://docs.anthropic.com/en/docs/claude-code/memory
[cc-permissions]: https://docs.anthropic.com/en/docs/claude-code/settings#permissions
[cc-sandboxing]: https://www.anthropic.com/engineering/claude-code-sandboxing

![AI Coding Labb](resources/heading-image.png)

# Prerequisites

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

# Setup

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
2. While on the _Local_ tab, _Clone_ using SSH; you may alternatively use the GitHub CLI if you have already set it up.

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

- _VS Code or Codespaces_: if the tab isn't visible yet, hit _Ctrl+Shift+P_ to show the command palette, then Claude > Open in New Tab.
- _Terminal emulator_: first make sure you are in the directory where you've cloned the repository, then run the command _claude_.

Select the option to authenticate with a Claude subscription and use your account to sign in.

# Claude Configuration

Claude Code can be configured at two levels:

- **`CLAUDE.md`** — a markdown file in your project root that Claude reads at the start of every session. Use it to capture coding conventions, build commands, and any project-specific instructions. Run `/init` to generate one automatically. See the [memory guide][cc-memory] for details.
- **`settings.json`** — a JSON file at `.claude/settings.json` in your project (or `~/.claude/settings.json` for user-wide settings). Use it to control tool permissions and environment variables. See the [settings reference][cc-settings] for the full list of options.

**Permissions** let you control which tools Claude can use without asking. Rules are defined under a `permissions` key with `allow` and `deny` lists. Deny rules block an operation outright; allow rules let Claude proceed without prompting. See the [permissions documentation][cc-permissions] for the full syntax.

# Sandboxing

> **Note:** This section applies only to participants running the exercises locally with the Claude CLI. GitHub Codespaces users can skip this section.

Sandboxing restricts the commands Claude Code can run to a defined set of filesystem paths and network hosts, reducing the risk of unintended changes outside your working directory. Once configured, Claude works freely within those boundaries without prompting for permission on every action.

Run `/sandbox` inside Claude Code to enable and configure the sandbox. On macOS it works out of the box; on Linux and WSL2 additional packages must be installed first — see the [sandboxing documentation][cc-sandboxing] for setup instructions.

# Exercises

## E1 - Refactor the Asset Management Application

A FastAPI web application that manages hardware and software assets in an organisation. The code is under `assets_management_app`. Use Claude Code to extend it with the following:

1. An endpoint to add one or more tags to an asset.
2. Activate or deactivate an asset. Inactive assets should not appear in listings by default; record when and by whom the asset was deactivated.
3. Decommission an asset. This is a permanent action; record when and by whom it was carried out.
4. Retrieve an asset by ID. Inactive and decommissioned assets can be looked up by ID.

## E2 - Create an Application from Scratch

A companion web API where devices can report security events caught by a local agent. Requirements are documented in `threat_management_app/README.md`.

1. Adjust the description or requirements as needed — for example, swap the language or stack, or tweak the functional requirements.
2. Instruct Claude to read `threat_management_app/README.md` and implement the API with tests.
3. Review the output and iterate with follow-up prompts.

