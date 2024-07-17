# Fetches the latest keybindings from https://github.com/codebling/vs-code-default-keybindings 
# and updates the package.json files in the linuxkeybindings, mackeybindings and windowskeybindings directories.

import json
import re
import requests

sources = {
    'linux': 'https://raw.githubusercontent.com/codebling/vs-code-default-keybindings/master/linux.keybindings.json',
    'mac': 'https://raw.githubusercontent.com/codebling/vs-code-default-keybindings/master/macos.keybindings.json',
    'windows': 'https://raw.githubusercontent.com/codebling/vs-code-default-keybindings/master/windows.keybindings.json'
}

for platform, url in sources.items():
    # Fetch keybindings for each platform from https://github.com/codebling/vs-code-default-keybindings
    response = requests.get(url)
    response.raise_for_status()
    body = response.text

    # Get all lines starting with "//"
    comments = '\n'.join([line for line in body.splitlines() if line.startswith('//')])
  
    # Remove all lines starting with "//"
    keybindings = json.loads('\n'.join([line for line in body.splitlines() if not line.startswith('//')]))
    
    # Extract version from comments using regex
    version = re.search(r'\d+\.\d+\.\d+', comments).group(0)

    # Load package.json
    with open(f'{platform}keybindings/package.json', 'r+') as f:
        # Load in the package.json file
        package = json.load(f)

        # Update the package.json file with the new keybindings and version
        package['version'] = version
        package['engines']['vscode'] = f'^{version}'
        package['contributes']['keybindings'] = keybindings
        
        # Write changes to the package.json file
        f.seek(0)
        json.dump(package, f, indent='\t')