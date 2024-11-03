-- Inserting data into Companies
INSERT INTO Companies (id, name, address) VALUES 
(1, 'Innovate LLC', '123 Main St'),
(2, 'TechCorp', '456 Oak Ave'),
(3, 'SoftSolutions', '789 Pine Rd'),
(4, 'DevCorp', '123 Elm St'),
(5, 'NetSolutions', '789 Birch Ave'),
(6, 'CloudBase', '987 Maple St'),
(7, 'AlphaSoft', '654 Walnut St'),
(8, 'BetaTech', '321 Cedar St'),
(9, 'OmegaCorp', '111 Oak Ridge'),
(10, 'BlueSky Solutions', '102 Sunset Blvd');

-- Inserting data into Candidates
INSERT INTO Candidates (id, name, surname, email, phone) VALUES
(1, 'J2ohn', 'Doe', 'john1.doe@example.com', '380994926865'),
(2, 'Jane', 'Smith', 'jane.smith2@example.com', '380911926866'),
(3, 'Michael', 'Johnson', 'michael.johnson3@example.com', '380991938867'),
(4, 'Emily', 'Davis', 'emily.davis4@example.com', '380291926868'),
(5, 'Chris', 'Wilson', 'chris.wilson5@example.com', '381991926869'),
(6, 'Paul', 'Taylor', 'paul.taylor6@example.com', '380991926861'), 
(7, 'Lucy', 'Brown', 'lucy.brown7@example.com', '320991926870'),
(8, 'David', 'White', 'david.white8@example.com', '380921926871'),
(9, 'Jessica', 'Moore', 'jessica.moore9@example.com', '380991926872'),
(10, 'Daniel', 'Anderson', 'daniel.anderson10@example.com', '380991926873');

-- Inserting data into Contact_person
INSERT INTO Contact_person (id, name, phone, email) VALUES
(1, 'John Doe', 223457719, 'jo22hn.doe11@example.com'),
(2, 'Jane Smith', 987654331, 'jane.smith12@example.com'),
(3, 'Michael Johnson', 551555555, 'michael.johnson13@example.com'),
(4, 'Emily Davis', 444441444, 'emily.davis14@example.com'),
(5, 'Chris Wilson', 333313333, 'chris.wilson15@example.com'),
(6, 'Paul Taylor', 222221222, 'paul.taylor16@example.com'),
(7, 'Lucy Brown', 111111211, 'lucy.brown17@example.com'),
(8, 'David White', 999991999, 'david.white18@example.com'),
(9, 'Jessica Moore', 888188888, 'jessica.moore19@example.com'),
(10, 'Daniel Anderson', 717777777, 'daniel.anderson20@example.com');

-- Inserting data into Projects
INSERT INTO Projects (id, name) VALUES 
(1, 'Project A'), 
(2, 'Project B'), 
(3, 'Project C'), 
(4, 'Project D'), 
(5, 'Project E'), 
(6, 'Project F'), 
(7, 'Project G'), 
(8, 'Project H'), 
(9, 'Project I'), 
(10, 'Project J');

-- Inserting data into Interviews
INSERT INTO Interviews (id, date, company_id, candidate_id) VALUES
(1, '2023-10-10 09:00:00', 1, 1),
(2, '2023-10-11 10:30:00', 2, 2),
(3, '2023-10-12 11:45:00', 3, 3),
(4, '2023-10-13 09:00:00', 4, 4),
(5, '2023-10-14 10:30:00', 5, 5),
(6, '2023-10-15 11:45:00', 6, 6),
(7, '2023-10-16 12:00:00', 7, 7),
(8, '2023-10-17 14:30:00', 8, 8),
(9, '2023-10-18 15:00:00', 9, 9),
(10, '2023-10-19 16:00:00', 10, 10);

-- Inserting data into Interview_Results
INSERT INTO Interview_Results (id, rating, candidate_id, interview_id) VALUES
(1, 'high', 1, 1),
(2, 'medium', 2, 2),
(3, 'low', 3, 3),
(4, 'medium', 4, 4),
(5, 'high', 5, 5),
(6, 'low', 6, 6),
(7, 'medium', 7, 7),
(8, 'high', 8, 8),
(9, 'low', 9, 9),
(10, 'medium', 10, 10);

-- Inserting data into Experience
INSERT INTO Experience (id, job_title, start_date, end_date, company_id, candidate_id) VALUES
(1, 'Software Engineer', '2020-01-01', '2023-01-01', 1, 1),
(2, 'System Analyst', '2019-05-01', '2022-05-01', 2, 2),
(3, 'Project Manager', '2018-09-01', '2021-09-01', 3, 3),
(4, 'Frontend Developer', '2019-02-01', '2022-03-01', 4, 4),
(5, 'Backend Developer', '2018-07-01', '2021-07-01', 5, 5),
(6, 'Data Scientist', '2017-09-01', '2020-09-01', 6, 6),
(7, 'UI/UX Designer', '2016-04-01', '2019-04-01', 7, 7),
(8, 'DevOps Engineer', '2015-05-01', '2018-05-01', 8, 8),
(9, 'Product Owner', '2021-06-01', '2023-06-01', 9, 9),
(10, 'Business Analyst', '2019-03-01', '2022-03-01', 10, 10);

-- Inserting data into Vacanci
-- Оновлений SQL-запит для вставки у Vacanci з правильною назвою колонки
INSERT INTO Vacanci (id, title, description, contact_person_id, Projects_id, company_id) VALUES
(1, 'Software Engineer', 'Develop software applications', 1, 1, 1),
(2, 'System Analyst', 'Analyze system requirements', 2, 2, 2),
(3, 'Project Manager', 'Manage software projects', 3, 3, 3),
(4, 'Frontend Developer', 'Develop frontend applications', 4, 4, 4),
(5, 'Backend Developer', 'Develop backend services', 5, 5, 5),
(6, 'Data Scientist', 'Analyze data and build models', 6, 6, 6),
(7, 'UI/UX Designer', 'Design user interfaces', 7, 7, 7),
(8, 'DevOps Engineer', 'Manage infrastructure and CI/CD', 8, 8, 8),
(9, 'Product Owner', 'Own the product development', 9, 9, 9),
(10, 'Business Analyst', 'Analyze business processes', 10, 10, 10);


-- Inserting data into Skills
INSERT INTO Skills (id, name) VALUES
(1, 'Java'), 
(2, 'Python'), 
(3, 'JavaScript'), 
(4, 'SQL'), 
(5, 'HTML'), 
(6, 'CSS'), 
(7, 'C++'), 
(8, 'C#'), 
(9, 'Ruby'), 
(10, 'Swift');

-- Inserting data into Candidates_has_Skills
-- Оновлений SQL-запит для вставки у Candidates_has_Skills без колонки id
INSERT INTO Candidates_has_Skills (candidate_id, skill_id, level) VALUES
(1, 1, 'senior'),
(2, 2, 'middle'),
(3, 3, 'junior'),
(4, 4, 'middle'),
(5, 5, 'junior'),
(6, 6, 'senior'),
(7, 7, 'middle'),
(8, 8, 'senior'),
(9, 9, 'junior'),
(10, 10, 'middle');
