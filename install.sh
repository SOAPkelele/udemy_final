#!/usr/bin/env bash
# Устанавливаем supervisorctl
apt-get update &&\
apt-get install supervisor -y &&\
# Создаем директорию telegrambot в /home
mkdir -p /home/telegrambot &&\
# Перемещаем все что в текущей директории в эту папку
mv  ./* /home/telegrambot &&\
mv ./.env.dist /home/telegrambot/.env &&\
# Заходим в эту папку
cd /home/telegrambot &&\
# Перемещаем файл конфига в папку супервайзера
mv bot.conf /etc/supervisor/conf.d/bot.conf &&\
apt install python3-pip &&\
python3 -m pip install -r requirements.txt -y &&\

# Теперь пусть супервайзер подгрузит новый кофиг
supervisorctl reread &&\
supervisorctl update
# На этом этапе бот не заработает, потому что нужно прописать все данные в .env и после этого перезапустить в супервайзере