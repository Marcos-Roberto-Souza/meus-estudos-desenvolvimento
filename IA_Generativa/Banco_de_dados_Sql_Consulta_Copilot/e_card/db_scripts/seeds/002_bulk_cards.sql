INSERT INTO tbl_collections (collection_set_name, release_date, total_cards_in_collection)
VALUES 
('Jungle', '1999-06-16', 64),
('Fossil', '1999-10-10', 62),
('Team Rocket', '2000-04-24', 83),
('Neo Genesis', '2000-12-16', 111),
('Scarlet & Violet—151', '2023-09-22', 210),
('Sun & Moon', '2017-02-03', 149);

SET @base := (SELECT id FROM tbl_collections WHERE collection_set_name='Base Set' LIMIT 1);
SET @jungle := (SELECT id FROM tbl_collections WHERE collection_set_name='Jungle' LIMIT 1);
SET @fossil := (SELECT id FROM tbl_collections WHERE collection_set_name='Fossil' LIMIT 1);
SET @rocket := (SELECT id FROM tbl_collections WHERE collection_set_name='Team Rocket' LIMIT 1);
SET @neo := (SELECT id FROM tbl_collections WHERE collection_set_name='Neo Genesis' LIMIT 1);
SET @sv151 := (SELECT id FROM tbl_collections WHERE collection_set_name='Scarlet & Violet—151' LIMIT 1);
SET @sunmoon := (SELECT id FROM tbl_collections WHERE collection_set_name='Sun & Moon' LIMIT 1);

INSERT INTO tbl_cards (collection_id, card_number_in_collection, name, hp, type, stage, info, attack, damage, weak, resists, retreat) VALUES
(@base, '2/102', 'Blastoise', 100, 'Water', 'Stage 2', 'Hydro Pump does more damage for each Water Energy attached.', 'Hydro Pump', '40+', 'Lightning ×2', 'None', 3),
(@base, '3/102', 'Venusaur', 100, 'Grass', 'Stage 2', 'Energy Trans lets you move Grass Energy between your Pokémon.', 'Solar Beam', '60', 'Fire ×2', 'None', 2),
(@base, '7/102', 'Hitmonchan', 70, 'Fighting', 'Basic', 'Jab and Special Punch combo attacker.', 'Special Punch', '40', 'Psychic ×2', 'None', 2),
(@base, '15/102', 'Ninetales', 80, 'Fire', 'Stage 1', 'Lure can disrupt your opponent''s board.', 'Fire Blast', '80', 'Water ×2', 'None', 1),
(@base, '18/102', 'Gyarados', 100, 'Water', 'Stage 1', 'Brutal splash attacker with high damage.', 'Dragon Rage', '50', 'Grass ×2', 'Fighting -30', 3),

(@jungle, '1/64', 'Clefable', 70, 'Colorless', 'Stage 1', 'Metronome copies a foe''s attack.', 'Metronome', '-', 'Fighting ×2', 'Psychic -30', 1),
(@jungle, '4/64', 'Flareon', 70, 'Fire', 'Stage 1', 'Quick attacker evolving from Eevee.', 'Flamethrower', '60', 'Water ×2', 'None', 1),
(@jungle, '5/64', 'Jolteon', 70, 'Lightning', 'Stage 1', 'Fast pressure with Pin Missile.', 'Pin Missile', '20×', 'Fighting ×2', 'None', 1),
(@jungle, '6/64', 'Kangaskhan', 90, 'Colorless', 'Basic', 'Fetch draws cards for setup.', 'Comet Punch', '20×', 'Fighting ×2', 'None', 3),
(@jungle, '7/64', 'Mr. Mime', 40, 'Psychic', 'Basic', 'Invisible Wall reduces big hits.', 'Meditate', '10+', 'Psychic ×2', 'None', 1),

(@fossil, '1/62', 'Aerodactyl', 60, 'Fighting', 'Stage 1', 'Prehistoric Power shuts off evolutions.', 'Wing Attack', '30', 'Grass ×2', 'Fighting -30', 2),
(@fossil, '2/62', 'Articuno', 70, 'Water', 'Basic', 'Freeze Dry potential paralysis.', 'Blizzard', '50', 'Metal ×2', 'Fighting -30', 2),
(@fossil, '3/62', 'Ditto', 50, 'Colorless', 'Basic', 'Transform mirrors opponent''s Active.', 'Giant Growth', '-', 'Fighting ×2', 'None', 1),
(@fossil, '4/62', 'Dragonite', 100, 'Colorless', 'Stage 2', 'Step In offers pivot utility.', 'Slam', '40×', 'Lightning ×2', 'Fighting -30', 2),
(@fossil, '6/62', 'Gengar', 80, 'Psychic', 'Stage 2', 'Curse moves damage counters.', 'Dark Mind', '30', 'Darkness ×2', 'Fighting -30', 1),

