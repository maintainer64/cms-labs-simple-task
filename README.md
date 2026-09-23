# CMS Labs Tasks: примеры лабораторных работ

[![CI](https://github.com/maintainer64/cms-labs-tasks/actions/workflows/ci.yml/badge.svg)](https://github.com/maintainer64/cms-labs-tasks/actions/workflows/ci.yml)
[![CodeQL](https://github.com/maintainer64/cms-labs-tasks/actions/workflows/codeql.yml/badge.svg)](https://github.com/maintainer64/cms-labs-tasks/actions/workflows/codeql.yml)

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/maintainer64/cms-labs-tasks?quickstart=1)

Это коллекция примеров лабораторных работ CMS Labs, которые можно выполнять в браузере или локально. Каждый модуль содержит:

- Jupyter Notebook с описанием и заданиями;
- topology для локального Containerlab и шаблон для Clabgate/Clabernetes;
- изолированное окружение сетевых узлов;
- имя отдельного checker, возвращающего структурированный JSON-отчёт;
- автоматические проверки репозитория и полного жизненного цикла лаборатории.

## Быстрый старт в GitHub

1. Нажмите **Open in GitHub Codespaces**.
2. Дождитесь сообщения `CMS Labs environment is ready` в терминале.
3. Codespaces автоматически откроет JupyterLab на порту `8888`.
4. Откройте `modules/SDN_Lab_5/Lab5.ipynb` и выполняйте задания.
5. Запустите проверку:

   ```bash
   ./scripts/lab check
   ```

Codespace автоматически запускает:

- официальный Containerlab devcontainer `latest`;
- два узла лабораторной topology;
- `ghcr.io/maintainer64/cms-labs-jupyter:latest`;
- `ghcr.io/maintainer64/cms-labs-checker:latest` по команде проверки.

Порт Jupyter остаётся приватным портом Codespace и защищается авторизацией GitHub. Внутренний Jupyter token отключён только внутри этого защищённого окружения.

## Запуск на компьютере

Рекомендуемый способ одинаков для Linux, macOS и Windows:

1. Установите Docker и Visual Studio Code.
2. Установите расширение **Dev Containers**.
3. Клонируйте репозиторий и откройте его в VS Code.
4. Выполните `Dev Containers: Rebuild and Reopen in Container`.

После сборки окружение поднимется автоматически. Управлять им можно командами:

```bash
./scripts/lab up       # поднять topology и JupyterLab
./scripts/lab status   # показать состояние
./scripts/lab check    # получить JSON-отчёт checker
./scripts/lab reset    # удалить выполненную конфигурацию узлов
./scripts/lab down     # остановить лабораторию
```

На Linux с уже установленными Docker и Containerlab эти команды можно запускать напрямую без Dev Container.

## Каталог лабораторных работ

| Модуль | Тип | Тема | Среда | Проверка |
|---|---|---|---|---|
| `SDN_Lab_5` | `network-lab` | Автоматизация SSH и мониторинг SNMP | Jupyter + Containerlab/Clabernetes | `automatic-checker` |

Откройте [`Lab5.ipynb`](modules/SDN_Lab_5/Lab5.ipynb), чтобы начать работу. Машиночитаемый список находится в [`catalog.json`](catalog.json), расширенное описание типов — в [`description.md`](description.md), а контракт модуля — в [`modules/SDN_Lab_5/lab.json`](modules/SDN_Lab_5/lab.json).

## Production-контур

Локальный runner воспроизводит те же три артефакта, которые использует production:

- Clabgate читает `topology.template.yaml` и создаёт topology в namespace попытки;
- Jupyter запускается из общего standalone-образа;
- `TEST_PATH=sdn_lab_5` выбирает пакет `labs/sdnlab5` в общем checker-образе.

Полный CMS backend и Moodle/LTI намеренно не запускаются внутри Codespace: их роль здесь заменяет локальный runner. Сама лабораторная topology, Jupyter и проверка совпадают с production-контрактом.

Внутри директории модуля единственным файлом `.yaml/.yml` является production-манифест. Это важно: Clabgate рекурсивно собирает все YAML из `labs_path` и применяет их как Kubernetes-ресурсы. Локальная topology поэтому имеет расширение `.clab`, а метаданные — `.json`.
