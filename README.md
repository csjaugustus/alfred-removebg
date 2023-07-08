# removebg-alfred-workflow
An Alfred workflow that uses the RemoveBG API to remove plain image backgrounds.<br>
Uses the removebg API to remove white (or other plain colors) backgrounds from any given image.<br>
File types supported: .jpeg/.jpg/.png/.webp<br>
Non-PNG images will be converted to PNG first automatically.<br>
Supports keyword trigger or Universal Action.<br>

## Installation
1. Install python3 and its dependencies: requests and Pillow.
2. Sign up at https://www.remove.bg/ and get your API key from your account dashboard.
3. Paste the API key in the configuration, and you're good to go!

## Usage
1. Keyword Trigger: rmbg + filename (supports single file only)
2. Universal Action: Select one or multiple files, and choose "Remove BG" from the results.<br>
Note: All changes will be in-place, meaning the original image will be replaced.
