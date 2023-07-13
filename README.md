# GHGA User Documentation

A built version of this documentation is available at [https://ghga-de.github.io/docs](https://ghga-de.github.io/docs).
## Quick Start

For setting up the development environment, we rely on the
[devcontainer feature](https://code.visualstudio.com/docs/remote/containers) of vscode
in combination with Docker Compose.

To use it, you have to have Docker Compose as well as vscode with its "Remote - Containers" extension (`ms-vscode-remote.remote-containers`) installed.
Then open this repository in vscode and run the command
`Remote-Containers: Reopen in Container` from the vscode "Command Palette".

This will give you a full-fledged, pre-configured development environment including:
- infrastructural dependencies of the service (databases, etc.)
- all relevant vscode extensions pre-installed
- pre-configured linting and auto-formatting
- a pre-configured debugger
- automatic license-header insertion

Moreover, inside the devcontainer, there are two convenience commands available
(please type them in the integrated terminal of vscode):
- `dev_install` - Install dependencies
- `dev_launcher` - Start a continuous build process. The documentation is served on a local webserver an refreshes automatically when changes are made to the markdown documents.


## License
This repository is free to use and modify according to the [Apache 2.0 License](./LICENSE).
