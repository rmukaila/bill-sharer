README

##Dev notes##
how to install with pip on windows

1. make sure the projects virtual env is active
2. run: python -m pip install <package name>

how to install an npm package

1. deactivate the virtual env if it's activated (this necessary causes problems with updating package-lock.json etc)
2. Be in the projects root directory (shared_bills_calculator) at the same directory level as the manage.py file
3. run your npm command. example: npm install -D flyonui@latest

how to run the tailwind css engine when developing

1. npm run watch:css
