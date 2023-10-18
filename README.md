
# RemoveBG Al![Uploading CleanShot 2023-10-18 at 15.38.06@2x.png…]()

fred Workflow
An Alfred workflow that uses the RemoveBG API to remove plain image backgrounds.<br>
Uses the removebg API to remove white (or other plain colors) backgrounds from any given image.<br>
File types supported: .jpeg/.jpg/.png/.webp<br>
Non-PNG images will be converted to PNG first automatically.<br>
Supports keyword trigger or Universal Action.<br>

## Installation
1. Download workflow from [Packal page](http://www.packal.org/workflow/removebg).
2. Install python3 and its dependencies: requests and Pillow.
3. Sign up at https://www.remove.bg/ and get your API key from your account dashboard.
4. Paste the API key in the configuration, and you're good to go!

## Usage
1. Keyword Trigger: rmbg + filename (supports single file only)
2. Universal Action: Select one or multiple files, and choose "Remove BG" from the results.<br>
Note: All changes will be in-place, meaning the original image will be replaced.
