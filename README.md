just made this pyqt app quickly to ease my job applications on waterlooworks, since I maintain a separate note for my job apps it became a 10 click process to go to a job description.

```bash
source .env/bin/activate && nohup python app.py 2>/dev/null & deactivate && cd   
```

# pyinstaller command to install one binary file with icon as icon.png and name as "WW Open Job Description"
```
pyinstaller --onefile --icon=icon.png app.py --name "WW Open Job Description" --windowed
```