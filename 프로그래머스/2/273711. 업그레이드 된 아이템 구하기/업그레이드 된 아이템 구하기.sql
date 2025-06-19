SELECT p_info.item_id, p_info.item_name, p_info.rarity
FROM item_info AS info
    JOIN item_tree AS parent ON info.item_id=parent.parent_item_id
    JOIN item_info AS p_info ON parent.item_id=p_info.item_id
WHERE info.rarity='RARE'
ORDER BY p_info.item_id DESC;