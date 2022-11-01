# Bill-Manager

## Developement Setup

#### Requirements
1. Install [Python](https://www.python.org/downloads/) 3 or above
2. Install [Node JS](https://nodejs.org/en/download/)

#### Python Environment Setup

1. Create python virtual environment
   `python -m venv .venv`

2. Activate the environment
   `.venv\Scripts\activate.bat` (windows)
   `source .venv\scripts\activate` (linux)

3. Install the external dependencies
   `python -m pip install -r requirements.txt`


#### VSCode Configuration (Optional)

1. Open this repo/folder in vscode
2. Configure the default intepreter by opening the command pallet
   (View -> Command Pallet or by shortcut `ctrl+shift+p`) and typing in 
   `Python: Select Interpreter`
3. Select the .venv you created earlier - it will likely already be the 
   recommended one

#### Install Frontend package
1. Navigate to  `cd frontend`
2. Install npm packages `npm install .`
3. Run the production build `npm run prod`
4. (Optional) To Start Frontend application alone use `npm start`

### Run the Application 
1. Activate the environment `.venv\Scripts\activate.bat`
2. To Start the `python run.py`