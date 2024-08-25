[![Github top language](https://img.shields.io/github/languages/top/FredHappyface/VSCode.OSKeybindings.svg?style=for-the-badge&cacheSeconds=28800)](../../)
[![Issues](https://img.shields.io/github/issues/FredHappyface/VSCode.OSKeybindings.svg?style=for-the-badge&cacheSeconds=28800)](../../issues)
[![License](https://img.shields.io/github/license/FredHappyface/VSCode.OSKeybindings.svg?style=for-the-badge&cacheSeconds=28800)](/LICENSE.md)
[![Commit activity](https://img.shields.io/github/commit-activity/m/FredHappyface/VSCode.OSKeybindings.svg?style=for-the-badge&cacheSeconds=28800)](../../commits/master)
[![Last commit](https://img.shields.io/github/last-commit/FredHappyface/VSCode.OSKeybindings.svg?style=for-the-badge&cacheSeconds=28800)](../../commits/master)

# VSCode.OSKeybindings.Mac

<img src="https://raw.githubusercontent.com/FredHappyface/VSCode.OSKeybindings/master/mackeybindings/Mac.png" alt="Project Icon" width="100">

[![Static Badge](https://img.shields.io/badge/Mac_Keybindings-VSCode_Marketplace-purple?style=for-the-badge&cacheSeconds=28800)](https://marketplace.visualstudio.com/items?itemName=fredhappyface.mackeybindings)
[![VSCode Installs](https://img.shields.io/visual-studio-marketplace/i/fredhappyface.mackeybindings.svg?style=for-the-badge&cacheSeconds=28800)](https://marketplace.visualstudio.com/items?itemName=fredhappyface.mackeybindings)
[![VSCode Rating](https://img.shields.io/visual-studio-marketplace/stars/fredhappyface.mackeybindings.svg?style=for-the-badge&cacheSeconds=28800)](https://marketplace.visualstudio.com/items?itemName=fredhappyface.mackeybindings)
[![VSCode Version](https://img.shields.io/visual-studio-marketplace/v/fredhappyface.mackeybindings.svg?style=for-the-badge&cacheSeconds=28800)](https://marketplace.visualstudio.com/items?itemName=fredhappyface.mackeybindings)

[![Static Badge](https://img.shields.io/badge/Mac_Keybindings-Open_VSX-purple?style=for-the-badge&cacheSeconds=28800)](https://open-vsx.org/extension/fredhappyface/linuxkeybindings)
[![Open VSX Downloads](https://img.shields.io/open-vsx/dt/fredhappyface/linuxkeybindings.svg?style=for-the-badge&cacheSeconds=28800)](https://open-vsx.org/extension/fredhappyface/linuxkeybindings)
[![Open VSX Rating](https://img.shields.io/open-vsx/stars/fredhappyface/linuxkeybindings.svg?style=for-the-badge&cacheSeconds=28800)](https://open-vsx.org/extension/fredhappyface/linuxkeybindings)
[![Open VSX Version](https://img.shields.io/open-vsx/v/fredhappyface/linuxkeybindings.svg?style=for-the-badge&cacheSeconds=28800)](https://open-vsx.org/extension/fredhappyface/linuxkeybindings)

Use Mac Keybindings on any OS

Keybindings provided by https://github.com/codebling/vs-code-default-keybindings - Thank you!

This extension does not remove any existing bindings. On the same OS as that of
the keybindings that means everything will be bound twice. On other OSes that
means that the keybindings will be in addition to the default (note that they
take precedence over the default bindings)

## Issues/ Conflicts

There are some known issues and conflicts with other keybinding extensions.
Currently, this is best fixed manually - see

- https://github.com/yzhang-gh/vscode-markdown/issues/396
- https://github.com/Microsoft/vscode/issues/39888

Here is a list of those that I have suffered from. Follow the links and copy the
contents of the file into your keybindings JSON file. Note that I'll add these
to the extension at some point:

- [Markdown All In One](https://github.com/FredHappyface/VSCode.OSKeybindings/blob/master/MarkdownAllInOne.json)

## Building

To build and publish a VS Code extension, follow these steps:

1. **Install Dependencies**:
   Make sure you have Node.js and npm installed. Then, install the VS Code Extension CLI:
   ```bash
   npm install -g @vscode/vsce
   ```

2. **Build the Extension**:
   Navigate to your extension directory and run:
   ```bash
   npm install
   npm run compile
   ```

3. **Package the Extension**:
   Use the `vsce` CLI to package your extension:
   ```bash
   vsce package
   ```

## Publish the Extension

### Publishing on Visual Studio Code Marketplace

Follow the instructions on the [Visual Studio Code Marketplace](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) to publish your extension. You'll need a Personal Access Token (PAT) from Azure DevOps or GitHub for authentication.

Use the `vsce` CLI to publish your extension:

```bash
vsce publish
```

### Publishing on Open VSX

In addition to the Visual Studio Code Marketplace, you can publish your extension on Open VSX, an open-source alternative for Visual Studio Code extensions. To publish on Open VSX, follow these steps:

1. **Create an Open VSX Account**:
   Sign up for an account on the [Open VSX Registry](https://open-vsx.org/).

2. **Install the Open VSX CLI**:
   Install the `ovsx` CLI tool using npm:
   ```bash
   npm install -g ovsx
   ```

3. **Publish Your Extension**:
   Then, use the `ovsx` CLI to publish it:
   ```bash
   ovsx publish <file> -p <token>
   ```

For detailed instructions and additional resources, visit the [Open VSX documentation](https://github.com/eclipse/openvsx/wiki/Publishing-Extensions).

## Licence
BSD2-Patent License
Copyright (c) FredHappyface
(See the [LICENSE](https://github.com/FredHappyface/VSCode.OSKeybindings/blob/master/LICENSE.md) for more information.)
