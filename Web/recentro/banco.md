### Banco utilizado: 
SQL Server

### Modelo Conceitual
![a](/conceitual.png)

### Físico
'''
CREATE TABLE Org (
    org_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    org_nome VARCHAR(50),
    org_end VARCHAR(50),
    org_reg VARCHAR(50),
    org_cnpj VARCHAR(50),
);

CREATE TABLE Post (
    post_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    post_title VARCHAR(50),
    post_data DATE,
    post_topico VARCHAR(50),
);

CREATE TABLE Guia (
    guia_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    guia_title VARCHAR(50),
    guia_tipo VARCHAR(50),
);

CREATE TABLE Org_contato (
    org_id INTEGER,
    org_ctt VARCHAR(50),
    PRIMARY KEY (org_ctt, org_id)
);

CREATE TABLE Org_especialidade (
    org_id INTEGER,
    org_espec_id INTEGER,
    org_reciclagem CHAR,
    org_domestico CHAR,
    org_industrial CHAR,
    org_hospitalar CHAR,
    org_agricola CHAR,
    org_eletronico CHAR,
    org_radioativo CHAR,
    PRIMARY KEY (org_espec_id, org_id)
);

CREATE TABLE Usuario (
    user_id INTEGER PRIMARY KEY,
    user_nome VARCHAR(50),
    user_tipo VARCHAR(50)
);

CREATE TABLE Comentario (
    com_id INTEGER,
    user_id INTEGER,
    post_id INTEGER,
    PRIMARY KEY (com_id, user_id, post_id),
    Foreign Key (user_id) REFERENCES Usuario(user_id),
    Foreign Key (post_id) REFERENCES Post(post_id)
);
 
ALTER TABLE Org ADD CONSTRAINT FK_Org_2
    FOREIGN KEY (user_id)
    REFERENCES Usuario (user_id)
    ON DELETE CASCADE;
 
ALTER TABLE Post ADD CONSTRAINT FK_Post_2
    FOREIGN KEY (user_id)
    REFERENCES Usuario (user_id)
    ON DELETE CASCADE;
 
ALTER TABLE Guia ADD CONSTRAINT FK_Guia_2
    FOREIGN KEY (user_id)
    REFERENCES Usuario (user_id)
    ON DELETE CASCADE;
 
ALTER TABLE Org_contato ADD CONSTRAINT FK_Org_contato_2
    FOREIGN KEY (org_id)
    REFERENCES Org (org_id)
    ON DELETE CASCADE;
 
ALTER TABLE Org_especialidade ADD CONSTRAINT FK_Org_especialidade_2
    FOREIGN KEY (org_id)
    REFERENCES Org (org_id)
    ON DELETE CASCADE;
'''
