CREATE TABLE IF NOT EXISTS tbl_collections (
  id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  collection_set_name VARCHAR(255) NOT NULL,
  release_date DATE NOT NULL,
  total_cards_in_collection INT UNSIGNED NOT NULL,
  PRIMARY KEY (id),
  UNIQUE KEY ux_collections_name (collection_set_name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS tbl_cards (
  id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  collection_id BIGINT UNSIGNED NOT NULL,
  card_number_in_collection VARCHAR(64) NOT NULL,
  name VARCHAR(255) NOT NULL,
  hp INT UNSIGNED NULL,
  type VARCHAR(64) NULL,
  stage VARCHAR(64) NULL,
  info TEXT NULL,
  attack TEXT NULL,
  damage VARCHAR(32) NULL,
  weak VARCHAR(64) NULL,
  resists VARCHAR(64) NULL,
  retreat INT UNSIGNED NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  CONSTRAINT fk_cards_collection FOREIGN KEY (collection_id) REFERENCES tbl_collections(id) ON UPDATE CASCADE ON DELETE RESTRICT,
  UNIQUE KEY ux_cards_collection_number (collection_id, card_number_in_collection),
  KEY ix_cards_collection_id (collection_id),
  KEY ix_cards_name (name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TRIGGER IF EXISTS tcg_cards_updated_at;
DELIMITER $$
CREATE TRIGGER tcg_cards_updated_at
BEFORE UPDATE ON tbl_cards
FOR EACH ROW
BEGIN
  SET NEW.updated_at = CURRENT_TIMESTAMP;
END$$
DELIMITER ;