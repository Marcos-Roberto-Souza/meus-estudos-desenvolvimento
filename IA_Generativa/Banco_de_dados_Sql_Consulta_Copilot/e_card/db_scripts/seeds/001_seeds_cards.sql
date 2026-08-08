INSERT INTO tbl_collections (collection_set_name, release_date, total_cards_in_collection)
VALUES ('Base Set', '1999-01-09', 102);

INSERT INTO tbl_cards (
  collection_id, card_number_in_collection, name, hp, type, stage, info, attack, damage, weak, resists, retreat
)
VALUES
(
  1, '4/102', 'Charizard', 120, 'Fire', 'Stage 2',
  'Energy Burn ability text', 'Fire Spin', '100', 'Water x2', 'Fighting -30', 3
);
