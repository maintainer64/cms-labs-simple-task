# Описание SDN_Lab_5

`cms-labs-simple-task` содержит одну воспроизводимую лабораторную работу — `SDN_Lab_5`. Репозиторий можно указывать в `CMS_TASK_URL` полной GitHub-ссылкой:

```text
CMS_TASK_URL=https://github.com/maintainer64/cms-labs-simple-task
```

Лаборатория размещается в `modules/SDN_Lab_5` и не является Git-подмодулем. Это позволяет Clabgate закрепить попытку на одном commit SHA и получить notebook, topology и метаданные согласованной версии.

## Типы

Контракт лаборатории описывает её по нескольким независимым признакам:

- `network-lab` — предметный тип: практическая работа с сетевыми узлами;
- `jupyter-notebook` — пользовательский интерфейс с заданием и кодом студента;
- `containerlab` — локальный topology runtime для Codespaces и Dev Container;
- `clabernetes` — Kubernetes runtime, разворачиваемый Clabgate;
- `automatic-checker` — автоматическая проверка с JSON-отчётом и оценкой.

Способы запуска перечисляются отдельно: `github-codespaces`, `local-devcontainer` и `clabgate-kubernetes`. Следующие работы можно будет добавлять в `modules/` без изменения контракта текущей работы.

## SDN_Lab_5

Практическая работа знакомит с программной настройкой Linux-based сетевых узлов через SSH и чтением состояния по SNMP. Студент назначает адреса лабораторному каналу, проверяет связность и получает структурированный отчёт.

Типы: `network-lab`, `jupyter-notebook`, `containerlab`, `clabernetes`, `automatic-checker`.

В отличие от старой коллекции, пример не зависит от приватных Cisco IOL-образов или внутренней сети университета и полностью запускается в GitHub Codespaces.
