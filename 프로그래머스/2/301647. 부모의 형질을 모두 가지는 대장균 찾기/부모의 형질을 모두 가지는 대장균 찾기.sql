SELECT child.id, child.genotype, parent.genotype AS parent_genotype
FROM ecoli_data AS child 
    JOIN ecoli_data AS parent
    ON child.parent_id = parent.id
WHERE child.genotype & parent.genotype = parent.genotype
ORDER BY child.id;