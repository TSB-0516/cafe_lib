use Lib;

create table books_issued
(
Book_Id varchar(20),
issueto varchar(30)
);

Insert INTO books_issued VALUES
('727','Mary Gibson'),
('111','Heloise Perez'),
('162','Milo Lee'),
('686','Margaret Shaw'),
('433','Lily Ford'),
('627','Hazel Flores');

select * from books_issued;
drop table books_issued;