Welcome to Yggdrasil's WotLK 3.3.5a Transfer Tool.

PIP requirements:
pip install shutil datetime csv os re glob math subprocess sys

Instructions:
0, Prep: Delete contents of RawData folder
1. Copy account WTF folder contents (WoW-directory\WTF\Account\Accountname\) and place in RawData folder
2. Depending on your OS, there's two approaches:
2a. Windows: Assure you have Python set up (Windows Store or manually, both work fine) and PIP-ed, and run the CMD in the root dir. It will detect
2b. Linux: Assure you have Python set up and PIP-ed. Determine whether the data you are trying to transfer is originating from retail or 3.3.5a and run the mega_transfer script in the respective expansion source to convert to Yggdrasil's import script.
3. Enter variables requested by script.
4. Open the produced CombinedMacroOutput.txt in root dir and copy into SDM (https://felbite.com/addon/4135-superdupermacro/). If doing 3.3.5a transfer, consider using the main and off spec macros too (not applicable for retail due to talent tree differences).
5. Load in the new toon.
5a. Create character with same name as entered in step 3, click SDM macro and wait 30-60 seconds for the macro to process
5b. If transferring talents, the talent macros may need to be run 2-3 times per spec to ensure all talents get locked in.
