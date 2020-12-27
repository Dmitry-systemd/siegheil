#!/usr/bin/env bash
# как юзать
#
#        $ API=abcdef123456 RASIA=2 NAME=NewAccTest ./get_num.bash
# NAME - имя файла новой сессии
# API - это наш апи ключ. 
# RASIA - выбор страны.
# 0 - расия
# 1 - украина 
# 2 - казахстан
export API=62510ee7f6d81cb50dc1d6de018Ae3d7 
export RASIA=0
export service=tg
export forward=0
export operator=any
export ref=442230
output=$(curl -s "http://sms-activate.ru/stubs/handler_api.php?api_key=$API&action=getNumber&service=$service&forward=$forward&operator=$operator&ref=$ref&country=$RASIA")
export id=$(echo $output | awk -F: '{print $2}')
export number=$(echo $output | awk -F: '{print $3}' )
echo "Отправляю смс на номер $number"
printf "$number\n" | ./create_session.py $NAME # получаем ошибку EOFError
while true
do
    output=$(curl -s "https://sms-activate.ru/stubs/handler_api.php?api_key=$API&action=getStatus&id=$id")
    code=$(echo $output | awk -F: '{print $2}')
    if [ $code ]
    then 
        echo "Получен код $code"
        printf "$number\n$code\n$code\n" | ./create_session.py $NAME 
        exit
    fi
    sleep 1
done