@echo off
PYTHON 0_Cleaner.py
PYTHON 1_CharSelector.py
PYTHON 2_Sectioner.py
PYTHON 3_Splitter.py
PYTHON 4_SplitCleaner.py
PYTHON 5_Recipient.py
echo Character filtering done!
echo.

echo Starting container filtering...
PYTHON 10_ContainersNoCount.py
PYTHON 11_ContainersExtractor.py
PYTHON 12_ContainersFilterMacro.py
echo Container filtering done!
echo.


echo Starting achivement handling..
PYTHON 20_AchiExpacHandler.py
PYTHON 21_AchiExpacSelector.py
PYTHON 22_AchievementMacro.py
echo Achievement handling done!
echo.

echo Extracting quest information...
PYTHON 30_QuestCleaner.py
PYTHON 31_QuestIndexDecoder.py
PYTHON 32_QuestDecoder.py
PYTHON 33_QuestIDCombiner.py
PYTHON 34_QuestIDSort.py
PYTHON 35_QuestFiltering.py
PYTHON 36_QuestMacro.py
echo Quest extraction done!
echo.

echo Looking into faction affiliations...
PYTHON 40-ReputationFilter.py
PYTHON 41_ReputationDecoder.py
PYTHON 42_ReputationFailover.py
echo Faction reputations extracted!
echo.

echo Looking for mounts and pets...
PYTHON 50_Mounts.py
PYTHON 51_Pets.py
PYTHON 52_MountSpellIDs.py
PYTHON 53_MountFilter.py
PYTHON 54_MountsAndPetsMacro.py
PYTHON 55_CleanAchievementMountsandPets.py
echo Done looking for mounts and pets!
echo.

echo Finding level and gold!
PYTHON 60_LevelMacro.py
PYTHON 61_MoneyMacro.py
echo Done finding level and gold.
echo.

echo Checking for professions...
PYTHON 90_Professions.py
echo Done checking for professions.
echo.

echo Finalizing macro...
PYTHON 95_Conclude.py
PYTHON 999_Terminate.py