# BehaveProject

The Automation f/w has two scenarios login and logout
All Feature files are present inside features folder and categorized based on functionality
All Step defs are present inside steps folder
Hooks code is present in environment.py which opens browser and close browser after each scenario
Behave.ini is present outside the features folder and has attributes which has enabled console logs

And the command to run scenario is :
behave --define browser="chrome" --define env="stage" --tags=regression

behave --define timeout=900 -f allure_behave.formatter:AllureFormatter -o reports/ --no-capture --format plain  --tags=smoke