(@rocket, '4/82', 'Dark Charizard', 80, 'Fire', 'Stage 2', 'Nail Flick then Continuous Fireball.', 'Continuous Fireball', '50×', 'Water ×2', 'None', 2),
(@rocket, '5/82', 'Dark Blastoise', 70, 'Water', 'Stage 2', 'Rocket''s powerhouse cannon.', 'Hydrocannon', '30+', 'Lightning ×2', 'None', 2),
(@rocket, '7/82', 'Dark Gyarados', 70, 'Water', 'Stage 1', 'Final Beam punishes KOs.', 'Ice Beam', '30', 'Grass ×2', 'Fighting -30', 2),
(@rocket, '14/82', 'Dark Magneton', 60, 'Lightning', 'Stage 1', 'Sonicboom ignores Weakness/Resistance.', 'Magnetic Lines', '20', 'Fighting ×2', 'Metal -30', 1),
(@rocket, '22/82', 'Dark Alakazam', 60, 'Psychic', 'Stage 2', 'Teleport Blast for repositioning.', 'Mind Shock', '40', 'Psychic ×2', 'None', 2),

(@neo, '9/111', 'Typhlosion', 100, 'Fire', 'Stage 2', 'Fire Recharge accelerates energy.', 'Flame Wheel', '60', 'Water ×2', 'None', 2),
(@neo, '6/111', 'Feraligatr', 120, 'Water', 'Stage 2', 'Downpour synergy with Rain Dance.', 'Riptide', '10+', 'Lightning ×2', 'None', 3),
(@neo, '3/111', 'Meganium', 100, 'Grass', 'Stage 2', 'Wild Growth boosts Grass Energy.', 'Solarbeam', '50', 'Fire ×2', 'None', 2),
(@neo, '1/111', 'Ampharos', 80, 'Lightning', 'Stage 2', 'Gigavolt has flip-based bonus.', 'Gigavolt', '40+', 'Fighting ×2', 'Metal -30', 2),
(@neo, '15/111', 'Lugia', 90, 'Colorless', 'Basic', 'Elemental Blast discards three types.', 'Elemental Blast', '90', 'Lightning ×2', 'Fighting -30', 2),

(@sv151, '006/165', 'Charizard ex', 330, 'Fire', 'Stage 2', 'Powerful ex with massive output.', 'Burning Darkness', '180+', 'Water ×2', 'None', 3),
(@sv151, '003/165', 'Venusaur ex', 340, 'Grass', 'Stage 2', 'Healing and bulky control.', 'Ivy Storm', '150', 'Fire ×2', 'None', 3),
(@sv151, '009/165', 'Blastoise ex', 330, 'Water', 'Stage 2', 'Tanky cannon pressure.', 'Twin Cannons', '220', 'Lightning ×2', 'None', 3),
(@sv151, '025/165', 'Pikachu', 60, 'Lightning', 'Basic', 'Iconic mascot attacker.', 'Thunderbolt', '90', 'Fighting ×2', 'Metal -30', 1),
(@sv151, '149/165', 'Mewtwo', 130, 'Psychic', 'Basic', 'Psychic blast tempo.', 'Psyburn', '110', 'Darkness ×2', 'Fighting -30', 2),

(@sunmoon, '14/149', 'Incineroar', 160, 'Fire', 'Stage 2', 'Strike for high damage.', 'Flare Blitz', '200', 'Water ×2', 'None', 3),
(@sunmoon, '18/149', 'Primarina', 150, 'Water', 'Stage 2', 'Melodic attack utility.', 'Bubble Beat', '20+', 'Grass ×2', 'None', 2),
(@sunmoon, '2/149', 'Butterfree', 130, 'Grass', 'Stage 2', 'Status and spread options.', 'Quiver Dance', '-', 'Fire ×2', 'Fighting -20', 1),
(@sunmoon, '49/149', 'Vikavolt', 150, 'Lightning', 'Stage 2', 'Strong acceleration and damage.', 'Strong Charge', '-', 'Fighting ×2', 'Metal -20', 3),
(@sunmoon, '35/149', 'Alolan Muk', 120, 'Darkness', 'Stage 1', 'Type shutdown ability.', 'Crunch', '70', 'Fighting ×2', 'Psychic -20', 3);