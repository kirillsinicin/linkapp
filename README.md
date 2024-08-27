# linkapp - сокращатель ссылок
Приложение развёрнуто на хостинге [pythonanywhere](https://www.pythonanywhere.com/about/company_details/)
## Как пользоваться сервисом через Postman
### Регистрация
1. POST-запрос по адресу https://kirillsinitsin.pythonanywhere.com/auth/register
2. Тело запроса вида:
```console
"login":"your_login"
"password":"your_password"
```
3. Отправить запрос
> В таком случае вернётся Bearer-токен, который понадобится при создании короткой ссылки.
> Примечание: иногда хостинг может не обработать запрос, в таком случае его нужно просто повторить.
### Создание короткой ссылки
1. POST-запрос по адресу https://kirillsinitsin.pythonanywhere.com/links/create
2. Тело запроса вида:
```console
"name":"link_name"
"destination":"original_link"
```
3. В разделе "Authorization" выбрать тип "Bearer Token", затем вставить в поле сгенерируемый токен
4. Отправить запрос
> После чего вы получите ссылку, которая будет перенаправлять на оригинальный адрес
> Пример [ссылки](https://kirillsinitsin.pythonanywhere.com/links/2fafe1ef7c), которая ведёт на этот проект.
