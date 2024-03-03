# [Molotov](https://molotov.readthedocs.io/en/stable/index.html) API Blast

## Введение

Проект **Molotov API Blast** представляет собой комплекс скриптов для тестирования нагрузки на API, используя библиотеку Molotov. Эти скрипты включают в себя выполнение GET и POST запросов, обработку исключений и логирование.

## Установка

Для начала работы с проектом вам потребуется [Python](https://www.python.org/) 3.7 или более новый. Вы можете установить Molotov с помощью pip:

```bash
pip install molotov

```
## Установка проекта

Следуйте этим шагам для установки и запуска проекта:

1. **Клонирование репозитория**
    ```bash
    git clone https://github.com/ZhikharevAl/FastApi-Molotov-Testing.git
    ```

2. **Создание и запуск Docker-файла**
   Перейдите в директорию проекта и запустите Docker:
    ```bash
    cd FastApi-Molotov-Testing
    docker build -t <название образа> .
    docker run -it --rm <название образа>
    ```
   
3. **Запуск сценариев Molotov**
   В зависимости от того, как вы настроили свой проект, вы можете запустить сценарии Molotov следующим образом:
    ```bash
   docker exec -it <container_id> molotov -w <workers> -p <processes> -d <duration> -x <script>

    ```
- `<container_id>`: Идентификатор Docker контейнера, в котором вы хотите выполнить команду.
- `<workers>`: Количество рабочих процессов, которые вы хотите использовать для тестирования.
- `<processes>`: Количество процессов, которые вы хотите использовать для тестирования.
- `<duration>`: Продолжительность тестирования в секундах.
- `<script>`: Имя скрипта Molotov, который вы хотите запустить.
  