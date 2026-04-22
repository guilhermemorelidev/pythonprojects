-- SQLite
CREATE TABLE disciplinas (
    codigo INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    carga_horaria INTEGER NOT NULL,
    area TEXT NOT NULL CHECK (area IN ('humanas', 'exatas')),
    dependencia INTEGER,
    nota_minima REAL DEFAULT 0.0,
    faixa_ensino TEXT NOT NULL,
    
    FOREIGN KEY (dependencia) REFERENCES disciplinas(codigo)
);

INSERT INTO disciplinas 
(codigo, nome, carga_horaria, area, dependencia, nota_minima, faixa_ensino)
VALUES
(1, 'Matemática Básica', 60, 'exatas', NULL, 5.0, 'fundamental'),
(2, 'Português', 60, 'humanas', NULL, 5.0, 'fundamental'),
(3, 'História Geral', 50, 'humanas', NULL, 6.0, 'fundamental'),
(4, 'Geografia', 50, 'humanas', NULL, 6.0, 'fundamental'),
(5, 'Ciências', 60, 'exatas', NULL, 5.5, 'fundamental'),

(6, 'Álgebra', 70, 'exatas', 1, 6.0, 'medio'),
(7, 'Literatura', 60, 'humanas', 2, 6.5, 'medio'),
(8, 'Física', 80, 'exatas', 1, 7.0, 'medio'),
(9, 'Química', 80, 'exatas', 5, 7.0, 'medio'),
(10, 'Sociologia', 50, 'humanas', NULL, 6.0, 'medio'),

(11, 'Filosofia', 50, 'humanas', NULL, 6.0, 'medio'),
(12, 'Geometria', 70, 'exatas', 1, 6.5, 'medio'),
(13, 'Biologia', 70, 'exatas', 5, 6.5, 'medio'),
(14, 'Redação', 60, 'humanas', 2, 7.0, 'medio'),
(15, 'Estatística', 60, 'exatas', 6, 7.0, 'medio'),

(16, 'Cálculo I', 90, 'exatas', 6, 7.0, 'superior'),
(17, 'Cálculo II', 90, 'exatas', 16, 7.5, 'superior'),
(18, 'Programação', 80, 'exatas', NULL, 6.5, 'superior'),
(19, 'Banco de Dados', 80, 'exatas', 18, 7.0, 'superior'),
(20, 'Engenharia de Software', 80, 'exatas', 18, 7.0, 'superior'),

(21, 'Psicologia', 60, 'humanas', NULL, 6.5, 'superior'),
(22, 'Economia', 70, 'humanas', NULL, 6.5, 'superior'),
(23, 'Administração', 70, 'humanas', NULL, 6.0, 'superior'),
(24, 'Direito', 80, 'humanas', NULL, 7.0, 'superior'),
(25, 'Metodologia Científica', 60, 'humanas', NULL, 6.5, 'superior'),

(26, 'Inteligência Artificial', 80, 'exatas', 18, 8.0, 'superior'),
(27, 'Machine Learning', 80, 'exatas', 26, 8.5, 'superior'),
(28, 'Redes de Computadores', 70, 'exatas', 18, 7.0, 'superior'),
(29, 'Segurança da Informação', 70, 'exatas', 28, 7.5, 'superior'),
(30, 'Ética Profissional', 50, 'humanas', NULL, 6.0, 'superior');

SELECT * FROM disciplinas