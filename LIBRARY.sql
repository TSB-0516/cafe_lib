Create database Lib;
use Lib;

create table LIBRARY
(
Book_Id varchar(20),
Title varchar(30),
Author varchar(30),
Status varchar(30)
);

INSERT INTO LIBRARY VALUES
('543','To Kill a Mockingbird','Harper Lee','available'),
('712','The Great Gatsby','F. Scott Fitzgerald ','available'),
('834','Ulysses','James Joyce','available'),
('727','The Catcher in the Rye','J. D Salinger','issued'),
('953','Pride and Prejudice','Jane Austen','available'),
('385','Adventures of Huckleberry Finn','Mark Twain','available'),
('686','To the Lighthouse','Virginia Woolf','issued'),
('537','The Sound and the Fury','William Faulkner','available'),
('274','Nineteen Eighty four','George Orwell','available'),
('433','What Evolution Is','Ernst Mayr','issued'),
('865','The Selfish Gene','Richard Dawkins','avaialble'),
('162','The Black Swan','Nassim Nicholas Taleb','issued'),
('309','Man’s Search for Meaning','Viktor Frankl','available'),
('735','The Genealogy of Morals','Friedrich Nietzsche','available'),
('885','Out of Your Mind','Alan Watts','available'),
('627','Sapiens','Yuval Noah Harari','issued'),
('111','Untamed','Glennon Doyle','issued'),
('824','Quiet','Susan Cain','available'),
('555','Citizen: An American Lyric','Claudia Rankine','available'),
('373','Outliers','Malcolm Gladwell','available'),
('638','The Happiness Project','Gretchen Rubin','available');

select * from LIBRARY;
drop table LIBRARY;
drop database Lib