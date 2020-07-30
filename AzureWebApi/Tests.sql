
INSERT INTO  ContactsSet VALUES ('Asahi','myemail@mail.com','5555555555')
SELECT * FROM ContactsSet

UPDATE ContactsSet SET Phone = '555555'


EXEC sp_rename  'ContactsSet' ,'ContactSet'