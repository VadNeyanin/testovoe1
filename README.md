## Краткое описание реализации

### Раздел 1. Скрипт

Использовал python и модульную архитектуру. 

**main** создает основную логику скрипта

**logger** содержит функцию, которая форматирует логи, возвращает строковую переменную.

**code_checker** содержит функцию, которая проверяет код статуса больше или равен 400, возвращает true или false

**request** содержит функцию, которая обращается по заданному url и возвращает код статуса ответа и текст ответа.

**.env.example** является примером файла переменных, все переменные там.

### Раздел 2. Docker

Dockerfile проверял через **hadolint**. Спустя несколько итераций вывод после проверки оказался пустым. Скрипт выполняется не от суперпользователя.

### Раздел 3. Ansible

Плейбук и роли были созданы с помощью ansible creator (потому и такая струкура). Примеры работы оставил в логах [success.log](/part_3_ansible/success.log) и [error.log](/part_3_ansible/error.log) (отключил доступ к сети на момент выполнения скрипта).

Плейбук выполняет две роли [docker-install](/part_3_ansible/collections/ansible_collections/v_neyanin/httpscript/roles/docker-install/) и [start-script-and-check](/part_3_ansible/collections/ansible_collections/v_neyanin/httpscript/roles/start-script-and-check/). 

В docker-install вносил изменения в директории [tasks](/part_3_ansible/collections/ansible_collections/v_neyanin/httpscript/roles/docker-install/tasks/). Из особенностей - определение ОС.

В start-script-and-check также вносил изменения в [tasks](/part_3_ansible/collections/ansible_collections/v_neyanin/httpscript/roles/start-script-and-check/tasks/) и [vars](/part_3_ansible/collections/ansible_collections/v_neyanin/httpscript/roles/start-script-and-check/vars/). Контейнер запускается в фоне, docker logs читается с фильтром ошибок. Проверяется успешность выполнения контейнера и логи в docker logs.

"Определить целевую систему" понял как операционную систему, потому что только в таком случае возникают различия в тасках. А изменить систему исполнения, в соответствии с [ansible.cfg](/part_3_ansible/ansible.cfg), можно в [host.ini](/part_3_ansible/inventory/hosts.ini) (собственно там и приведен пример как запускать на localhost, как на удаленном). Запуск плейбука осуществляется по команде
```
ansible-playbook linux_playbook.yml
```