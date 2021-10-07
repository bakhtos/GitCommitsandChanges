This is a simple miner to create a csv file with all projects' commits (GIT_COMMITS.csv) and changes of files for each commit (GIT_COMMITS_CHANGES.csv). If run on a folder contaning several projects, it creates such files for each projects as well as one master file combining all projects.
Originally written in [CloudSEA.AI](https://research.tuni.fi/cloudsea/) Research group of Tampere University to create the [Technical Debt Dataset](https://github.com/clowee/The-Technical-Debt-Dataset)

The program expects to find a file call ```CONST.py``` in the parent directory of the cloned repository (ie in the same folder where ```git clone git@github.com:bakhtos/GitCommitsandChanges.git``` was run) which defines at least these constants:

```python
ABS_REPO_PATH = # Folder where analyzed projects were cloned to 
ABS_SAVE_PATH = # Folder where to save the results
```

The program will create the output folder, if it does not exists yet.
If the folder with projects is empty (does not contain any folders) a ```FileNotFoundError``` is raised.
For each project in the ```ABS_REPO_PATH``` a folder with the same name is created in ```ABS_SAVE_PATH```, where that projects' results are stored. The master file combining all projects is stored in ```ABS_SAVE_PATH``` itself.
