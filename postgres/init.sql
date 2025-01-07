CREATE TABLE table1 (
    id SERIAL PRIMARY KEY,
    f_name VARCHAR(20),
    l_name VARCHAR(20),
    birth_date DATE,
    phone_number BIGINT
);

INSERT INTO table1 (f_name, l_name, birth_date, phone_number) VALUES
    ('Михаил', 'Кузьмин', TO_DATE('12-06-2003', 'DD-MM-YYYY'), 934617277),
    ('Мухсин', 'Гулов', TO_DATE('11-11-2011', 'DD-MM-YYYY'), 1234566789),
    ('Темур', 'Паллаев', TO_DATE('10-10-2010', 'DD-MM-YYYY'), 987654321),
    ('Рустам', 'Ходжаев', TO_DATE('15-12-2015', 'DD-MM-YYYY'), 741258963),
    ('Просто', 'Чел', TO_DATE('11-11-2011', 'DD-MM-YYYY'), 369852147);