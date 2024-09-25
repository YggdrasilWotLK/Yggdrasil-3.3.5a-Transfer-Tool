@echo off
echo _____________::_Toon Transfer Utility v2.0 beta_::_____________

echo.
PYTHON 00_CheckRetailVersus335a.py
PYTHON 00_TerminateIfRetail.py
PYTHON DeleteEmptyAccountFolder.py
PYTHON ClearOldTransferInfo.py
PYTHON WebsiteTransfer.py
PYTHON WTF-Cleaner.py
echo.
PYTHON ClearFolders.py
PYTHON AccountFolderCleaner.py
PYTHON NameExtractor.py
echo.
PYTHON Recipient.py
echo.
PYTHON QuestCleaner.py
PYTHON RawDataMover.py

echo.
echo Filtering input by character...
PYTHON clean_altoholicdatastore_lua.py
echo Input filtering complete!

echo.
echo Extracting talent information...
PYTHON talent_macro.py
PYTHON talent_macro_cleaner.py
PYTHON talent_macro_casttimeprepend.py
echo Extracting talent information done!

echo.
echo Extracting glyphs...
PYTHON GlyphExtractor-1.py
PYTHON GlyphExtractor-2.py
PYTHON GlyphExtractor-3.py
PYTHON GlyphExtractor-4.py
echo Exctracting glyphs done!

echo.
echo Extracting level...
PYTHON LevelExtractor.py
echo Extracting level done!

echo.
echo Extracting bag info...
PYTHON EnchantIDs.py
PYTHON 0_fileprepaltocontainers.py
PYTHON 0_RemoveNoCountBags.py
PYTHON 01_AltoBagsCount.py
PYTHON 02_AltoBagsCount.py
PYTHON 01_AltoBagsIDs.py
PYTHON 03_AltoBags.py
PYTHON 04_AltoBagCleaner.py
PYTHON 04.5_AltoBagCleaner.py
PYTHON 05_AltoBagMacro.py
PYTHON AltoBagMacroCleaner.py
PYTHON 01_FormatNoCountBags.py
PYTHON BagExtractor.py
echo Extracting bag info done!

echo.
echo Extracting achievement info...
PYTHON AchievementGranter.py
echo Extracting achievement done!

echo.
echo Extracting currency info...
PYTHON CurrencyExtractor.py
echo Extracting currency done!

echo.
echo Extracting worn equipment...
PYTHON InventoryExtractor.py
echo Extracting worn equipment done!

echo.
echo Extracting faction and reputation info...
PYTHON FactionExtractor.py
PYTHON FactionIDReplacer.py
echo Extracting faction and reputation done!

echo.
echo Extracting pets and mounts info...
PYTHON PetMountGranter.py
echo Extracting pets and mounts done!

echo.
echo Extracting gold...
PYTHON GoldExtractor.py
echo Extracting gold done!

echo.
echo Extracting spellbook and dual talent specialization info...
PYTHON DualTalentLearner.py
echo Extracting spellbook done!

echo.
echo Extracting Profession Spell ID info...
PYTHON ProfessionSpellID.py
echo Extracting Profession Spell ID done!

echo.
echo Extracting Spell IDs for skills, professions, etc...
PYTHON 10-skills.py
PYTHON 11-skillscleanup.py
PYTHON 12-SkillProfessionLearner.py
PYTHON 13-SkillArmorLearner.py
PYTHON 14-SkillWeaponsLearner.py
echo Extracting Spell IDs for skills, professions, etc. done!

echo.
echo Extracting level of skills, professions, etc...
PYTHON 15-SkillLeveler.py
echo Extracting level of skills, professions, etc. done!

echo.
echo Extracting quest information...
PYTHON QuestExtractor-1.py
PYTHON QuestExtractor-2.py
PYTHON add_quest.py
echo Extracting quests in progress done!

echo.
echo Creating macro...
PYTHON InnTeleporter.py
PYTHON OutputCombiner.py
PYTHON Copyer.py
PYTHON ClearTXTFiles.py
echo Macro created! Remember to check error messages above. Character details:
echo.
PYTHON CharDetails.py
echo.
pause