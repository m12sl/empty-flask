# Yet Another Empty Flask project

Единообразное развертывание сайта на виртуальной машине или на удаленном сервере с помощью Ansible

Подключение по `ssh` к виртуалке требует специфических настроек. Работающий вариант `vagrant ssh` или такой:

```
cd local-vm
vagrant ssh-config > ssh.config
ssh -F ./ssh.config vagrant@dev.local -i .vagrant/machines/dev/virtualbox/private_key
```

выглядит диковато. 
Я бы хотел иметь возможность `ssh dev.local`, со стандартным ключом.
Но пробросить ключ пока не получилось.

В случае проблем стоит почистить `~/.ssh/known_hosts`.


В devops/inventory указаны параметры для доступа к виртуалке, с относительным путем до Vagrant ключа.
Порт **ansible_ssh_port** должен совпадать с **host** из Vagrantfile: 

```
config.vm.network :forwarded_port, guest: 22, host: 9980, id: "ssh"
``` 

Проверить работоспособность можно так

```
cd devops
ansible local -i inventory -m ping -vvvv
```


### Пишем playbooks & roles

Плохо: для локальной разработки и деплоя на удаленку нужны разные юзеры. Сейчас они задаются явно в site.yml

Состояние:

Похоже, что работает.

1. Надо убрать жесткий хардкод

2. Сделать перезагрузку сервисов через `handlers` или `notification`


