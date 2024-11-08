-- Initialization script for Matrix-themed MySQL database

-- Create the main database if it does not exist
CREATE DATABASE IF NOT EXISTS matrix_db;
USE matrix_db;

-- Table 1: Users table for login
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

-- Insert an admin user into the users table
INSERT INTO users (username, password) VALUES ('admin', 'KLASFaslfj234#434$@'); 

-- Table 2: Main flags table
CREATE TABLE IF NOT EXISTS flags (
    id INT AUTO_INCREMENT PRIMARY KEY,
    flag VARCHAR(255) NOT NULL
);

-- Insert flags into the flags table
INSERT INTO flags (flag) VALUES ('cahsi-{take_the_blue_pill}');
INSERT INTO flags (flag) VALUES ('cahsi-{you_have_a_choice}');
INSERT INTO flags (flag) VALUES ('cahsi-{what_is_the_matrix}');

-- Table 3: Secrets table
CREATE TABLE IF NOT EXISTS secrets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    hint VARCHAR(255) NOT NULL,
    flag VARCHAR(255) NOT NULL
);

-- Insert flags and hints into the secrets table
INSERT INTO secrets (hint, flag) VALUES ('The truth is hidden deeper', 'cahsi-{free_your_mind}');
INSERT INTO secrets (hint, flag) VALUES ('Trust in Morpheus', 'cahsi-{down_the_rabbit_hole}');
INSERT INTO secrets (hint, flag) VALUES ('Reality is an illusion', 'cahsi-{wake_up_neo}');

-- Table 4: Agents table with hidden flags
CREATE TABLE IF NOT EXISTS agents (
    id INT AUTO_INCREMENT PRIMARY KEY,
    agent_name VARCHAR(255) NOT NULL,
    access_code VARCHAR(255) NOT NULL
);

-- Insert flags disguised as agent access codes
INSERT INTO agents (agent_name, access_code) VALUES ('Agent Smith', 'cahsi-{mr_anderson}');
INSERT INTO agents (agent_name, access_code) VALUES ('Agent Brown', 'cahsi-{dodge_this}');
INSERT INTO agents (agent_name, access_code) VALUES ('Agent Jones', 'cahsi-{he_is_the_one}');

-- Table 5: Codes table with encoded flags
CREATE TABLE IF NOT EXISTS codes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    code_name VARCHAR(255) NOT NULL,
    encoded_flag VARCHAR(255) NOT NULL
);

-- Insert encoded flags into the codes table
INSERT INTO codes (code_name, encoded_flag) VALUES ('code_red', TO_BASE64('cahsi-{reality_is_a_prison}'));
INSERT INTO codes (code_name, encoded_flag) VALUES ('code_blue', TO_BASE64('cahsi-{see_through_the_illusion}'));
INSERT INTO codes (code_name, encoded_flag) VALUES ('code_green', TO_BASE64('cahsi-{freedom_of_choice}'));

-- Table 6: Files table with ROT13 encoded flags
CREATE TABLE IF NOT EXISTS files (
    id INT AUTO_INCREMENT PRIMARY KEY,
    file_name VARCHAR(255) NOT NULL,
    encrypted_flag VARCHAR(255) NOT NULL
);

-- Insert ROT13 encoded flags into the files table
INSERT INTO files (file_name, encrypted_flag) VALUES ('file1.txt', 'cahsi-{gurer_ner_ab_grpu}');  -- ROT13: "there_are_no_spoons"
INSERT INTO files (file_name, encrypted_flag) VALUES ('file2.txt', 'cahsi-{pynff_vf_abg_grpu}');  -- ROT13: "class_is_not_real"
INSERT INTO files (file_name, encrypted_flag) VALUES ('file3.txt', 'cahsi-{gur_erny_ovbaf}');    -- ROT13: "the_real_virus"

-- Table 7: Hidden Clues table with SHA256 hashes of flags
CREATE TABLE IF NOT EXISTS hidden_clues (
    id INT AUTO_INCREMENT PRIMARY KEY,
    clue_description VARCHAR(255) NOT NULL,
    hashed_flag VARCHAR(255) NOT NULL
);

-- Insert SHA256 hashed flags into the hidden_clues table
INSERT INTO hidden_clues (clue_description, hashed_flag) VALUES ('Knowledge of reality lies in hashing', SHA2('cahsi-{open_your_mind}', 256));
INSERT INTO hidden_clues (clue_description, hashed_flag) VALUES ('Only the chosen one can see this', SHA2('cahsi-{believe_in_the_one}', 256));
INSERT INTO hidden_clues (clue_description, hashed_flag) VALUES ('A vision of truth emerges', SHA2('cahsi-{code_to_freedom}', 256));
