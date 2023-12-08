![CleanShot 2023-10-18 at 15 38 06@2x](https://github.com/csjaugustus/removebg-alfred-workflow/assets/61149391/385a4fda-3bd0-45f2-9d51-cee9eeed9589)
# RemoveBG Alfred Workflow
An Alfred workflow that uses the RemoveBG API to remove image backgrounds.<br>
It performs significantly better than Apple's background removal especially for complex images.<br>
File types supported: .jpeg/.jpg/.png/.webp<br>
Non-PNG images will be converted to PNG first automatically.<br>
Supports keyword trigger or File Action.<br>

## Installation
1. Download workflow file above.
2. Install python3 and its dependencies: `requests` and `Pillow`.
3. Sign up at [RemoveBG](https://www.remove.bg/) and get your API key from your account dashboard.
4. Paste the API key in the configuration, and you're good to go!

## Usage
1. Keyword Trigger: `rmbg` filename (supports single file only)
2. File Action: Select one or multiple files, and choose "Remove BG" from the results.<br>
Note: All changes will be in-place, meaning the original image will be replaced.
