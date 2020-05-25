#!/usr/bin/env bash
# Создаем директорию telegrambot в /home
mkdir -p /home/telegrambot
# Перемещаем все что в текущей директории в эту папку
mv -R . /home/telegrambot
# Заходим в эту папку
cd /home/telegrambot
# Перемещаем файл конфига в папку супервайзера
mv bot.conf /etc/supervisor/conf.d/bot.conf
# Теперь пусть супервайзер подгрузит новый кофиг
supervisorctl reread
supervisorctl update
