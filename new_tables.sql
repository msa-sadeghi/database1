CREATE TABLE exams(
	id SERIAL PRIMARY KEY,
	class_subject_id INT REFERENCES class_subjects(id),
	title VARCHAR(100),
	date DATE
);

CREATE TABLE exam_results(
	id SERIAL PRIMARY KEY,
	exam_id INT REFERENCES exams(id),
	student_id INT REFERENCES students(id),
	score NUMERIC(5,2)
);

CREATE TABLE notifications(
	id SERIAL PRIMARY KEY,
	user_id INT REFERENCES users(id),
	title TEXT,
	message TEXT,
	date DATE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE parents(
	id SERIAL PRIMARY KEY,
	student_id INT REFERENCES students(id),
	name VARCHAR(100),
	phone VARCHAR(20),
	relation VARCHAR(20)
);