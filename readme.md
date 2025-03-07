uvicorn main:app
uvicorn app.main:app —reload
alembic revision -m "create posts table”


alembic init alembic
alembic revision -m "create posts table”
alembic current
alembic upgrade <rev_number>
alembic downgrade -1


ssh -i git root@137.184.220.208

sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip
sudo pip3-install virtualenv
sudo apt install postgresql postgresql-contrib -y
su - postgres
psql -U postgres
\password postgres

sudo vi postgresql.conf
sudo vi pg_hba.conf
systemctl restart postgresql

adduser ntltsrs
su - ntltsrs
sudo apt upgrade

cd app
mkdir src
git clone https://github.com/ntserashchuk/example-fastapi.git
in app folder:
cd app/src


cat requirements.txt
pip install -r requirements.txt

printenv

vi .profile

set -o allexport; source /ntltsrs/.env; set +o allexport

alembic upgrade head
uvicorn --host 0.0.0.0 app.main:app 

pip install gunicorn
pip install httptools
pip install uvloop

pip freeze


start from app src
gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app --bind 0.0.0.0:8000


cd /etc/systemd/system
sudo vi api.service
sudo systemctl restart api.service
sudo systemctl status api.service


pkill -9 gunicorn
lsof -i :8000


sudo apt install nginx -y
systemctl start nginx
cd /etc/nginx/sites-available


sudo apt-get install python3-certbot-nginx
sudo certbox --nginx
systemctl enable nginx

sudo ufw allow http
sudo ufw allow https
sudo ufw allow 5432
sudo ufw enable
sudo ufw status


https://certbot.eff.org/instructions?ws=nginx&os=pip
https://ap.www.namecheap.com/Domains/DomainControlPanel/ntltsrs.site/domain/
https://cloud.digitalocean.com/networking/domains/ntltsrs.site?i=b6d9de



docker build -t fastapi .