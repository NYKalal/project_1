# project_1

Deployment commands:
step 1: launch an ec2 ubuntu instance in AWS

step2: click on instance and press "connect"
        your ec2 instance will be launched
        
step3: runnfollowing commands:
        sudo apt update
        sudo apt upgrade -y
        git clone <"ulr of your git project repository">
        (# you need to create .env file because api_key is protected in environment variable.)
        touch .env
        ls -a
        vi .env
        (press i to insert into the file, copy you api_key and paste and press esc and :wq to save and quit the file)
        cat .env
        sudo apt install python3-pip
        pip install -r requirements.txt
        python3 -m streamlit run streamlitAPP.py

step4: go to, ec2 instance->security->security groups->edit inbound rules->add rule
       select custom TCP    8501    custom  0.0.0.0/0 -> save rule

step5: copy the public IP of your instance and paste in your browser along with streamlit port -> say -> 44.211.131.13:8501

your application is running perfect
thank you
