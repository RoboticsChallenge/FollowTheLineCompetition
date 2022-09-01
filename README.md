# Follow The Line Competition
http://jderobot.github.io/RoboticsAcademy/exercises/AutonomousCars/follow_line/

Competition in follow the line 
- [x] Image proccessing completed 

First section of progam sorts out imageproccessing.
To start programing car, start at line 49 from https://github.com/RoboticsChallenge/FollowTheLineCompetition/blob/main/InitialCode/InitialStarter.py

## Current Record
| Time(min:sec:ms)| Name | Controller Type |  
|-----------------|---------------|-----------------|
| 04:07:0593 | Fredrik Skavlem | Bang-bang Controller |
    
### How to get Started in Windows
#### install Docker
    -   docker install file
            https://docs.docker.com/desktop/windows/wsl/
    -   install linux kernel(needed for docker) only step 4 and 5.
            https://docs.microsoft.com/en-us/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package
    -   Open Windows PowerShell as adminitrator (terminal for windows) and exeute
            wsl --set-default-version 2
    -   Restart Computer
#### How to start competition window
    -   site for exercise and info about program variables
        http://jderobot.github.io/RoboticsAcademy/exercises/AutonomousCars/follow_line/
    -   open Windows PowerShell, execute command to get latest build
            docker pull jderobot/robotics-academy:latest
    -   Wait for build to finish download
    -   start docker program from PowerShell
            docker run --rm -it -p 8000:8000 -p 2303:2303 -p 1905:1905 -p 8765:8765 -p 6080:6080 -p 1108:1108 jderobot/robotics-academy
    -   Open web browser and go to 127.0.0.1:8000/
