# Создание Ноды

В качестве примера рассматривается Нода для джойстика **chooseMode.py**.
Для создания ноды необходимо:
1. Инициализировать ноду внутри программы (строка **8**);
2. При необходимости, написать Издателя (строка **7**);
3. При необходимости, написать Подписчика (строки **14**);
4. Настроить публикации (строка **30**).

## 1. Инициализация ноды:
```
rospy.init_node(<Имя ноды>)
```

## 2. Написание издателя:
```
pub = rospy.Publisher(<Топик>, <Тип сообщения>, queue_size=10)
```

## 3. Написание подпичика:
```
rospy.Subscriber(<Топик>, <Сообщение>, <Функция для обработки данных из топика>)
```

## 4. Настройка публикации:
```
pub.publish(<Сообщение>)
```
__https://wiki.ros.org/rospy_tutorials/Tutorials/WritingPublisherSubscriber__



Далее, необходимо настроить запуск Ноды для запуска в рамках единого launch-файла:
1. Подключить ноду (строка **1**);
2. Дополнить код для корректной работы (строка **33**);
3. Добавить Ноду в launch-файл (**robot.launch**, строка **4**).

## 1. Подключение ноды:
В начале файла необходимо написать:
```
#!/usr/bin/python3
```

## 2. Дополнить код для корректной работы:
```
rospy.sleep(0.05)
rospy.spin()
```
__https://robocraft.ru/technology/686__

## 3. Добавить Ноду в launch-файл (в примере - в robot.launch):
```
<node pkg="<Имя пакета>" type="<Название файла>" name="<Новое имя ноды (по нему можно обращаться к новой ноде)>"/>
```


Ниже представлен код тестовой Ноды, от которого можно отталкиваться при создании собственных Нод (**NodeForNodeTest.py**):
```
#!/usr/bin/python3

import rospy
from std_msgs.msg import Int8

class TestNode():
    def __init__(self):
        rospy.init_node('TestNode')
        self.TestPub = rospy.Publisher('TestTopic', Int8, queue_size=20)

    def pub(self):
        for i in range(127):
            self.TestPub.publish(Int8(i))
            rospy.sleep(0.05)
        rospy.loginfo("Done!")

if __name__=='__main__':
    TestObj = TestNode()
    TestObj.pub()
    # rospy.spin()
```