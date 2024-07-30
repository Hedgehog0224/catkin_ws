# Ноды, применяемые в проекте:
1 - **lidar** -\
2 - **Joy** -\
3 - **ChoseMode** -\
4 - **UltraSonic** -\
5 - **MainNode** -\
6 - **MatMotor** -\
7 - **ШимКонтроллер** -\

# Топики, применяемые в проекте:
1 - **scan** -\
2 - **Joy** -\
3 - **Mode** -\
4 - **distance** -\
5 - **вычисления** -\
6 - **скорости** -\

# Связь между Нодами посредством Топиков:
1 - **lidar** --(**scan**)-> **MainNode**\
2 - **Joy** --(**Joy**)-> **ChoseMode**\
3 - **ChoseMode** --(**Mode**)-> **MainNode**\
4 - **UltraSonic** --(**distance**)-> **MainNode**\
5 - **MatMotor** --(**вычисления**)-> **MainNode**\
6 - **MainNode** --(**скорости**)-> **MatMotor**\
7 - **MatMotor** ---> **ШимКонтроллер**\
