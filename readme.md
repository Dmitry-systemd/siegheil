# Документация устарела!
Она не охватывыет кучу вещей, например вк, зиг хайль мессенжер и гуй.
## VTSoft SIEGHEIL-III - флуд бот телеграм

У siegheil.py есть следующие параметры:

`--target` - Кого ебать будем. Можно вставить @username или хеш из ссылки на приватный чат. т.е. часть после joinchat/. Например, GxmaxU1a5udiTYXRfOMZFA. А так же, можно указать путь к файлу с списком таргетов или разделить таргеты пробелом. (несколько таргетов не работает в режиме рейда).

`--mode` - режим работы

    spam-seq - спам по одному сообщению по таргетам. Работает по таргетам одним юзером до тех пор, пока это возможно. После того, как юзер ловит бан, выбирается другой юзер. [готово, но не протестировано]

    spam-par - спам по одному сообщению по таргетам. Каждый юзер берет на себя последний таргет из списка. [пока не готово]

    raid - флуд сообщениями в конкретный чат.
     
    db - создание базы данных из юзеров чатов из таргета. Одним юзером по очереди собираются таргеты. В случае неудачи, пробуется другой юзер.

    setpic - установить аватарки. 

    join - подписаться на канал / вступить в группу.

    read - накрутить просмотры на канал. Один фейк может только один раз посмотреть конкретный пост. Если в --target будет только @юзернейм канала, то будут получены все посты из канала => если их дохуя, то это займет много времени. Однако, можно указать --target @channel:40, чтоб прочитать пост с айди 40 или --target @channel:30-60, чтоб прочитать посты с 30 по 60, --target @channel:30+, чтоб прочитать все после 30.

`--file` - файл, которым флудим. Можно указать несколько, разделяя пробелом. А ещё, если твой шелл может так, то можно `--file "$(ls porno/*.jpg)"`. В режиме создания базы - файл, куда будут заноситься юзернеймы.

`--msg` - сообщение, которое надо слать. Если указан файл, то это будет к нему подписью.

`--pause` - пауза между каждым действием. В секундах.

`--sessions` - выбор сессий. Разделяя пробелом. @all - все сессии в текущей директории.

`--verbose 1` - срать в терминал ненужной инфой.

`--update 1` - проверять обновления.


`create_session.py` создаст файл .session и выйдет. Пример - `./create_session.py MySession`

# fake activity generator 

`--sessions` - выбор сессий. Разделяя пробелом. @all - все сессии в текущей директории.

`--names` - имена для фейков. 0 - не менять.

`--messages` - текстовые сообщения, которые шлют фейки. Разделяя их \n===\n===\n запишите в файл, путь к которому укажите.

`--files` - файлы, которые шлют фейки. сюда можно всякие мемы и ржачные гифы запихать. пиши путь к папке, в которой лежат файлы.

`--chatnames` - фейки создают групповые чаты. названия для них скиньте сюда

`--pics` - авы. пиши путь к папке, в которой лежат файлы.
# FAQ (фак ю)

> что это

не твое блядское дело. софтина для стопламерс.

> я боту написал файл а он ниработаит памаги

в пути не должно быть пробелов. не потому, что я не мог сделать иначе, а потому что пошел нахуй пидор.
