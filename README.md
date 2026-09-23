# SDN_Lab_5 — CMS Labs

[![CI](https://github.com/maintainer64/cms-labs-tasks/actions/workflows/ci.yml/badge.svg)](https://github.com/maintainer64/cms-labs-tasks/actions/workflows/ci.yml)
[![CodeQL](https://github.com/maintainer64/cms-labs-tasks/actions/workflows/codeql.yml/badge.svg)](https://github.com/maintainer64/cms-labs-tasks/actions/workflows/codeql.yml)

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/maintainer64/cms-labs-tasks?quickstart=1)

Это воспроизводимый стенд одной лабораторной работы CMS Labs. Сейчас Codespace и локальный Dev Container запускают именно `SDN_Lab_5`; новые работы (например, Bank) будут добавляться позже отдельными модулями. Лаборатория содержит:

- Jupyter Notebook с описанием и заданиями;
- topology для локального Containerlab и шаблон для Clabgate/Clabernetes;
- изолированное окружение сетевых узлов;
- имя отдельного checker, возвращающего структурированный JSON-отчёт;
- автоматические проверки репозитория и полного жизненного цикла лаборатории.

## Быстрый старт в GitHub Codespaces

1. Нажмите **Open in GitHub Codespaces**.
2. Дождитесь сообщения `CMS Labs environment is ready` в терминале.
3. Codespaces автоматически поднимет topology из двух узлов и JupyterLab на порту `8888`.
4. Откройте `modules/SDN_Lab_5/Lab5.ipynb` — это единственная лаборатория текущего Codespace.
5. Выполните задания в Notebook и запустите проверку:

   ```bash
   ./scripts/lab check
   ```

Codespace автоматически запускает:

- официальный Containerlab devcontainer `latest`;
- два узла лабораторной topology;
- `ghcr.io/maintainer64/cms-labs-jupyter:latest`;
- `ghcr.io/maintainer64/cms-labs-checker:latest` по команде проверки.

Порт Jupyter остаётся приватным портом Codespace и защищается авторизацией GitHub. Внутренний Jupyter token отключён только внутри этого защищённого окружения.

Production-кнопка CMS будет открывать тот же `Lab5.ipynb` через workspace session Clabgate. Codespace предназначен для самостоятельного выполнения работы, а CMS frontend — для запуска изолированной Kubernetes-попытки с тем же GitHub commit.

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

## Текущая лабораторная работа

| Модуль | Тип | Тема | Среда | Проверка |
|---|---|---|---|---|
| `SDN_Lab_5` | `network-lab` | Автоматизация SSH и мониторинг SNMP | Jupyter + Containerlab/Clabernetes | `automatic-checker` |

Откройте [`Lab5.ipynb`](modules/SDN_Lab_5/Lab5.ipynb), чтобы начать работу. Контракт `SDN_Lab_5` находится в [`modules/SDN_Lab_5/lab.json`](modules/SDN_Lab_5/lab.json). [`catalog.json`](catalog.json) оставлен как будущий registry для следующих лабораторных.

## Production-контур

Локальный runner воспроизводит те же три артефакта, которые использует production:

- Clabgate читает `topology.template.yaml` и создаёт topology в namespace попытки;
- Jupyter запускается из общего standalone-образа;
- `TEST_PATH=sdn_lab_5` выбирает пакет `labs/sdnlab5` в общем checker-образе.

Полный CMS backend и Moodle/LTI не нужны для решения учебного задания в Codespace. CMS frontend и Clabgate используют тот же session-протокол в Kubernetes-стенде API; topology, Jupyter и checker совпадают с production-контрактом.

Внутри директории модуля единственным файлом `.yaml/.yml` является production-манифест. Это важно: Clabgate рекурсивно собирает все YAML из `labs_path` и применяет их как Kubernetes-ресурсы. Локальная topology поэтому имеет расширение `.clab`, а метаданные — `.json`.
