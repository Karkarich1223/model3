-- SQL скрипт для создания базы данных симулятора автосервиса
-- Урок 6: Создание базы данных и таблиц

-- Создание таблицы пользователей
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    login TEXT NOT NULL,
    password TEXT NOT NULL
);

-- Создание таблицы для учета работы
CREATE TABLE work_user (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    id_user INTEGER NOT NULL,
    count_avto INTEGER NOT NULL,
    sec INTEGER NOT NULL,
    FOREIGN KEY (id_user) REFERENCES users(id) ON DELETE CASCADE
);

-- Добавление тестовых пользователей
INSERT INTO users (login, password) VALUES ('admin', 'admin123');
INSERT INTO users (login, password) VALUES ('user1', 'pass1');
INSERT INTO users (login, password) VALUES ('user2', 'pass2');
INSERT INTO users (login, password) VALUES ('user3', 'pass3');
INSERT INTO users (login, password) VALUES ('user4', 'pass4');
INSERT INTO users (login, password) VALUES ('user5', 'pass5');
