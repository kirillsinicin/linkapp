-- Изменили таблицы
ALTER TABLE link ADD user_id VARCHAR(255);
ALTER TABLE link ADD CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES user(id);
ALTER TABLE link DROP CONSTRAINT original_link;
ALTER TABLE link DROP CONSTRAINT short_link;
-- Добавили юзера как в локальной бд
INSERT user VALUES ("3fdb408b-bffd-491a-9e65-3e93774d43a9","user1", "user1");
--Присвоили этому юзеру все ссылки
UPDATE link SET user_id="3fdb408b-bffd-491a-9e65-3e93774d43a9" WHERE user_id is NULL;
--Сделать user_id not null
ALTER TABLE link MODIFY user_id VARCHAR(255) NOT NULL;
