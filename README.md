# VioletPang_Project4
# FastAPI - Travelist

This is the repository for individual project4 IDS706. In this project, a microservice on AWS is built by using AWS lambda function. 
You can also delopy this project onto AWS EC2 and run it on the cloud. 

![alt text](https://user-images.githubusercontent.com/65413798/204110894-6e32ebfc-b521-43eb-8fa1-ba6b09b2c341.png)

# Deploying to AWS EC2

Log into your AWS account and create an EC2 instance (`t2.micro`), using the latest stable
Ubuntu Linux AMI.

[SSH into the instance](https://aws.amazon.com/blogs/compute/new-using-amazon-ec2-instance-connect-for-ssh-access-to-your-ec2-instances/) and run these commands to update the software repository and install
our dependencies.

```bash
sudo apt-get update
sudo apt install -y python3-pip nginx
```

Clone the FastAPI server app (or create your `main.py` in Python).

```bash
git clone https://github.com/pixegami/fastapi-tutorial.git
```

Add the FastAPI configuration to NGINX's folder. Create a file called `fastapi_nginx` (like the one in this repository).

```bash
sudo vim /etc/nginx/sites-enabled/fastapi_nginx
```

And put this config into the file (replace the IP address with your EC2 instance's public IP):

```
server {
    listen 80;   
    server_name <YOUR_EC2_IP>;    
    location / {        
        proxy_pass http://127.0.0.1:8000;    
    }
}
```


Start NGINX.

```bash
sudo service nginx restart
```

Start FastAPI.

```bash
cd fastapi-tutorial
python3 -m uvicorn main:app
```

Update EC2 security-group settings for your instance to allow HTTP traffic to port 80.

Now when you visit your public IP of the instance, you should be able to access your API.

# Deploying FastAPI to AWS Lambda

Before getting started, please first install all the library in the requirement and then zip all the files by using the command below: 

```bash
pip install -t lib -r requirements.txt
```

To zip it up all the files: 

```bash
(cd lib; zip ../lambda_function.zip -r .)
```

Finally add the mai and json file to the zip: 

```bash
zip lambda_function.zip -u main.py
zip lambda_function.zip -u cities.json
```
