# Руководство по установке всего Программного Обеспечения

# Часть 1 - Raspberry Pi 4

## 1. Установка ОС на Raspberry Pi
Не смотря на существование специализированной для одноплатного компьютера операционной системы Raspberry Pi OS, в проекте применяется дистрибутив **Ubuntu Server 20.04.5 LTS (64-bit)**.

![Image_1](https://github.com/Hedgehog0224/catkin_ws/blob/docs/Documentation/Images/Folder-3-1/003-1-01.png)

- _https://ubuntu.com/download/raspberry-pi_;
- _https://ubuntu.com/blog/ubuntu-20-04-lts-is-certified-for-the-raspberry-pi_;
- _https://ubuntu.com/tutorials/how-to-install-ubuntu-on-your-raspberry-pi#1-overview_;
- _https://robotclass.ru/articles/raspberry-pi-os-install/_;
- _https://habr.com/ru/sandbox/174416/_.


### 1.1 Установка Raspberry Pi Imager
Нельзя просто взять и поставить какую-либо операционную систему на Raspberry при помощи загрузочного носителя (будь то флешка или microSD-карта).

![Image_2](https://github.com/Hedgehog0224/catkin_ws/blob/docs/Documentation/Images/Folder-3-1/003-1-2.jpg)

Вместо этого применяется приложение **Raspberry Pi Imager**. Оно позволяет быстро и просто установить **Ubuntu Server 20.04** или иную операционную систему на карту microSD, готовую к использованию с вашим одноплатником.

Приложение скачивается с официального сайта - _https://www.raspberrypi.com/software/_.

![Image_3](https://github.com/Hedgehog0224/catkin_ws/blob/docs/Documentation/Images/Folder-3-1/003-1-3.png)


### 1.2 Работа в Установщике Raspberry Pi Imager
После установки запускаете приложение. Для нажатия доступно три кнопки: **Выбрать устройство**, **Выбрать ОС** и **Выбрать Запоминающее Устройство**.

![Image_4](https://github.com/Hedgehog0224/catkin_ws/blob/docs/Documentation/Images/Folder-3-1/003-1-4.png)

- Во-первых, необходимо **Выбрать устройство** - из предоставленного списка пункт, соответствующий модели вашего МК. В наборе применяется модель **Raspberry Pi 4B**.

![Image_5](https://github.com/Hedgehog0224/catkin_ws/blob/docs/Documentation/Images/Folder-3-1/003-1-5.png)

- Во-вторых, необходимо **Выбрать ОС**, которую требуется установить.\
Для установки **Ubuntu Server 20.04.5 LTS (64-bit)** выбираете *Other general-purpose OS -> Ubuntu -> Ubuntu Server 20.04.5 LTS (64-bit)*.

![Image_6](https://github.com/Hedgehog0224/catkin_ws/blob/docs/Documentation/Images/Folder-3-1/003-1-06.png)\
![Image_7-1](https://github.com/Hedgehog0224/catkin_ws/blob/docs/Documentation/Images/Folder-3-1/003-1-7-1.png)
![Image_7-2](https://github.com/Hedgehog0224/catkin_ws/blob/docs/Documentation/Images/Folder-3-1/003-1-7-2.png)

- В-третьих, из списка выбрать неободимый пункт (скорее всего, будет отображаться единственный пункт - вставленная в разъём компьютера microSD).

![Image_8](https://github.com/Hedgehog0224/catkin_ws/blob/docs/Documentation/Images/Folder-3-1/003-1-08.png)\
![Image_9](https://github.com/Hedgehog0224/catkin_ws/blob/docs/Documentation/Images/Folder-3-1/003-1-9.png)\
![Image_10](https://github.com/Hedgehog0224/catkin_ws/blob/docs/Documentation/Images/Folder-3-1/003-1-010.png)\
![Image_11](https://github.com/Hedgehog0224/catkin_ws/blob/docs/Documentation/Images/Folder-3-1/003-1-11.png)

Далее, необходимо нажать на кнопку **Далее**. В открывшимся окне нажать на кнопку **Изменить параметры**. Далее:
1. Выбрать раздел **Общее**. Вводите *Имя хоста*, задаёте *Имя пользователя* и *Пароль* (пароль требуется для подключения к МК и автоматически шифруется при последующем открытии приложения), *SSID* (название Wi-Fi, к которому подключается МК), *Пароль* (происходит то же, что и с предыдущим). Обязательно необходимо выбрать *Страну Wi-Fi* как **RU**. Можно настроить часовой пояс.

![Image_12](https://github.com/Hedgehog0224/catkin_ws/blob/docs/Documentation/Images/Folder-3-1/003-1-12.png)

2. Выбрать раздел **Службы**, выбрать **Включить SSH** (настройка аутентификации по паролю в зависимости от пожеланий). Это необходимо для последующей работы с удалённого устройства.

![Image_13](https://github.com/Hedgehog0224/catkin_ws/blob/docs/Documentation/Images/Folder-3-1/003-1-13.png)

3. Выбрать раздел **Параметры**. Настройка по усмотрению.

![Image_14](https://github.com/Hedgehog0224/catkin_ws/blob/docs/Documentation/Images/Folder-3-1/003-1-14.png)

Для последующей установки необходимо сохранить параметры (нажав на кнопку **Сохранить**) и нажать на кнопку **Да**. Происходит запись образа на microSD. В противном случае, можно вернуться к изменению параметров (кнопка **Изменить параметры**), либо вернуть параметры по умолчанию (кнопка **Нет, очистить параметры**), либо стереть все существующие данные с microSD, либо вернуться к настройке параметров установщика, нажав на крестик в правом верхнем углу окна.

Когда настройка параметров завершена, необходимо смонтировать образ на запоминающее устройство. В финальном окне жмём кнопку **Да** и ждём завершения процедуры копирования.

### 1.3 Установка ОС на Raspberry Pi
После записи образа на microSD необходимо вытащить её из порта компьютера и вставить в порт одноплатного компьютера. Затем, подключаем Raspberry Pi к питанию. Необходимо дождаться готовности одноплатного компьютера к работе - должен беспрерывно гореть красный и перестать мигать зелёный светодиоды.


## 2. Начало работы с Raspberry Pi
### 2.1 Подключение к Raspberry Pi
Необходимо подключиться к одноплатному компьютеру через протокол SSH. Для этого в терминале следует ввести следующую команду:

`ssh <Имя пользователя>@<имя хоста>.local`

После, требуется ввести пароль пользователя. Подключение установлено.

### 2.2 Настройка I2C-портов
Для дальнейшей корректной работы образовательного робота нужно провести настройку портов для передачи данных по протоколу I2C:
1. Ввести команду `sudo raspi-config`. В открытом окне выбрать третий пункт (**3 Interface Options**).

![Image_15](https://github.com/Hedgehog0224/catkin_ws/blob/docs/Documentation/Images/Folder-3-1/003-1-15.png)

2. При помощи клавиш-стрелок выбрать **Select** , открывается подробные настройки интерфейса.

![Image_16](https://github.com/Hedgehog0224/catkin_ws/blob/docs/Documentation/Images/Folder-3-1/003-1-16.png)

3. Выбрать пятый пункт (**I5 I2C**).

![Image_17](https://github.com/Hedgehog0224/catkin_ws/blob/docs/Documentation/Images/Folder-3-1/003-1-17.png)

4. Выбрать **Select**, **Yes**, **OK**.

![Image_18](https://github.com/Hedgehog0224/catkin_ws/blob/docs/Documentation/Images/Folder-3-1/003-1-18.png)
![Image_19](https://github.com/Hedgehog0224/catkin_ws/blob/docs/Documentation/Images/Folder-3-1/003-1-19.png)
![Image_20](https://github.com/Hedgehog0224/catkin_ws/blob/docs/Documentation/Images/Folder-3-1/003-1-20.png)

Итог - порты для корректной работы I2C запущены. Необходимо выйти из настроек, выбрав **Finish**.

![Image_21](https://github.com/Hedgehog0224/catkin_ws/blob/docs/Documentation/Images/Folder-3-1/003-1-21.png)


_https://www.raspberrypi.com/documentation/computers/configuration.html_

## 2.3 Настройка ОС после установки
- apt-get update
- apt-get install -y --no-install-recommends 
- apt-get install ros-noetic-ros-base=1.5.0-1*
- apt-get install nano
- apt-get install git
- apt-get install python3-pip
- apt-get install ros-noetic-joy
- apt-get install ros-noetic-rplidar-ros
- python3 -m pip install evdev
- python3 -m pip install RPi.GPIO
- python3 -m pip install pyserial
- python3 -m pip install board
- python3 -m pip install opencv-contrib-python
- pip3 install adafruit-circuitpython-pca9685
- pip3 install adafruit-circuitpython-motor

## 3. Удаление ОС с Raspberry Pi
При возникновении неустранимых критических ошибок на уровне ОС, неорбходимо извлечь microSD-карту, подключить к компьютеру и на этапе работы в установщике **Raspberry Pi Imager** перезаписать установщик.


## 4. Конфигурации, Настройки и Параметры Raspberry Pi
__https://www.raspberrypi.com/documentation/computers/configuration.html__

Необходимо выбрать необходимые разделы из представленных и подробно описать их:
- Интерактивные конфигурации;
    * Параметры системы;
    * Параметры отображения;
    * Параметры интерфейса;
    * Параметры производительности;
    * Параметры локализации;
    * Расширенные возможности;
- Неинтерактивные конфигурации;
    * Параметры системы;
    * Параметры отображения;
    * Варианты интерфейса;
    * Параметры производительности;
    * Варианты локализации;
    * Расширенные возможности;
    * Обновление;
- Дисплеи;
- Аудио;
- Беспроводное подключение;
- Отключение экрана;
- Внешнее хранилище;
- Настройка Raspberry Pi;
- Параметры безопасности и доступа;
- Удалённая настройка;
- Точка доступа;
- Прокси-сервер;
- Содержимое папки загрузчика?;
- Настройки UART.

## 5. Установка ROS на ОС
ROS Noetic.

- _https://www.ros.org/_;
- *https://ru.wikipedia.org/wiki/ROS_(операционная_система)*;

# Часть 2 - Jetson Nano Orin