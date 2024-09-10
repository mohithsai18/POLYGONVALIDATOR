# POLYGONVALIDATOR


Task 2: Polygon Validator Monitoring Tool

Objective

Develop a monitoring tool for Polygon Validators.
Features

    Develop a containerized monitoring tool for Polygon Validator Node which is capable of tracking all the checkpoints signed and proposed by the validator.
    It must be able to trackBor and Heimdall height
    Build Alerting if checkpoints are being missed or heights are out of sync.

Resources:

    Validator performance metrics
    [Checkpoints] (https://docs.polygon.technology/pos/architecture/heimdall/checkpoints/#rest-apis)
    RPC-endpoint

    Deliverables:

    Containerized monitoring solution with Container File in the repository.
    Config file that allows setting the validator address
    Monitoring Requirements:
        Checkpoints being signed by given validator address in configuration file.
        Checkpoints being proposed by validator.
        Bor and Heimdall Height is increasing and in sync.
    In the case where any of the above monitoring requirements are not being met then you must fire alerts that are routed to Telegram. (Take input of chat id and bot token in config file.)
    Ability to choose the rpc endpoint for the tool in the config file which is used to query and compare.




    THIS IS THE TASK,I HAVE BEEN GIVEN TO IMPLEMENT.



PRE-REQUISITES:

1. config.yaml
2. requirements.txt
3. Dockerfile
4. monitoring_tool.py


Make sure all these are in same directory. I have named my directory as polygonvalidator.

STEP 1: Fetching the Validator's address from PIP-4 using this  https://snapshot.4everland.link/ipfs/bafkreifzsqzjbj2cwc6vv6job7ei36vpkn6xtfsi3xfcmyht4ld2uafpyy.
and paste it in the config file. similarly fetch the "chat id" and "token id" from telegram bots.
Also we can fetch using this URL - https://api.telegram.org/botYOUR_BOT_TOKEN/getUpdates    , replace YOUR_BOT_TOKEN with your TOKEN , and run it in the browser.

STEP 2: Filled  out the URL for bor and heimdall (ENDPOINTS).

STEP 3: Use the following commands to create a Docker image and run it using the PRE-REQUISITES.

a) navigate to the polygonvalidator directory.

cd polygonvalidator


b) build the docker image

docker build -t polygon-validator-monitoring .


c) run the docker image

docker run -d polygon-validator-monitoring

![1](https://github.com/user-attachments/assets/851d5dfe-4514-4d61-84c4-ab01756590cb)


d) We observe the container ID being displayed here.





e) Also we can use certain commands to explore more:

![WhatsApp Image 2024-09-10 at 22 36 51](https://github.com/user-attachments/assets/2e255483-9c1f-4a14-ad6c-a7d0a2fb9600)

Here at the bottom we can see the container ID being used.


1) This command is used to see all the existing containers.

docker ps -a   

2) This command is used to remove all the containers present.

   docker system prune -a
   
3) This command is used to restart the container.

    docker restart <container_name_or_id>


 Finally we recieve alerts in telegram in our polygonvalidorbot that was created initially .


 ![2](https://github.com/user-attachments/assets/606cabeb-75b6-48ec-9584-7a90a331c953)



    

    




  

  







    
