# Tree-Menu

## Установка

Для начала работы с проектом выполните следующие шаги:

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/FIFSAK/Tree-Menu
   cd Tree-Menu/app
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver


- **Доступ к админке**: 
 login: admin, password: 123
- **Urls**:
    -  http://127.0.0.1:8000/  - главная страница со всеми меню
    -  http://127.0.0.1:8000/admin/ - админка
    -  http://127.0.0.1:8000/menu/названиеменю/ - страница с меню